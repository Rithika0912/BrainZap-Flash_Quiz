from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Inbuilt questions data
inbuilt_questions_data = [
    {
        "Question": "What is the capital of France?",
        "Answer": "Paris",
        "Options": ["Paris", "Rome", "Berlin", "Madrid"],
        "Category": "Geography",
        "Difficulty": "Easy"
    },
    {
        "Question": "Who is the CEO of Tesla?",
        "Answer": "Elon Musk",
        "Options": ["Elon Musk", "Jeff Bezos", "Tim Cook", "Sundar Pichai"],
        "Category": "Business",
        "Difficulty": "Medium"
    },
    {
        "Question": "What is the chemical symbol for water?",
        "Answer": "H2O",
        "Options": ["H2O", "CO2", "O2", "N2"],
        "Category": "Chemistry",
        "Difficulty": "Easy"
    },
    {
        "Question": "Who wrote \"Romeo and Juliet\"?",
        "Answer": "William Shakespeare",
        "Options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Leo Tolstoy"],
        "Category": "Literature",
        "Difficulty": "Medium"
    },
    {
        "Question": "What is 5 + 7?",
        "Answer": "12",
        "Options": ["12", "10", "13", "15"],
        "Category": "Math",
        "Difficulty": "Easy"
    },
    {
        "Question": "Who invented the light bulb?",
        "Answer": "Thomas Edison",
        "Options": ["Thomas Edison", "Isaac Newton", "Alexander Graham Bell", "Nikola Tesla"],
        "Category": "History",
        "Difficulty": "Medium"
    },
    {
        "Question": "What is the largest planet in our Solar System?",
        "Answer": "Jupiter",
        "Options": ["Jupiter", "Earth", "Saturn", "Mars"],
        "Category": "Astronomy",
        "Difficulty": "Hard"
    },
    {
        "Question": "Who developed the theory of relativity?",
        "Answer": "Albert Einstein",
        "Options": ["Albert Einstein", "Isaac Newton", "Stephen Hawking", "Marie Curie"],
        "Category": "Science",
        "Difficulty": "Hard"
    },
    {
        "Question": "What is the longest river in the world?",
        "Answer": "Nile",
        "Options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "Category": "Geography",
        "Difficulty": "Medium"
    },
    {
        "Question": "Who discovered penicillin?",
        "Answer": "Alexander Fleming",
        "Options": ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Gregor Mendel"],
        "Category": "Medicine",
        "Difficulty": "Hard"
    },
    {
        "Question": "What is the smallest prime number?",
        "Answer": "2",
        "Options": ["2", "1", "3", "5"],
        "Category": "Math",
        "Difficulty": "Easy"
    },
    {
        "Question": "What gas do plants absorb?",
        "Answer": "Carbon Dioxide",
        "Options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Helium"],
        "Category": "Science",
        "Difficulty": "Easy"
    },
    {
        "Question": "How many continents are there?",
        "Answer": "7",
        "Options": ["7", "5", "6", "8"],
        "Category": "Geography",
        "Difficulty": "Easy"
    },
    {
        "Question": "Which planet is known as the Red Planet?",
        "Answer": "Mars",
        "Options": ["Mars", "Jupiter", "Saturn", "Venus"],
        "Category": "Astronomy",
        "Difficulty": "Easy"
    },
    {
        "Question": "What is the square root of 64?",
        "Answer": "8",
        "Options": ["8", "6", "7", "9"],
        "Category": "Math",
        "Difficulty": "Medium"
    },
    {
        "Question": "Who painted the Mona Lisa?",
        "Answer": "Leonardo da Vinci",
        "Options": ["Leonardo da Vinci", "Michelangelo", "Picasso", "Van Gogh"],
        "Category": "Art",
        "Difficulty": "Medium"
    },
    {
        "Question": "In which year did World War II end?",
        "Answer": "1945",
        "Options": ["1945", "1942", "1939", "1950"],
        "Category": "History",
        "Difficulty": "Hard"
    },
    {
        "Question": "Which language has the most native speakers?",
        "Answer": "Mandarin",
        "Options": ["Mandarin", "English", "Spanish", "Hindi"],
        "Category": "Language",
        "Difficulty": "Hard"
    },
    {
        "Question": "How many players are there in a football team?",
        "Answer": "11",
        "Options": ["11", "10", "12", "9"],
        "Category": "Sports",
        "Difficulty": "Easy"
    },
    {
        "Question": "What is the boiling point of water in Celsius?",
        "Answer": "100",
        "Options": ["100", "90", "80", "120"],
        "Category": "Chemistry",
        "Difficulty": "Easy"
    },
    {
        "Question": "Who is the author of Harry Potter?",
        "Answer": "J.K. Rowling",
        "Options": ["J.K. Rowling", "Stephen King", "Roald Dahl", "Suzanne Collins"],
        "Category": "Literature",
        "Difficulty": "Easy"
    },
    {
        "Question": "What is the currency of Japan?",
        "Answer": "Yen",
        "Options": ["Yen", "Won", "Renminbi", "Rupee"],
        "Category": "Economics",
        "Difficulty": "Medium"
    },
    {
        "Question": "What is the tallest mountain in the world?",
        "Answer": "Mount Everest",
        "Options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "Category": "Geography",
        "Difficulty": "Medium"
    },
    {
        "Question": "What does DNA stand for?",
        "Answer": "Deoxyribonucleic Acid",
        "Options": ["Deoxyribonucleic Acid", "Ribonucleic Acid", "Dinucleic Acid", "Nucleic Protein"],
        "Category": "Biology",
        "Difficulty": "Hard"
    },
    {
        "Question": "How many sides does a hexagon have?",
        "Answer": "6",
        "Options": ["6", "5", "7", "8"],
        "Category": "Math",
        "Difficulty": "Easy"
    },
    {
        "Question": "Which animal is known as the king of the jungle?",
        "Answer": "Lion",
        "Options": ["Lion", "Tiger", "Elephant", "Leopard"],
        "Category": "Biology",
        "Difficulty": "Easy"
    },
    {
        "Question": "Which is the fastest land animal?",
        "Answer": "Cheetah",
        "Options": ["Cheetah", "Lion", "Horse", "Leopard"],
        "Category": "Biology",
        "Difficulty": "Medium"
    },
    {
        "Question": "Who was the first man on the moon?",
        "Answer": "Neil Armstrong",
        "Options": ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard"],
        "Category": "History",
        "Difficulty": "Medium"
    },
    {
        "Question": "What is the national flower of India?",
        "Answer": "Lotus",
        "Options": ["Lotus", "Rose", "Jasmine", "Marigold"],
        "Category": "Culture",
        "Difficulty": "Easy"
    },
    {
        "Question": "Which ocean is the largest?",
        "Answer": "Pacific Ocean",
        "Options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
        "Category": "Geography",
        "Difficulty": "Medium"
    }
]

def load_questions():
    questions_for_quiz = []
    # Create a mutable copy of the inbuilt questions to shuffle
    shuffled_pool = list(inbuilt_questions_data) 
    random.shuffle(shuffled_pool)

    # Take the first 10 questions from the shuffled pool
    # Adjust this slice if you want more or fewer questions in the quiz
    selected_questions = shuffled_pool[:10] 

    for q_data in selected_questions:
        # Create a copy of choices to shuffle for each question instance
        choices = list(q_data["Options"]) 
        random.shuffle(choices)
        questions_for_quiz.append({
            "Question": q_data["Question"],
            "Answer": q_data["Answer"],
            "Choices": choices 
        })
    
    return questions_for_quiz

@app.route('/')
def index():
    return render_template('quiz.html', questions=load_questions())

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_answer = data['user_answer'].strip().lower()
    correct_answer = data['correct_answer'].strip().lower()
    result = 'correct' if user_answer == correct_answer else 'incorrect'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)