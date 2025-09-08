## Forms in Django

### 1. Introduction to forms
* Forms in web application are interfaces for collecting user input (such as login details,comments, feedback).

- Use Cases
    - user authentication.
    - collecting feedback
    - creating/updating products and records.

- Types of Forms in Django

| Type          | Description                                                                                    |
|---------------|------------------------------------------------------------------------------------------------|
| Django Forms  | Python classes using `forms.Form` or `forms.ModelForm` for powerful form logic and validations |
| HTML Forms    | Standard HTML `<form>` tags managed manually in the Django view                                |

---

### 2. Using GET,POST, and HTTP in froms

* Forms contains elements for collection of data or input from a visitor at a particular level (say login, registration, reviews,
posting on internet), but in all these a form must specify 2 things :
    - `WHERE`: the URL to which the data corresponding to the user’s input should be returned.
    - `HOW`: the HTTP method the data should be returned by.
    - i.e, `<form method="how" action="where">`.

* HTTP methods (GET,POST,PUT,DELETE,PATCH)
- but here in forms we are only dealing with 2 HTTP methods (GET and POST).
    - GET: used for retrieving data from the server (search, filter)
    - POST: send data to the server (create, update, delete)

*sample html form*
```html
<form method="POST" action="/submit/">
  <input type="text" name="username" />
  <input type="submit" value="Submit" />
</form>
```

*sample django view*
```python
def submit_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        return HttpResponse(f"Hello {username}")
    return render(request, 'form.html')
```

---

### 3. Building form using Django
* `forms.Form` is the base class for all forms in Django.
* `forms.ModelForm` is a subclass of `forms.Form` that makes it easier to create forms.

  * Automatic HTML generation for forms
  * Built-in validation and error handling
  * Protection against common security threats (like CSRF, XSS)

* In django a form class written in a forms.py file works as model that is mapped to the html form elements in the templates.(it is just like a models.py where a db model is mapped to database thing).
* In django forms their are fields for different input types like (CharField, EmailField) and each field handles many complex things inside them (say validation, input clean up, required, labels, initial, localize).

*so we start with*
- first define a class using `forms.Form` in `forms.py`.
- use the form instance in ur view.
- render the form in ur django template.
- A Form instance has an `is_valid()` method, which `runs validation routines` for all its fields and in its `cleaned_data` attribute.

*sample code*
- *forms.py*
    ```python
        from django import forms

        class ContactForm(forms.Form):
            name = forms.CharField(label='Your Name', max_length=100)
            email = forms.EmailField()
            message = forms.CharField(widget=forms.Textarea)
    ```

- *views.py*
    ```python
        from .forms import ContactForm

        def contact_view(request):
            if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                    # process form.cleaned_data
                    return HttpResponse("Thank you for contacting us!")
            else:
                form = ContactForm()
            return render(request, 'contact.html', {'form': form})
    ```

- *another example views.py with more commenting*
    ```python
        from django.http import HttpResponseRedirect
        from django.shortcuts import render

        from .forms import NameForm

        def get_name(request):
            # if this is a POST request we need to process the form data
            if request.method == "POST":
                # create a form instance and populate it with data from the request:
                form = NameForm(request.POST) # This is called “binding data to the form” (it is now a bound form).
                # check whether it's valid:
                if form.is_valid():
                    # process the data in form.cleaned_data as required
                    # ...
                    # redirect to a new URL:
                    return HttpResponseRedirect("/thanks/")
                # when isvalid() not true form goes with data using the last render line so that 
                # user can edit the form's currently populated data and submit again.

            # if a GET (or any other method) we'll create a blank form
            else:
                form = NameForm() # what we can expect to happen the first time we visit the URL. (unbound form)

            return render(request, "name.html", {"form": form})
    ```

- *contact.html*
    - All the form’s fields and their attributes will be unpacked into HTML markup 
        from that `{{ form }}` by Django’s template language.
    ```html
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Send</button>
        </form>
    ```
    - `{{ form.as_p }}` : Renders the form’s fields as HTML wrapped in <p> tags.
    - `{{ form.as_table }}` : Renders fields inside <tr> and <td> for table layout.
    - `{{ form.as_ul }}` : Renders fields as <li> elements inside an unordered list.

    - If you don’t want these auto layouts, you can render each field manually:
        ```html
            {{ form.name.label_tag }}
            {{ form.name }}
            {{ form.name.errors }}
        ```

**Django Form Fields & Browser Validation**

- `URLField`, `EmailField`, `IntegerField` → render as type="url", type="email", type="number".
- Browsers add their own validation (stricter than Django).
    - To disable:
        - Use novalidate on `<form>` 
            - `<form method="post" novalidate>`, or
        - Change widget (e.g., TextInput).

---

### 4. CSRF
* CSRF stands for Cross-Site Request Forgery.
* It is a type of attack that ticks the broswer to submit a request you didn't intend.

