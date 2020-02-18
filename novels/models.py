from novels import db



class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username =db.Column(db.String(20),unique=True, nullable=False)
    email =db.Column(db.String(120),unique=True, nullable=False)
    password=db.Column(db.String(60),nullable=False)
    novel=db.relationship('Novel', backref='author',lazy=True)
    
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Novel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title =db.Column(db.String(100),unique=True, nullable=False)
    description =db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    
    def __repr__(self):
        return f"Novel('{self.title}', '{self.description}')"
