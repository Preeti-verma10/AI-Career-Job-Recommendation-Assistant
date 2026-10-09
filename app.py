import streamlit as st

from modules.recommendation import generate_recommendation


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Career & Job Recommendation Assistant",
    page_icon="🎯",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎯 AI Career & Job Recommendation Assistant")

st.write(
    "Get personalized career recommendations based on your "
    "education, skills, interests, experience, and preferred location."
)

st.divider()


# --------------------------------------------------
# USER PROFILE
# --------------------------------------------------

st.header("👤 Enter Your Profile")


education = st.selectbox(
    "Education",
    [
        "Diploma in IT",
        "Degree in IT",
        "Degree in Computer Science",
        "Degree in Business",
        "Other"
    ]
)


skills_input = st.text_input(
    "Skills",
    placeholder="Example: Python, SQL, Power BI"
)


interests_input = st.text_input(
    "Career Interests",
    placeholder="Example: Data, Business, Technology"
)


experience = st.selectbox(
    "Experience Level",
    [
        "Fresher",
        "Entry Level",
        "1-2 Years",
        "3+ Years"
    ]
)


location = st.text_input(
    "Preferred Location",
    placeholder="Example: Ahmedabad"
)


st.divider()


# --------------------------------------------------
# RECOMMENDATION BUTTON
# --------------------------------------------------

if st.button("🚀 Get Career Recommendations"):

    if not skills_input or not interests_input:

        st.warning(
            "Please enter your skills and career interests."
        )

    else:

        # Convert skills entered by user into a list
        user_skills = [
            skill.strip()
            for skill in skills_input.split(",")
            if skill.strip()
        ]

        # Convert interests entered by user into a list
        user_interests = [
            interest.strip()
            for interest in interests_input.split(",")
            if interest.strip()
        ]


        # Generate recommendations
        recommendations = generate_recommendation(
            user_skills,
            user_interests,
            top_n=3
        )


        # --------------------------------------------------
        # RESULTS
        # --------------------------------------------------

        st.success(
            "Career recommendations generated successfully!"
        )

        st.header("🎯 Recommended Career Paths")


        for index, recommendation in enumerate(
            recommendations,
            start=1
        ):

            st.subheader(
                f"{index}. {recommendation['career_role']}"
            )


            # Match Score
            st.write(
                f"**Match Score:** "
                f"{recommendation['score']}"
            )


            # Matching Skills
            matching_skills = recommendation[
                "matching_skills"
            ]

            if matching_skills:

                st.write(
                    "**Matching Skills:** "
                    + ", ".join(matching_skills)
                )

            else:

                st.write(
                    "**Matching Skills:** None"
                )


            # Skill Gaps
            missing_skills = recommendation[
                "missing_skills"
            ]

            if missing_skills:

                st.write(
                    "**Skill Gaps:** "
                    + ", ".join(missing_skills)
                )

            else:

                st.write(
                    "**Skill Gaps:** "
                    "No major skill gaps found"
                )


            # --------------------------------------------------
            # PERSONALIZED LEARNING ROADMAP
            # --------------------------------------------------

            st.write(
                "### 📚 Personalized Learning Roadmap"
            )


            roadmap = recommendation[
                "learning_roadmap"
            ]


            if roadmap:

                for item in roadmap:

                    st.write(
                        f"**🎯 {item['skill'].title()}**"
                    )


                    for step_number, step in enumerate(
                        item["steps"],
                        start=1
                    ):

                        st.write(
                            f"{step_number}. {step}"
                        )

            else:

                st.write(
                    "No additional learning roadmap is required."
                )


            st.divider()