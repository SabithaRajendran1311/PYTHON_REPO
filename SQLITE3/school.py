import sqlite3
conn=sqlite3.connect("school.db")
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
class TEXT NOT NULL
)''')
def add_student(name, student_class):
    c.execute("INSERT INTO student (name, class) VALUES (?, ?)", (name, student_class))
    conn.commit()
    print("student added sucessfuly.")
def get_students_by_class(student_class):
    c.execute("SELECT * FROM student WHERE class=?", (student_class,))
    students= c.fetchall()
    if students:
        for student in students:
            print(f" ID: {student[0]}, Name: {student[1]}, Class: {student[2]}")
    else:
        print("no student found for the given class.")
def delete_student(student_id):
    c.execute("DELETE FROM student WHERE id=?", (student_id,))
    conn.commit()
    print("student deleted sucessfully")
def update_student_class(student_id, new_class):
    c.execute("UPDATE student SET class=? WHERE id=?", (new_class, student_id))
    conn.commit()
    print("student's class updated sucessfully.")
while True:
    print("1. Add student")
    print("2. Get student by class")
    print("3. Delete student")
    print("4. Update student's class")
    print("5. exit")
    choice =input("enter your choice (1-5):")
    if choice == "1":
        name=input("enter student name:")
        student_class=input("enter student class:")
        add_student(name, student_class)
    elif choice == "2":
        student_class = input("enter class to retrieve student:")
        get_students_by_class(student_class)
    elif choice == "3":
        student_id = input("enter student ID to delete:")
        delete_student(student_id)
    elif choice == "4":
        student_id = input("enter student ID to update class:")
        new_class=input("enter new class:")
        update_student_class(student_id, new_class)
    elif choice == "5":
        break
conn.close()
    
