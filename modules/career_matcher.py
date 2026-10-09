import pandas as pd


def load_career_data():
    """Load career data from CSV file."""
    return pd.read_csv("data/career_data.csv")


def normalize_text(text):
    """Normalize text for better matching."""
    text = text.lower().strip()

    replacements = {
        "cyber security": "cybersecurity",
        "cyber security analyst": "cybersecurity",
        "data analytics": "data",
        "data analyst": "data",
        "business analyst": "business",
        "machine learning": "machine learning",
        "web development": "web development",
        "software development": "software",
        "programming": "programming"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def match_careers(user_skills, user_interests):
    """
    Match user's skills and interests with career roles.
    Returns careers ranked by matching score.
    """

    df = load_career_data()

    user_skills = {
        normalize_text(skill)
        for skill in user_skills
    }

    user_interests = {
        normalize_text(interest)
        for interest in user_interests
    }

    results = []

    for _, row in df.iterrows():

        career_skills = {
            normalize_text(skill)
            for skill in row["skills"].split("|")
        }

        career_interests = {
            normalize_text(interest)
            for interest in row["interests"].split("|")
        }

        career_role = normalize_text(row["career_role"])

        matching_skills = user_skills.intersection(career_skills)
        matching_interests = user_interests.intersection(
            career_interests
        )

        # Extra match when user's interest relates directly
        # to the career role.
        role_match = any(
            interest in career_role
            or career_role in interest
            for interest in user_interests
        )

        score = (
            len(matching_skills) * 2
            + len(matching_interests) * 3
            + (3 if role_match else 0)
        )

        results.append({
            "career_role": row["career_role"],
            "score": score,
            "matching_skills": ", ".join(matching_skills),
            "matching_interests": ", ".join(matching_interests)
        })

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return results