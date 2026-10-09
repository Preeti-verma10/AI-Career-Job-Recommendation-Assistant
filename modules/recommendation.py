from modules.career_matcher import match_careers
from modules.skill_gap import analyze_skill_gap


# Learning roadmap for common skills
LEARNING_ROADMAP = {
    "python": [
        "Python fundamentals",
        "Functions and OOP",
        "File handling and APIs",
        "Python projects"
    ],
    "sql": [
        "SQL basics",
        "Joins and subqueries",
        "Aggregate functions",
        "Advanced SQL practice"
    ],
    "excel": [
        "Excel formulas",
        "IF, SUMIF and COUNTIF",
        "Lookup functions",
        "Pivot tables and charts"
    ],
    "statistics": [
        "Descriptive statistics",
        "Mean, median and mode",
        "Probability basics",
        "Data interpretation"
    ],
    "power bi": [
        "Power BI fundamentals",
        "Data cleaning with Power Query",
        "Data modelling",
        "Dashboard development"
    ],
    "pandas": [
        "Pandas basics",
        "DataFrames and Series",
        "Data cleaning",
        "Data analysis projects"
    ],
    "machine learning": [
        "Machine learning fundamentals",
        "Supervised learning",
        "Regression and classification",
        "ML projects"
    ],
    "communication": [
        "Business communication",
        "Professional email writing",
        "Presentation skills",
        "Interview communication"
    ],
    "business analysis": [
        "Business analysis fundamentals",
        "Requirement gathering",
        "Process analysis",
        "Business case preparation"
    ],
    "networking": [
        "Networking fundamentals",
        "TCP/IP and OSI model",
        "IP addressing",
        "Network troubleshooting"
    ],
    "linux": [
        "Linux fundamentals",
        "Linux commands",
        "File and permission management",
        "Linux troubleshooting"
    ],
    "cybersecurity": [
        "Cybersecurity fundamentals",
        "Common cyber threats",
        "Network security",
        "Security best practices"
    ],
    "security tools": [
        "Security monitoring basics",
        "Vulnerability scanning",
        "Security analysis tools",
        "Hands-on security practice"
    ],
    "git": [
        "Git fundamentals",
        "Repositories and commits",
        "Branches and merging",
        "GitHub workflow"
    ],
    "oop": [
        "Object-oriented programming",
        "Classes and objects",
        "Inheritance and polymorphism",
        "OOP projects"
    ],
    "apis": [
        "API fundamentals",
        "HTTP and REST APIs",
        "API requests",
        "API integration projects"
    ]
}


def generate_learning_roadmap(missing_skills):
    """
    Generate a personalized learning roadmap
    based on missing skills.
    """

    roadmap = []

    for skill in missing_skills:

        skill_lower = skill.lower().strip()

        if skill_lower in LEARNING_ROADMAP:

            roadmap.append({
                "skill": skill,
                "steps": LEARNING_ROADMAP[skill_lower]
            })

        else:

            roadmap.append({
                "skill": skill,
                "steps": [
                    f"Learn {skill} fundamentals",
                    f"Practice {skill}",
                    f"Build a small {skill} project"
                ]
            })

    return roadmap


def generate_recommendation(
    user_skills,
    user_interests,
    top_n=3
):
    """
    Generate career recommendations,
    skill gaps and personalized learning roadmaps.
    """

    career_matches = match_careers(
        user_skills,
        user_interests
    )

    recommendations = []

    for career in career_matches[:top_n]:

        career_role = career["career_role"]

        skill_gap = analyze_skill_gap(
            user_skills,
            career_role
        )

        roadmap = generate_learning_roadmap(
            skill_gap["missing_skills"]
        )

        recommendations.append({
            "career_role": career_role,
            "score": career["score"],
            "matching_skills": skill_gap["matching_skills"],
            "missing_skills": skill_gap["missing_skills"],
            "learning_roadmap": roadmap
        })

    return recommendations