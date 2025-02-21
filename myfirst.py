"""def reverse_dict(d1):
    return {v:k for k,v in d1.items()}



dict1={
    1:234,
    3:77,
    6:9787
}
print(reverse_dict(dict1))

dict2={
    4:7758,
    3:74743,
    1:5747,
    9:65747
}

def common_keys(d1,d2):
    return list(set(d1.keys()) & set(d2.keys()))

print(common_keys(dict2,dict1))

nest={
    1:{
    6446:74747,
    454646:456437,
    646:64848

},
    2:{
        3536:6474,
        4636:464646
    }
}
def nested_dict_value(nest, obj, y):
    if obj in nest and y in nest[obj]:
        return nest[obj][y]
    return None

print(nested_dict_value(nest,2,3536))

list=[1,3,5,4,3,1,1,8,9]

def count_elements(l):
    sum = 0
    a=0
    for x in l:
        erg=l.count(x)
    print(erg)

print(count_elements(list))

"""
data = [
    {"name": "Alice", "subject": "Math", "grade": 79},
    {"name": "Alice", "subject": "Science", "grade": 88},
    {"name": "Alice", "subject": "Arts", "grade": 50},
    {"name": "Bob", "subject": "Math", "grade": 78},
    {"name": "Bob", "subject": "Science", "grade": 84},
    {"name": "Bob", "subject": "Arts", "grade": 75},
    {"name": "Charlie", "subject": "Math", "grade": 88},
    {"name": "Charlie", "subject": "Science", "grade": 64},
    {"name": "Charlie", "subject": "Arts", "grade": 61},
    {"name": "Linda", "subject": "Math", "grade": 58},
    {"name": "Linda", "subject": "Science", "grade": 87},
    {"name": "Linda", "subject": "Arts", "grade": 80},
    {"name": "Maria", "subject": "Math", "grade": 64},
    {"name": "Maria", "subject": "Science", "grade": 75},
    {"name": "Maria", "subject": "Arts", "grade": 73}
]

# Initialize dictionaries
student_grades = {}
subject_grades = {}

# Populate the dictionaries
for entry in data:
    name, subject, grade = entry["name"], entry["subject"], entry["grade"]

    # Process student grades
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

    # Process subject grades
    if subject not in subject_grades:
        subject_grades[subject] = []
    subject_grades[subject].append(grade)

# Calculate averages
average_per_student = {name: sum(grades) / len(grades) for name, grades in student_grades.items()}
average_per_subject = {subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()}

# Print results
print("Average grade per student:")
for student, avg in average_per_student.items():
    print(f"{student}: {avg:.2f}")

print("\nAverage grade per subject:")
for subject, avg in average_per_subject.items():
    print(f"{subject}: {avg:.2f}")

