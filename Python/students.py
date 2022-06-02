students = [("Allen Anderson", "Computer Science"),
("Edgar Einstein", "Engineering"),
("Farrah Finn", "Fine Arts")]

"""3. The add_new_student function can be rewritten as seen below and still maintain
identical functionality: students[len(students)] = (name, major)"""
"""THE REWRITTEN VERSION BELOW IS FALSE"""
"""def add_new_student(students, name, major):
    students[len(students)] = (name, major)"""
"""5. The add_new_student function adds a new student in the last place in the list."""
def add_new_student(students, name, major):
    students.append((name, major))
    return students
"in order to print the returned"

"""def update_student(students, index, name, major):
    students[index] = (name, major)"""
"""1. In the update_student function, the '(' and ')' parentheses can be removed without
causing any errors."""
"""TRUE AS BELOW"""
def update_student(students, index, name, major):
    students[index] = name, major

def find_students_by_name(students, name):
    return [student for student in students if name in student[0]]

"""4. Calling get_all_majors(students) returns a list of 3 tuples."""
def get_all_majors(students):
    return [student[1] for student in students]


print("MAIN")
print(students)
print("------------------------------------------------------")

"""1. In the update_student function, the '(' and ')' parentheses can be removed without
causing any errors. - TRUE"""
update_student(students, 0, "Amir Tocha", "Tourism and Hospitality")
print(students)
if "Allen Anderson" not in students:
    print("""1. In the update_student function, the '(' and ')' parentheses can be removed without causing any errors. - TRUE""")
    print("------------------------------------------------------")

"""2. Calling find_students_by_name(students, 'in') returns a list of 2 tuples."""
vol1 = find_students_by_name(students, 'in')
if len(vol1) == 2:
    print("The data amount =", len(vol1))
    print("""2. Calling find_students_by_name(students, 'in') returns a list of 2 tuples. - TRUE""")
    print("------------------------------------------------------")
else: print("FALSE")

"""3. The add_new_student function can be rewritten as seen below and still maintain
identical functionality: students[len(students)] = (name, major)"""
add_new_student(students, "Samet Çolak", "Industrial Engineering")
if "Samet Çolak" not in students:
    print("""3. The add_new_student function can be rewritten as seen below and still maintain identical functionality: students[len(students)] = (name, major) - FALSE""")
    print(students)
    print("------------------------------------------------------")

"""4. Calling get_all_majors(students) returns a list of 3 tuples."""
print(get_all_majors(students))
if len(get_all_majors(students)) > 3:
    print("""4. Calling get_all_majors(students) returns a list of 3 tuples. - TRUE""")
    print(students)
    print("------------------------------------------------------")

"""5. The add_new_student function adds a new student in the last place in the list."""
add_new_student(students, "Özge Çolak", "GENIUS")
print(students)
print("""5. The add_new_student function adds a new student in the last place in the list. - TRUE """)
print("------------------------------------------------------")

""""6. The name of the first student in the array can be set to the new_name variable, like
students[0][0] = new_name"""
"""FALSE"""
"""new_name = "TEST TEST"
students[0][0] = new_name
print(students)"""
