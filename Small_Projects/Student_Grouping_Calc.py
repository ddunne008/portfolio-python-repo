# Question 3 is a program which caluclates the amount of groups that is needed and how many students are leftover
students = input("Enter amount of students: ")
group_size = input("Enter the required group size: ")

students = float(students)
group_size = float(group_size)

amount_of_groups = (students // group_size)
left_over_students = students % group_size

if left_over_students ==0:
    print(f"there are {amount_of_groups} groups of students")
    print(f"there are {left_over_students} remaining students who are not in a group")
