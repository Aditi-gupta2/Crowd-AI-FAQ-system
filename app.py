
from flask import Flask, render_template, request, redirect
from faq_model import get_best_answer
app = Flask(__name__)

faqs = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    q = request.form['question']
    a = get_best_answer(q)
    return render_template('result.html', question=q, answer=a)

@app.route('/admin')
def admin():
    return render_template('admin.html', faqs=faqs)

@app.route('/add_faq', methods=['POST'])
def add_faq():
    faqs.append({
        "question": request.form['question'],
        "answer": request.form['answer']
    })
    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)
