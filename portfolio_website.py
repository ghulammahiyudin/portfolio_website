import streamlit as st
import google.generativeai as genai
from PIL import Image
from persona import persona

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title='Ghulam Mahiyudin - Portfolio', page_icon=":wave:", layout='wide')


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


def main():

    st.markdown("""
        <div class="header">
            <a href="">Home</a>
            <a href="#about">About</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    """, unsafe_allow_html=True)

    show_home()
    show_bot()
    show_about()
    show_resume()
    show_projects()
    show_contact()
    show_footer()


def show_home():

    st.markdown("<a id='home'></a>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.title("")
        st.subheader("Hi, There :wave:")
        st.title("I'm Ghulam Mahiyudin")
        st.write("")
        st.write("""
                I'm Software Engineering student and having expertise in frontend technologies including HTML, CSS, JavaScript, and Bootstrap. I am dedicated, a quick learner, and consistently strive to enhance my skills.
                """)

    with col2:
        st.image("images/coder.png")

    st.write("---")


def show_bot():

    col1, col2, col3 = st.columns([1.5, 0.3, 1.2])

    with col1:

        st.subheader("Interact with my personal AI bot.")
        user_input = st.text_input(label="Curious about something?", placeholder="Enter your Query here:")
        if st.button('Send a Spark', use_container_width=True):
            prompt = persona + "Here is the question that the user asked: " + user_input
            response = model.generate_content(prompt)
            st.write(response.text)

    with col2:
        st.write("")

    with col3:
        st.image("images/hero.jpg")

    st.write("---")


def show_about():

    st.markdown("<a id='about'></a>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:

        st.subheader("About me")
        st.write("""I'm Ghulam Mahiyudin, with expertise in frontend technologies including HTML, CSS, JavaScript, and Bootstrap. I have worked on various projects such as business, blogs, and portfolio websites. I am dedicated, a quick learner, and consistently strive to enhance my skills.
        """)
        st.write("""Also I'm studying Software Engineering. I'm having understanding of C++, with OOP and DSA concetps. Also I have explored Desktop Application Development, Mobile Application Development Web Development during my degree.
        """)
        st.subheader("I like to code and explore the coding world!")

    with col2:
        st.subheader("My Skills")

        skills = {
            "HTML": 85,
            "CSS": 75,
            "JavaScript": 70,
            "Bootstrap": 80,
            "Python": 60
        }

        for skill, level in skills.items():
            st.write(skill)
            st.progress(level)

    st.write("---")


def show_resume():

    col1, col2 = st.columns([1, 1])

    with col1:

        st.text("Internship")
        st.subheader("Frontend Developer")
        st.write("""
        *August - September 2023*

        Agile Web Solutions, Sialkot, Pakistan

        Major: HTML, CSS, JS, Bootstrap
        """)

        st.text("Certification")
        st.subheader("Responsive Web Design")
        st.write("""
        *April 2023*

        FreeCodeCamp.org

        Major: HTML & CSS
        """)

    with col2:
        st.text("Education")
        st.subheader("BS Software Engineering")
        st.write("""
        *2021 - Present*

        University of Sialkot, Sialkot, Pakistan

        Major: C++, OOP, DSA, SQL
        """)

        st.subheader("FSC Pre Engineering")
        st.write("""
        *2019 - 2021*

        The Standard College, Sialkot, Pakistan

        Major: Maths, Physics, Chemistry
        """)

    st.write("---")


def show_projects():

    st.markdown("<a id='projects'></a>", unsafe_allow_html=True)

    st.header('Projects')

    # Project data
    projects = [

        {
            "image": "images/beauticas.png",
            "description": "Designed its interface using HTML, CSS, and JS. And used owl-carousel and fancy box popup library.",
            "url": "https://beauticas.com"
        },
        {
            "image": "images/max-gold-impex.png",
            "description": "Designed its interface using HTML, CSS, and JS. And used owl-carousel and fancy box popup library.",
            "url": "https://maxgoldimpex.com"
        },
        {
            "image": "images/adidas.png",
            "description": "I made its interface using HTML, CSS, and JS. And used slick slider and fancy box popup library.",
            "url": "https://ghulammahiyudin.github.io/adidas-landing-page/"
        },
        {
            "image": "images/ideanet.it.png",
            "description": "I was a member of the frontend team and made the interface at the initial stage using HTML, CSS, JS, and Bootstrap.",
            "url": "https://ideanet.it"
        },
        {
            "image": "images/kavish-enterprises.png",
            "description": "I have designed its interface using HTML, CSS, JS, and Bootstrap. Also used owl-carousel and fancy box popup library.",
            "url": "https://kavishenterprises.com"
        }
    ]

    for i in range(0, len(projects), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(projects):
                project = projects[i + j]
                with col:
                    image = Image.open(project["image"])
                    st.image(image, use_column_width=True)
                    st.write(project["description"])
                    st.markdown(f'<a class="project-button" href="{project["url"]}" target="_blank">View Project</a>',
                                unsafe_allow_html=True)

    st.write("---")


def show_contact():

    st.markdown("<a id='contact'></a>", unsafe_allow_html=True)

    st.header('Get in touch with me!')
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
            <form action="https://formsubmit.co/ghulammahiyudinashraf@email.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" rows="3" required></textarea>
                <button type="submit">SEND MESSAGE</button>
            </form>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="contact-detail">
                <p>Email: <a href="mailto:ghulammahiyudinn@gmail.com">ghulammahiyudinn@gmail.com</a></p>
                <p>Phone: <a href="tel:+923092941887">+92 309 2941887</a></p>
                <p>LinkedIn: <a href="https://www.linkedin.com/in/ghulammahiyudin" target="_blank">linkedin.com/in/ghulammahiyudin</a></p>
                <p>GitHub: <a href="https://github.com/ghulammahiyudin" target="_blank">github.com/ghulammahiyudin</a></p>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")


def show_footer():

    st.write("© 2024 Ghulam Mahiyudin. All rights reserved.")


if __name__ == "__main__":
    main()
