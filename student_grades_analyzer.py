grades = [88, 76, 93, 65, 81]
def print_grades():
    for grade in grades:
        print(grade)
def average_grade():
    total = sum(grades)
    count = len(grades)
    return total / count
def highest_grade():
    return max(grades)
def grade_feedback():
    if grades >= 90:
        return "Excellent"
    elif grades >= 70 and grades < 90:
        return "Good"
    else:
        return "Needs Improvement"
