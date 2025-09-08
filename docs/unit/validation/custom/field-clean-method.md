---
id: field-specific-clean
forward:
  - "[custom age field](./custom-fields.md)"
---

How to add an age field with a custom validation error (< 13 not allowed)?

---

- Use a `forms.IntegerField` for `age`
- Implement `def clean_age(self):` in the form to enforce the rule
- Raise `ValidationError` with a custom message when `age < 13`

```python
from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    age = forms.IntegerField(label="Age")

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age < 13:
            raise ValidationError("Age must be at least 13 years old.")
        return age
```

---

- `clean_<fieldname>()` runs automatically for that field during validation
- Return the cleaned value to allow validation to pass
- Prefer this when the rule is specific to a single field in one form 