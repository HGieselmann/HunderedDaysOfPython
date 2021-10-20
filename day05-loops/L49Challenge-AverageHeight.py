students_heights = input("Input a list of student heights: ").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

sum = 0
for height in students_heights:
    sum += height

print(f"The average height is {sum/len(students_heights)}.")