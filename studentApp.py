# Student App in Python using Dictionaries Method

students = [
{
    "id": 1,
    "email": "asif@gmail.com",
    "name": "Asif",
    "roll_no": 1,
    "marks": 90
},
{
    "id": 2,
    "email": "imran@gmail.com",
    "name": "Imran",
    "roll_no": 2,
    "marks": 80
},
{
    "id": 3,
    "email": "naveed@gmail.com",
    "name": "Naveed",
    "roll_no": 3,
    "marks": 70
},
{
    "id": 4,
    "email": "muhammad@gmail.com",
    "name": "Muhammad",
    "roll_no": 4,
    "marks": 60
},
{
    "id": 5,
    "email": "zeeshan@gmail.com",
    "name": "Zeeshan",
    "roll_no": 5,
    "marks": 50
}
]

# add a new student in  the list of students
newStudent = {
    "id": len(students)+1,
    "email": input("Enter email: "),
    "name": "Shahid",
    "roll_no": 6,
    "marks": 40
}
students.append(newStudent)

# update any student
