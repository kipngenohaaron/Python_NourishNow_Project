# Import necessary Flask modules and extensions
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import User, db, Donation, Article

# Create a Flask application instance
app = Flask(__name__)

# Configure the database URI and disable modification tracking
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nourishnow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the Flask-Migrate extension
migrate = Migrate(app, db)

# Initialize the SQLAlchemy extension with the app
db.init_app(app)

# Define the route for creating an article
@app.route('/articles', methods=['POST'])
def create_article():
    # Get JSON data from the request
    data = request.get_json()
    
    # Get the user ID from the JSON data
    user_id = data.get('user_id')
    
    # Query the User model to get the user object
    user = User.query.get(user_id)

    if user:
        # Create a new article using data from the request
        new_article = Article(
            user=user,
            author=user.name,
            title=data['title'],
            body=data['body']
        )
        # Add and commit the new article to the database
        db.session.add(new_article)
        db.session.commit()
        return jsonify({'message': 'Article created successfully'}), 201
    else:
        return jsonify({'message': 'User not found'}), 404

# Define the route for accessing a user's articles
@app.route('/articles/user/<int:user_id>', methods=['GET'])
def get_user_articles(user_id):
    # Query the User model to get the user object
    user = User.query.get(user_id)

    if user:
        # Query the Article model to get the user's articles
        articles = Article.query.filter_by(user_id=user_id).all()
        article_list = []

        for article in articles:
            # Create a dictionary with article data
            article_data = {
                'id': article.id,
                'author': article.author,
                'title': article.title,
                'body': article.body,
            }
            article_list.append(article_data)

        return jsonify({'articles': article_list})
    else:
        return jsonify({'message': 'User not found'}), 404

# Define the route for retrieving a specific article by ID
@app.route('/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    # Query the Article model to get the article object
    article = Article.query.get(article_id)

    if article:
        # Create a dictionary with article data
        article_data = {
            'id': article.id,
            'author': article.author,
            'title': article.title,
            'body': article.body,
        }
        return jsonify(article_data)
    else:
        return jsonify({'message': 'Article not found'}), 404

# Define the route for the home page
@app.route('/')
def index():
    return 'Hello World!'

# Define the route for user registration
@app.route('/signUp', methods=['POST'])
def create_user():
    # Create a new user object using data from the request
    new_user = User(name=request.json['name'], email=request.json['email'], password=request.json['password'])
    # Add and commit the new user to the database
    db.session.add(new_user)
    db.session.commit()

    # Create a dictionary with user data
    new_user_data = {
        'id': new_user.id,
        'name': new_user.name,
        'email': new_user.email
    }

    return jsonify(new_user_data)

# Define the route for user sign-in
@app.route('/signIn', methods=['POST'])
def signIn():
    # Query the User model to find a user with the provided email and password
    user = User.query.filter(User.email == request.json['email'], User.password == request.json['password']).first()
    if user is not None:
        # Create a dictionary with user data
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email
        }
        return jsonify(user_data, {'message': 'Login Successful'})
    else:
        return jsonify({'message': 'Invalid Credentials'})

# Define the route for adding cash donations
@app.route('/donateFunds/<int:id>', methods=['POST'])
def donate_funds(id):
    # Query the User model to get the user object
    user = User.query.filter(User.id == id).first()
    # Create a new donation object for cash
    donation = Donation(user=user, type="Cash", amount=request.json['amount'])
    # Add and commit the new donation to the database
    db.session.add(donation)
    db.session.commit()

    # Create a dictionary with donation data
    donation_data = {
        'id': donation.id,
        'user_id': donation.user_id,
        'type': donation.type,
        'amount': donation.amount,
        'date': donation.date
    }

    return jsonify(donation_data)

# Define the route for adding food donations
@app.route('/donateFood/<int:id>', methods=['POST'])
def donate_food(id):
    # Query the User model to get the user object
    user = User.query.filter(User.id == id).first()
    # Create a new donation object for food
    donation = Donation(user=user, type="Food", amount=request.json['amount'])
    # Add and commit the new donation to the database
    db.session.add(donation)
    db.session.commit()

    # Create a dictionary with donation data
    donation_data = {
        'id': donation.id,
        'user_id': donation.user_id,
        'type': donation.type,
        'amount': donation.amount,
        'date': donation.date
    }

    return jsonify(donation_data)

# Define the route for accessing a user's donations
@app.route('/userDonations/<int:id>')
def get_user_donations(id):
    # Query the User model to get the user object
    user = User.query.filter(User.id == id).first()
    # Get the user's donations
    donations = user.donations
    donation_list = []
    for donation in donations:
        # Create a dictionary with donation data
        donation_list.append({
            'id': donation.id,
            'user_id': donation.user_id,
            'type': donation.type,
            'amount': donation.amount,
            'date': donation.date
        })
    return jsonify(donation_list)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
