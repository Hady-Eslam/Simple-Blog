from itsdangerous.jws import TimedJSONWebSignatureSerializer as serializer
from flask_login import UserMixin
from flask import current_app
from App import login_manager, db




@login_manager.user_loader
def user_loaded(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(120), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)


    def generate_reset_token(self, expire_in=30):
        s = serializer(current_app.config['SECRET_KEY'], expires_in=expire_in)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    

    @staticmethod
    def varify_reset_token(token):
        s = serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
            return User.query.get(user_id)
        except:
            return None


    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
