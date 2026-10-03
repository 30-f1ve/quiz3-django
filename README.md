# quiz3_django

A beginner-friendly Django application demonstrating the basic
**Model → View → URL → Template** flow, built for Quiz #3.

## What it does

The home page lists every `Student` record stored in the database.

- **Model** (`main/models.py`) — defines the `Student` table
  (`first_name`, `last_name`, `email`, `course`, `year_level`,
  `date_enrolled`).
- **View** (`main/views.py`) — the `home` view fetches all `Student`
  records and passes them to a template.
- **URL** (`main/urls.py` + `config/urls.py`) — routes `/` to the
  `home` view.
- **Template** (`main/templates/main/home.html`) — renders the
  student list as a styled HTML table (`main/static/main/style.css`).

## Project structure

```
quiz3_django/
├── config/                 # Project package (settings, urls, wsgi)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                    # The app
│   ├── models.py            # Student model
│   ├── views.py              # home view
│   ├── urls.py                # app routes
│   ├── admin.py                # Student registered for Django admin
│   ├── templates/main/home.html
│   ├── static/main/style.css
│   └── management/commands/seed_students.py   # adds sample data
├── manage.py
├── requirements.txt
└── .gitignore
```

## Running it locally

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

# Add sample student records (3 are required; this adds 4):
python manage.py seed_students

# Or create an admin account and add records yourself:
python manage.py createsuperuser

python manage.py runserver
```

Then open the local URL shown in the terminal (usually
`http://127.0.0.1:8000/`). Visit `/admin/` to add, edit, or delete
students through the Django admin.

## Deploying

1. **GitHub** — push this whole folder (the `.gitignore` already
   excludes `venv/`, `db.sqlite3`, and `__pycache__/`).
2. **PythonAnywhere** — clone the GitHub repo (or upload it), create
   a virtualenv, `pip install -r requirements.txt`, run
   `migrate` and `seed_students`, then point a Web app at
   `config/wsgi.py` and reload.

Submit both links (PythonAnywhere + GitHub) as required by the quiz
instructions.
