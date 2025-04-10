# Django Movie Project

This Django project is designed to manage a movie collection. It allows users to add, view, update, and delete movies. It is a simple yet functional web application for managing movies.

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://bitbucket.org/xryanayrx/movie/src/master/
   cd movie
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source venv/bin/activate
     ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser to access the Django admin panel:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/` in your browser.

## Admin Access

To access the admin panel, visit `http://127.0.0.1:8000/admin/` and log in using the superuser credentials you created.

## Features

- Add, view, update, and delete movie records.
- Admin panel for managing movie data.

## License

This project is licensed under the MIT License.
