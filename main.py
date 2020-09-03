# Author: Boyuan Lai bjl5716@psu.edu
# Collaborator: Isha Thukral ixt5078@psu.edu
# Collaborator: Jenna Booth jmb8809@psu.edu
# Collaborator: Derek Avery daa5514@psu.edu

grade1 = input("Enter your course 1 letter grade: ")
credit1 = float(input("Enter your course 1 credit: "))
if grade1 == "A":
  point1 = 4.0  
elif grade1 == "A-":
  point1 = 3.67
elif grade1 == "B+":
  point1 = 3.33
elif grade1 == "B":
  point1 = 3.0
elif grade1 == "B-":
  point1 = 2.67
elif grade1 == "C+":
  point1 = 2.33
elif grade1 == "C":
  point1 = 2.0
elif grade1 == "D":
  point1 = 0.0
elif grade1 == "F":
  point1 = 0.0
else:
  point1 = 0.0

print(f"Grade point for course 1 is: {point1}")
  
grade2 = input("Enter your course 2 letter grade: ")
credit2 = float(input("Enter your course 2 credit: "))
if grade2 == "A":
  point2 = 4.0  
elif grade2 == "A-":
  point2 = 3.67
elif grade2 == "B+":
  point2 = 3.33
elif grade2 == "B":
  point2 = 3.0
elif grade2 == "B-":
  point2 = 2.67
elif grade2 == "C+":
  point2 = 2.33
elif grade2 == "C":
  point2 = 2.0
elif grade2 == "D":
  point2 = 0.0
elif grade2 == "F":
  point2 = 0.0
else:
  point2 = 0.0

print(f"Grade point for course 2 is: {point2}")

grade3 = input("Enter your course 3 letter grade: ")
credit3 = float(input("Enter your course 3 credit: "))
if grade3 == "A":
  point3 = 4.0  
elif grade3 == "A-":
  point3 = 3.67
elif grade3 == "B+":
  point3 = 3.33
elif grade3 == "B":
  point3 = 3.0
elif grade3 == "B-":
  point3 = 2.67
elif grade3 == "C+":
  point3 = 2.33
elif grade3 == "C":
  point3 = 2.0
elif grade3 == "D":
  point3 = 0.0
elif grade3 == "F":
  point3 = 0.0
else:
  point3 = 0.0
print(f"Grade point for course 3 is: {point3}")


GPA = ((point1*credit1)+(point2*credit2)+(point3*credit3))/(credit1+credit2+credit3)
print(f"Your GPA is: {GPA}")