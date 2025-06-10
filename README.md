# Django Translator App

This project is a simple translator app built with Django. It allows users to input text, select a target language, and get the translated result using the Python `translate` package.

## Features

- Input text to translate
- Select a target language
- Get instant translation results

## Getting Started

### Prerequisites

- Python 3.x
- Django
- `translate` package

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd pj_7_django
    ```

2. Install dependencies:
    ```bash
    pip install django translate
    ```

3. Run migrations:
    ```bash
    python manage.py migrate
    ```

4. Start the development server:
    ```bash
    python manage.py runserver
    ```

5. Open your browser and go to `http://127.0.0.1:8000/`

## Usage

- Enter the text you want to translate.
- Select the target language.
- Submit the form to see the translated text.

## Learning Goals

- Set up a Django project
- Create forms for user input
- Integrate third-party translation libraries
