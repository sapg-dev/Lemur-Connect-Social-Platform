
# LemurConnect

LemurConnect is a social networking platform for professionals to connect, share, and collaborate. This Django-React application provides a robust backend API with a sleek, responsive frontend.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Troubleshooting Common Issues](#troubleshooting-common-issues)
- [FAQ](#faq)
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
   git clone https://github.com/yourusername/lemurconnect.git
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
5. Collect static files:
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

### Dependency Conflicts

- Run `npm ls babel-jest` to check for babel-jest installations.
- Use `npm prune --production` to remove extraneous packages.
- Update project dependencies with `npm update`.

### Static Files Not Found

Ensure Django settings for `STATIC_URL` and `STATIC_ROOT` are configured properly and `DEBUG` is True during development.

### Database Table Errors

- Run `python manage.py migrate` to ensure all migrations are applied.
- Check if the SQLite3 database file is present and intact.

- 
### Build and Deployment on Pythonanywhere

After days and days of troubleshooting, I decided to abandon my original idea of hosting the backend api on pythonanywhere, and the frontend on entlify and connecting both of them through a Proxy. I decided to try using cactus but without much success, and ultimately spent days and days trying and troubleshooting different methods to ensure I could host the backend and frontend on the same hosting provider. Although it wasn't easy, I ultimately used django's template generator which isn't very intuitive to use, but works incredibly well. Setting it up on Pythonanywhere, was however, an equation I thought I would never solve.

### Build and Deployment on Netlify

Adjust build scripts for Netlify deployment to use the Linux environment settings.


## Contributing

I welcome contributions! Please read my [CONTRIBUTING.md](CONTRIBUTING.md) for details on my code of conduct and the process for submitting pull requests to this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

- Email: s@pacifictrout.com

---

Please note that 'LemurConnect' is a placeholder name for the project repository. Replace 'yourusername' with your actual GitHub username and update the contact email to the project's support line.
