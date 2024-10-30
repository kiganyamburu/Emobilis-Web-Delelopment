subjects = {}
total = 0


try:
    nuOfSubjects = int(input("Enter number of subjects: "))
except ValueError:
    print("The number of subjects must be an integer")
    exit()



for i in range(1, nuOfSubjects + 1):
    name = input(f"Enter the subject name {i}:  ")
    marks = int(input(f"Enter marks for subject {i}:  "))
    subjects[name] = marks
    total = total + marks


    average = total / len(subjects)
    subjects["Total"] = total
    subjects["Average"] = int(average)


print(subjects)