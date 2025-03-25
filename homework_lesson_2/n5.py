from collections import namedtuple

Employee = namedtuple("Employee",["emp_id", "name", "position", "salary"])

employees = (
    Employee(101, "Tom", "Software Engineer", 5000),
    Employee(102, "Tom1", "Data Analyst", 4500),
    Employee(103, "Tom2", "Project Manager", 6000)
)

e2 = employees[0]._replace(salary = employees[0].salary * 1.1)
print(e2._asdict())