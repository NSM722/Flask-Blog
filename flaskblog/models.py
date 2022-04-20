from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import my_database, login_manager, app
from flask_login import UserMixin #(the user is_authenticated, is_active, is_anonymous, get_id())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(my_database.Model, UserMixin):
    id = my_database.Column(my_database.Integer, primary_key=True)
    username = my_database.Column(my_database.String(10), unique=True, nullable=False)
    email = my_database.Column(my_database.String(120), unique=True, nullable=False)
    image_file = my_database.Column(my_database.String(20), nullable=False, default='default.jpg')
    password = my_database.Column(my_database.String(60), nullable=False)
    posts = my_database.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expiry_in_secs=1800):
        s = Serializer(app.config['SECRET_KEY'], expiry_in_secs)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
            s = Serializer(app.config['SECRET_KEY'])
            try:
                user_id = s.loads(token)['user_id']
            except:
                return None
            return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(my_database.Model):
    id = my_database.Column(my_database.Integer, primary_key=True)
    title = my_database.Column(my_database.String(100), nullable=False)
    date_posted = my_database.Column(my_database.DateTime, nullable=False, default=datetime.utcnow) # utc = 'Coordinated Universal Time'
    content = my_database.Column(my_database.Text, nullable=False)
    user_id = my_database.Column(my_database.Integer, my_database.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

