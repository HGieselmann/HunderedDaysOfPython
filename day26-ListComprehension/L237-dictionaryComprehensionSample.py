# base code:
# new_dict = {new_key:new_value for item in list}

import random
students = ['Alex', 'Paul', 'Frank']

student_grades = {student:random.randint(0, 100) for student in students}

passed_students ={student:value for (student, value) in student_grades.items() if value > 50}
print(passed_students)


sentence = "What is the Airspeed Velocity of an unladen Swallow?"
word_length = {word:len(word) for word in sentence.split(' ')}
print(word_length)



weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:((value *9/5)+32) for (day, value) in weather_c.items()}
print(weather_f)