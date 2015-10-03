from google.appengine.ext import db

class Questions(db.Model):
    user_name = db.StringProperty(required=True)
    course_tag = db.StringProperty(required = True)
    question = db.TextProperty(required =True)
    date = db.DateTimeProperty(auto_now_add=True)
    
    @classmethod
    def create(cls, user_name, course_tag, question, date):
        return ShoppingList(
            user_name=user_name,
            course_tag=course_tag,
            question = question,
            date = date
        )
    
class Publication(db.Model):
    user_name = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    link = db.StringProperty()
    authors = db.StringProperty(required=True,
                                multiline=True
                                )

    @classmethod
    def create_publication(cls, user_name, title, link, authors):
        return Publication(user_name=user_name,
                           title=title,
                           link=link,
                           authors=authors
                           )
    
    @classmethod
    def by_user_name(cls, user_name):
        return Publication.all().filter('user_name =', user_name)

    @classmethod
    def by_id(cls, publication_id):
        return Publication.get_by_id(publication_id)


class Award(db.Model):
    user_name = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    details = db.TextProperty(required=True)

    @classmethod
    def creare_award(cls, user_name, title, details):
        return Award(user_name=user_name,
                     title=title,
                     details=details
                     )
        
    @classmethod
    def by_id(cls, award_id):
        return Award.get_by_id(award_id)

    @classmethod
    def by_user_name(cls, user_name):
        return Award.all().filter('user_name =', user_name)


class Work(db.Model):
    user_name = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    employer = db.StringProperty(required=True)
    start_date = db.StringProperty(required=True)
    end_date = db.StringProperty()
    details = db.TextProperty()
    
    @classmethod
    def creat_work(cls, user_name,
                   title, employer,
                   start_date, end_date, details):
        return Work(user_name=user_name,
                    title=title,
                    employer=employer,
                    start_date=start_date,
                    end_date=end_date,
                    details=details
                    )
    
    @classmethod
    def by_id(cls, work_id):
        return Work.get_by_id(work_id)

    @classmethod
    def by_user_name(cls, user_name):
        return Work.all().filter('user_name =', user_name).order('end_date')


class Education(db.Model):
    user_name = db.StringProperty(required=True)
    degree = db.StringProperty(required=True)
    majors = db.ListProperty(str, required=True)
    school = db.StringProperty(required=True)
    gpa = db.StringProperty()
    graduation = db.StringProperty(required=True)
    courses = db.ListProperty(str, required=True)
    
    @classmethod
    def create_edu(cls, user_name, degree,
                   school, majors, gpa, graduation, courses):
        return Education(user_name=user_name,
                         degree=degree,
                         school=school,
                         majors=majors,
                         gpa=gpa,
                         graduation=graduation,
                         courses=courses
                         )

    @classmethod
    def by_id(cls, edu_id):
        return Education.get_by_id(edu_id)

    @classmethod
    def by_user_name(cls, user_name):
        return Education.all().filter('user_name =',
                                      user_name).order('graduation')


class TechnicalSkill(db.Model):
    user_name = db.StringProperty(required=True)
    title = db.StringProperty(required=True)
    level = db.StringProperty(required=True)

    @classmethod
    def create_skill(cls, user_name, title, level):
        return TechnicalSkill(user_name=user_name,
                              title=title,
                              level=level
                              )

    @classmethod
    def by_id(cls, skill_id):
        return TechnicalSkill.get_by_id(skill_id)
    
    @classmethod
    def by_user_name(cls, user_name):
        return TechnicalSkill.all().filter('user_name =', user_name)


class ToDo(db.Model):
    user_name = db.StringProperty(required=True)
    task = db.StringProperty(required=True)
    status = db.BooleanProperty(required=True)
    date = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_id(cls, id):
        return ToDo.get_by_id(id)

    @classmethod
    def by_user_name(cls, user_name):
        return ToDo.all().filter('user_name =', user_name).order('date')

    @classmethod
    def create_todo(cls, user_name, task,):
        return ToDo(user_name=user_name,
                    task=task,
                    status=False)


class Summary(db.Model):
    user_name = db.StringProperty(required=True)
    summary = db.TextProperty(required=True)

    @classmethod
    def create_summary(cls, user_name, summary):
        return Summary(user_name=user_name,
                       summary=summary)

    @classmethod
    def by_id(cls, sid):
        return Summary.get_by_id(sid)

    @classmethod
    def by_user_name(cls, user_name):
        return Summary.all().filter('user_name =', user_name).get()


class ShoppingList(db.Model):
    user_name = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    items = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def create(cls, user_name, name, items):
        return ShoppingList(
            user_name=user_name,
            name=name,
            items=items
        )

    @classmethod
    def by_id(cls, list_id):
        return ShoppingList.get_by_id(list_id)

    @classmethod
    def get_by_user_name(cls, user_name):
        return ShoppingList.all().filter('user_name =',
                                         user_name).order('-created')


class Major(db.Model):
    user_name = db.StringProperty(required=True)
    subjects = db.StringProperty(required=True)
    completed = db.BooleanProperty(required=True)

    @classmethod
    def create_major(cls, user_name, subjects):
        return Major(user_name=user_name,
                     subjects=subjects,
                     completed=False
                     )

    @classmethod
    def by_id(cls, mid):
        return Major.get_by_id(mid)

    @classmethod
    def get_by_user_name(cls, user_name):
        return Major.all().filter('user_name = ', user_name)
