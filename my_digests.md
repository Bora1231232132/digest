# 🧠 My Daily Digests

## 📑 Digest: www.geeksforgeeks.org/python/python-web-development-django/

[Read Original Source](https://www.geeksforgeeks.org/python/python-web-development-django/)

- Django is a "batteries-included" Python web framework for rapid development, known for its excellent documentation, scalability, and adoption by major companies, leveraging Python's extensive libraries.
- It follows an MVT (Model-View-Template) architecture:
  - **Model:** Manages data logic and database interaction.
  - **View:** Handles user interface presentation.
  - **Template:** Defines static HTML with dynamic content.
- Setting up a Django project involves creating a virtual environment, installing Django via pip, starting a project and running the server using `manage.py`.
- Key project files include `manage.py` (CLI), `settings.py` (configuration), `urls.py` (URL routing), and `wsgi.py` (web server interface).
- Django uses an app structure, where apps are reusable, independent modules for specific functionalities, created with `startapp` and registered in `settings.py`.
- Views are Python functions or classes that process web requests and return responses, categorized into Function-Based (often for CRUD operations) and Class-Based (offering structured code and reusability).
- URL patterns in `urls.py` map incoming URLs to specific view functions, with the ability to include URL configurations from individual apps.
- Django Models simplify database interaction through an Object-Relational Mapper (ORM), defining database tables and fields as Python classes. Changes to models require running `makemigrations` and `migrate` commands to update the database schema.

---
