print("------------------------------------")
employee_details = {23: {'name': 'John','department': 'HR','salary': 70000}
, 45: {'name': 'Alice','department': 'Finance','salary': 23000}, 67: {'name': 'Bob','department': 'IT','salary': 75000}
, 89: {'name': 'Charlie','department': 'Marketing','salary': 40000}}

l = [i['name'] for i in employee_details.values() if i['salary'] < 50000]
print(l)