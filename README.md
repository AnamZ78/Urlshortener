URL Shortener with Password Protection and Analytics

Overview:
A URL shortener that allows users to shorten URLs, set expiry times, and add password protection. It also provides access logs for analytics.

Features:
- Shorten URLs.
- Optional password protection.
- Set expiry time (default: 24 hours).
- View access logs for shortened URLs.

Technologies Used:
- Backend: Django (Python)
- Database: SQLite (with username: admin, password: admin)
- Frontend: HTML Forms

Prerequisites:
- Python 3.x
- Django (`pip install django`)
- SQLite (default with Django)
- Git (for cloning the project)

Steps to Run the Application:

1. Clone the GitHub Repository:
   git clone https://github.com/yourusername/yourprojectname.git

2. Navigate to the Project Directory:
   cd yourprojectname

3. Set up a Virtual Environment (optional):
   python3 -m venv venv
   Activate:
   On Windows: venv\Scripts\activate
   On Mac/Linux: source venv/bin/activate

4. Install Dependencies:
   pip install -r requirements.txt (or manually install Django: pip install django)

5. Set up the Database:
   python manage.py migrate

6. Create a Superuser:
   python manage.py createsuperuser

7. Run the Development Server:
   python manage.py runserver

8. Access the Application:
   Visit http://127.0.0.1:8000/ to use the URL shortener.

Database Credentials:
- Username: admin
- Password: admin
- Database: SQLite

How to Use:
1. Shorten URL: Enter a long URL, set a password/expiry, and click "Shorten."
2. Access Shortened URL: Visit the shortened URL and enter a password if set.
3. View Analytics: View access logs for each shortened URL.

Contributing:
Feel free to fork and create a pull request.

License:
MIT License
