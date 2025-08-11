# Regex Notes for Django

Regular expressions (regex) are patterns used to match strings.  
In Django, regex is commonly used in:
- **URL patterns** (especially in older versions before `path()` replaced most `re_path()` cases)
- **Form field validation**
- **Custom validators**
- **Data extraction in views or utils**

---

### 1. Basic Syntax

| Symbol / Pattern | Meaning | Example | Matches |
|------------------|---------|---------|---------|
| `.`              | Any single character except newline | `a.c` | `abc`, `a-c` |
| `^`              | Start of string | `^Hello` | `Hello World` |
| `$`              | End of string | `world$` | `my world` |
| `[]`             | Character set | `[aeiou]` | `a`, `e` |
| `[^]`            | Negated set | `[^0-9]` | Any non-digit |
| `\d`             | Digit (0–9) | `\d\d` | `12` |
| `\D`             | Non-digit | `\D+` | `abc` |
| `\w`             | Word char (letters, digits, `_`) | `\w+` | `Hello_123` |
| `\W`             | Non-word char | `\W+` | `@#&` |
| `\s`             | Whitespace | `\s+` | space, tab |
| `\S`             | Non-whitespace | `\S+` | `word` |

---

### 2. Quantifiers

| Quantifier | Meaning | Example | Matches |
|------------|---------|---------|---------|
| `*`        | 0 or more | `ab*` | `a`, `ab`, `abb` |
| `+`        | 1 or more | `ab+` | `ab`, `abb` |
| `?`        | 0 or 1 | `ab?` | `a`, `ab` |
| `{n}`      | Exactly n | `a{3}` | `aaa` |
| `{n,}`     | n or more | `a{2,}` | `aa`, `aaa` |
| `{n,m}`    | Between n and m | `a{2,4}` | `aa`, `aaa`, `aaaa` |

---

### 3. Grouping and Alternation

| Pattern | Meaning | Example | Matches |
|---------|---------|---------|---------|
| `()`    | Grouping | `(abc)+` | `abc`, `abcabc` |
| `|`     | OR | `cat|dog` | `cat`, `dog` |

---

### 4. Special Constructs (Advanced)

These are powerful for more precise matching.

| Pattern | Name | Meaning | Example | Matches |
|---------|------|---------|---------|---------|
| `(?=...)` | Positive lookahead | Asserts that what follows matches ... but doesn’t consume it | `\w+(?=\.)` | Matches `file` in `file.txt` |
| `(?!...)` | Negative lookahead | Asserts that what follows does NOT match ... | `^(?!admin)\w+` | Matches any word not starting with `admin` |
| `(?<=...)` | Positive lookbehind | Asserts that what precedes matches ... | `(?<=@)\w+` | Matches `gmail` in `user@gmail.com` |
| `(?<!...)` | Negative lookbehind | Asserts that what precedes does NOT match ... | `(?<!\$)\d+` | Matches numbers not preceded by `$` |
| `(?#...)` | Comment | Allows comments inside pattern | `\d{3}(?#area code)-\d{4}` | Matches phone formats, ignores comment |

⚠ **Note**: Lookbehind in Python must have fixed width (e.g., `(?<=abc)` is fine, `(?<=a+)` is not).

---

### 5. Regex in Django URLs

In Django’s **`urls.py`** you can use:
- `path()` → simpler, no regex
- `re_path()` → regex-based routing

**Example:**
```python
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year),
]
```

### 6. regex method
| Method                           | Description                                                   | Example                                                              | Output                 |
| -------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------- | ---------------------- |
| `re.match(pattern, string)`      | Matches **only at the start** of the string.                  | `re.match(r'\d+', '123abc').group()`                                 | `'123'`                |
| `re.search(pattern, string)`     | Scans the **entire string** for the **first** match.          | `re.search(r'\d+', 'abc 123 xyz').group()`                           | `'123'`                |
| `re.findall(pattern, string)`    | Returns **all non-overlapping** matches as a list of strings. | `re.findall(r'\d+', '12 drummers, 11 pipers')`                       | `['12', '11']`         |
| `re.finditer(pattern, string)`   | Returns an **iterator** yielding match objects.               | `[m.group() for m in re.finditer(r'\d+', '12 drummers, 11 pipers')]` | `['12', '11']`         |
| `re.fullmatch(pattern, string)`  | Matches if the **entire string** matches the pattern.         | `re.fullmatch(r'\d+', '123')`                                        | Match object           |
| `re.split(pattern, string)`      | Splits string by pattern matches.                             | `re.split(r'[;,\s]\s*', 'a, b; c  d')`                               | `['a', 'b', 'c', 'd']` |
| `re.sub(pattern, repl, string)`  | Replaces matches with `repl`.                                 | `re.sub(r'\d+', '#', '123 and 456')`                                 | `'# and #'`            |
| `re.subn(pattern, repl, string)` | Same as `sub` but also returns **number of replacements**.    | `re.subn(r'\d+', '#', '123 and 456')`                                | `('# and #', 2)`       |
