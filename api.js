// ================================
// Backend API Base URL
// ================================

const BASE_URL = "http://127.0.0.1:5000";

// ================================
// Start Interview
// ================================

async function startInterview(data) {

    try {

        const response = await fetch(`${BASE_URL}/start-interview`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(data)

        });

        return await response.json();

    } catch (error) {

        console.error("Start Interview Error:", error);

        return {
            status: "error",
            message: "Unable to connect to the server."
        };

    }

}

// ================================
// Submit Candidate Answer
// ================================

async function submitAnswer(candidateAnswer) {

    try {

        const response = await fetch(`${BASE_URL}/submit-answer`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                candidate_answer: candidateAnswer

            })

        });

        return await response.json();

    }

    catch (error) {

        console.error(error);

        return {

            status: "error",

            message: "Unable to submit answer."

        };

    }

}

// ================================
// Get Interview Status
// ================================

async function getStatus() {

    try {

        const response = await fetch(`${BASE_URL}/status`);

        return await response.json();

    }

    catch (error) {

        console.error(error);

        return null;

    }

}

// ================================
// Reset Interview
// ================================

async function resetInterview() {

    try {

        const response = await fetch(`${BASE_URL}/reset-interview`, {

            method: "POST"

        });

        return await response.json();

    }

    catch (error) {

        console.error(error);

        return {

            status: "error",

            message: "Unable to reset interview."

        };

    }

}