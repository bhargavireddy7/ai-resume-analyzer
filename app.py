import gradio as gr
import matplotlib.pyplot as plt
from fpdf import FPDF
from utils.job_matcher import match_job_description
from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.score_calculator import calculate_score
from utils.interview_generator import generate_questions
from utils.resume_suggestions import generate_resume_suggestions


# =========================
# SKILL PIE CHART
# =========================
def chat_response(message, history):

    response = (
        "Based on your resume analysis:\n\n"
        "👉 Improve Python and SQL skills\n"
        "👉 Add more real-world projects\n"
        "👉 Strengthen ATS keywords\n"
        "👉 Highlight leadership experience"
    )

    history.append((message, response))

    return "", history
def generate_chart(skills):

    plt.figure(figsize=(7, 7))

    values = [1] * len(skills)

    plt.pie(
        values,
        labels=skills,
        autopct='%1.1f%%',
        startangle=90
    )

    plt.title("Skill Distribution")

    chart_path = "skills_chart.png"

    plt.savefig(chart_path)

    plt.close()

    return chart_path


# =========================
# PDF REPORT
# =========================

def generate_pdf(score, skills, questions, suggestions):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size=16)

    pdf.cell(200, 10, txt="AI Resume Analysis Report", ln=True)

    pdf.ln(10)

    pdf.set_font("Arial", size=13)

    pdf.cell(200, 10, txt=f"ATS Score: {score}%", ln=True)

    pdf.ln(5)

    pdf.cell(200, 10, txt="Skills:", ln=True)

    for skill in skills:
        pdf.cell(200, 10, txt=f"- {skill}", ln=True)

    pdf.ln(5)

    pdf.cell(200, 10, txt="Interview Questions:", ln=True)

    for question in questions:
        pdf.multi_cell(0, 10, f"- {question}")

    pdf.ln(5)

    pdf.cell(200, 10, txt="AI Suggestions:", ln=True)

    for suggestion in suggestions:
        pdf.multi_cell(0, 10, f"- {suggestion}")

    pdf_path = "resume_report.pdf"

    pdf.output(pdf_path)

    return pdf_path


# =========================
# MAIN ANALYSIS FUNCTION
# =========================

def analyze_resume(pdf_file, job_description):

    # =========================
    # EXTRACT TEXT
    # =========================
    resume_text = extract_text_from_pdf(pdf_file)

    # =========================
    # SKILL EXTRACTION
    # =========================
    skills = extract_skills(resume_text)

    # =========================
    # ATS SCORE
    # =========================
    score = calculate_score(skills)

    # =========================
    # INTERVIEW QUESTIONS
    # =========================
    questions = generate_questions(skills)

    # =========================
    # AI SUGGESTIONS
    # =========================
    suggestions = generate_resume_suggestions(skills, score)

    # =========================
    # JOB MATCHING (SAFE HANDLING)
    # =========================
    if job_description and job_description.strip():

        match_score, matched_skills, missing_skills = match_job_description(
            skills,
            job_description
        )

    else:

        match_score = 0
        matched_skills = []
        missing_skills = []

    # =========================
    # DEBUG (OPTIONAL)
    # =========================
    print("\n===== DEBUG =====")
    print("Skills:", skills)
    print("Matched:", matched_skills)
    print("Missing:", missing_skills)

    # =========================
    # CHART
    # =========================
    chart = generate_chart(skills)

    # =========================
    # PDF REPORT
    # =========================
    pdf_report = generate_pdf(
        score,
        skills,
        questions,
        suggestions
    )

    # =========================
    # FORMAT OUTPUTS
    # =========================
    skills_output = "\n".join(
        [f"🏷️ {skill}" for skill in skills]
    )

    questions_output = "\n\n".join(
        [f"{i+1}. {q}" for i, q in enumerate(questions)]
    )

    suggestions_output = "\n".join(
        [f"• {s}" for s in suggestions]
    )

    matched_output = "\n".join(
        [f"✅ {skill}" for skill in matched_skills]
    ) if matched_skills else "No matching skills found"

    missing_output = "\n".join(
        [f"❌ {skill}" for skill in missing_skills]
    ) if missing_skills else "No missing skills detected"

    # =========================
    # RETURN TO GRADIO
    # =========================
    return (
        skills_output,
        score,
        questions_output,
        suggestions_output,
        chart,
        pdf_report,
        matched_output,
        missing_output,
        match_score
    )

# =========================
# PREMIUM CSS
# =========================

