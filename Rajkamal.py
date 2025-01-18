import streamlit as st
from streamlit.components.v1 import html
import time
st.set_page_config(page_icon="logo.gif")
# Add custom CSS for styling
def add_custom_css():
    st.markdown("""
    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }
        .main {
            background-color: #f4f7f6;
        }
        .sidebar .sidebar-content {
            background-color: #1c1c1c;
            color: #fff;
        }
        .stApp {
            font-family: 'Roboto', sans-serif;
        }
        h1 {
            font-size: 3rem;
            color: #1c1c1c;
            text-align: center;
            margin-top: 2rem;
        }
        .section-title {
            color: #1c1c1c;
            font-size: 2rem;
            font-weight: bold;
            margin-top: 2rem;
            text-align: center;
        }
        .about-text {
            font-size: 1.1rem;
            color: #333;
            text-align: justify;
            line-height: 1.8;
            margin-top: 1rem;
        }
        .card {
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 2rem;
            margin: 1rem 0;
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-10px);
        }
        .card-title {
            font-size: 1.5rem;
            color: #007bff;
            font-weight: bold;
        }
        .animate-text {
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .contact-card {
            background-color: #007bff;
            color: #fff;
            border-radius: 8px;
            padding: 2rem;
            text-align: center;
        }
        .contact-card h2 {
            font-size: 1.8rem;
        }
    </style>
    """, unsafe_allow_html=True)

# Home Page with Animations and Advanced Layout
def home_page():
    st.title("Welcome to My Portfolio!")
   

    # Animated Text Introduction
    st.markdown('<p class="animate-text">Hello! I am a passionate software developer.</p>', unsafe_allow_html=True)

    # Display an introduction paragraph

    st.markdown("""
    I'm a self-taught developer with a passion for solving real-world problems using technology. 
    My goal is to build applications that not only solve problems but also provide a great user experience. 
    I enjoy working on challenging projects and constantly strive to improve my skills.""")

    # Use columns for a neat layout
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('### My Skills')
        st.markdown("""
        - Python Programming
        - Machine Learning
        - Data Analysis
        - Web Development (Flask,Streamlit)
        """)
    
    with col2:
        st.markdown('### Tools I Use')
        st.markdown("""
        - Git/GitHub
        - MYSQL
        - VS Code
        - Microsoft Power BI
        """)

    # Interactive button to navigate to About Page
    if st.button('Learn More About Me'):
        st.write("Click on the sidebar to explore more!")

# About Page with Advanced Layout
def about_page():
    st.html("<center><h1>About Me</center>")
    
    st.markdown('<p class="section-title">A Little Bit About Myself</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Pursuing a B.Tech in Artificial Intelligence and Data Science at CARE College of Engineering,
    serving as the Department Vice President and Hostel Resident Leader. Proactively organize workshops on Web Development and AI, 
    alongside conducting daily programming classes for junior students to enhance their coding skills. 
    Committed to fostering technical growth and leadership within the academic community. 

    
    """)

    # Two columns layout for more detailed info
    col1, col2 = st.columns(2)
    with col1:
        st.image('Rajkamal.png', caption="My Photo", use_container_width=50)
    
    with col2:
        st.markdown("""
        I'm passionate about learning new technologies and continuously improving my skills to stay at the forefront of the tech industry. 
        With a strong interest in problem-solving, I enjoy building innovative solutions that address real-world challenges. 
        I thrive in collaborative environments, actively engage with professionals to exchange ideas, and contribute to the open-source community to promote shared learning. 
        Additionally, I take pride in mentoring peers and junior students, fostering a culture of knowledge-sharing and technical excellence.
        """)

# Projects Page with Interactive Cards
def projects_page():
    st.title("My Projects")
    
    st.markdown('<p class="section-title">Highlighted Projects</p>', unsafe_allow_html=True)

    # Example project cards
    project1, project2 = st.columns(2)
    with project1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">MySQL Database Application with Python GUI (Tkinter)</div>', unsafe_allow_html=True)
        st.markdown("""
        This project creates a small-scale database application using Tkinter for the GUI and MySQL Connector for database interaction. 
        It supports basic SQL operations: INSERT, UPDATE, DELETE,SELECT.The app allows users to manage and manipulate data in a 
        MySQL database through an intuitive interface.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("""
        - **Gitup Link**:  [MY DB](https://github.com/rk-rajkamalR/MY-DB)
        """)
    
    with project2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Image Classification Application with Python (OpenCv)</div>', unsafe_allow_html=True)
        st.markdown("""
        Image classification leverages Open Computer Vision (openCV's) image processing to identify crime scenes, suspects, or evidence. 
        Automated tagging uses machine learning to categorize and label images based on predefined criteria. 
        This streamlines image retrieval and supports efficient analysis.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
       
        st.markdown("""
        - **Githup Link**:  [Image Classification](https://github.com/rk-rajkamalR/image-classification-)
        """)

    # Additional project cards (add more if necessary)
    st.markdown('<div class="card">',unsafe_allow_html=True)
    
    

    st.markdown('<div class="card-title">Gemini AI Integration Hub</div>', unsafe_allow_html=True)
    st.markdown("""
    Developed a web application using Python Streamlit, seamlessly integrating Google’s Gemini AI via API key for enhanced functionality. 
    The app leverages Gemini AI's capabilities to deliver intelligent and dynamic features, providing users with an interactive and efficient experience. 
    Designed with a focus on scalability and ease of use, it demonstrates proficiency in API integration and cutting-edge AI technologies.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("""
    - **View Site**:  [Gemini Clone](https://rajkamal-rk.onrender.com/)
    """)

# Contact Page with Advanced Layout and Cards
def contact_page():
    st.title("Contact Me")

    st.markdown('<p class="section-title">Get in Touch</p>', unsafe_allow_html=True)
    
    # Contact form
    contact_card = st.container()
    with contact_card:
        st.markdown('<div class="contact-card">', unsafe_allow_html=True)
        st.markdown('<h2>Contact Information</h2>', unsafe_allow_html=True)
        st.markdown("""
        - **Email**: rajkamalrk.in@gmail.com
        - **LinkedIn**: [My LinkedIn](https://www.linkedin.com/in/rajkamal-ravichandran/?originalSubdomain=in)
        - **GitHub**: [My GitHub](https://github.com/Rajkamal123456789)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Using a form for more advanced interaction
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            st.write(f"Thank you {name} for reaching out! I will get back to you shortly.")
            st.write(f"Message: {message}")

# Information Page with More Details
def information_page():
    st.title("Additional Information")
    
    st.markdown('<p class="section-title">More About My Work</p>', unsafe_allow_html=True)
    
    st.write("""
    - I'm constantly exploring new frameworks and libraries.
    - I am passionate about building scalable and efficient solutions.
    - My goal is to make a positive impact in the tech world.
    - I participate in open-source projects to improve and contribute to the community.
    """)

# Main Function with Navigation
def main():
    add_custom_css()  # Add custom CSS styling
    menu = ["Home", "About", "Projects", "Contact", "Information"]
    choice = st.sidebar.selectbox("Select a Page", menu)

    if choice == "Home":
        home_page()
    elif choice == "About":
        about_page()
    elif choice == "Projects":
        projects_page()
    elif choice == "Contact":
        contact_page()
    elif choice == "Information":
        information_page()

if __name__ == "__main__":
    main()
