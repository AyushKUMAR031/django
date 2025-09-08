
1. Make sure you have a model defined in `apps/guestBook/models.py`:

   ```python
   from django.db import models

   class Entry(models.Model):
       name = models.CharField(max_length=100)
       title = models.CharField(max_length=200)
       message = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return f"{self.name} - {self.title}"
   ```

2. Run **makemigrations** for your app:

   ```bash
   python manage.py makemigrations guestBook
   ```

3. Apply migrations to create the table:

   ```bash
   python manage.py migrate
   ```

4. Verify the table is created:

   ```bash
   python manage.py showmigrations
   ```

---
