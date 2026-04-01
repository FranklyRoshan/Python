
# ===============================================================
# Iterate over Pandas Dataframe
# ===============================================================
import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key,value) in student_dict.items():
    # print(value)
    pass

# Using Pandas to looping through  dictionaries:
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop though a data frame
# for (key,value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame
for(index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        # print(row.score)
        pass

# Angela Notes

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass


# ===============================================================
# Data Frame Comprehension
# ===============================================================
"""
Data Frame comprehension
new_dict = {new_key:new_value for (index, row) in df.iterrows()}

Conditional Data Frame Comprehension
new_dict = {new_key:new_value for (index, row) in df.iterrows() if condition}
"""
