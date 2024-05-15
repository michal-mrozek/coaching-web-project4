# Coaching Service Application

This is a Django-based web application designed to facilitate the management of a coaching service. It includes features for managing coaches, students, schedules, and sessions. The application aims to provide an efficient and user-friendly platform for both coaches and students.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**: Secure login and registration for coaches and students.
- **Profile Management**: Manage coach and student profiles.
- **Scheduling**: Schedule sessions between coaches and students.
- **Session Management**: Track and manage coaching sessions.
- **Notifications**: Email notifications for session reminders and updates.
- **Payment Integration**: Integration with payment gateways for session payments.

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- PostgreSQL (or any other preferred database)

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/coaching-service.git
    cd coaching-service
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**
    - Update the `DATABASES` setting in `settings.py` with your database configuration.

5. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Access the application:**
    Open a web browser and go to `http://127.0.0.1:8000`.

## Usage

### Admin Panel

- Access the admin panel at `http://127.0.0.1:8000/admin`.
- Use the admin panel to manage users, coaches, students, sessions, and schedules.

### User Interface

- Coaches and students can log in and manage their profiles.
- Students can book sessions with available coaches.
- Coaches can manage their schedules and track sessions.


## Configuration

### Environment Variables

Create a `.env` file in the root directory and add the following variables:

```plaintext
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
EMAIL_HOST=smtp.your-email-provider.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
```

## Manual Tests
### User Authentication

1 **Register a new user**

- Log in with the registered user.
- Verify that the user can log out successfully.

2 **Profile Management**

- Update user profile information.
- Verify that the changes are reflected correctly.

3 **Scheduling**

- Create a new session as a coach.
- Book a session as a student.
- Verify that the session appears correctly in both coach and student schedules.

4 **Notifications**

- Ensure email notifications are sent for session reminders and updates.
- Verify that the email content is correct.

5 **Payment Integration**

- Test the payment process using test credentials from the payment gateway.
- Ensure that successful payments are processed and reflected correctly in the system.
- Verify that failed payments are handled gracefully.

### License
This project is licensed under the MIT License.