from flask import Flask, render_template, request, jsonify, make_response
import csv
import random

app = Flask(__name__)

def load_questions():
    questions = []
    with open('quiz_data.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            question = {
                "Question": row['Question'],
                "Answer": row['Answer'],
                "Choices": [row['Option1'], row['Option2'], row['Option3'], row['Option4']],
                "Category": row['Category'],
                "Difficulty": row['Difficulty']
            }
            questions.append(question)
    
    return random.sample(questions, 10) if len(questions) >= 10 else questions

@app.route('/')
def index():
    quiz_questions = load_questions()
    response = make_response(render_template('quiz.html', questions=quiz_questions))
    response.headers["Cache-Control"] = "no-store"  # Prevent caching
    return response

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data.get('user_answer')
    correct_answer = data.get('correct_answer')

    if user_answer == correct_answer:
        return jsonify({"result": "correct"})
    else:
        return jsonify({"result": "wrong"})

if __name__ == '__main__':
    app.run(debug=True)
