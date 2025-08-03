### 🐍 What is a **Slug** in Django?

#### 🔹 **Concept / Idea**

* A **slug** is a short label for something, containing only letters, numbers, underscores or hyphens.
* It is often used in URLs to make them **readable** and **SEO-friendly**.
* Example: Instead of `/blog/1234`, we use `/blog/what-is-a-slug`.

#### 🔹 **Use in Django**

* Django provides a special field called `SlugField` to store slugs in models.
* You can generate slugs from titles or names using Django utilities.

#### 🔹 **Example Code**

**Model (models.py):**

```python
from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # converts "Hello World!" → "hello-world"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
```

**URL Pattern (urls.py):**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('blog/<slug:slug>/', views.blog_detail, name='blog-detail'),
]
```

**View (views.py):**

```python
from django.shortcuts import get_object_or_404, render
from .models import BlogPost

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})
```

#### 🔹 Applications

* Making URLs more meaningful (SEO).
* Replacing numeric IDs with readable identifiers.
* Used in blogs, e-commerce products, categories, etc.

