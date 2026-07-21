from agents.question_generator import QuestionGenerator
from agents.expected_answer_agent import ExpectedAnswerAgent
from agents.response_evaluator import ResponseEvaluator
from agents.scoring_agent import ScoringAgent


class InterviewCoordinator:

    def __init__(self):

        self.question_generator = QuestionGenerator()
        self.expected_answer_agent = ExpectedAnswerAgent()
        self.response_evaluator = ResponseEvaluator()
        self.scoring_agent = ScoringAgent()

        self.reset()

    def reset(self):

        self.job_role = ""
        self.experience_level = ""
        self.interview_type = ""

        self.total_questions = 0
        self.current_question = 0

        self.current_question_text = ""
        self.current_expected_answer = ""

        self.evaluations = []

        self.question_generator.reset_questions()

    # -------------------------------------------------

    def start_interview(
        self,
        job_role,
        experience_level,
        interview_type,
        total_questions
    ):

        self.reset()

        self.job_role = job_role
        self.experience_level = experience_level
        self.interview_type = interview_type
        self.total_questions = total_questions

        return self.next_question()

    # -------------------------------------------------

    def next_question(self):

        self.current_question += 1

        if self.current_question > self.total_questions:

            return self.finish_interview()

        question = self.question_generator.generate_question(

            job_role=self.job_role,

            experience_level=self.experience_level,

            interview_type=self.interview_type,

            question_number=self.current_question

        )

        expected_answer = self.expected_answer_agent.generate_expected_answer(

            job_role=self.job_role,

            experience_level=self.experience_level,

            interview_question=question

        )

        self.current_question_text = question
        self.current_expected_answer = expected_answer

        return {

            "status": "question",

            "question_number": self.current_question,

            "total_questions": self.total_questions,

            "question": question

        }

    # -------------------------------------------------

    def submit_answer(self, candidate_answer):

        evaluation = self.response_evaluator.evaluate_response(

            job_role=self.job_role,

            experience_level=self.experience_level,

            interview_question=self.current_question_text,

            expected_answer=self.current_expected_answer,

            candidate_answer=candidate_answer

        )

        self.evaluations.append(evaluation)

        if self.current_question >= self.total_questions:

            return self.finish_interview()

        next_question = self.next_question()

        return {

            "status": "continue",

            "evaluation": evaluation,

            "next_question": next_question

        }

    # -------------------------------------------------

    def finish_interview(self):

        report = self.scoring_agent.generate_final_feedback(

            job_role=self.job_role,

            evaluations=self.evaluations

        )

        return {

            "status": "completed",

            "report": report,

            "evaluations": self.evaluations

        }