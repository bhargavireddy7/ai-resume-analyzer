def generate_questions(skills):

    questions = {

        "Communication": "Tell me about a time you handled communication challenges.",

        "Leadership": "Describe a leadership experience.",

        "Customer Service": "How would you handle an angry customer?",

        "Sports": "How has sports helped you develop teamwork skills?",

        "Coaching": "What qualities are important for a coach?",

        "Cash Handling": "How do you ensure accuracy while handling cash?"
    }

    generated_questions = []

    for skill in skills:

        if skill in questions:
            generated_questions.append(questions[skill])

    return generated_questions