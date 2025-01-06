
# Art Gallery Project

Welcome to the Art Gallery Project!
This Django-based application allows users to upload images and videos of artwork, complete with titles and captions. Users can easily search for artworks based on these criteria, making it a user-friendly platform for discovering and showcasing artistic expressions.

## Features

- Upload Artworks: Users can upload images and videos of their artwork.
- Search Functionality: Users can search for artworks by title or caption.
- User-Friendly Interface: A clean and intuitive interface that enhances user experience.
- Caching with Redis: Improved performance through caching, reducing database load.
- SQLite Database: Lightweight and easy-to-manage database for storing artwork information.


## Installation

Prerequisites

Before you begin, ensure you have the following installed:
Python (version 3.13 or higher)
Redis server

1.Clone the Repository
```bash
  git clone https://github.com/ErfanMelon/art-gallery.git
  cd art-gallery
```
2.Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3.Install Required Packages

Install Django and django-redis:

```bash
pip install django django-redis
```

4.Set Up the Database

Run the following commands to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

5.Run the Redis Server

Make sure your Redis server is running. You can start it using:

```bash
redis-server
```

6.Start the Development Server

Run the Django development server:

```bash
python manage.py runserver
```

7.Access the Application

Open your web browser and navigate to `http://127.0.0.1:8000` to view the application.