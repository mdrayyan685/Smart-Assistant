import streamlit as st
from backend import document_parser, summarizer, qa_engine, logic_questioner

st.title("📄 Smart Research Summarization Assistant")

uploaded_file = st.file_uploader("Upload a PDF or TXT", type=['pdf', 'txt'])
if uploaded_file:
    file_path = f"./{uploaded_file.name}"
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.read())

    text = (document_parser.extract_text_from_pdf(file_path)
            if file_path.endswith('.pdf') else
            document_parser.extract_text_from_txt(file_path))

    st.subheader("📌 Document Summary")
    st.write(summarizer.generate_summary(text))

    mode = st.radio("Select Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        question = st.text_input("Enter your question:")
        if question:
            answer = qa_engine.answer_question(question, text)
            st.success(f"Answer: {answer}")
    else:
        questions = logic_questioner.generate_logic_questions(text)
        for q in questions:
            user_answer = st.text_input(q)
            if user_answer:
                st.write("✅ Recorded! (Evaluation logic to be added)")
