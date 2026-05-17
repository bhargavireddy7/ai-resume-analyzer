def generate_resume_suggestions(skills, score):

    suggestions = []

    if score < 70:
        suggestions.append(
            "Add more relevant skills to improve ATS score."
        )

    if "Python" not in skills:
        suggestions.append(
            "Include technical skills like Python or SQL."
        )

    if "Leadership" not in skills:
        suggestions.append(
            "Add leadership experiences or team activities."
        )

    if "Communication" not in skills:
        suggestions.append(
            "Highlight communication skills in your resume."
        )

    if "Project Management" not in skills:
        suggestions.append(
            "Mention projects or project management experience."
        )

    if len(skills) < 5:
        suggestions.append(
            "Try adding certifications and internships."
        )

    if not suggestions:
        suggestions.append(
            "Excellent resume! Your profile looks strong."
        )

    return suggestions