- *example*
    - *if a malicious site submits a POST request to ur django app (as a logged-in user), it could perform unwanted actions.*

#### CSRF protection in Django
- django provides automatic csrf protection using.
    - `{% csrf_token %}` in templates.
    - `CsrfViewMiddleware` (enabled by default).
- Its a CSRF middleware and template tag. 

- *code*
    ```html
        <form method="POST">
            {% csrf_token %}
            ...
        </form>
    ```

**How it works**
- a hidden csrfViewMiddleware is present in there for outgoing request which sends a secret cookie (and that value changes every time of security).
- and its not a simple secret , each time it is scrambled differently using a mask.
- and for incoming request there must be a CSRF cookie to get validated.
- it verifies the `origin header` to protect against cross-subdomain-attacks.

- **Note**
    - It deliberately ignores GET requests (and other requests that are defined as ‘safe’ by RFC 9110 Section 9.2.1). These requests ought never to have any potentially dangerous side effects, and so a CSRF attack with a GET request ought to be harmless. 
    - RFC 9110 Section 9.2.1 defines POST, PUT, and DELETE as ‘unsafe’, and all other methods are also assumed to be unsafe, for maximum protection.

- If `{% csrf_token %}` is missing from cross-site or token is not validating, Django will return a 403 Forbidden error.

[more on CSRF](./csrf.md)

---

### 5. POST redirect in Django (PRG Pattern)

* PRG stands for `Post-Redirect-Get`.
* It is a pattern used to prevent duplicate form submissions.
* After a form POST, if you reload the page, the data can be resubmitted (bad for things like transactions).

    ```python

    from django.shortcuts import redirect

    def contact_view(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save() # Save or send email [when modelform is used cause it is connected to db so for saving that].
                Contact.objects.create(**data)   # explicitly saving to DB in forms.form

                return redirect('thank_you')  # ✅ Redirect after POST
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})
        # thank_you would be another view that just renders a success message.

    # also see sending email format
    from django.core.mail import send_mail

    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        send_mail(
            subject=f"New Contact from {name}",
            message=message,
            from_email=email,
            recipient_list=["admin@example.com"],
        )
    ```
- **`forms.Form` vs `forms.modelForm`**
    - forms.Form → Just validation, no DB. You manually handle data.
    - forms.ModelForm → Connected to a model; form.save() writes directly to the database.
        - Database itself is configured in settings.py, and models map to tables.
            ## 🔹 3. Where is the DB connection?
            * Django connects to the database using settings in **`settings.py`** under `DATABASES`.
            * Example (SQLite default):

                ```python
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': BASE_DIR / 'db.sqlite3',
                    }
                }
                ```
            * For PostgreSQL/MySQL:

                ```python
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.postgresql',
                        'NAME': 'mydb',
                        'USER': 'myuser',
                        'PASSWORD': 'mypassword',
                        'HOST': 'localhost',
                        'PORT': '5432',
                    }
                }
                ```
            * Each **`models.Model`** class corresponds to a table in this database.
---

### 6. Data Validation with Django Forms

* why validation ?
    - so that user don't enter invalid data (letters in a phone number).
    - required fields aren't left empty.
    - data follows a specific rule (like email format, password strength).

* Django features in this ..
    * Django has `built-in validation`. (like EmailField -> checks email format)
    * `form.is_valid()` → returns `True` if data passes validation.
    * `form.cleaned_data` → gives sanitized input.
    * Custom validation with `clean_<fieldname>()`.
    ```python
        email = forms.EmailField(required=True)
    ```
    - and provides `custom validation`. (like clean_<field>() -> custom task via this method)  

    * in dj, validation happens automatically when u call:
        ```python
            form.is_valid()
        ```

    ```python
    class SignupForm(forms.Form):
        username = forms.CharField(max_length=20)
        age = forms.IntegerField()

        def clean_age(self):
            age = self.cleaned_data.get('age')
            if age < 18:
                raise forms.ValidationError("You must be at least 18 years old.")
            return age
    ```

* Custom field Validation
    * form validation are done after cleaning, generally done by `form.is_valid()` function.
    * for customizing each field or required fields personally.
        - we have `Validators` : These are functions or callbacks that takes one argument and raiseerror for the input.
            - to_python()
            - validate()
        
    * example :
        ```python
            from django import forms

            class CustomAgeField(forms.IntegerField):
                def to_python(self, value):
                    # Convert raw input to integer, raise error if fails
                    try:
                        return int(value)
                    except (TypeError, ValueError):
                        raise forms.ValidationError('Not a valid integer.')

                def validate(self, value):
                    super().validate(value)
                    if value < 18:
                        raise forms.ValidationError("Must be at least 18.")
                        
            class ProfileForm(forms.Form):
                email = forms.CharField(max_length=100, validators=[validate_gmail])
                age = CustomAgeField()
        ```
    
---