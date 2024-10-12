from flask_sqlalchemy import SQLAlchemy
import datetime
import enum



db = SQLAlchemy()


class MyEnum(enum.Enum):
    one = 1
    two = 2
    three = 3

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    picture = db.Column(db.String(250), unique=True, nullable=True)
    # levelAccess = db.Column(db.Enum(MyEnum))
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "tel": self.tel,
            "picture": self.picture,
            "email": self.email,
            # do not serialize the password, it's a security breach
        }


#    def get_reset_token(self, expires_sec=1800):
 #       s = Serializer(app.config['SECRET_KEY'], expires_sec)
  #      return s.dumps({'user_id': self.id}).decode('utf-8')
    
   # @staticmethod
  #  def verify_reset_token(token):
   #     s = Serializer(app.config['SECRET_KEY'])
    #    try:
     #       user_id = s.loads(token)['user_id']
      #  except:
       #     return None
        #return User.query.get(user_id)
    
class Activities(db.Model):
    __tablename__ = "activities"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), unique=False, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    responsible = db.Column(db.String(80), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "responsible": self.responsible,
        }

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(250), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tel = db.Column(db.String(20), unique=False, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    picture = db.Column(db.String(255), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "description": self.description,
            "picture": self.picture,
        }

class Testimony(db.Model):
    __tablename__ = "testimony"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)
    dateTestimony = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "description": self.description,
            "dateTestimony": self.dateTestimony
        }

class PastEvents(db.Model):
    __tablename__ = "pastevents"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(300), unique=False, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    picture = db.Column(db.String(255), unique=False, nullable=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "date": self.date,
            "picture": self.picture
        }