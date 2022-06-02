import sqlite3 as sq

def connect():
    conn = sq.connect("C:/Users/samet.colak/PycharmProjects/Samet Çolak_bloopark(WORKING STUDENT TEST CASE)/Python and SQLite/test.db")
    curr = conn.cursor()
    return conn, curr

def cleandb(curr, tables):
    cmd = "DROP TABLE IF EXISTS {}"
    for table in tables:
        drop = cmd.format(table)
        curr.execute(drop)

"""1. Create Python classes that represent these data definitions"""

def create_tables(curr):
    cmd = """
       CREATE TABLE students(
        id INTEGER PRIMARY KEY,
        firstName VARCHAR(30) NOT NULL,
        lastName VARCHAR(30) NOT NULL
       );
       CREATE TABLE enrollments(
        id INTEGER NOT NULL PRIMARY KEY,
        year INTEGER NOT NULL,
        studentId INTEGER NOT NULL
       );
       """
    print("CREATING TABLES")
    curr.executescript(cmd)

def display_tables(curr):
    print("\nTABLE 'Students'")
    curr.execute("SELECT * FROM students")
    rows = curr.fetchall()
    for row in rows:
        print(row)
    print("\nTABLE 'Enrollments'")
    curr.execute("SELECT * FROM enrollments")
    rows = curr.fetchall()
    for row in rows:
        print(row)

def insert_data(conn, curr):
    cmd = """
        INSERT INTO students(id, firstName, lastName) VALUES
        ('1', 'Samet', 'Çolak'),
        ('2', 'Anakin', 'Skywalker'),
        ('3', 'John', 'Travolta'),
        ('4', 'John', 'Wick'),
        ('5', 'Harry', 'Potter');
        INSERT INTO enrollments(id, year, studentId) VALUES
        ('42', '2022', '1234'),
        ('55', '2021', '6678'),
        ('61', '2021', '0909'),
        ('110', '2020', '9678'),
        ('210', '2020', '6456');
        """
    curr.executescript(cmd)
    conn.commit()

"""2. Write a method that returns the number of students whose first name is John."""

def find_byname(curr):
    john_named = """SELECT * FROM students WHERE firstName = "John";"""
    curr.execute(john_named)
    john_named_list = curr.fetchall()
    print("\nThe number of students whose first name is 'John':", len(john_named_list))

"""3. Assuming that the table containing the students enrolled in a yearly course has
incorrect data in records with ids between 20 and 100. Write method that updates the
field 'year' of every faulty record to 2015."""

def find_bycourseid_and_change(curr):
    incorrect_data = """SELECT * FROM enrollments WHERE id > 20 AND id < 100;"""
    curr.execute(incorrect_data)
    data = curr.fetchall()
    print("\nTABLE 'incorrect data'\n", data)
    change_query = """UPDATE enrollments SET year = '2015' WHERE id > 20 AND id < 100;"""
    curr.execute(change_query)
    curr.execute("SELECT * FROM enrollments")
    rows = curr.fetchall()
    print("\nTABLE 'Enrollments' after changings\n", rows)

def main():
    tables = ["students", "enrollments"]
    conn, curr = connect()
    cleandb(curr, tables)
    create_tables(curr)
    insert_data(conn, curr)
    display_tables(curr)
    find_byname(curr)
    find_bycourseid_and_change(curr)

if __name__ == "__main__":
    main()