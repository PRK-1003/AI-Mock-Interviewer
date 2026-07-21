from groq_service import groq
from prompts import QUESTION_GENERATOR_PROMPT


class QuestionGenerator:

    def __init__(self):
        self.previous_questions = []

    def generate_question(
        self,
        job_role,
        experience_level,
        interview_type,
        question_number
    ):
        """
        Generate one interview question based on the candidate profile.
        """

        previous = "\n".join(self.previous_questions)

        user_prompt = f"""
Job Role:
{job_role}

Experience Level:
{experience_level}

Interview Type:
{interview_type}

Question Number:
{question_number}

Previously Asked Questions:
{previous if previous else "None"}

Generate ONLY one new interview question.
"""

        response = groq.generate_response(
            system_prompt=QUESTION_GENERATOR_PROMPT,
            user_prompt=user_prompt,
            temperature=0.5
        )

        self.previous_questions.append(response)

        return response

    def reset_questions(self):
        """
        Clears previously generated questions.
        """
        self.previous_questions = []