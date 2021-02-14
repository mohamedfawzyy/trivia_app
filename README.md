# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### install project dependencies Backend

1. install virtual ENV
2. activate virtual ENV
3. install requirments in  `requirements.txt`
4. Run the development server

```
python -m virtualenv env
source env/bin/activate
pip install -r requirements.txt
set FLAK_APP=flaskr
set FLASK_ENV=development
flask run
```
### API Reference

- start server by pasting this url in the browser   `http://127.0.0.1:5000/`

## Endpoints
 

1. ## GET categories

- Request `curl http://127.0.0.1:5000/categories`
- Response
```
{
  "access": true,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "total_categories": 6
}
```
2. ## GET questions

- Request `curl http://127.0.0.1:5000/questions`
- Response 
return 10 questions per page.
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": "Entertainment",
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "AlAhly",
      "category": "Sports",
      "difficulty": 4,
      "id": 3,
      "question": "the last team won the Egyotian league?"
    },
    {
      "answer": "Tom Cruise",
      "category": "Entertainment",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "Entertainment",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "Sports",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "Sports",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "Lake Victoria",
      "category": "Geography",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "Geography",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "Geography",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "Art",
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist-initials M C was a creator of optical illusions?"
    }
  ],
  "success": true,
  "total_questions": 17
}
```
3. Delete question 
- Request `curl -X Delete http://127.0.0.1:5000/questions/2`
- Response 
```
{
  "deleted_id": 2,
  "success": true
}
```

4. ## Post questions

- Request 
```
curl -X POST -H "Content-Type:application/json" -d "{\"question\":\"the last team won the Egyotian league?\",\"answer\":\"AlAhly\",\"category\":\"Sports\",\"difficulty\":4}" http://127.0.0.1:5000/questions
```
- Response
```
{
  "current_questions": [
    {
      "answer": "Tom Cruise",
      "category": "Entertainment",
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": "Entertainment",
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": "Sports",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "Sports",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "Lake Victoria",
      "category": "Geography",
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "Geography",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "Geography",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "Art",
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist-initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": "Art",
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": "Art",
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }
  ],
  "success": true
}
```
5. ## search question
- Request 
```
curl -X POST -H "Content-Type:application/json" -d "{\"searchTerm\":\"Which\"}" http://127.0.0.1:5000/questions/search
```
- Response
```
{
  "currentCategory": null,
  "questions": [
    {
      "answer": "Brazil",
      "category": "Sports",
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": "Sports",
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": "Geography",
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": "Geography",
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": "Art",
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist-initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Jackson Pollock",
      "category": "Art",
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "Scarab",
      "category": "History",
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "totalQuestions": 7
}
```
6. ## GET question by category
- Request `curl http://127.0.0.1:5000/categories/1/questions`

- Response
```
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": "Science",
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": "Science",
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": "Science",
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```
7. ## get quizzes
- Request `curl -H "Content-Type:application/json" -d "@data.json" -X POST http://127.0.0.1:5000/quizzes`
- `data.json` is a file with json data 
```
{
    "previous_questions":[16,17],
    "quiz_category":{
        "type":"Art",
        "id":2
    }
}
```
- Response
```
1:5000/quizzes
{
  "previous_questions": [
    16,
    17,
    19
  ],
  "question": {
    "answer": "Jackson Pollock",
    "category": "Art",
    "difficulty": 2,
    "id": 19,
    "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
  },
  "success": true
}
```
## Error handler

1. ## 404 not found
- Request `curl http://127.0.0.1:5000/categories/9/questions`
- Response 
```
{
  "error": 404,
  "message": "resource not found",
  "success": false
}
```
2. ## and so on for  422, 400 errors



### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

### Requirements
- `install npm`

## start server
- `npm start`

### Authors
Mohamed fawzy authored the API (__init__.py), test suite (test_flaskr.py), and this README.and others files were created by [Udacity](https://www.udacity.com) 
