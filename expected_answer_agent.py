from groq_service import groq
from prompts import EXPECTED_ANSWER_PROMPT


class ExpectedAnswerAgent:

    def __init__(self):
        pass

    def generate_expected_answer(
        self,
        job_role,
        experience_level,
        interview_question
    ):
        """
        Generate an ideal reference answer for the given interview question.
        """

        user_prompt = f"""
Job Role:
{job_role}

Experience Level:
{experience_level}

Interview Question:
{interview_question}

Generate the ideal interview answer.
"""

        response = groq.generate_response(
            system_prompt=EXPECTED_ANSWER_PROMPT,
            user_prompt=user_prompt,
            temperature=0.3
        )

        return response