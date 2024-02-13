

# Amazing Spider-Man WebTracker
![Screenshot 2024-02-13 112308](https://github.com/PereiraJames/Spider-ManCollection/assets/82026997/faa6f4a1-8889-4302-a854-dedadc5b9a52)

Welcome to the Amazing Spider-Man WebTracker GitHub repository! This project is developed using Django Framework and leverages the Marvel API to track various aspects related to Spider-Man.

## Features
- Track information related to the Spider-Man issue (Collected, Damaged, Issue Number...)
- Utilizes the Marvel API for accessing Spider-Man related data.
- Database storage powered by MySQL.
- AJAX used for backend updating MySQL.
### Update database on the fly
![Screenshot 2024-02-13 112557](https://github.com/PereiraJames/Spider-ManCollection/assets/82026997/003991ac-ab55-4390-ba10-4b2fb7518504)

### Filter according to (Issue Number / State / Series Year)
![Screenshot 2024-02-13 112354](https://github.com/PereiraJames/Spider-ManCollection/assets/82026997/a9b4f69f-e675-4216-8079-1753839257e7)
![Screenshot 2024-02-13 112541](https://github.com/PereiraJames/Spider-ManCollection/assets/82026997/d4a1d453-6499-498b-9fcd-b42c65590b22)

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
