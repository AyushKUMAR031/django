## Forms in Django

### 1. Introduction to forms
* Forms in web application are interfaces for collecting user input (such as login details,comments, feedback).

- Use Cases
    - user authentication.
    - collecting feedback
    - creating/updating products and records.

- Types of Forms in Django

| Type          | Description                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| Django Forms  | Python classes using `forms.Form` or `forms.ModelForm` for powerful form logic and validations |
| HTML Forms    | Standard HTML `<form>` tags managed manually in the Django view                              |


### 2. Using GET,POST, and HTTP in froms

* HTTP methods
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


### 3. Building form using Django
* `forms.Form` is the base class for all forms in Django.
* `forms.ModelForm` is a subclass of `forms.Form` that makes it easier to create forms

*so we start with*
- first define a class using `forms.Form` in `forms.py`.
- use the form instance in ur view.
- render the form in ur django template.

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

- *contact.html*
    ```html
        <form method="POST">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Send</button>
        </form>
    ```

### 4. CSRF
* CSRF stands for Cross-Site Request Forgery. 
* It is a type of attack that ticks the broswer to submit a request you didn't intend.

- *example*
    - *if a malicious site submits a POST request to ur django app (as a logged-in user), it could perform unwanted actions.*

#### CSRF protection in Django
- django provides automatic csrf protection using.
    - `{% csrf_token %}` in templates.
    - `CsrfViewMiddleware` (enabled by default).

- *code*
    ```html
        <form method="POST">
            {% csrf_token %}
            ...
        </form>
    ```

- If `{% csrf_token %}` is missing, Django will return a 403 Forbidden error.


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
            # Save or send email
            return redirect('thank_you')  # ✅ Redirect after POST
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

```

### 6. Data Validation with Django Forms

* why validation ?
    - so that user don't enter invalid data (letters in a phone number).
    - required fields aren't left empty.
    - data follows a specific rule (like email format, password strength).

* Django features in this ..
    - Django has `built-in validation`. (like EmailField -> checks email format)
    ```python
        email = forms.EmailField(required=True)
    ```
    - and provides `custom validation`. (like clean_<field>() -> custom task via this mehtod)  

* in dj, validation happens automatically when u call:
    ```python
        form.is_valid()
    ```

