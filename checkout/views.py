from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderItem
from profiles.models import UserProfile

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            'membership_len': request.POST.get('membership_len'),
            'membership_price': request.POST.get('membership_price'),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    months = request.GET.get('months')
    price = request.GET.get('price')

    if request.method == 'POST':

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address': request.POST['street_address'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.order_total = int(request.POST['membership_price'])
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.save()
            mem_price = request.POST['membership_price']
            mem_length = request.POST['membership_len']

            order_item = OrderItem(
                order=order,
                membership_length=int(mem_length),
                membership_price=int(mem_price),
            )
            order_item.save()

            return redirect(reverse('checkout_success', args=[order.order_number]))

        else:
            messages.error(request, 'There was an error with your form. \
                                Please double check your information.')

    else:
        if not months or not price:
            messages.error(request, "Choose valid months and price")
            return redirect(reverse('work_with_me'))

        stripe_total = round(int(price) * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            )
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'months': months,
        'price': price,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile

    order.save()
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)