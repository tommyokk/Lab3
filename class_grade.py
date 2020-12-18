



"""
start
create a list to store 5 numbers (float)
capture user's input 5 times for their grades
each time we capture the user's input, we append the number to the list
sort the list ascending, then splice the items starting at index 2
once we have 3 highest numbers in the list, sum them up and divide by 3
output a messge to the user
end

"""

"""
create list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

"""

grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]

grades = sum(grades)

result = grades / 3

print("average grade {0:.2f}%".format(result))
print(grades, 'results', result)





