
# LemurConnect

LemurConnect is a social networking platform for professionals to connect, share, and collaborate. This Django-React application provides a robust backend API with a sleek, responsive frontend.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project uses Django as a backend framework to provide a RESTful API and React for the frontend to create an interactive user experience.

## Features

- User Authentication
- Profile Management
- Post/Update Sharing
- Real-time Notifications
- API Integration

## Technology Stack

- **Frontend:** React, Redux for state management
- **Backend:** Django REST Framework for a powerful API backend
- **Database:** SQLite for development, PostgreSQL for production
- **Styling:** Bootstrap for responsive design

## Setup and Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/sapg-dev/lemurconnect.git
   ```
2. Navigate to the project directory:
   ```shell
   cd lemurconnect
   ```
3. Install backend dependencies:
   ```shell
   pip install -r requirements.txt
   ```
4. Apply migrations to create the database schema:
   ```shell
   python manage.py migrate
   ```
5. Collect static files(before that the build directory should be created and populated with the optimized build production):
   ```shell
   python manage.py collectstatic --noinput
   ```
6. Install frontend dependencies:
   ```shell
   npm install
   ```
7. Start the frontend development server:
   ```shell
   npm start
   ```
8. Start the backend development server:
   ```shell
   python manage.py runserver
   ```

## Configuration



## Troubleshooting Common Issues

I had an enormous amount of trouble getting this project deployed online. At first, I thought that it would be much simpler to have the frontend hosted using Netlify, and hosting the backend through PythonAnywhere, and simply connecting both through a proxy set-up in packages.json, and changing the axios.defaults.baseURL to my PythonAnywhere domain. However, this solution did not work for a couple of reasons, to begin with, the Axios request was corrupted on arrival. The issues I encountered included CORS (Cross-Origin Resource Sharing) errors, which are common when the frontend and backend are hosted on different domains. Even after setting the proxy, the browser security model was blocking the requests from being executed.  To resolve these issues, I had to ensure that the backend server provided the appropriate CORS headers to allow for cross-origin requests from the frontend domain. This involved configuring my PythonAnywhere backend to set headers like Access-Control-Allow-Origin to include my Netlify domain. I also made sure to return the correct headers for OPTIONS preflight requests, which are automatically made by browsers in a CORS context.  After fixing the CORS configuration, I faced another hurdle: the proxy configuration in package.json was not being respected by Netlify upon deployment because it only works in a development environment created by create-react-app. For a production environment, I needed to set up a Netlify _redirects file or netlify.toml to handle proxying.  Lastly, I discovered that the issue with Axios requests being "corrupted on arrival" was due to a misconfiguration in the way I was serializing data before sending it over Axios. I had to ensure that the request payloads were correctly formatted as JSON, and any necessary Content-Type headers were being set to application/json. Ultimately, despite my efforts to separate the frontend and backend between Netlify and PythonAnywhere, the solution didn’t work out as planned. The issues with Axios and CORS proved too complex to resolve within my project's timeline and with the hosting configurations I had initially chosen. After wrestling with numerous deployment errors and configuration mismatches, I decided to simplify the approach.  I moved all components of my project to be served from PythonAnywhere. By hosting both the frontend and the backend on the same platform, I could avoid the CORS issues that arise with cross-domain requests entirely. I adapted my codebase to serve the React-built static files directly from PythonAnywhere, treating them as I would any static assets in a traditional web application.  This change meant configuring my PythonAnywhere account to handle static files and point to the compiled React project as the root for my website's static resources. I updated my application's routes to render these static templates, which allowed me to maintain a single domain for both my API and the user interface without the need for complex proxy configurations.  Rendering static templates through PythonAnywhere simplified the architecture, reduced points of failure, and allowed for a more straightforward debugging process. It was a compromise between my ideal deployment strategy and what was practical, ensuring that my project was online and functional for users. Sometimes, deploying both parts of a web application on the same service is the most effective way to manage and troubleshoot it, especially when external factors like time and complexity are at play.

By using pythonanywhere, I had to perform relatively small changes to my settings.py, and my index.js: 

```python
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORS_ALLOW_ALL_ORIGINS = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'your-pythonanywhere-domain.com',
    # ... other hostnames ...
]

CORS_ALLOWED_ORIGINS = [
    'https://your-frontend-domain.com',
    # ... additional origins ...
]

# Application definition

INSTALLED_APPS = [
    # ... your Django apps ...
    'corsheaders',
    # ... other installed apps ...
]

MIDDLEWARE = [
    # ... other middleware classes ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ... other middleware classes ...
]

ROOT_URLCONF = 'your_project.urls'

TEMPLATES = [
    # ... your templates settings ...
]

TEMPLATES_DIR = os.path.join(BASE_DIR, '..', 'frontend', 'build')

WSGI_APPLICATION = 'your_project.wsgi.application'

# ... your database configuration ...

# ... your password validation configuration ...

# ... your user authentication model ...

# Internationalization
# ... your internationalization settings ...

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', 'frontend', 'build', 'static'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')

# ... your GitHub OAuth client configuration ...

```
And for the index.js file, I simply had to add this line:
```javascript
// Set the base URL for all Axios requests
axios.defaults.baseURL = 'https://your-backend-domain.com';
```

### Dependency Conflicts

This issue might have only been caused by my local machine. I had a node_modules folder placed outside of the root directory, which when I decided to use ```  
npm start/npm run build```
would output a dependency error. A temporary solution I found  was to:

- Run `npm ls babel-jest` to check for babel-jest installations.
- Use `npm prune --production` to remove extraneous packages.
- Update project dependencies with `npm update`.

but also change the start/build scripts in packages.json to : ```"start": "set \"NODE_OPTIONS=--openssl-legacy-provider\" && react-scripts start" ```, of course change start to build for the build command. This solved the problem on the surface but not fully.

### Static Files Not Found

Ensure Django settings for `STATIC_URL` and `STATIC_ROOT` are configured properly and `DEBUG` is True during development.

### Database Table Errors

- Run `python manage.py migrate` to ensure all migrations are applied.
- Check if the SQLite3 database file is present and intact.


### Build and Deployment on Netlify

Adjust build scripts for Netlify deployment to use the Linux environment settings.


## Contributing

I welcome contributions! Please read my [CONTRIBUTING.md](CONTRIBUTING.md)(soon to come) for details on my code of conduct and the process for submitting pull requests to this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

- Email: s@pacifictrout.com

---

