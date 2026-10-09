import pandas as pd


def load_career_data():
    """Load career data from CSV file."""
    return pd.read_csv("data/career_data.csv")


def analyze_skill_gap(user_skills, career_role):
    """
    Compare user's skills with the required skills
    for a selected career role.
    """

    df = load_career_data()

    user_skills = {
        skill.strip().lower()
        for skill in user_skills
    }

    career = df[
        df["career_role"].str.lower() == career_role.lower()
    ]

    if career.empty:
        return {
            "career_role": career_role,
            "matching_skills": [],
            "missing_skills": []
        }

    required_skills = {
        skill.strip().lower()
        for skill in career.iloc[0]["skills"].split("|")
    }

    matching_skills = user_skills.intersection(required_skills)
    missing_skills = required_skills - user_skills

    return {
        "career_role": career_role,
        "matching_skills": sorted(matching_skills),
        "missing_skills": sorted(missing_skills)
    }