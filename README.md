# Kapadia High School Website

A Django-based website for Kapadia High School, showcasing the school's campuses, facilities, and CBSE certification documents.

## Features

- Multiple campus pages (Chandkheda, Chhatral, IFFCO Township, Kadi)
- CBSE certification document access
- Responsive design with Bootstrap
- Campus facilities showcase

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Run the development server:
   ```
   python manage.py runserver
   ```

## Deployment on Render

### Prerequisites

1. Create a [Render](https://render.com/) account
2. Create a new PostgreSQL database on Render (optional, can use SQLite for small sites)

### Deployment Steps

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure the following settings:
   - **Name**: kapadia-high-school (or your preferred name)
   - **Environment**: Python
   - **Region**: Choose the region closest to your users
   - **Branch**: main (or your default branch)
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn kapadiaschool.wsgi:application`
   - **Plan**: Free (or choose a paid plan for production)

4. Add the following environment variables:
   - `SECRET_KEY`: Generate a new secret key
   - `DEBUG`: Set to False for production
   - `DATABASE_URL`: If using Render PostgreSQL, this will be automatically added

5. Click "Create Web Service"

Your website will be deployed and available at the URL provided by Render.

## Project Structure

- `kapadiaschool/` - Main project directory
  - `kapadiaschool/` - Project settings
  - `khschool/` - Main app
  - `templates/` - HTML templates
  - `static/` - Static files (CSS, JS, images)
  - `gallery/` - Media files
  - `requirements.txt` - Python dependencies
  - `build.sh` - Build script for Render
  - `Procfile` - Process file for web servers
  - `runtime.txt` - Python version specification
