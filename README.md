# CoC Stantanpuram — Church Blog Website

Full-stack Django blog website built with SQLite, Bootstrap 5.

## Deploy to Render (Free)

1. Push this repo to **GitHub**
2. Go to https://render.com → **New Web Service**
3. Connect your GitHub repo
4. Set:
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn Blog.wsgi`
5. Click **Create Web Service**

App will auto-deploy on every push to `main`.

## Deploy to PythonAnywhere (Free)

1. Push to GitHub
2. Open bash console on PythonAnywhere
3. Clone: `git clone https://github.com/Rayapparaju/blog_CoCStantanpuram.git`
4. Set up virtualenv and install requirements
5. Configure WSGI file to point to `Blog.wsgi`
6. Set `DEBUG = False` and `ALLOWED_HOSTS` in settings

## Run Locally

```bash
cd Blog
pip install -r requirements.txt
python manage.py runserver
```

Admin: `/admin/` — user: `admin` / password: `admin123`
