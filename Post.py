import base
import json
import tables

class Question(base.RequestHandler):
    def post(self):
        output_json = {}
        user_name = self.request.get('user_name')
        question = self.request.get('question')
        course_tag = self.request.get('course_tag')
        if username and question and tag:
            
            
            questions = tables.Questions.create(
                user_name = self.user.user_name,
                question = question,
                course_tag = course_tag
            )
            questions.put()
            output_json['status'] = 'OK'
        else:
            output_json['status'] = 'ERR'
            output_json['error'] = 'Items are missing'