"""Defines handler paths and initializes the app."""
import webapp2
import base
import signup
import resume
import todo
import user
import lists


class MainPage(base.RequestHandler):
    def get(self, usr=None):
        if usr:
            u = user.User.by_name(usr)
            if u:
                self.redirect('/' + usr + '/resume')
            else:
                self.render('404.html')
        elif self.user:
            self.render("faq.html", loged_user=self.user)
        else:
            self.render("mainpage.html")


class FaqPage(base.RequestHandler):
    def get(self):
        self.render("faq.html")


class SettingsPage(base.RequestHandler):
    def get(self):
        self.render("settings.html")
 
      
class CatPage(base.RequestHandler):
    def get(self):
        self.render("cats.html")


class ListPage(base.RequestHandler):
    def get(self):
        if self.user:
            self.render("lists.html", loged_user=self.user)
        else:
            self.render('/')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/catclicker', CatPage),
    ('/todo', todo.ToDoPage),
    ('/todo_json', todo.GetJSON),
    ('/updatetodo', todo.Update),
    ('/settings', SettingsPage),
    ('/signup', signup.SignUp),
    ('/login', signup.Login),
    ('/question', Post.Question),
    ('/logout', signup.Logout),
    ('/welcome', signup.ConfirmUserSignup),
    ('/resume', resume.Resume),
    (r'/resume/(.*)', resume.Resume),
    ('/resume_json', resume.GetJSON),
    ('/updateresume', resume.UpdateEducation),
    ('/updatework', resume.UpdateWork),
    ('/updateaward', resume.UpdateAward),
    ('/updatepublication', resume.UpdatePublication),
    ('/updateselfsummary', resume.UpdateSelfSummary),
    ('/updatetechnicalskill', resume.UpdateTechnicalSkill),
    ('/editpublication', resume.EditPublication),
    ('/editeducation', resume.EditEducation),
    ('/editwork', resume.EditWork),
    ('/editaward', resume.EditAward),
    ('/deleteeducation', resume.DeleteEducation),
    ('/deletework', resume.DeleteWork),
    ('/deleteaward', resume.DeleteAward),
    ('/deletepublication', resume.DeletePublication),
    ('/lists', ListPage),
    ('/createshoppinglist', lists.CreateShoppingList),
    ('/lists_get_json', lists.GetJson),
    ('/createcourse', lists.CreateCourse),
    ('/updatecourse', lists.UpdateCourse)
    ], debug=True)
