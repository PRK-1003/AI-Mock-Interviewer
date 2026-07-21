// ===============================
// DOM Elements
// ===============================

const startBtn = document.getElementById("startBtn");
const submitBtn = document.getElementById("submitBtn");
const restartBtn = document.getElementById("restartBtn");

const progressSection = document.getElementById("progressSection");
const questionCard = document.getElementById("questionCard");
const evaluationCard = document.getElementById("evaluationCard");
const reportCard = document.getElementById("reportCard");

const questionText = document.getElementById("questionText");
const answerBox = document.getElementById("candidateAnswer");

const progressFill = document.getElementById("progressFill");
const progressText = document.getElementById("progressText");

const evaluationContent = document.getElementById("evaluationContent");

// ===============================
// Start Interview
// ===============================

startBtn.addEventListener("click", async () => {

    const jobRole = document.getElementById("jobRole").value.trim();
    const experience = document.getElementById("experience").value;
    const interviewType = document.getElementById("interviewType").value;
    const questionCount = document.getElementById("questionCount").value;

    if (jobRole === "") {
        alert("Please enter Job Role.");
        return;
    }

    startBtn.disabled = true;
    startBtn.innerText = "Starting...";

    const response = await startInterview({

        job_role: jobRole,
        experience_level: experience,
        interview_type: interviewType,
        total_questions: questionCount

    });

    startBtn.disabled = false;
    startBtn.innerText = "Start Interview";

    if (response.status === "question") {

        progressSection.classList.remove("hidden");
        questionCard.classList.remove("hidden");

        showQuestion(response);

    } else {

        alert(response.message || "Unable to start interview.");

    }

});

// ===============================
// Show Question
// ===============================

function showQuestion(data) {

    questionText.innerText = data.question;

    answerBox.value = "";

    progressText.innerText =
        `Question ${data.question_number} / ${data.total_questions}`;

    const percentage =
        (data.question_number / data.total_questions) * 100;

    progressFill.style.width = percentage + "%";

    evaluationCard.classList.add("hidden");

}

// ===============================
// Submit Answer
// ===============================

submitBtn.addEventListener("click", async () => {

    const answer = answerBox.value.trim();

    if (answer === "") {

        alert("Please enter your answer.");

        return;

    }

    submitBtn.disabled = true;
    submitBtn.innerText = "Evaluating...";

    const response = await submitAnswer(answer);

    submitBtn.disabled = false;
    submitBtn.innerText = "Submit Answer";

    if (response.status === "continue") {

        showEvaluation(response.evaluation);

        setTimeout(() => {

            showQuestion(response.next_question);

        }, 2500);

    }

    else if (response.status === "completed") {

        questionCard.classList.add("hidden");
        progressSection.classList.add("hidden");
        evaluationCard.classList.add("hidden");

        reportCard.classList.remove("hidden");

        renderDashboard(response.report);

    }

});

// ===============================
// Evaluation
// ===============================

function showEvaluation(result) {

    evaluationCard.classList.remove("hidden");

    evaluationContent.innerHTML = `

        <div class="score-grid">

            <div class="score-card">
                <h3>Technical</h3>
                <p>${result.technical_accuracy}</p>
            </div>

            <div class="score-card">
                <h3>Completeness</h3>
                <p>${result.completeness}</p>
            </div>

            <div class="score-card">
                <h3>Clarity</h3>
                <p>${result.clarity}</p>
            </div>

            <div class="score-card">
                <h3>Communication</h3>
                <p>${result.communication}</p>
            </div>

            <div class="score-card">
                <h3>Confidence</h3>
                <p>${result.confidence}</p>
            </div>

        </div>

        <div class="feedback-box">

            <h4>Strengths</h4>

            <ul>

                ${(result.strengths || [])
                    .map(item => `<li>${item}</li>`)
                    .join("")}

            </ul>

            <h4>Suggestions</h4>

            <ul>

                ${(result.suggestions || [])
                    .map(item => `<li>${item}</li>`)
                    .join("")}

            </ul>

        </div>

    `;

}

// ===============================
// Restart
// ===============================

restartBtn.addEventListener("click", async () => {

    await resetInterview();

    location.reload();

});