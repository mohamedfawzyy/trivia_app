import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def pantiagte_questions(request,collections):
  page=request.args.get('page',1,type=int)
  start=(page-1)*QUESTIONS_PER_PAGE
  end=start+QUESTIONS_PER_PAGE
  current_questions=[question.format() for question in collections]
  return current_questions[start:end]

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors=CORS(app,resources={r"/api/*":{"origins":"*"}})
  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,PATCH,POST,DELETE,OPTIONS')
    return response
  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories',methods=['GET'])
  def get_categories():
    categories=Category.query.order_by(Category.id).all()
    allCategories={}
    for category in categories:
      allCategories[category.id]=category.type
    return jsonify({
      "access":True,
      "categories": allCategories,
      "total_categories":len(categories)
    })
   

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 
  
  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions',methods=['GET'])
  def get_questions():
    questions=Question.query.order_by(Question.id).all()
    categories=Category.query.order_by(Category.id).all()
    current_questions=pantiagte_questions(request,questions)
    if len(current_questions) == 0:
      abort(404)
    allCategories={}
    for category in categories:
      allCategories[category.id]=category.type

    return jsonify({
      "categories":allCategories,
      "success":True,
      "questions":current_questions,
      "total_questions":len(questions),
      "current_category":None
    })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>',methods=['DELETE'])
  def delete_question(question_id):
    try:
      question=Question.query.filter(Question.id == question_id).one_or_none()
      if question is None:
        abort(404)
      question.delete()
      
      
      return jsonify({
      
        "success":True,
        "deleted_id":question_id,
        
      })  
    except:
      abort(422)  
      
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  
  @app.route('/questions',methods=['POST'])
  def create_question():
    body=request.get_json()
    try:
      new_question=body.get('question',None)
      new_answer=body.get('answer',None)
      difficulty=body.get('difficulty',None)
      category=body.get('category',None)
      question=Question(question=new_question,answer=new_answer,difficulty=difficulty,category=category)
      question.insert()
      current_questions=pantiagte_questions(request,Question.query.all())
      return jsonify({
        "success":True,
        "current_questions":current_questions
      })
    except:
      abort(400)
  
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  
  @app.route('/questions/search',methods=['POST'])
  def search_question():
    body=request.get_json()
    search=body.get('searchTerm',None)
    try:
      collections=Question.query.filter(Question.question.ilike('%{}%'.format(search))).all()
      if len(collections) == 0:
        abort(404)
      current_questions=pantiagte_questions(request,collections)
      return jsonify({
        "questions":current_questions,
        "totalQuestions":len(collections),
        "currentCategory":None,
        "success":True
      })  
    except:
      abort(422)
      
  ''' 
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions',methods=['GET'])
  def get_question_by_category(category_id):
    category=Category.query.filter(Category.id==category_id).one_or_none()
    if category is None:
      abort(404)
    else:
      questions=Question.query.filter(Question.category==category.type).all()
      current_questions=pantiagte_questions(request,questions)
      return jsonify({
        "questions":current_questions,
        "success":True,
        "total_questions":len(questions),
        "current_category":category.type
      })  

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes',methods=['POST'])
  def play_quiz():
    body=request.get_json()
    previous_questions=body.get('previous_questions',None)
    quiz_category=body.get('quiz_category',None)
    used_questions=[]
    notused_questions=[]
    try:
      if quiz_category["id"] == 0 :
        questions=Question.query.order_by(Question.id).all()
      else:
        questions=Question.query.filter(Question.category == quiz_category["type"]).all()
      for question in questions:
        if question.id in previous_questions:
          used_questions.append(question)
        else:
          notused_questions.append(question)  
          
      current_notused_questions=pantiagte_questions(request,notused_questions)
      random_question=current_notused_questions[random.randint(0,len(current_notused_questions)-1)]
      previous_questions.append(random_question["id"])
      return jsonify({
       "success":True,
       "previous_questions":previous_questions,
       "question":random_question

      })
    except:
      abort(422)  


  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def error_not_found(error):
    return jsonify({
        "success":False,
        "message":"resource not found",
        "error":404
    }),404
  @app.errorhandler(422)
  def error_unprocessable(error):
    return jsonify({
        "success":False,
        "message":"unprocessable",
        "error":422
    }),422 
  @app.errorhandler(400)
  def error_bad_request(error):
    return jsonify({
        "success":False,
        "message":"bad request",
        "error":400
    }),400    
  return app

    