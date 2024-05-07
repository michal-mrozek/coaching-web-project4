from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .form import UserProfileForm


@login_required
def profile(request):
    """Display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = get_object_or_404(UserProfile, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,

        'on_profile_page': True,
    }

    return render(request, template, context)

