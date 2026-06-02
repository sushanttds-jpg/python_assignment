
students = {
    1: {"name": "susan", "fee": 49500, "marks": [92, 95, 91, 96, 94]},  
    2: {"name": "susant", "fee": 49501, "marks": [90, 88, 92, 95, 91]},  
    3: {"name": "sushant", "fee": 49500, "marks": [95, 98, 96, 97, 94]}  
}

student_list = [] 
total_class_percentage = 0 
for roll_number, details in students.items():
    total_marks = sum(details["marks"])
    percentage = total_marks / 5
    total_class_percentage = total_class_percentage + percentage
    details["percentage"] = percentage
    details["roll_number"] = roll_number
    student_list.append(details)
def get_percentage(student_record):
    return student_record["percentage"]
sorted_students = sorted(student_list, key=get_percentage, reverse=True)
for student in sorted_students:
    print(f"Roll: {student['roll_number']}, Name: {student['name']}, Percentage: {student['percentage']}%")
total_students = len(students)
class_average = total_class_percentage / total_students
print(f"\nAverage Class Percentage: {class_average}%")