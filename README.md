# Amazing Spider-Man WebTracker

Welcome to the Amazing Spider-Man WebTracker GitHub repository! This project is developed using Django Framework and leverages the Marvel API to track various aspects related to Spider-Man.

## Features
- Track information related to the Spider-Man issue (Collected, Damaged, Issue Number...)
- Utilizes the Marvel API for accessing Spider-Man related data.
- Database storage powered by MySQL.
- AJAX used for backend updating MySQL.

## Technologies Used
- Django Framework
- Marvel API
- MySQL

## Installation
To run this project locally, follow these steps:
1. Clone the repository:
    ```bash
    git clone https://github.com/PereiraJames/Spider-ManCollection.git
    ```
2. Navigate into the project directory:
    ```bash
    cd Spider-ManCollection
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up your MySQL database and update the database settings in `settings.py` accordingly.
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```
7. Visit `http://localhost:8000` in your web browser to access the application.
