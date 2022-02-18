import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Looping through a data frame like before
# for (key, value) in student_data_frame.items():
#     print(value)

# Looping through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)