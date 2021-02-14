import os
import unittest
import json
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}@{}/{}".format('postgres:123','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question={
            'question':'how many days are in the year?',
            'answer':"365",
            'difficulty':1,
            'category':"Science"
        }
        self.quiz={
        "previous_questions":[8,9],
        "quiz_category":{
            "type":"Science",
            "id":1
        }
        }
        self.quiz_error={
        "quiz_category":{
            "type":"Science",
            "id":1
        }
        }

        # binds the app to the current context
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
        
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
     
    def test_get_pantigate_questions(self):
        res=self.client().get('/questions?page=1')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])
        self.assertTrue(data['questions'])

    def test_404_get_pantigate_questions_error(self):
        res=self.client().get('/questions?page=1000')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEquals(data['message'],"resource not found")   
    
    def test_delete_question(self):
        res=self.client().delete('/questions/2')
        data=json.loads(res.data)
        question=Question.query.filter(Question.id==2).one_or_none()
        self.assertEquals(res.status_code,200)
        self.assertEquals(data['success'],True)
        self.assertEquals(question,None)
        self.assertEquals(data['deleted_id'],2)

    def test_422_delete_questions_error(self):
        res=self.client().delete('/questions/600')
        data=json.loads(res.data)
        self.assertEquals(res.status_code,422)
        self.assertEquals(data['success'],False)
        self.assertEquals(data['message'],"unprocessable")
             
       
    def test_post_question(self):
        res=self.client().post('/questions',json=self.new_question) 
        data=json.loads(res.data)

        self.assertEquals(res.status_code,200)
        self.assertEquals(data['success'],True)
        self.assertTrue(len(data["current_questions"]))  
        self.assertTrue(data['current_questions'])
    
    def error_400_test_post_question(self):
        res=self.client().post('/questions',json={
            'question':'how many days are in the year?',
            'answer':"365"}) 
        data=json.loads(res.data)
        self.assertEquals(res.status_code,400)
        self.assertEquals(data['success'],False) 
        self.assertEquals(data['message'],"bad request")    
    
    def test_search_question(self):
        res=self.client().post('/questions/search',json={'searchTerm':'Which'})
        data=json.loads(res.data)    
        self.assertEquals(data['success'],True)
        self.assertEquals(res.status_code,200)
        self.assertTrue(data['questions'])

    def error_404_test_search_question(self):
        res=self.client().post('/questions/search',json={'searchTerm':'mohamed'})
        data=json.loads(res.data)    
        self.assertEquals(data['success'],False)
        self.assertEquals(res.status_code,404)
        self.assertEquals(data['message'],"resource not found") 

    def error_422_test_search_question(self):
        res=self.client().post('/questions/search',json={'search':'mohamed'})
        data=json.loads(res.data)    
        self.assertEquals(data['success'],False)
        self.assertEquals(res.status_code,422)
        self.assertEquals(data['message'],"unprocessable")    


    def test_get_question_by_category(self):
        res=self.client().get('/categories/1/questions')
        data=json.loads(res.data)
        self.assertEquals(data['success'],True)
        self.assertEquals(res.status_code,200)
        self.assertTrue(data['current_category'])
        self.assertTrue(data['questions'])

    def error_404_test_get_question_by_category(self):
        res=self.client().get('/categories/9/questions')
        data=json.loads(res.data)
        self.assertEquals(data['success'],False)
        self.assertEquals(res.status_code,404)
        self.assertEquals(data['message'],"resource not found")  

    
    def test_quiz(self):
        res=self.client().post('/quizzes',json=self.quiz)    

        data=json.loads(res.data)
        self.assertEquals(data['success'],True)
        self.assertEquals(res.status_code,200)
        self.assertTrue(data["previous_questions"])
        self.assertTrue(data["question"])

    def error_422_test_quiz(self):
        res=self.client().post('/questions/search',json=self.quiz_error)
        data=json.loads(res.data)    
        self.assertEquals(data['success'],False)
        self.assertEquals(res.status_code,422)
        self.assertEquals(data['message'],"unprocessable")  


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()