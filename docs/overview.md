# 1. Introduction
### **Django:** 
- It is a powerful high-level, open-source Python web framework for building web applications.

    - **Uses:** Build secure, scalable sites fast.
    - **Pattern:** Follows Model-View-Template (MVT).
    - **Includes:** Tools for databases, templates, user auth, admin panel.
    - **Structure:** Projects (main app) + Apps (modular features).
    - **Strengths:** Clean code, reusable, secure, and rapid development.

- **Batteries Included:**  
  Ships with everything you need—ORM, auth system, admin, templates, form handling, URL routing, and more.

- **DRY Principle:**  
  Designed for *Don't Repeat Yourself*—encourages reusable code and less duplication.

### **MVT:**

Django’s core structure is **MVT (Model-View-Template)**:

- **Model:** Handles database. Defines the structure of your data (like tables).
- **View:** Contains the logic. Processes requests and prepares data for display.
- **Template:** Controls presentation. Renders HTML using data sent by the view.

**Flow:**  
User request → **View** (fetches/modifies) **Model** data → (sends) to **Template** → (displays to user).

```
IN SHORT :
Model = Data | View = Logic | Template = Display
```

