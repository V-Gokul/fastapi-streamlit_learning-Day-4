import streamlit as st

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Modern Calculator",
    page_icon="🧮",
    layout="centered"
)

# -----------------------
# Custom CSS
# -----------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.main-card {
    background: rgba(255,255,255,0.08);
    padding: 35px;
    border-radius: 20px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}

.title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:white;
    margin-bottom:10px;
}

.subtitle {
    text-align:center;
    color:#CBD5E1;
    margin-bottom:30px;
}

.result-box {
    background:#2563EB;
    color:white;
    padding:18px;
    border-radius:12px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Card
# -----------------------
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="title">🧮 Smart Calculator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Modern Streamlit Calculator</div>',
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0)

with col2:
    num2 = st.number_input("Second Number", value=0.0)

operation = st.selectbox(
    "Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Modulus",
    ],
)

if st.button("Calculate", use_container_width=True):
    try:
        if operation == "Addition":
            result = num1 + num2

        elif operation == "Subtraction":
            result = num1 - num2

        elif operation == "Multiplication":
            result = num1 * num2

        elif operation == "Division":
            if num2 == 0:
                st.error("Cannot divide by zero.")
                st.stop()
            result = num1 / num2

        elif operation == "Power":
            result = num1 ** num2

        elif operation == "Modulus":
            result = num1 % num2

        st.markdown(
            f'<div class="result-box">Result: {result}</div>',
            unsafe_allow_html=True,
        )

    except Exception as e:
        st.error(str(e))

st.markdown("</div>", unsafe_allow_html=True)
