import user
import base
import re
import json
from google.appengine.api import mail


NAME_RE = re.compile("^[a-zA-Z]{3,100}$")
EMAIL_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")
PASS_RE = re.compile("^.{5,20}$")


class SignUp(base.RequestHandler):
    def is_valid_name(self, username):
        if username and NAME_RE.match(username):
            u = user.User.by_name(username)
            if u:
                return (False, 'Username exists. Choose another.')
            else:
                return (True, 'Passed!')
        else:
            return (False, 'Username is not valid.')
        
    def is_valid_password(self, password):
        return password and PASS_RE.match(password)

    def is_valid_email(self, email):
        if email and EMAIL_RE.match(email):
            u = user.User.by_email(email)
            if u:
                return (False, 'There is an account ' +
                               'associated with that email.'
                        )
            else:
                return (True, 'Passed!')
        else:
            return (False, 'Email is not valid')
    
    def send_confirmation_email(self, user):
        message = mail.EmailMessage(sender="VirtualClass " +
                                    "<noreply@visitorspoint.appspotmail.com>",
                                    subject="Confirm your registration"
                                    )
        message.to = user.email
        message.body = "Welcome"
        message.html = """
        <html>
        <head>
        <link rel ="stylesheet"
        href="http://visitorspoint.appspot.com/stylesheets/main.css">
        </head>
        <body>
        <div class="title-top-curved">
           Welcome to Virtual Class!
        </div>
        <div class="box-top-menu">
          Congratulations!
        <p> You have sucessfully created an account in Foducate.
        Please click the link below to verify your account.
        </p>
        <p>You will not be able to access your account before verification.
        </p>
        <p>Thank you for using Foducate.</p>
        </div>
        </body>
        </html>
               <b>Welcome</b>
          """

    def post(self):
        has_error = False
        user_name = self.request.get('user_name')
        first_name = self.request.get('first_name')
        last_name = self.request.get('last_name')
        email = self.request.get('email')
        password = base.hash_str(self.request.get('password'))
        output_json = {}
        valid_name = self.is_valid_name(user_name)
        if not valid_name[0]:
            has_error = True
            output_json['user_name_error'] = valid_name[1]

        valid_email = self.is_valid_email(email)
        if not valid_email[0]:
            has_error = True
            output_json['email_error'] = valid_email[1]
    

        if has_error:
            output_json['status'] = 'ERR'
        else:
            u = user.User.create_user(first_name=first_name,
                                      last_name=last_name,
                                      user_name=user_name,
                                      email=email,
                                      password=password)
            coord = None
            # base.get_user_location(self.request.remote_addr)
            if coord:
                u.location = coord
            u.put()
            self.login(u)
            self.send_confirmation_email(u)
            output_json['status'] = 'OK'
        self.render_json(json.dumps(output_json))


class Login(base.RequestHandler):
    def post(self):
        user_name = self.request.get('login_name')
        password = base.hash_str(self.request.get('login_pass'))
        output_json = {}
        u = user.User.by_name(user_name)
        if u:
            if self.validate_password(u, password):
                self.login(u)
            else:
                output_json['status'] = 'ERR'
                output_json['password_error'] = 'Incorrect Password!'
        else:
            u = user.User.by_email(user_name)
            if u:
                if self.validate_password(u, password):
                    self.login(u)
                    output_json['status'] = 'OK'
                else:
                    output_json['status'] = 'ERR'
                    output_json['password_error'] = 'Incorrect password!'
            else:
                output_json['status'] = 'ERR'
                output_json['name_error'] = 'Invalid username!'
        self.render_json(json.dumps(output_json))
    
    def validate_password(self, user, password):
        return user.password == password


class Logout(base.RequestHandler):
    def get(self):
        self.logout(self.user)

