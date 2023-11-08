from flask import render_template
from app.questions import bp
from app.models.question import Question

@bp.route('/')
def index():
    questions = Question.query.all()
    return render_template('questions/index.html', questions=questions)