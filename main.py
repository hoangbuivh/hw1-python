grades = [["A", 4.0], ["A-", 3.67], ["B+", 3.33], ["B", 3.0], ["B-", 2.67], ["C+", 2.33], ["C", 2], ["D", 1.0], ["F", 0.0], ["F", 0.0], ["G", 0.0], ["H", 0.0], ["I", 0.0], ["J", 0.0],["K", 0.0], ["L", 0.0], ["M", 0.0], ["N", 0.0], ["O", 0.0], ["P", 0.0], ["Q", 0.0], ["R", 0.0],["S", 0.0], ["T", 0.0], ["U", 0.0], ["V", 0.0], ["W", 0.0], ["X", 0.0], ["Y", 0.0], ["Z", 0.0]]
gradepointList = []
creditpointList = []
for i in range(1,4):
  lettergrade = input(f"Enter your course {i} letter grade: ")
  credit = float(input(f"Enter your course {i} credit: "))
  creditpointList.append(credit)
  for grade in grades:
    if grade[0] == lettergrade: 
      gradepoint = grade[1]
      gradepointList.append(gradepoint)

  print(f"Grade point for course {i} is: {gradepoint}")

gpa  = (gradepointList[0]*creditpointList[0] + gradepointList[1]*creditpointList[1] + gradepointList[2]*creditpointList[2]) / (creditpointList[0] + creditpointList[1]+ creditpointList[2])
print("Your GPA is:", gpa)