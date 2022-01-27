def main():
    student_scores = {
      "Harry": 81,
      "Ron": 78,
      "Hermione": 99, 
      "Draco": 74,
      "Neville": 62,
    }
    # 🚨 Don't change the code above 👆

    #TODO-1: Create an empty dictionary called student_grades.
    student_grades = {}

    #TODO-2: Write your code below to add the grades to student_grades.👇
    scoring_criteria = ["Fail", "Acceptable", "Exceeds Expectations", "Outstanding"]
    for key in student_scores:
        if student_scores[key] <= 70:
            student_grades[key] = scoring_criteria[0]
        elif student_scores[key] <= 80:
            student_grades[key] = scoring_criteria[1]
        elif student_scores[key] <= 90:
            student_grades[key] = scoring_criteria[2]
        else:
            student_grades[key] = scoring_criteria[3]

        

    # 🚨 Don't change the code below 👇
    print(student_grades)

if __name__ == '__main__':
    main()