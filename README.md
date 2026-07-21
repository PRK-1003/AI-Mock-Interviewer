# AI-Powered Multi-Agent Mock Interview Evaluation System

An AI-powered mock interview platform that generates interview questions, evaluates candidate responses, calculates scores, and provides personalized feedback using **Groq Llama 3.3**.

## Features

- AI-generated interview questions
- Expected answer generation
- AI response evaluation
- Performance scoring
- Detailed interview feedback
- Interactive dashboard
- REST API with Flask

## Tech Stack

- Python
- Flask
- HTML, CSS, JavaScript
- Groq API (Llama 3.3 70B)
- Prompt Engineering

## Project Structure

```
backend/
 ├── agents/
 ├── app.py
 ├── coordinator.py
 ├── groq_service.py
 ├── prompts.py

frontend/
 ├── css/
 ├── js/
 └── index.html
```

##  Run the Project

1. Install dependencies:
```bash
pip install -r backend/requirements.txt
```

2. Create a `.env` file:

```env
GROQ_API_KEY=your_api_key
MODEL=llama-3.3-70b-versatile
```

3. Start the backend:

```bash
cd backend
python app.py
```

4. Open `frontend/index.html` using **Live Server**.

## Evaluation Metrics

- Technical Accuracy (30%)
- Completeness (25%)
- Clarity (15%)
- Communication (15%)
- Confidence (15%)

## Future Enhancements

- PDF report generation
- Voice-based interviews
- User authentication
- Interview history
- Database integration

## Author

**Sarah G**
