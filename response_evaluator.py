import json
import re

from groq_service import groq
from prompts import RESPONSE_EVALUATOR_PROMPT


class ResponseEvaluator:

    def __init__(self):
        pass

    def evaluate_response(
        self,
        job_role,
        experience_level,
        interview_question,
        expected_answer,
        candidate_answer
    ):

        user_prompt = f"""
Job Role:
{job_role}

Experience Level:
{experience_level}

Interview Question:
{interview_question}

Expected Answer:
{expected_answer}

Candidate Answer:
{candidate_answer}
"""

        response = groq.generate_response(
            system_prompt=RESPONSE_EVALUATOR_PROMPT,
            user_prompt=user_prompt,
            temperature=0.2
        )

        print("\n========== RAW GROQ RESPONSE ==========")
        print(response)
        print("=======================================\n")

        try:

            cleaned = response.strip()

            cleaned = cleaned.replace("```json", "")
            cleaned = cleaned.replace("```", "")

            match = re.search(r"\{.*\}", cleaned, re.DOTALL)

            if match:
                cleaned = match.group(0)

            evaluation = json.loads(cleaned)

            print("\nParsed Evaluation")
            print(evaluation)

            return evaluation

        except Exception as e:

            print("\nJSON Parsing Failed")
            print(e)

            return {

                "technical_accuracy":0,
                "completeness":0,
                "clarity":0,
                "communication":0,
                "confidence":0,

                "strengths":[],
                "weaknesses":[],
                "missing_points":[],
                "suggestions":[],

                "raw_response":response,
                "error":str(e)

            }