from transformers import pipeline

qa_model = pipeline("question-answering")

def answer_question(question, context):
    result = qa_model(question=question, context=context)
    return result['answer']
