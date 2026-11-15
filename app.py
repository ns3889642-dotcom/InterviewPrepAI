import streamlit as st
import pandas as pd
import plotly.express as px

from modules.question_bank import get_random_question
from modules.evaluator import evaluate_answer
from modules.database import (
    create_table,
    save_interview,
    get_interview_history
)
from modules.report_generator import generate_pdf_report


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="InterviewPrep AI",
    page_icon="🎯",
    layout="wide"
)

create_table()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "answer" not in st.session_state:
    st.session_state.answer = ""

if "result" not in st.session_state:
    st.session_state.result = None

if "last_selection" not in st.session_state:
    st.session_state.last_selection = None


# --------------------------------------------------
# PROFESSIONAL UI DESIGN
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #f5f7ff 0%,
        #eef2ff 100%
    );
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #172554 0%,
        #312e81 100%
    );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] div[data-testid="stAlert"] {
    background-color: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.25);
}

section[data-testid="stSidebar"] div[data-testid="stAlert"] p {
    color: white !important;
}

h1 {
    color: #1e3a8a !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #263b80 !important;
    font-weight: 700 !important;
}

.stButton > button {
    background: linear-gradient(
        90deg,
        #4338ca,
        #2563eb
    );
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
    transition: 0.3s;
}

.stButton > button:hover {
    background: #3730a3;
    color: white;
    border: none;
}

.stDownloadButton > button {
    background: linear-gradient(
        90deg,
        #4338ca,
        #2563eb
    );
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 600;
}

div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #e0e7ff;
    box-shadow: 0 4px 12px rgba(30, 58, 138, 0.08);
}

.stTextArea textarea,
.stTextInput input {
    border-radius: 10px;
    border: 1px solid #c7d2fe;
    background-color: white;
}

