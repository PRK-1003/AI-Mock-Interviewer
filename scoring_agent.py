from groq_service import groq
from prompts import SCORING_AGENT_PROMPT


class ScoringAgent:

    def __init__(self):

        self.weights = {
            "technical_accuracy":0.30,
            "completeness":0.25,
            "clarity":0.15,
            "communication":0.15,
            "confidence":0.15
        }

    def calculate_scores(self, evaluations):

        if len(evaluations) == 0:
            return None, 0

        print("\n========== EVALUATIONS ==========")
        print(evaluations)
        print("=================================\n")

        total = {

            "technical_accuracy":0,
            "completeness":0,
            "clarity":0,
            "communication":0,
            "confidence":0

        }

        for evaluation in evaluations:

            total["technical_accuracy"] += evaluation.get("technical_accuracy",0)
            total["completeness"] += evaluation.get("completeness",0)
            total["clarity"] += evaluation.get("clarity",0)
            total["communication"] += evaluation.get("communication",0)
            total["confidence"] += evaluation.get("confidence",0)

        averages = {}

        for key in total:

            averages[key] = round(total[key]/len(evaluations),2)

        overall = 0

        for key,weight in self.weights.items():

            overall += averages[key]*weight

        overall = round(overall*10,2)

        return averages,overall

    def get_rating(self,score):

        if score>=90:
            return "Excellent"

        elif score>=80:
            return "Very Good"

        elif score>=70:
            return "Good"

        elif score>=60:
            return "Needs Improvement"

        else:
            return "Requires Significant Practice"

    def generate_final_feedback(
        self,
        job_role,
        evaluations
    ):

        averages,overall_score = self.calculate_scores(evaluations)

        rating = self.get_rating(overall_score)

        user_prompt = f"""
Job Role: {job_role}

Overall Score: {overall_score}

Rating: {rating}

Average Scores:

Technical Accuracy: {averages['technical_accuracy']}

Completeness: {averages['completeness']}

Clarity: {averages['clarity']}

Communication: {averages['communication']}

Confidence: {averages['confidence']}

Generate a professional interview report.
"""

        report = groq.generate_response(

            system_prompt=SCORING_AGENT_PROMPT,

            user_prompt=user_prompt,

            temperature=0.3

        )

        return {

            "overall_score":overall_score,

            "rating":rating,

            "average_scores":averages,

            "final_feedback":report

        }