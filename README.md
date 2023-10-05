
# Flask Donation and Article Management App

This is a Flask-based web application for managing user donations and articles. It allows users to create accounts, make cash or food donations, write articles, and view their donation and article history. The application uses SQLAlchemy to interact with a SQLite database.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Routes and Endpoints](#routes-and-endpoints)
- [Database Models](#database-models)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these steps to get the Flask application up and running:

1. Clone the repository to your local machine:
   ```shell
   git clone https://github.com/yourusername/flask-donation-app.git
   cd flask-donation-app
   ```

2. Create a virtual environment (optional but recommended):
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   ```

3. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

4. Initialize the SQLite database:
   ```shell
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Start the Flask application:
   ```shell
   flask run
   ```

6. Access the application in your web browser at `http://localhost:5000`.

## Features

- User registration and authentication.
- Cash and food donation functionality.
- Article creation and retrieval.
- Viewing user donation and article history.
- A simple home page.

## Routes and Endpoints

- `/` (Home Page)
- `/signUp` (User Registration)
- `/signIn` (User Authentication)
- `/donateFunds/<int:id>` (Add Cash Donation)
- `/donateFood/<int:id>` (Add Food Donation)
- `/userDonations/<int:id>` (View User's Donations)
- `/articles` (Create Article)
- `/articles/user/<int:user_id>` (View User's Articles)
- `/articles/<int:article_id>` (View Specific Article)

## Database Models

### User Model

- `id` (Primary key and unique identifier)
- `name` (User's name)
- `email` (User's email address, unique)
- `password` (User's password)
- Relationships:
  - `donations` (One-to-many relationship with `Donation` model)
  - `articles` (One-to-many relationship with `Article` model)

### Donation Model

- `id` (Primary key and unique identifier)
- `user_id` (Foreign key referencing the `User` model)
- `type` (Type of donation, e.g., "Cash" or "Food")
- `amount` (Donation amount or quantity)
- `date` (Date and time of the donation, defaulting to the current UTC time)

### Article Model

- `id` (Primary key and unique identifier)
- `user_id` (Foreign key referencing the `User` model)
- `author` (Author's name, can be the same as the user's name)
- `title` (Title of the article)
- `body` (Content of the article as text)

## Usage Examples

You can use tools like Postman to interact with the API and test the routes and endpoints described above. Refer to the provided examples in the Postman section of this README for detailed steps on adding donations and articles.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

