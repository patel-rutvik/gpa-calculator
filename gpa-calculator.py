# Simple GPA Calculator ran through terminal
# Made by: Rutvik Patel

debug = False
scale = {"CR": 0, "A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0}

try:
    # get input
    num_classes = int(input("Number of classes taken: "))
    grades = []
    weight = []
    for i in range(0, num_classes):
        user_in = input("Class grade and credit weight (separated by a space): ").split()
        grades.append(user_in[0])
        weight.append(float(user_in[1]))

    # calculate
    total_credits = 0
    for i in range(0, num_classes):
        total_credits += weight[i]
    if debug:
        print("The total credits taken are: ", total_credits)

    gpa = 0
    weighted_grades = 0
    for i in range(0, num_classes):
        weighted_grades += scale[grades[i]] * weight[i]
    if debug:
        print("Your weighted grades achieved is: ", weighted_grades)
    gpa = weighted_grades / total_credits
    # display answer
    print("Your GPA is: ", gpa)
except ValueError:
    print("Please check your input and try again.")