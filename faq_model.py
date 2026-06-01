
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_questions=[
"How to reset password?",
"How to register account?",
"How to contact support?"
]

faq_answers=[
"Use forgot password option.",
"Click signup button.",
"Contact support team."
]

def get_best_answer(user_question):
    vectorizer=TfidfVectorizer()
    vectors=vectorizer.fit_transform(faq_questions+[user_question])
    sim=cosine_similarity(vectors[-1],vectors[:-1])
    return faq_answers[sim.argmax()]
