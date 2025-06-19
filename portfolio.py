import streamlit as st
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Welcome | Yuvraj", layout="wide")

# Rainbow wave CSS bar
st.markdown("""
    <style>
    .rainbow-line {
        height: 5px;
        background: linear-gradient(270deg, #ff0040, #ffae00, #00ff73, #00cfff, #8b00ff, #ff0040);
        background-size: 600% 600%;
        animation: wave 6s linear infinite;
        border-radius: 10px;
        margin: 10px 0;
    }

    @keyframes wave {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
""", unsafe_allow_html=True)

# Rainbow bar above navbar
st.markdown('<div class="rainbow-line"></div>', unsafe_allow_html=True)

# Horizontal menu
selected2 = option_menu(
    menu_title=None,
    options=["Home", "About", "Projects", "Skills", "Contact"],
    icons=["house", "person", "briefcase", "backpack" ,"person-rolodex"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Rainbow bar below navbar
st.markdown('<div class="rainbow-line" style="margin-top: -10px;"></div>', unsafe_allow_html=True)

# Display selected item
if selected2 == "Home":
    import time

    def typewriter(text, speed=0.03):
        typed_text = ""
        placeholder = st.empty()
        for char in text:
            typed_text += char
            placeholder.markdown(f"<h3 style='color:#00ffff;font-family:monospace;'>{typed_text}</h3>", unsafe_allow_html=True)
            time.sleep(speed)

    with st.container():
        st.markdown("""
            <style>
            .glitch {
                font-family: monospace;
                font-size: 28px;
                background: linear-gradient(90deg, red, green, blue);
                -webkit-background-clip: text;
                color: transparent;
                animation: wave 3s linear infinite;
            }
            @keyframes wave {
                0% { background-position: 0% 50%; }
                100% { background-position: 100% 50%; }
            }
            </style>
        """, unsafe_allow_html=True)

        # Typewriter effect welcome line
        typewriter("🧠 Welcome to the Simulation...", speed=0.05)

        # Glitch/wave effect subtitle
        st.markdown("<div class='glitch'>Booting up LLMs, Agents, and Backend Magic...</div>", unsafe_allow_html=True)

    st.markdown("""
    <style>
    .chat-bubble {
        background-color: #f0f0f5;
        border-radius: 15px;
        padding: 12px 20px;
        margin: 10px 0;
        display: inline-block;
        font-size: 18px;
        animation: fadeIn 1s ease-in;
        color: black;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)

    chat_lines = [
        "🤖: Hey, I’m <strong><strong style='color:#ff2800;font-family:monospace;'>Yuvraj</strong> — I don’t just chat with LLMs, I build them.",
        "🤖: I work with <strong>LLMs, RAG pipelines, and backend systems</strong> to create powerful AI-driven apps.",
        "🤖: I build with <strong>LangChain, Flask, Django, Streamlit, and FAISS</strong> — the full-stack force behind my AI tools.",
        "🤖: <strong>Always curious</strong>, <strong>always building ⚡</strong>",
    ]

    for line in chat_lines:
        st.markdown(f"<div class='chat-bubble'>{line}</div>", unsafe_allow_html=True)
        time.sleep(1.1)


elif selected2 == "About":
    st.header("👤 About Me")
    st.markdown("""
        <style>
        .typewriter {
    width: fit-content;
    margin: auto;
}
        
        
        .typewriter h3 {
    display: inline-block;
    overflow: hidden;
    border-right: .15em solid orange;
    white-space: nowrap;
    letter-spacing: .10em;
    animation: typing 4s steps(40, end), blink-caret .75s step-end infinite;
    color: #fff;
}


        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }

        @keyframes blink-caret {
            from, to { border-color: transparent }
            50% { border-color: orange; }
        }

        .timeline {
            border-left: 2px solid #FFD700;
            margin-left: 20px;
            padding-left: 20px;
        }
        .timeline-item {
            margin-bottom: 20px;
        }
        .timeline-item h4 {
            margin-bottom: 4px;
            color: #FFD700;
        }

        .belief-card {
            background: rgba(255,255,255,0.05);
            border: 1px solid #444;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            box-shadow: 0 0 10px rgba(255,255,255,0.1);
        }

        .pfp-container {
            width: 160px;
            height: 160px;
            border-radius: 50%;
            padding: 6px;
            background: linear-gradient(45deg, #FFD700, #ff7e5f, #feb47b);
            animation: borderGlow 5s infinite linear;
            margin: auto;
        }

        .pfp-container img {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            object-fit: cover;
        }

        @keyframes borderGlow {
            0% { filter: hue-rotate(0deg); }
            100% { filter: hue-rotate(360deg); }
        }
        </style>
    """, unsafe_allow_html=True)

    # Profile picture
    st.markdown("""
        <div class="pfp-container">
            <img src="https://avatars.githubusercontent.com/u/184723232?v=4" alt="Profile">
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Auto-type intro
    st.markdown("""
        <div class="typewriter">
          <h3>
    Yuvraj Kumar <br>
    Always curious, <br> 
                always building ⚡<br>
</h3>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Timeline
    st.subheader("🛤️ My Journey Into AI")
    st.markdown("""
    <div class="timeline">
        <div class="timeline-item">
            <h4>2024 – Discovery</h4>
            <p>Got curious about how ChatGPT works. It blew my mind and changed my career path.</p>
        </div>
        <div class="timeline-item">
            <h4>2025 - First Real Build</h4>
            <p>
                I built my first AI-powered project using LangChain, Mistral AI, Streamlit, and Django — 
                combining LLMs with solid backend logic to create a working product. 
                It was the “this is what I want to do” moment.
            </p>
        </div>
        <div class="timeline-item">
            <h4>Currently — Learning from the Roots</h4>
            <p>
                I’m now exploring Generative AI and LLMs from the ground up — going deep into how they actually work. 
                I’m also studying “LLMs From Scratch” by Sebastian Raschka to strengthen my understanding of tokenization, 
                architecture, training, and fine-tuning. 
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    #certification and achievements
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("🏆 Certifications & Achievements")
    belief_cols = st.columns(2)
    with belief_cols[0]:
        st.markdown("""
        <div class="belief-card">
            <h5>🏆 Finalist – Smart India Hackathon 2024</h5>
            <p>Built and integrated a rooftop-type classification ML model using Flask.</p>
        </div>
        """, unsafe_allow_html=True)
    with belief_cols[1]:
        st.markdown("""
        <div class="belief-card">
            <h5>🌐 CS50’s Web Programming</h5>
            <p>Mastered backend and frontend development with Django, SQL, JavaScript, and more.</p>
        </div>
        """, unsafe_allow_html=True)

elif selected2 == "Projects":
     
     st.markdown("""
                    <style>
                        .section-title {
                            text-align: center;
                            font-size: 30px;
                            color: #ff2800;
                            margin-bottom: 40px;
                        }

                        .project-card {
                            background: rgba(255, 255, 255, 0.05);
                            border: 1px solid #333;
                            padding: 1.5rem;
                            border-radius: 15px;
                            margin-bottom: 2rem;
                            box-shadow: 0 0 20px rgba(255,255,255,0.05);
                            transition: all 0.3s ease;
                        }

                        .project-card:hover {
                            transform: translateY(-5px);
                            box-shadow: 0 0 25px rgba(255,255,255,0.1);
                        }

                        .project-name {
                            font-size: 24px;
                            font-weight: bold;
                            color: #fff;
                        }

                        .tags {
                            margin: 0.5rem 0;
                        }

                        .tag {
                            display: inline-block;
                            background: #ff2800;
                            color: black;
                            padding: 0.3rem 0.6rem;
                            border-radius: 5px;
                            margin-right: 0.5rem;
                            font-size: 13px;
                            font-weight: 600;
                        }

                        .project-desc {
                            color: #ccc;
                            margin: 1rem 0;
                            font-size: 16px;
                        }

                        .buttons a {
                            text-decoration: none;
                            padding: 0.4rem 0.8rem;
                            margin-right: 1rem;
                            background: transparent;
                            border: 1px solid #ff2800;
                            color: #FFD700;
                            border-radius: 5px;
                            font-weight: 500;
                        }

                        .buttons a:hover {
                            background: #ff2800;
                            color: black;
                        }
                    </style>

                    <div class="section-title">🚀 Featured Projects</div>
                """, unsafe_allow_html=True)

                # --- Project 1: Lawgic AI ---
     st.markdown("""
                    <div class="project-card">
                        <div class="project-name">⚖️ Lawgic AI</div>
                        <div class="tags">
                            <span class="tag">LLM</span>
                            <span class="tag">RAG</span>
                            <span class="tag">LangChain</span>
                            <span class="tag">Django</span>
                            <span class="tag">Streamlit</span>
                        </div>
                        <div class="project-desc">
                            Lawgic AI gives you clear and reliable legal knowledge based on verified sources. Just ask your question, and it provides easy-to-understand answers to help you learn about laws, rights, and legal concepts—no complicated language, no confusion.
                        </div>
                        <div class="buttons">
                            <a href="https://github.com/yuvraj-kumar-dev/Lawgic_AI" target="_blank">GitHub</a>
                            <a href="https://lawgicai.streamlit.app/" target="_blank">Live Demo</a>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

                # --- Project 2: ResuMate ---
     st.markdown("""
                    <div class="project-card">
                        <div class="project-name">📄 ResuMate</div>
                        <div class="tags">
                            <span class="tag">Generative AI</span>
                            <span class="tag">Resume Builder</span>
                            <span class="tag">Streamlit</span>
                            <span class="tag">Hugging Face</span>
                        </div>
                        <div class="project-desc">
                           ResuMate is an AI agent that analyzes your resume and provides personalized feedback based on your required job description to improve its clarity, impact, and professionalism, ensuring it stands out to employers. Perfect for job seekers at any experience level.
                        </div>
                        <div class="buttons">
                            <a href="https://github.com/yuvraj-kumar-dev/ResuMate" target="_blank">GitHub</a>
                            <a href="https://resu-mate.streamlit.app/" target="_blank">Live Demo</a>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
    
if selected2 == "Skills":
    st.markdown("""
                <style>
                    .badge-box {
                        background: rgba(255, 255, 255, 0.05);
                        padding: 0.8rem 1.2rem;
                        border: 1px solid #444;
                        border-radius: 12px;
                        margin: 8px;
                        display: inline-block;
                        color: white;
                        font-weight: 500;
                        box-shadow: 0 0 10px rgba(255,255,255,0.1);
                    }
                    .section-title {
                        text-align: center;
                        font-size: 28px;
                        margin-bottom: 20px;
                        color: #FFD700;
                    }
                </style>
            """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>🧠 Skills Dashboard</div>", unsafe_allow_html=True)

            # --- Radar Chart ---
    categories = ['Programming Languages', 'Frameworks & Libraries', 'Web Development', 'AI/ML']
    skills_rating = [80, 75, 70, 65]  # out of 100

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
                r=skills_rating,
                theta=categories,
                fill='toself',
                name='Skill Level',
                line=dict(color='gold')
            ))

    fig.update_layout(
            polar=dict(
                bgcolor="rgba(0,0,0,0)",
                radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor='gray',
                linecolor='white',
                tickfont=dict(color='white')
                ),
                angularaxis=dict(
                    tickfont=dict(color='white')
                )
            ),
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)"
            )

    st.plotly_chart(fig, use_container_width=True)

            # --- Badges/Skills ---
    st.markdown("### 🏗️ Programming Languages")
    st.markdown("""
            <div class="badge-box">Python</div>
            <div class="badge-box">C</div>
            <div class="badge-box">JavaScript</div>
            """, unsafe_allow_html=True)

    st.markdown("### 🧰 Frameworks & Libraries")
    st.markdown("""
            <div class="badge-box">LangChain</div>
            <div class="badge-box">Transformers</div>
            <div class="badge-box">Hugging Face</div>
            <div class="badge-box">MistralAI API</div>
            """, unsafe_allow_html=True)

    st.markdown("### 🌐 Web Development")
    st.markdown("""
            <div class="badge-box">HTML</div>
            <div class="badge-box">CSS</div>
            <div class="badge-box">JavaScript</div>
            <div class="badge-box">Django</div>
            <div class="badge-box">Flask</div>
            """, unsafe_allow_html=True)

    st.markdown("### 📦 DevOps & Deployment")
    st.markdown("""
            <div class="badge-box">Render</div>
            <div class="badge-box">Railway</div>
            <div class="badge-box">Streamlit Cloud</div>
            """, unsafe_allow_html=True)

    st.markdown("### 🤖 AI/ML")
    st.markdown("""
            <div class="badge-box">LLMs</div>
            <div class="badge-box">RAG</div>
            <div class="badge-box">Prompt Engineering</div>
            <div class="badge-box">Fine-Tuning</div>
            """, unsafe_allow_html=True)
    
    
if selected2 == "Contact":
    st.markdown("""
                    <style>
                        [data-testid="stSidebar"] {
                            display: none;
                        }
                        [data-testid="collapsedControl"] {
                            display: none;
                        }
                    </style>
                """, unsafe_allow_html=True)

                # Hide sidebar
    st.markdown("""
                    <style>
                        [data-testid="stSidebar"] { display: none; }
                        [data-testid="collapsedControl"] { display: none; }
                        .chat-bubble {
                            background-color: #f0f0f5;
                            border-radius: 12px;
                            padding: 10px 15px;
                            margin: 8px 0;
                            display: inline-block;
                            font-size: 16px;
                            color: black;
                        }
                          .user {
            background: #f1efe7;
            color: #000000;
            text-align: right;
        }
                        .bot { text-align: left; background: rgba(255, 255, 255, 0.1); color: white; }
                        .social-icons a {
                            text-decoration: none;
                            font-weight: 600;
                            font-size: 18px;
                            margin-right: 15px;
                        }
                    </style>
                """, unsafe_allow_html=True)

                # Title
    st.markdown("<h1 style='text-align:center;'>📬 Contact Me</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>Let's connect, collaborate, or create something incredible together.</p>", unsafe_allow_html=True)

                # --- AI Chatbox Section ---
    st.markdown("### 🤖 Ask me anything!")

                # Chat context
    preset_responses = {
                        "Who are you?": "I'm Yuvraj Kumar — a developer crafting smart systems with LLMs, GenAI, and backend engineering. Passionate about building real-world AI tools using LangChain, Flask, Streamlit, and Django, I'm currently deep-diving into LLM internals, fine-tuning, and creating AI agents that actually do stuff.",
                        "How to contact": "You can email me at yuvrajkumar.dev@gmail.com or use the social links below.",
                        "Resume": "You can click below to access my resume or visit my LinkedIn.",
                        "GitHub": "Find my projects at https://github.com/yuvraj-kumar-dev.",
                        "LinkedIn": "I'm on LinkedIn at www.linkedin.com/in/yuvrajkumardev."
                    }

                    # --- Select-based Chat ---
    option = st.selectbox("🤖 Ask a question:", list(preset_responses.keys()))

    if option:
                        st.markdown(f"<div class='chat-bubble user'>🧑‍💻 You: {option}</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='chat-bubble bot'>🤖: {preset_responses[option]}</div>", unsafe_allow_html=True)

                    # --- QR Code Section ---
    if option == "Resume":
                        import requests

                        st.markdown("### 📄 My Resume")

                        # View and download links
                        view_link = "https://drive.google.com/file/d/1Sfv7nIERz90GdRyf8XQSI88uqadpu9Ny/view"
                        download_link = "https://drive.google.com/uc?export=download&id=1Sfv7nIERz90GdRyf8XQSI88uqadpu9Ny"

                        # View resume as hyperlink
                        st.markdown(f"[👀 View Resume]({view_link})", unsafe_allow_html=True)

                        # Fetch the resume file and make download button
                        response = requests.get(download_link)
                        st.download_button(
                            label="📥 Download Resume",
                            data=response.content,
                            file_name="Yuvraj_Kumar_Resume.pdf",
                            mime="application/pdf"
                        )
                    

                    # --- Contact Buttons ---
    st.markdown("### 🌐 Social Links")
    st.markdown("""
                    <div class="social-icons">
                        <a href="mailto:yuvrajkumar.dev@gmail.com" target="_blank">📧 Email</a>
                        <a href="https://github.com/yuvraj-kumar-dev" target="_blank">💻 GitHub</a>
                        <a href="https://www.linkedin.com/in/yuvrajkumardev" target="_blank">🔗 LinkedIn</a>
                        <a href="https://huggingface.co/enlightenment" target="_blank">🤗 HuggingFace</a>
                    </div>
                    """, unsafe_allow_html=True)

                    # Rain effect
    rain(emoji="✉️", font_size=20, falling_speed=5, animation_length="infinite")



