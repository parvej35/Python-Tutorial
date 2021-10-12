# Playing with List

courses = ['History', 'Math', 'Physics', 'Chemistry']
print("1) Printing all value in list:")
print(courses, end='\n\n')

print("2) Positional[2] value in list: " + str(courses[2]), end='\n\n')

courses_in_range = courses[0:2]
print("3) List value in certain range (0~2): " + str(courses_in_range))

courses_in_range = courses[:3]
print("4) Another way to show list value in certain range (0~3): " + str(courses_in_range))

courses_in_range = courses[1:]
print("5) Another way to show list value in certain range (1~...): " + str(courses_in_range), end='\n\n')

courses.append('Biology')  # Adding new value into list at last position
print("6) Add new value in list: " + str(courses), end='\n\n')

courses.insert(0, 'English')  # Adding new value into list at certain position
print("7) Add new value at a certain position in the list: " + str(courses), end='\n\n')

courses_2 = ['Data Science', 'Geography']
courses.append(courses_2)
print("8) Add a list into another list: \n" + str(courses), end='\n\n')

courses.extend(courses_2)
print("9) Add a list into another list using 'EXTEND': \n" + str(courses), end='\n\n')

# ---------------------------------------------------------
courses.remove('Physics')  # remove a certain value in the list
print("10)Remove a value 'Physics' from the list: \n" + str(courses), end='\n\n')

courses.pop()  # remove last value of the list
print("10)Remove the last value in the list: \n" + str(courses), end='\n\n')

courses.reverse()  # Reverse the list
print("11)Reverse the list: \n" + str(courses), end='\n\n')

courses = ['History', 'Math', 'Physics', 'Chemistry']
numbers = [1, 3, 5, 2, 7, 4]

courses.sort()  # Sort list in the ascending order
numbers.sort()  # Sort list in the ascending order
print("12)Sort list in the ascending order: " + str(courses))
print("13)Sort list in the ascending order: " + str(numbers), end='\n\n')

courses.sort(reverse=True)  # Sort list in the descending order
numbers.sort(reverse=True)  # Sort list in the descending order
print("14)Sort list in the descending order: " + str(courses))
print("15)Sort list in the descending order: " + str(numbers), end='\n\n')

sorted_courses = sorted(courses)  # Sort list without impacting the original list
print("16)Sort list without impacting the original list: " + str(sorted_courses))

print("===========================================================================", end='\n\n')

numbers = [1, 4, 6, 2, 9, 15, 25, 20]
total = sum(numbers)
print("17)Total sum of the value in the list: " + str(total), end='\n\n')
