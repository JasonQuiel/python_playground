


def grade_calc(ass_1, ass_2, test):

    total_points = ass_1 + ass_2 + test
    percentage = (total_points / 300) * 100

    if percentage >= 90:
        print(percentage)
        print("Your Grade is a A")
    elif percentage >= 80:
        print(percentage)
        print("Your Grade is a B")
    elif percentage >= 70:
        print(percentage)
        print("Your Grade is a C")
    elif percentage >= 60:
        print(percentage)
        print("Your Grade is a D")
    else:
        print("You need to retake the class")
    

print("Each Assessment and Test is worth 100 points!")
assessment_one = input("Enter your FIRST score: ")
assessment_two = input("Enter your SECOND score: ")
assessment_test = input("Enter your TEST score: ")

ass_1 = float(assessment_one)
ass_2 = float(assessment_two)
test = float(assessment_test)


grade_calc(ass_1, ass_2, test)
