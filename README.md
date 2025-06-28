# Smart Research Summarization Assistant

## Overview
This AI assistant reads research documents and enables:
- Document summarization (≤ 150 words)
- Free-form Q&A with context
- Logic-based "Challenge Me" mode
- Reference-based justification

## Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/your-repo/genai_assistant.git
cd genai_assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

## Architecture
- `Streamlit`: Frontend UI
- `transformers`: Summarization & QnA
- `PyMuPDF`: PDF reading
- `sentence-transformers`: Optional enhancements for semantic search

## File Structure
```
genai_assistant/
├── app.py
├── requirements.txt
├── README.md
└── backend/
    ├── document_parser.py
    ├── summarizer.py
    ├── qa_engine.py
    ├── logic_questioner.py
    └── utils.py
```
