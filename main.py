import streamlit as st
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

st.set_page_config(
    page_title="SubSmart",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.html("""
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"], .main {
    background: #090c10 !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #e8edf3 !important;
  }
  #MainMenu, footer, header { visibility: hidden !important; }
  
  .block-container { padding: 0 !important; max-width: 100% !important; }
  section[data-testid="stMain"] > div { padding-top: 0 !important; }

  .grid-bg {
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background-image:
      linear-gradient(rgba(0,212,170,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,212,170,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
  }
  .orb1 {
    position: fixed; width: 600px; height: 600px; border-radius: 50%;
    background: radial-gradient(circle, rgba(0,212,170,0.13) 0%, transparent 70%);
    top: -200px; left: -200px; z-index: 0; pointer-events: none;
    animation: pulse 6s ease-in-out infinite;
  }
  .orb2 {
    position: fixed; width: 500px; height: 500px; border-radius: 50%;
    background: radial-gradient(circle, rgba(0,153,255,0.10) 0%, transparent 70%);
    bottom: -150px; right: -150px; z-index: 0; pointer-events: none;
    animation: pulse 8s ease-in-out infinite reverse;
  }
  @keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50%       { transform: scale(1.15); opacity: 0.7; }
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .land-wrap {
    position: relative; z-index: 1; min-height: 88vh;
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 60px 24px; text-align: center;
  }
  .badge {
    display: inline-flex; align-items: center; gap: 8px;
    border: 1px solid #00d4aa; background: rgba(0,212,170,0.08);
    color: #00d4aa; font-size: 12px; font-weight: 600;
    letter-spacing: 2px; text-transform: uppercase;
    padding: 6px 18px; border-radius: 100px; margin-bottom: 28px;
    animation: fadeUp 0.5s ease both;
  }
  .land-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(48px, 8vw, 90px);
    font-weight: 800; line-height: 1.0; letter-spacing: -2px;
    color: #e8edf3; animation: fadeUp 0.6s 0.1s ease both;
  }
  .land-title span {
    background: linear-gradient(135deg, #00d4aa, #0099ff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  }
  .land-sub {
    font-size: 18px; color: #5a6478; max-width: 500px;
    margin: 20px auto 48px; line-height: 1.7;
    animation: fadeUp 0.6s 0.2s ease both;
  }
  .features {
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 16px; max-width: 900px; width: 100%;
    margin: 56px auto 0; animation: fadeUp 0.6s 0.35s ease both;
  }
  .feat-card {
    background: #111720; border: 1px solid #1e2530;
    border-radius: 16px; padding: 26px 20px; text-align: left;
    transition: border-color 0.25s, transform 0.25s;
  }
  .feat-card:hover { border-color: #00d4aa; transform: translateY(-5px); }
  .feat-icon { font-size: 26px; margin-bottom: 12px; }
  .feat-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 14px; margin-bottom: 8px; color: #e8edf3; }
  .feat-desc { font-size: 13px; color: #5a6478; line-height: 1.6; }

  .auth-outer {
    position: relative; z-index: 1;
    padding: 0px 24px 40px;
  }
  .auth-card {
    background: #111720; border: 1px solid #1e2530;
    border-radius: 24px; padding: 48px 44px; width: 100%; max-width: 460px;
    box-shadow: 0 40px 80px rgba(0,0,0,0.6);
    animation: fadeUp 0.45s ease both;
  }
  .auth-logo { font-size: 38px; text-align: center; margin-bottom: 8px; }
  .auth-title { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 28px; text-align: center; margin-bottom: 4px; color: #e8edf3; }
  .auth-sub { color: #5a6478; font-size: 14px; text-align: center; margin-bottom: 36px; }
  .form-label { font-size: 11px; font-weight: 600; letter-spacing: 1.2px; text-transform: uppercase; color: #5a6478; margin-bottom: 8px; display: block; }
  .switch-link { text-align: center; font-size: 13px; color: #5a6478; margin-top: 20px; }
  .switch-link span { color: #00d4aa; cursor: pointer; font-weight: 600; }
  .divider { display: flex; align-items: center; gap: 12px; margin: 20px 0; color: #5a6478; font-size: 12px; }
  .divider::before, .divider::after { content: ''; flex: 1; height: 1px; background: #1e2530; }

  [data-testid="stTextInput"] input {
    background: #0a0e14 !important; border: 1px solid #1e2530 !important;
    border-radius: 10px !important; color: #e8edf3 !important;
    font-family: 'DM Sans', sans-serif !important; font-size: 15px !important;
  }
  [data-testid="stTextInput"] input:focus {
    border-color: #00d4aa !important;
    box-shadow: 0 0 0 3px rgba(0,212,170,0.12) !important; outline: none !important;
  }
  [data-testid="stTextInput"] label { display: none !important; }

  [data-testid="stButton"] > button {
    background: linear-gradient(135deg, #00d4aa, #0099ff) !important;
    color: #090c10 !important; font-weight: 700 !important; font-size: 15px !important;
    border-radius: 12px !important; border: none !important;
    box-shadow: 0 0 28px rgba(0,212,170,0.25) !important;
    font-family: 'DM Sans', sans-serif !important;
  }
  [data-testid="stButton"] > button:hover {
    box-shadow: 0 0 48px rgba(0,212,170,0.4) !important;
    transform: translateY(-1px) !important;
  }
  [data-testid="stAlert"] { border-radius: 12px !important; }
  .welcome-name { font-family: 'Syne', sans-serif; font-size: 30px; font-weight: 800; color: #e8edf3; }

  /* unified auth card via streamlit column */
  [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlockBorderWrapper"],
  div[data-testid="column"]:has(.form-label) {
    background: #111720 !important;
    border: 1px solid #1e2530 !important;
    border-radius: 24px !important;
    padding: 8px 20px 28px !important;
    box-shadow: 0 40px 80px rgba(0,0,0,0.5) !important;
  }
  .welcome-sub  { color: #5a6478; font-size: 14px; margin-top: 4px; }
</style>
""")

# ── Session state ──────────────────────────────────────────────────────────────
if "page"      not in st.session_state: st.session_state.page      = "landing"
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "username"  not in st.session_state: st.session_state.username  = ""
if "user_id"   not in st.session_state: st.session_state.user_id   = None  # ✅ CHANGE 1

st.markdown('<div class="grid-bg"></div><div class="orb1"></div><div class="orb2"></div>', unsafe_allow_html=True)

# Hide sidebar on non-dashboard pages
if st.session_state.page != "dashboard":
    st.html("<style>[data-testid=\"stSidebar\"] { display: none !important; }</style>")


# ══════════════════════════════════════════════════════════════════════════════
# LANDING
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.page == "landing":

    st.markdown("""
    <div class="land-wrap">
      <div class="badge">💳 &nbsp; Subscription Intelligence</div>
      <h1 class="land-title">Take control of<br><span>every subscription</span></h1>
      <p class="land-sub">SubSmart tracks, analyzes, and alerts you about your subscriptions —
      so you never overpay or miss a renewal again.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([3, 1, 3])
    with c2:
        if st.button("→  Get Started", key="goto_login"):
            st.session_state.page = "login"
            st.rerun()

    st.markdown("""
    <div class="features">
      <div class="feat-card"><div class="feat-icon">📊</div>
        <div class="feat-title">Spending Analysis</div>
        <div class="feat-desc">Visualize monthly spend across all subscriptions in one dashboard.</div></div>
      <div class="feat-card"><div class="feat-icon">🔔</div>
        <div class="feat-title">Renewal Alerts</div>
        <div class="feat-desc">Get notified before any subscription renews so you stay in control.</div></div>
      <div class="feat-card"><div class="feat-icon">💡</div>
        <div class="feat-title">Health Score</div>
        <div class="feat-desc">Your personal subscription health score — spot waste instantly.</div></div>
      <div class="feat-card"><div class="feat-icon">🕵️</div>
        <div class="feat-title">Hidden Losses</div>
        <div class="feat-desc">Detect forgotten subscriptions quietly draining your wallet.</div></div>
    </div>
    <div style="height:80px"></div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LOGIN
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "login":

    cb, _ = st.columns([1, 7])
    with cb:
        if st.button("← Back", key="back_btn"):
            st.session_state.page = "landing"
            st.rerun()

    _, cf, _ = st.columns([1, 2, 1])
    with cf:
        st.markdown("""
        <div style="text-align:center; padding: 32px 0 28px;">
          <div style="font-size:38px; margin-bottom:10px;">💳</div>
          <div style="font-family:'Syne',sans-serif; font-weight:800; font-size:28px; color:#e8edf3; margin-bottom:4px;">Welcome back</div>
          <div style="color:#5a6478; font-size:14px;">Sign in to your SubSmart account</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="form-label">Email</span>', unsafe_allow_html=True)
        email = st.text_input("e", placeholder="Enter your email", key="email_input", label_visibility="collapsed")

        st.markdown('<span class="form-label" style="margin-top:14px;display:block;">Password</span>', unsafe_allow_html=True)
        password = st.text_input("p", placeholder="Enter your password", type="password", key="pass_input", label_visibility="collapsed")

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        if st.button("Sign In  →", key="login_btn"):
            if not email.strip() or not password.strip():
                st.error("Please enter both email and password.")
            else:
                try:
                    from db_connection import get_connection
                    conn = get_connection()
                    if conn is None:
                        st.error("❌ Could not connect to database.")
                    else:
                        cur = conn.cursor()
                        cur.execute(
                            "SELECT NAME, USER_ID FROM loginUsers WHERE EMAIL = :1 AND PASSWORD = :2",  # ✅ CHANGE 2
                            [email.strip(), password.strip()]
                        )
                        row = cur.fetchone()
                        cur.close(); conn.close()
                        if row:
                            st.session_state.logged_in = True
                            st.session_state.username  = row[0]
                            st.session_state.user_id   = row[1]  # ✅ CHANGE 2
                            st.session_state.page      = "dashboard"
                            st.rerun()
                        else:
                            st.error("❌ Invalid email or password.")
                except Exception as e:
                    st.error(f"Database error: {e}")

        st.markdown("""
        <div class="divider">or</div>
        <div class="switch-link">Don't have an account? <span id="goto-signup">Sign Up</span></div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
        if st.button("Create an account →", key="goto_signup"):
            st.session_state.page = "signup"
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# SIGN UP
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "signup":

    cb2, _ = st.columns([1, 7])
    with cb2:
        if st.button("← Back to Login", key="back_to_login"):
            st.session_state.page = "login"
            st.rerun()

    _, cf2, _ = st.columns([1, 2, 1])
    with cf2:
        st.markdown("""
        <div style="text-align:center; padding: 32px 0 28px;">
          <div style="font-size:38px; margin-bottom:10px;">✨</div>
          <div style="font-family:'Syne',sans-serif; font-weight:800; font-size:28px; color:#e8edf3; margin-bottom:4px;">Create account</div>
          <div style="color:#5a6478; font-size:14px;">Join SubSmart and take control of your subscriptions</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="form-label">Full Name</span>', unsafe_allow_html=True)
        new_name = st.text_input("n", placeholder="Enter your full name", key="signup_name", label_visibility="collapsed")

        st.markdown('<span class="form-label" style="margin-top:14px;display:block;">Email</span>', unsafe_allow_html=True)
        new_email = st.text_input("ne", placeholder="Enter your email", key="signup_email", label_visibility="collapsed")

        st.markdown('<span class="form-label" style="margin-top:14px;display:block;">Password</span>', unsafe_allow_html=True)
        new_pass = st.text_input("np", placeholder="Create a password", type="password", key="signup_pass", label_visibility="collapsed")

        st.markdown('<span class="form-label" style="margin-top:14px;display:block;">Confirm Password</span>', unsafe_allow_html=True)
        confirm_pass = st.text_input("cp", placeholder="Confirm your password", type="password", key="confirm_pass", label_visibility="collapsed")

        st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

        if st.button("Create Account  →", key="signup_btn"):
            if not new_name.strip() or not new_email.strip() or not new_pass.strip() or not confirm_pass.strip():
                st.error("Please fill in all fields.")
            elif new_pass != confirm_pass:
                st.error("❌ Passwords do not match.")
            elif len(new_pass) < 6:
                st.error("❌ Password must be at least 6 characters.")
            else:
                try:
                    from db_connection import get_connection
                    conn = get_connection()
                    if conn is None:
                        st.error("❌ Could not connect to database.")
                    else:
                        cur = conn.cursor()
                        cur.execute("SELECT COUNT(*) FROM loginUsers WHERE EMAIL = :1", [new_email.strip()])
                        count = cur.fetchone()[0]

                        if count > 0:
                            st.error("❌ An account with this email already exists.")
                        else:
                            cur.execute(
                                "INSERT INTO loginUsers (NAME, EMAIL, PASSWORD, CREATED_AT) VALUES (:1, :2, :3, SYSDATE)",
                                [new_name.strip(), new_email.strip(), new_pass.strip()]
                            )
                            conn.commit()
                            cur.close(); conn.close()
                            st.success("✅ Account created! Redirecting to login...")
                            import time; time.sleep(1.5)
                            st.session_state.page = "login"
                            st.rerun()

                except Exception as e:
                    st.error(f"Database error: {e}")

        st.markdown("""
        <div class="switch-link" style="margin-top:16px;">
          Already have an account? <span>Sign In</span>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.page == "dashboard":

    st.markdown(f"""
    <div style="padding:40px 48px 20px;position:relative;z-index:1;">
      <div class="welcome-name">Hey, {st.session_state.username} 👋</div>
      <div class="welcome-sub">Welcome back to SubSmart</div>
    </div>""", unsafe_allow_html=True)

    cl, _ = st.columns([1, 7])
    with cl:
        if st.button("Sign Out", key="logout"):
            st.session_state.logged_in = False
            st.session_state.username  = ""
            st.session_state.user_id   = None
            st.session_state.page      = "landing"
            st.rerun()

    try:
        import importlib.util
        pages_dir = os.path.join(os.path.dirname(__file__), "pages")
        spec = importlib.util.spec_from_file_location("Dashboard", os.path.join(pages_dir, "Dashboard.py"))
        mod  = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as e:
        st.info(f"Dashboard loading — connect your pages here. ({e})")