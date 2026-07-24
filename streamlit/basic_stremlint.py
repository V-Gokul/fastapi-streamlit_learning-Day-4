import datetime

import streamlit as st


# Configure page settings before rendering any UI elements.
st.set_page_config(page_title="Streamlit Components Lab", page_icon="🧪", layout="wide")

st.title("Streamlit Components Lab")
st.caption("Hands-on mini scenarios to learn the most useful Streamlit components.")

with st.sidebar:
	# Sidebar is useful for app-wide controls and navigation-like inputs.
	st.header("Learning Navigator")
	student_name = st.text_input("Your name", placeholder="Type your name")
	learning_level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"], index=0)
	dark_theme = st.toggle("Pretend dark-mode preference", value=False)

	st.divider()
	st.subheader("Progress")
	level_to_progress = {"Beginner": 30, "Intermediate": 65, "Advanced": 90}
	progress_value = level_to_progress[learning_level]
	st.progress(progress_value, text=f"Estimated progress: {progress_value}%")


if "feedback_submitted" not in st.session_state:
	# session_state keeps values across reruns triggered by widget interactions.
	st.session_state.feedback_submitted = False

if student_name:
	st.success(f"Welcome, {student_name}. Explore each scenario and interact with the widgets.")
else:
	st.info("Tip: Enter your name in the sidebar for a personalized experience.")

if dark_theme:
	st.warning("Dark-mode toggle is just a demo state for learning purposes.")


tab1, tab2, tab3, tab4 = st.tabs(
	[
		"Scenario 1: Grade Analyzer",
		"Scenario 2: Health & Budget",
		"Scenario 3: Schedule Planner",
		"Scenario 4: Feedback Form",
	]
)


with tab1:
	st.subheader("Student Grade Analyzer")
	st.write("Use numeric inputs, sliders, radio buttons, and metrics.")

	col1, col2 = st.columns(2)
	with col1:
		math_score = st.number_input("Math score", min_value=0, max_value=100, value=78)
		science_score = st.number_input("Science score", min_value=0, max_value=100, value=82)
		english_score = st.number_input("English score", min_value=0, max_value=100, value=75)

	with col2:
		attendance = st.slider("Attendance (%)", min_value=0, max_value=100, value=88)
		grading_scheme = st.radio("Grading scheme", ["Lenient", "Standard", "Strict"], horizontal=True)
		extra_credit = st.checkbox("Apply extra credit (+3 marks)", value=False)

	score_avg = (math_score + science_score + english_score) / 3
	if extra_credit:
		score_avg = min(score_avg + 3, 100)

	penalty = 0
	if attendance < 75:
		# Example rule: low attendance reduces final score.
		penalty = 5

	if grading_scheme == "Lenient":
		final_score = min(score_avg - penalty + 2, 100)
	elif grading_scheme == "Strict":
		final_score = max(score_avg - penalty - 2, 0)
	else:
		final_score = max(min(score_avg - penalty, 100), 0)

	if final_score >= 90:
		grade = "A"
	elif final_score >= 80:
		grade = "B"
	elif final_score >= 70:
		grade = "C"
	elif final_score >= 60:
		grade = "D"
	else:
		grade = "F"

	m1, m2, m3 = st.columns(3)
	m1.metric("Final Score", f"{final_score:.1f}")
	m2.metric("Letter Grade", grade)
	m3.metric("Attendance Penalty", f"-{penalty}")

	st.bar_chart(
		{
			"Scores": {
				"Math": math_score,
				"Science": science_score,
				"English": english_score,
				"Final": round(final_score, 1),
			}
		}
	)


with tab2:
	st.subheader("Health + Budget Helper")
	st.write("Use forms, selectboxes, and computed outputs in one scenario.")

	# st.form batches multiple inputs and computes results only on submit.
	with st.form("health_budget_form"):
		st.markdown("#### Part A: BMI Calculator")
		height_cm = st.number_input("Height (cm)", min_value=100.0, max_value=230.0, value=170.0)
		weight_kg = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=68.0)

		st.markdown("#### Part B: Monthly Expense Split")
		income = st.number_input("Monthly income", min_value=0.0, value=50000.0, step=500.0)
		rent = st.number_input("Rent", min_value=0.0, value=15000.0, step=500.0)
		food = st.number_input("Food", min_value=0.0, value=6000.0, step=500.0)
		transport = st.number_input("Transport", min_value=0.0, value=2500.0, step=250.0)
		others = st.number_input("Other expenses", min_value=0.0, value=3000.0, step=500.0)

		submitted = st.form_submit_button("Calculate")

	if submitted:
		# BMI formula: weight (kg) divided by squared height in meters.
		bmi = weight_kg / ((height_cm / 100) ** 2)
		total_expenses = rent + food + transport + others
		savings = income - total_expenses

		if bmi < 18.5:
			bmi_label = "Underweight"
		elif bmi < 25:
			bmi_label = "Normal"
		elif bmi < 30:
			bmi_label = "Overweight"
		else:
			bmi_label = "Obese"

		c1, c2, c3 = st.columns(3)
		c1.metric("BMI", f"{bmi:.1f}")
		c2.metric("BMI Category", bmi_label)
		c3.metric("Savings", f"Rs. {savings:,.0f}")

		st.table(
			{
				"Category": ["Rent", "Food", "Transport", "Others", "Total", "Income"],
				"Amount": [rent, food, transport, others, total_expenses, income],
			}
		)


with tab3:
	st.subheader("Daily Schedule Planner")
	st.write("Use date/time input, multiselect, and color picker.")

	plan_date = st.date_input("Select date", value=datetime.date.today())
	start_time = st.time_input("Start time", value=datetime.time(9, 0))
	end_time = st.time_input("End time", value=datetime.time(17, 0))
	tasks = st.multiselect(
		"Choose tasks",
		["Study Python", "Build API", "Exercise", "Read docs", "Work on project", "Practice DSA"],
		default=["Study Python", "Work on project"],
	)
	highlight_color = st.color_picker("Highlight color", "#1f77b4")

	st.write("### Plan Summary")
	st.markdown(
		f"""
		- Date: **{plan_date}**
		- Time: **{start_time.strftime('%H:%M')} to {end_time.strftime('%H:%M')}**
		- Tasks selected: **{len(tasks)}**
		"""
	)

	if tasks:
		# HTML rendering is enabled here to demonstrate dynamic styling.
		for item in tasks:
			st.markdown(f"<p style='color:{highlight_color}'>- {item}</p>", unsafe_allow_html=True)
	else:
		st.warning("No tasks selected yet.")


with tab4:
	st.subheader("Feedback Collection Demo")
	st.write("Use text area, file upload, toggle states, and status messaging.")

	experience = st.select_slider("How was your learning experience?", options=[1, 2, 3, 4, 5], value=4)
	topic = st.selectbox("Which topic did you enjoy most?", ["Widgets", "Forms", "Layout", "State", "Charts"])
	comments = st.text_area("Comments", placeholder="Share your thoughts")
	screenshot = st.file_uploader("Upload screenshot (optional)", type=["png", "jpg", "jpeg"])

	if st.button("Submit feedback"):
		# Clicking this button flips state so success message persists.
		st.session_state.feedback_submitted = True

	if st.session_state.feedback_submitted:
		st.success("Feedback submitted successfully.")
		st.write(
			{
				"experience": experience,
				"favorite_topic": topic,
				"comment_length": len(comments),
				"file_uploaded": screenshot is not None,
			}
		)

		with st.expander("Why this scenario matters"):
			st.write(
				"This section demonstrates a realistic feedback workflow with both optional and required fields."
			)