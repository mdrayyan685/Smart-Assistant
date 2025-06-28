from transformers import pipeline

summarizer = pipeline("summarization")

def generate_summary(text, max_words=150):
    summary = summarizer(text[:3000], max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
