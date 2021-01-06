# 5.1 - average heights
# --------------------------------------
def one():
  # 🚨 Don't change the code below 👇
  student_heights = input("Input a list of student heights ").split()
  for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
  # 🚨 Don't change the code above 👆


  #Write your code below this row 👇

  i = total_height = 0
  for student_height in student_heights:
    i += 1
    total_height += student_height
  average_height = round(total_height / i)

  print(f"Average student height is {average_height}")

# 5.2 - highest score
# --------------------------------------
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

high_score = 0
for score in student_scores:
  if score > high_score:
    high_score = score
print(f"The highest score in the class is: {high_score}")