from flask import Flask, request, jsonify
from flask_cors import CORS

from coordinator import InterviewCoordinator

app = Flask(__name__)
CORS(app)

# ---------------------------------------
# Initialize Interview Coordinator
# ---------------------------------------

coordinator = InterviewCoordinator()

# ---------------------------------------
# Home Route
# ---------------------------------------

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "message": "AI Mock Interviewer Backend Running",

        "status": "success"

    })


# ---------------------------------------
# Start Interview
# ---------------------------------------

@app.route("/start-interview", methods=["POST"])
def start_interview():

    try:

        data = request.get_json()

        job_role = data["job_role"]

        experience = data["experience_level"]

        interview_type = data["interview_type"]

        total_questions = int(data["total_questions"])

        response = coordinator.start_interview(

            job_role,

            experience,

            interview_type,

            total_questions

        )

        return jsonify(response)

    except Exception as e:

        return jsonify({

            "status":"error",

            "message":str(e)

        }),500


# ---------------------------------------
# Submit Answer
# ---------------------------------------

@app.route("/submit-answer", methods=["POST"])
def submit_answer():

    try:

        data = request.get_json()

        answer = data["candidate_answer"]

        response = coordinator.submit_answer(answer)

        return jsonify(response)

    except Exception as e:

        return jsonify({

            "status":"error",

            "message":str(e)

        }),500


# ---------------------------------------
# Reset Interview
# ---------------------------------------

@app.route("/reset-interview", methods=["POST"])
def reset():

    coordinator.reset()

    return jsonify({

        "status":"success",

        "message":"Interview Reset Successfully"

    })


# ---------------------------------------
# Get Current Status
# ---------------------------------------

@app.route("/status", methods=["GET"])
def status():

    return jsonify({

        "current_question": coordinator.current_question,

        "total_questions": coordinator.total_questions,

        "completed": len(coordinator.evaluations)

    })


# ---------------------------------------
# Run Server
# ---------------------------------------

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )