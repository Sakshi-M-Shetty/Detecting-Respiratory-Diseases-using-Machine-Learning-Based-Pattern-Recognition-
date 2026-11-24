import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Respiratory Disease Detection",
    layout="wide",
    page_icon="🫁"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    font-family: 'Segoe UI', sans-serif;
}

/* Main container */
.block-container {
    padding-top: 2rem;
}

/* Glass card */
.glass {
    background: rgba(255,255,255,0.08);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Title */
.title {
    font-size: 34px;
    font-weight: 700;
    color: white;
}

/* Subtitle */
.subtitle {
    font-size: 16px;
    color: #d1d1d1;
    margin-bottom: 20px;
}

/* Inputs */
.stTextInput>div>div>input {
    border-radius: 10px;
    padding: 12px;
}

/* Button */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    opacity: 0.9;
}

/* Branding panel */
.brand {
    color: white;
    padding: 40px;
}

.brand h1 {
    font-size: 40px;
}

.brand p {
    font-size: 18px;
    color: #ccc;
}

</style>
""", unsafe_allow_html=True)

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([1.2, 1])

# ------------------ LEFT PANEL (Branding) ------------------
with col1:
    st.markdown("""
    <div class="brand">
        <h1>🫁 Respiratory AI</h1>
        <p>
        Detect respiratory diseases using advanced Machine Learning models 
        trained on spirometry data.
        </p>
    </div>
    """, unsafe_allow_html=True)

    

# ------------------ RIGHT PANEL (Login Card) ------------------
with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.markdown('<div class="title">Admin Login</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Secure access to system dashboard</div>', unsafe_allow_html=True)

    username = st.text_input("👤 Username", placeholder="Enter admin username")
    password = st.text_input("🔒 Password", type="password", placeholder="Enter password")

    login = st.button(" Login")

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ AUTHENTICATION ------------------
if login:
    if username == "admin" and password == "admin123":
        st.success("Login successful!")

        st.markdown("## 📊 Dashboard")
        
        col1, col2, col3 = st.columns(3)

        col1.metric("Patients", "120", "+10")
        col2.metric("Predictions", "340", "+25")
        col3.metric("Accuracy", "96%", "+2%")

        st.info("System ready for spirometry-based prediction.")

    else:
        st.error("Invalid credentials. Try again.")