student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
for keys,value in student_scores.items():
  if value  in range(91,100):
    student_scores[keys] = "Outstanding"
  elif value in range(81,90):
    student_scores[keys] = "Exceeds Expectations"
  elif value in range(71,80):
    student_scores[keys] = "Acceptable"
  elif value <=70:
    student_scores[keys] = "Fail"

student_grades = student_scores
    
  

# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)
