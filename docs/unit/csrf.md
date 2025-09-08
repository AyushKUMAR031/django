## 🔹 CSRF Middleware & Core Functions

* **`CsrfViewMiddleware`**

  * Automatically checks CSRF tokens on unsafe HTTP methods (`POST`, `PUT`, `PATCH`, `DELETE`).
  * Enabled by default in `MIDDLEWARE` settings.

* **`django.middleware.csrf.get_token(request)`**

  * Forces generation of a CSRF token for the current request.
  * Useful if you need the token outside a form (e.g., in a custom template).

* **`django.middleware.csrf.rotate_token(request)`**

  * Creates a new CSRF token for the session, invalidating the old one.
  * Often used after login to prevent **session fixation** attacks.

---

## 🔹 Template Tag

* **`{% csrf_token %}`**

  * Inserts the hidden `<input>` with the CSRF token inside a form.
  * Example:

    ```html
    <form method="post">
        {% csrf_token %}
        <input type="text" name="username">
        <button type="submit">Submit</button>
    </form>
    ```

---

## 🔹 Decorators

* **`@csrf_protect`**

  * Ensures that CSRF validation is applied to a specific view.
  * Example:

    ```python
    from django.views.decorators.csrf import csrf_protect

    @csrf_protect
    def my_view(request):
        ...
    ```

* **`@csrf_exempt`**

  * Skips CSRF validation for a specific view.
  * Use carefully (e.g., for webhooks or API endpoints).
  * Example:

    ```python
    from django.views.decorators.csrf import csrf_exempt

    @csrf_exempt
    def webhook_receiver(request):
        ...
    ```

* **`@requires_csrf_token`**

  * Ensures a CSRF token is always present in the context, even if the form fails.
  * Often used in custom error templates.

---

## 🔹 AJAX / JavaScript Integration

* When sending AJAX requests with `fetch` or `XMLHttpRequest`, you must include the CSRF token in the headers:

  ```javascript
  fetch("/submit/", {
      method: "POST",
      headers: {
          "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify({ data: "test" })
  })
  ```

---

Good point — you’re asking *where exactly these are written/defined* in Django.

Here’s the breakdown:

---

### 1. **`CsrfViewMiddleware`**

* Location: **`django/middleware/csrf.py`**
* It’s a middleware class that Django applies automatically (if present in `settings.py` → `MIDDLEWARE`).
* Example from `settings.py`:

  ```python
  MIDDLEWARE = [
      "django.middleware.security.SecurityMiddleware",
      "django.contrib.sessions.middleware.SessionMiddleware",
      "django.middleware.csrf.CsrfViewMiddleware",   # <--- here
      ...
  ]
  ```

---

### 2. **`get_token(request)`**

* Defined in: **`django/middleware/csrf.py`**
* Usage:

  ```python
  from django.middleware.csrf import get_token

  def my_view(request):
      token = get_token(request)
      return JsonResponse({"csrfToken": token})
  ```
* It ensures a CSRF token exists for the request and returns it.

---

### 3. **`rotate_token(request)`**

* Also defined in: **`django/middleware/csrf.py`**
* Usage:

  ```python
  from django.middleware.csrf import rotate_token

  def login_view(request):
      # After user logs in
      rotate_token(request)
      ...
  ```
* It invalidates the old token and generates a new one (commonly used after login/logout).

---

[more more on CSRF](https://docs.djangoproject.com/en/5.2/ref/csrf/)