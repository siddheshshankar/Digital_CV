import streamlit as st
import constants as c

# Config #
st.set_page_config(page_title='Digital CV | Siddhesh Shankar', page_icon=':wave:')

# Header #
st.markdown("<h1 style='text-align: center;'>Siddhesh Shankar</h1>", unsafe_allow_html=True)
st.write(c.DESCRIPTION)

# Skills #
st.markdown("<h2 style='text-align: center;'>Skills 👨‍💻 </h2>", unsafe_allow_html=True)
st.write("""
●	Python Development, Automation and Business Intelligence.\n
●	Familiarity in working with various statistical concepts and data science techniques.\n
●	Skill stack include Python, R, SQL, Power BI, PyCharm, Git, Hive, Azure DevOps.
""")

# Work History #
st.markdown("<h2 style='text-align: center;'>Work History 💼 </h2>", unsafe_allow_html=True)

# Gartner
st.markdown("<h4> ✔️ Senior Data Analyst | Gartner | 10/2022 - Present</h4>", unsafe_allow_html=True)
st.write(c.WORK_GARTNER)

# BlackRock
st.markdown("<h4> ✔️ Analyst | BlackRock | 04/2019 - 09/2022</h4>", unsafe_allow_html=True)
st.write(c.WORK_BLK)

# S&P Global
st.markdown("<h4> ✔️ Data Researcher 1 | S&P Global | 04/2018 - 04/2019</h4>", unsafe_allow_html=True)
st.write(c.WORK_SP)

# NABARD
st.markdown("<h4> ✔️ Intern | NABARD | 05/2017 - 07/2017</h4>", unsafe_allow_html=True)
st.write(c.WORK_NABARD)

# Education #
st.markdown("<h2 style='text-align: center;'>Education 🎓 </h2>", unsafe_allow_html=True)
st.markdown("<h6> ✔ M.Sc. Quantitative Finance | Pondicherry University | 2016 - 2018 | CGPA : 9.5</h6>",
            unsafe_allow_html=True)
st.markdown("<h6> ✔ B.Sc. (H) Statistics | Delhi University | 2013 - 2016 | Percentage : 77.33% </h6>",
            unsafe_allow_html=True)

# Accomplishments #
st.markdown("<h2 style='text-align: center;'>Accomplishments 🏆 </h2>", unsafe_allow_html=True)
st.write(c.ACC)

# Certificates #
st.markdown("<h2 style='text-align: center;'>Certificates ✅ </h2>", unsafe_allow_html=True)
st.write(c.CERT)

# Additional Info #
st.markdown("<h2 style='text-align: center;'>Additional Information ✅ </h2>", unsafe_allow_html=True)
st.write(c.ADD)

