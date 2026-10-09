# AI-Career-Job-Recommendation-Assistant
AI-powered career and job recommendation assistant based on user skills, interests and profile.

**AICTE–IBM Internship Project | SDG 8: Decent Work and Economic Growth**

## 📌 Project Overview

The AI Career & Job Recommendation Assistant is a career guidance application that helps students, diploma holders, fresh graduates, and early-stage job seekers explore suitable career paths based on their skills and interests.

The application recommends relevant career roles, identifies missing skills, and provides a personalized learning roadmap to help users prepare for their desired careers.

## 🎯 Problem Statement

Many students and freshers struggle to identify career options that align with their skills and interests. They may also find it difficult to understand which skills they need to develop to become job-ready.

This project aims to make career exploration more structured and accessible through a simple, interactive recommendation system.

## 💡 Proposed Solution

The application accepts a user's skills and career interests, analyzes them against a predefined career dataset, and generates career recommendations.

For each recommended career, the application displays:

* Career match score
* Matching skills
* Skill gaps
* Personalized learning roadmap

Users can also enter their education, experience level, and preferred location as part of their profile.

## ✨ Key Features

* **Career Recommendations:** Suggests suitable career roles based on skills and interests.
* **Match Score:** Displays a score calculated by the recommendation algorithm.
* **Skill Gap Analysis:** Identifies skills the user may need to develop for a recommended role.
* **Learning Roadmap:** Provides suggested learning steps for missing skills.
* **Interactive Interface:** Allows users to enter their profile through a Streamlit application.
* **Career Dataset:** Uses a CSV dataset containing career roles, required skills, interests, education, experience level, and location information.

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* CSV dataset
* Rule-based career matching and skill gap analysis

## 📂 Project Structure

```text
IBM_project/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   └── career_data.csv
└── modules/
    ├── career_matcher.py
    ├── recommendation.py
    └── skill_gap.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Preeti-verma10/AI-Career-Job-Recommendation-Assistant.git
```

### 2. Open the project folder

```bash
cd AI-Career-Job-Recommendation-Assistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔄 How It Works

1. The user enters their skills and career interests.
2. The application compares the profile with the career dataset.
3. Career roles are ranked using a matching score.
4. The application identifies matching and missing skills.
5. A learning roadmap is generated for the recommended careers.

## 🌍 Sustainable Development Goal

This project aligns with **UN Sustainable Development Goal 8: Decent Work and Economic Growth** by supporting career awareness, skill development, and employment preparation.

## 🚀 Future Scope

* Integrate a larger and regularly updated job dataset.
* Improve recommendations using more detailed user profiles.
* Add job listings and relevant job links.
* Include curated learning resources and certifications.
* Explore machine learning techniques for more advanced career matching.

## 👩‍💻 Developed By

**Preeti Verma**

AICTE–IBM Internship Project | 2026
