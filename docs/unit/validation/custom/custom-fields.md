---
id: custom-fields
forward:
  - "[field-specific clean](./field-clean-method.md)"
noteId: 1757047059559
---

Can I create a reusable custom `AgeField` to enforce minimum age (13)?

---

- Yes. Subclass `forms.IntegerField` and add the age check in `validate()`
- Reuse this field across forms to avoid duplicating `clean_age()` logic

```python
from django import forms
from django.core.exceptions import ValidationError

class AgeField(forms.IntegerField):
    def validate(self, value):
        super().validate(value)
        if value is not None and value < 13:
            raise ValidationError("Age must be at least 13 years old.")

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    age = AgeField(label="Age")
```

---

- `validate()` is called during field validation after base checks
- Keep domain rules inside custom fields for reusability and consistency
- You can also parameterize minimum age via `__init__` if needed

