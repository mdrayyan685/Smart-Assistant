import random

def generate_logic_questions(text):
    lines = [l.strip() for l in text.split('\n') if len(l.strip()) > 50]
    questions = random.sample(lines, min(3, len(lines)))
    return [f"What does this statement mean? -> \"{q}\"" for q in questions]
