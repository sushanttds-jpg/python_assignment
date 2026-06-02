employees = {
    120: {"name": "Sushant", "salary": 1450000},
    121: {"name": "hari", "salary": 125040}
}
total_salary = sum(emp["salary"] for emp in employees.values())
avg_salary = total_salary / len(employees)
for emp_id, info in employees.items():
    print(f"ID: {emp_id}, Name: {info['name']}, Salary: {info['salary']}")
print(f"Average Salary: {avg_salary}")