#Author: Yan Lu yfl5541@psu.edu
grade1 = input("Enter your course 1 letter grade: ")
credit1 = input("Enter your course 1 credit: ")

if grade1 == "A":
  gp1 = 4.0
  print(f"Grade point for course 1 is: " + str(gp1))
elif grade1 == "A-":
  gp1 = 3.67
  print(f"Grade point for course 1 is: " + str(gp1)) 
elif grade1 == "B+":
  gp1 = 3.33
  print(f"Grade point for course 1 is: " + str(gp1))
elif grade1 == "B":
  gp1 = 3.0
  print(f"Grade point for course 1 is: " + str(gp1))
elif grade1 == "B-":
  gp1 = 2.67
  print(f"Grade point for course 1 is: " + str(gp1))
elif grade1 == "C+":
  gp1 = 2.33
  print(f"Grade point for course 1 is: " + str(gp1))
elif grade1 == "C":
  gp1 = 2.0
  print(f"Grade point for course 1 is: " + str(gp1))
elif grade1 == "D":
  gp1 = 1.0
  print(f"Grade point for course 1 is: " + str(gp1))
else:
  gp1 = 0.0
  print(f"Grade point for course 1 is: " + str(gp1))

grade2 = input("Enter your course 2 letter grade: ")
credit2 = input("Enter your course 2 credit: ")

if grade2 == "A":
  gp2 = 4.0
  print(f"Grade point for course 2 is: " + str(gp2))
elif grade2 == "A-":
  gp2 = 3.67
  print(f"Grade point for course 2 is: " + str(gp2)) 
elif grade2 == "B+":
  gp2 = 3.33
  print(f"Grade point for course 2 is: " + str(gp2))
elif grade2 == "B":
  gp2 = 3.0
  print(f"Grade point for course 2 is: " + str(gp2))
elif grade2 == "B-":
  gp2 = 2.67
  print(f"Grade point for course 2 is: " + str(gp2))
elif grade2 == "C+":
  gp2 = 2.33
  print(f"Grade point for course 2 is: " + str(gp2))
elif grade2 == "C":
  gp2 = 2.0
  print(f"Grade point for course 2 is: " + str(gp2))
elif grade1 == "D":
  gp2 = 1.0
  print(f"Grade point for course 2 is: " + str(gp2))
else:
  gp2 = 0.0
  print(f"Grade point for course 2 is: " + str(gp2))

grade3 = input("Enter your course 3 letter grade: ")
credit3 = input("Enter your course 3 credit: ")

if grade3 == "A":
  gp3 = 4.0
  print(f"Grade point for course 3 is: " + str(gp3))
elif grade3 == "A-":
  gp3 = 3.67
  print(f"Grade point for course 3 is: " + str(gp3)) 
elif grade3 == "B+":
  gp3 = 3.33
  print(f"Grade point for course 3 is: " + str(gp3))
elif grade3 == "B":
  gp3 = 3.0
  print(f"Grade point for course 3 is: " + str(gp3))
elif grade3 == "B-":
  gp3 = 2.67
  print(f"Grade point for course 3 is: " + str(gp3))
elif grade3 == "C+":
  gp3 = 2.33
  print(f"Grade point for course 3 is: " + str(gp3))
elif grade3 == "C":
  gp3 = 2.0
  print(f"Grade point for course 3 is: " + str(gp3))
elif grade3 == "D":
  gp3 = 1.0
  print(f"Grade point for course 3 is: " + str(gp3))
else:
  gp3 = 0.0
  print(f"Grade point for course 3 is: " + str(gp3))  
gpa = float((int(credit1) * gp1 + int(credit2) * gp2 + int(credit3) * gp3)/(int(credit1) + int(credit2) + int(credit3)))
print(f"Your GPA is: {gpa}")