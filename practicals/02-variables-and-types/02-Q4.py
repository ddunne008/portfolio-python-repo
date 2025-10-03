# Question 4 calculates how many students can equally receive a sweet
amount_of_sweets = input("Enter the amount of sweets: ")
amount_of_students = input("Enter the amount of students: ")

amount_of_sweets = int(amount_of_sweets)
amount_of_students = int(amount_of_students)


amount_of_students // amount_of_sweets

A = (amount_of_students % amount_of_sweets)

print(A, "students")
