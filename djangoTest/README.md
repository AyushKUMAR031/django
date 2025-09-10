# django-ayush

## Routes

| Route                  | View                  | Description                                      |
| ---------------------- | --------------------- | ------------------------------------------------ |
| /                      | `Me`                  | Renders the landing page.                        |
| /feedback/             | `feedback_view`       | Renders the feedback form and handles submission.|
| /feedback/success/     | `feedback_success_view` | Displays a success message after feedback submission.|
| /signup/               | `signup_view`         | Renders the signup form and handles user creation.|
| /login/                | `login_view`          | Renders the login form and handles user authentication.|
| /logout/               | `logout_view`         | Logs the user out and redirects to the landing page.|
| /admin/                | `admin.site.urls`     | The Django administration site.                  |