custom_css = """

/* BACKGROUND */

@media (prefers-color-scheme: light) {
    body {
        background: linear-gradient(135deg, #f8fafc, #dbeafe, #e0e7ff) !important;
        color: #111827 !important;
    }
}

@media (prefers-color-scheme: dark) {
    body {
        background: linear-gradient(135deg, #0f172a, #1e293b, #312e81) !important;
        color: #ffffff !important;
    }
}
@media screen and (max-width: 768px) {

    .gradio-container {
        padding: 10px !important;
    }

    .gr-row {
        flex-direction: column !important;
    }

    textarea, input {
        font-size: 14px !important;
    }

    .gr-button {
        width: 100% !important;
    }
}

/* MAIN CONTAINER */

.gradio-container {

    border-radius: 20px !important;

    padding: 20px !important;

    color: inherit !important;
}


/* BUTTONS */

.gr-button {

    background: linear-gradient(
        to right,
        #ff6ec4,
        #7873f5
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 14px !important;

    font-size: 18px !important;

    font-weight: bold !important;

    padding: 12px !important;

    transition: 0.3s ease !important;
}


/* BUTTON HOVER */

.gr-button:hover {

    transform: scale(1.05);

    box-shadow: 0px 0px 20px #a855f7;
}


/* TEXTBOXES */

textarea,
input {

    border-radius: 14px !important;

    border: 2px solid #c084fc !important;

    padding: 10px !important;
}


/* LABELS */

label {

    font-weight: bold !important;

    color: #111827 !important;
}


/* HEADINGS */

h1 {

    text-align: center;

    font-size: 42px !important;

    font-weight: bold !important;

    background: linear-gradient(
        to right,
        #ff6ec4,
        #7873f5
    );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}


h2, h3, h4 {

    color: #1f2937 !important;

    font-weight: bold !important;
}


/* MARKDOWN TEXT */

p, li {

    color: #374151 !important;

    font-size: 16px !important;
}


/* CARDS */

.block {
    border-radius: 18px !important;
    background: rgba(255, 255, 255, 0.08) !important;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.2);
    padding: 15px !important;
}


/* SLIDERS */

input[type="range"] {

    accent-color: #8b5cf6;
}
input[type="range"] {
    accent-color: #8b5cf6;
    transition: all 0.5s ease;
}
"""


# =========================
# UI
# =========================

with gr.Blocks() as demo:

    gr.Markdown(
        """
        #  AI Resume Analyzer
    """
    )

    resume_input = gr.File(
        label="Upload Resume PDF"
    )

    job_description_input = gr.Textbox(
        label="Job Description",
        lines=8,
        placeholder="Paste job description here..."
    )
    chatbot = gr.Chatbot(label="🤖 AI Career Assistant")

    chat_input = gr.Textbox(
        label="Ask anything about your resume",
        placeholder="e.g. How can I improve my resume?"
    )

    chat_button = gr.Button("Ask AI 💬")
    analyze_button = gr.Button(
        "Analyze Resume "
    )

    # =========================
    # SCORES
    # =========================

    with gr.Row():

        ats_score_output = gr.Slider(
         minimum=0,
         maximum=100,
         label="🎯 ATS Score",
         interactive=False,
         step=1
        )

        match_score_output = gr.Slider(
            minimum=0,
            maximum=100,
            label="🎯 Job Match Score",
            interactive=False,
            step=1
        )

    # =========================
    # SKILLS
    # =========================

    with gr.Row():

        skills_output = gr.Textbox(
            label="Extracted Skills",
            lines=8
        )

        matched_skills_output = gr.Textbox(
            label="Matching Skills",
            lines=8
        )

        missing_skills_output = gr.Textbox(
            label="Missing Skills",
            lines=8
        )

    # =========================
    # QUESTIONS
    # =========================

    questions_output = gr.Textbox(
        label="Interview Questions",
        lines=10
    )

    # =========================
    # AI SUGGESTIONS
    # =========================

    suggestions_output = gr.Textbox(
        label="AI Resume Suggestions",
        lines=8
    )

    # =========================
    # CHART
    # =========================

    chart_output = gr.Image(
        label="📈Skills Chart"
    )

    # =========================
    # PDF DOWNLOAD
    # =========================

    pdf_output = gr.File(
        label="📩Download Report PDF"
    )

    # =========================
    # BUTTON CLICK
    # =========================

    analyze_button.click(
        fn=analyze_resume,

        inputs=[
            resume_input,
            job_description_input
        ],

        outputs=[
            skills_output,
            ats_score_output,
            questions_output,
            suggestions_output,
            chart_output,
            pdf_output,
            matched_skills_output,
            missing_skills_output,
            match_score_output
        ]
    )


# =========================
# LAUNCH APP
# =========================
demo.launch(
    css=custom_css,
    theme=gr.themes.Base(
        primary_hue="violet",
        secondary_hue="pink",
        neutral_hue="slate"
    )
)