## 🔹 1. Where to write admin customizations

* Every Django app has an `admin.py` file.
* This is where you **register your models** and define **custom admin classes**.
* Example: `myapp/admin.py`

---

## 🔹 2. Default registration

By default, if you just register:

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

In the admin interface, you’ll see a basic form for `Student` objects, but the list page will look plain (only shows `__str__` value).

---

## 🔹 3. Customizing with `ModelAdmin`

To improve it, we define a class that inherits from `admin.ModelAdmin` and tell Django how to display things.

### Example

```python
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'teacher')   # columns to display in list page
    search_fields = ('name',)                   # adds a search bar
    list_filter = ('teacher',)                  # adds a sidebar filter
```

---

## 🔹 4. Explanation of each option

* **`list_display`** → controls which fields are shown in the table on the list page.

  * Without it → only `__str__` of object shows.
  * With it → you see multiple columns (like Excel).

* **`search_fields`** → adds a search bar on top of the list.

  * You can search by `name` (or multiple fields).
  * Example: `search_fields = ('name', 'teacher__name')` lets you search inside related teacher’s name.

* **`list_filter`** → adds a filter sidebar on the right.

  * Example: filter students by `teacher`.
  * You can also use date fields here (`list_filter = ('created_at',)`).

---

## 🔹 5. How it looks in Admin

* Before customization:

  * You only see: `Student object (1)` , `Student object (2)` … not useful.
* After customization:

  * A table with columns: **Name | Age | Teacher**.
  * A search bar on top.
  * A filter panel on the right.

---

## 🔹 6. More useful options (quick list)

* `ordering = ('age',)` → default sort order.
* `list_editable = ('age',)` → allows inline editing on list page.
* `readonly_fields = ('created_at',)` → make fields non-editable.
* `fieldsets` → organize form layout.
* `inlines` → show related models on the same form.

---

✅ Example with multiple options:

```python
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'teacher')
    list_editable = ('age',)            # edit age directly in list
    search_fields = ('name',)
    list_filter = ('teacher', 'age')
    ordering = ('-age',)                # newest (highest age) first
```

---

👉 So, to use this:

1. Open your app’s `admin.py`.
2. Import your model.
3. Define a `ModelAdmin` class with your settings.
4. Register the model (either with `@admin.register` or `admin.site.register`).

---

