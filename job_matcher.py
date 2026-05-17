def match_job_description(resume_skills, job_description):

    job_description = job_description.lower()

    matched_skills = []

    all_possible_skills = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Communication",
        "Leadership",
        "Customer Service",
        "Teamwork",
        "Problem Solving",
        "Coaching",
        "Sports",
        "Cash Handling"
    ]

    # MATCHING

    for skill in resume_skills:

        if skill.lower() in job_description:

            matched_skills.append(skill)

    # MISSING

    missing_skills = []

    for skill in all_possible_skills:

        if (
            skill.lower() in job_description
            and skill not in matched_skills
        ):

            missing_skills.append(skill)

    # BETTER SCORE

    total_required_skills = len(matched_skills) + len(missing_skills)

    if total_required_skills > 0:

        match_score = (
            len(matched_skills)
            / total_required_skills
        ) * 100

    else:

        match_score = 0

    return (
        round(match_score, 2),
        matched_skills,
        missing_skills
    )