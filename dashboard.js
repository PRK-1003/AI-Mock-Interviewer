// ========================================
// Render Final Interview Dashboard
// ========================================

function renderDashboard(report) {

    const dashboard = document.getElementById("dashboard");

    const averages = report.average_scores;

    dashboard.innerHTML = `

        <div class="report-score">

            <h1>${report.overall_score}%</h1>

            <h2>${report.rating}</h2>

        </div>

        <div class="score-grid">

            <div class="score-card">
                <h3>Technical Accuracy</h3>
                <p>${averages.technical_accuracy}</p>
            </div>

            <div class="score-card">
                <h3>Completeness</h3>
                <p>${averages.completeness}</p>
            </div>

            <div class="score-card">
                <h3>Clarity</h3>
                <p>${averages.clarity}</p>
            </div>

            <div class="score-card">
                <h3>Communication</h3>
                <p>${averages.communication}</p>
            </div>

            <div class="score-card">
                <h3>Confidence</h3>
                <p>${averages.confidence}</p>
            </div>

        </div>

        <div class="report-section">

            <h3>Final AI Feedback</h3>

            <p>

                ${formatFeedback(report.final_feedback)}

            </p>

        </div>

        <div class="text-center mt-20">

            <button onclick="downloadReport()">

                Download Report

            </button>

        </div>

    `;
}

// ========================================
// Format Feedback
// ========================================

function formatFeedback(text) {

    if (!text) {

        return "No feedback available.";

    }

    return text.replace(/\n/g, "<br>");

}

// ========================================
// Download Report
// ========================================

function downloadReport() {

    const report = document.getElementById("dashboard").innerText;

    const blob = new Blob(

        [report],

        {

            type: "text/plain"

        }

    );

    const url = window.URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.download = "Interview_Report.txt";

    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);

    window.URL.revokeObjectURL(url);

}