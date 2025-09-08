---
id: builtin-validators
forward:
  - "[field-specific clean](./field-clean-method.md)"
  - "[custom age field](./custom-fields.md)"
---

How to use Django's built-in validators in forms?

---

- Import validators from `django.core.validators`
- Attach them via the field's `validators=[...]` argument
- They run during form validation, before `clean_<field>()` and `clean()`

```python
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator, EmailValidator

class ProfileForm(forms.Form):
    # Age must be at least 13
    age = forms.IntegerField(
        label="Age",
        validators=[MinValueValidator(13, message="Age must be at least 13 years old.")]
    )

    # Email format validation (forms.EmailField already validates emails; shown here for pattern)
    email = forms.EmailField(
        label="Email",
        validators=[EmailValidator(message="Enter a valid email address.")]
    )

    # Username must be alphanumeric and underscores only, 3-30 chars
    username = forms.CharField(
        label="Username",
        min_length=3,
        max_length=30,
        validators=[
            RegexValidator(
                r"^\w{3,30}$",
                message="Username must be 3-30 chars, letters/numbers/underscore only.",
                code="invalid_username",
            )
        ]
    )
```

---

- Common validators: `MinValueValidator`, `MaxValueValidator`, `MinLengthValidator`, `MaxLengthValidator`, `RegexValidator`, `EmailValidator`, `URLValidator`, `validate_slug`, `validate_email`
- Use `message` and `code` to customize error text and error code
- Built-ins complement, not replace, form-specific `clean_<field>()` logic when needed
- For reusable domain rules (like age), consider a custom field (`AgeField`) that composes built-ins or adds logic
