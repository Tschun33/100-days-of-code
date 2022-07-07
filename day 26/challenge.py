import pandas as pd

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

data = sentence.split()

output = {text: len(text) for text in data}
print(output)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

weather_f = {day: (temperatur*9/5)+32 for (day, temperatur) in weather_c.items()}

# Write your code 👇 below:

print(weather_f)

# Loop through DataFrame

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

student_frame = pd.DataFrame(student_dict)

print(student_frame)

#for (key,value) in student_frame.items():
#    print(key)

for (index, row) in student_frame.iterrows():
    print(index, row)