div[data-baseweb="select"] {
    border-radius: 10px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

div[data-testid="stProgressBar"] > div > div {
    background-color: #4f46e5;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

st.sidebar.title("🎯 InterviewPrep AI")

st.sidebar.caption(
    "Your AI-powered interview preparation partner"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Practice Interview",
        "Performance Dashboard"
    ]
)

st.sidebar.divider()


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if page == "Home":

    st.title("🎯 Welcome to InterviewPrep AI")

    st.markdown(
        "### Prepare smarter. Practice better. Build confidence."
    )

    st.write(
        "Your personal AI-powered platform for interview preparation."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📝 Interview Practice")
        st.write(
            "Practice questions from Python, Java, C++, SQL, and HR."
        )

    with col2:
        st.subheader("🤖 AI Answer Evaluation")
        st.write(
            "Evaluate answers using text similarity and keyword matching."
        )

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📊 Performance Tracking")
        st.write(
            "Track your interview scores and review previous attempts."
        )

    with col4:
        st.subheader("📚 Multiple Difficulty Levels")
        st.write(
            "Choose Beginner, Intermediate, or Advanced questions."
        )

    st.divider()

    st.subheader("🚀 How It Works")

    st.markdown("""
    1. Select your interview subject.
    2. Choose your difficulty level.
    3. Generate an interview question.
    4. Write and submit your answer.
    5. Receive AI-based evaluation and feedback.
    6. Track your progress in the dashboard.
    """)

    st.info(
        "Start with Practice Interview from the sidebar."
    )


# --------------------------------------------------
# PRACTICE INTERVIEW
# --------------------------------------------------

elif page == "Practice Interview":

    st.title("📝 Practice Interview")

    st.write(
        "Select your subject and difficulty level to begin."
    )

    subjects = [
        "Python",
        "Java",
        "C++",
        "SQL",
        "HR"
    ]

    difficulties = [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

    col1, col2 = st.columns(2)

    with col1:
        subject = st.selectbox(
            "Choose Subject",
            subjects
        )

    with col2:
        difficulty = st.selectbox(
            "Choose Difficulty",
            difficulties
        )

    current_selection = (subject, difficulty)

    if st.session_state.last_selection != current_selection:

        st.session_state.current_question = None
        st.session_state.result = None
        st.session_state.answer = ""

        st.session_state.last_selection = current_selection

    if st.button("🎲 Generate Question", type="primary"):

        st.session_state.current_question = get_random_question(
            subject,
            difficulty
        )

        st.session_state.answer = ""
        st.session_state.result = None

    if st.session_state.current_question:

        question_data = st.session_state.current_question

        st.divider()

        st.subheader("Your Interview Question")

        st.info(question_data["question"])

        answer = st.text_area(
            "Write your answer:",
            key="answer",
            height=180,
            placeholder="Type your answer here..."
        )

        if st.button("🤖 Evaluate My Answer", type="primary"):

            if not answer.strip():

                st.warning(
                    "Please write an answer before submitting."
                )

            else:

                result = evaluate_answer(
                    answer,
                    question_data["keywords"],
                    question_data["reference_answer"]
                )

                st.session_state.result = result

                save_interview(
                    subject,
                    difficulty,
                    question_data["question"],
                    answer,
                    result["score"],
                    result["feedback"]
                )

        if st.session_state.result:

            result = st.session_state.result

            st.divider()

            st.subheader("🤖 AI Evaluation Result")

            score = result["score"]
            similarity = result["similarity_score"]
            keyword_score = result["keyword_score"]

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Overall Score",
                    f"{score}/100"
                )

            with col2:
                st.metric(
                    "Answer Similarity",
                    f"{similarity}%"
                )

            with col3:
                st.metric(
                    "Keyword Score",
                    f"{keyword_score}%"
                )

            st.progress(score / 100)

            st.subheader("💡 Feedback")

            st.success(result["feedback"])

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("**✅ Matched Keywords**")

                if result["matched_keywords"]:

                    for keyword in result["matched_keywords"]:
                        st.write(f"✓ {keyword}")

                else:
                    st.write("No expected keywords matched.")

            with col2:

                st.markdown("**📌 Missing Keywords**")

                if result["missing_keywords"]:

                    for keyword in result["missing_keywords"]:
                        st.write(f"• {keyword}")

                else:
                    st.write("No expected keywords are missing.")

            st.caption(
                "Scores are estimates based on text similarity "
                "and keyword coverage, not human interview judgments."
            )

            if st.button("🔄 Try Another Question"):

                st.session_state.current_question = None
                st.session_state.result = None
                st.session_state.answer = ""

                st.rerun()


# --------------------------------------------------
# PERFORMANCE DASHBOARD
# --------------------------------------------------

elif page == "Performance Dashboard":

    st.title("📊 Performance Dashboard")

    history = get_interview_history()

    if not history:

        st.info(
            "No interview attempts found. "
            "Start practicing to see your performance."
        )

    else:

        df = pd.DataFrame(
            history,
            columns=[
                "Subject",
                "Difficulty",
                "Question",
                "Score",
                "Date"
            ]
        )

        df["Score"] = pd.to_numeric(
            df["Score"],
            errors="coerce"
        )

        df = df.dropna(subset=["Score"])

        if df.empty:

            st.info("No valid score records available.")

        else:

            total_attempts = len(df)
            average_score = df["Score"].mean()
            best_score = df["Score"].max()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Attempts",
                    total_attempts
                )

            with col2:
                st.metric(
                    "Average Score",
                    f"{average_score:.1f}%"
                )

            with col3:
                st.metric(
                    "Best Score",
                    f"{best_score:.0f}%"
                )

            st.divider()

            # ------------------------------------------
            # INTERVIEW SCORE HISTORY
            # ------------------------------------------

            st.subheader("📈 Interview Score History")

            chart_df = df.reset_index(drop=True)

            chart_df["Attempt"] = range(
                1,
                len(chart_df) + 1
            )

            fig = px.line(
                chart_df,
                x="Attempt",
                y="Score",
                markers=True,
                title="Your Interview Performance"
            )

            fig.update_layout(
                xaxis_title="Interview Attempt",
                yaxis_title="Score",
                yaxis=dict(range=[0, 100])
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

            # ------------------------------------------
            # SUBJECT-WISE PERFORMANCE
            # ------------------------------------------

            st.subheader("📚 Subject-wise Performance")

            subject_df = (
                df.groupby("Subject")["Score"]
                .mean()
                .reset_index()
            )

            subject_fig = px.bar(
                subject_df,
                x="Subject",
                y="Score",
                color="Subject",
                title="Average Score by Subject"
            )

            subject_fig.update_layout(
                yaxis_title="Average Score",
                yaxis=dict(range=[0, 100])
            )

            st.plotly_chart(
                subject_fig,
                use_container_width=True
            )

            # ------------------------------------------
            # PREVIOUS INTERVIEW ATTEMPTS
            # ------------------------------------------

            st.subheader("📋 Previous Interview Attempts")

            display_df = df[
                [
                    "Subject",
                    "Difficulty",
                    "Question",
                    "Score",
                    "Date"
                ]
            ].sort_index(ascending=False)

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )

            st.divider()

            # ------------------------------------------
            # DOWNLOAD CSV
            # ------------------------------------------

            st.subheader("📥 Download Your Reports")

            csv_data = df.to_csv(
                index=False
            ).encode("utf-8")

            col1, col2 = st.columns(2)

            with col1:

                st.download_button(
                    label="⬇️ Download Interview History (CSV)",
                    data=csv_data,
                    file_name="interview_history.csv",
                    mime="text/csv",
                    use_container_width=True
                )

            # ------------------------------------------
            # DOWNLOAD PDF
            # ------------------------------------------

            with col2:

                pdf_data = generate_pdf_report(
                    df.itertuples(
                        index=False,
                        name=None
                    )
                )

                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf_data,
                    file_name="interview_performance_report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🎯 InterviewPrep AI | Practice • Evaluate • Improve"
)