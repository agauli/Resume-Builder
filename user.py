from google.appengine.ext import db
import base
import table

class User(db.Model):
    user_name = db.StringProperty(required=True)
    first_name = db.StringProperty(required=True)
    last_name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    password = db.StringProperty(required=True)
    location = db.GeoPtProperty()
    signup_date = db.DateTimeProperty(auto_now_add=True)

    # This method returns the User if the given id matches
    # the id
    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid)
    
    # This method returns the user with given name
    @classmethod
    def by_name(cls, name):
        u = db.GqlQuery("SELECT * FROM User WHERE user_name = :1", name).get()
        return u

    # This method returns the user with given email
    @classmethod
    def by_email(cls, email):
        e = User.all().filter('email =', email).get()
        if e:
            return e
        else:
            return None

    # Creates the object User
    @classmethod
    def create_user(cls, first_name, last_name, user_name, email, password):
        return User(first_name=first_name,
                    last_name=last_name,
                    user_name=user_name,
                    email=email,
                    password=password)

    # Validates the user
    @classmethod
    def login(cls, email, pw):
        user = cls.by_email(email)
        if user and base.valid_pw(user.name, pw, user.password):
            return user
