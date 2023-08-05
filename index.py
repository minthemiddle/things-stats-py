import things
all_todos = things.todos()
work_projects = things.projects(area = '3VFHRj4kQW1TL2mrJ1sWYN')

filtered_todos = [todo for todo in all_todos if not (todo['start'] == 'Someday' and todo['start_date'] is None)]
print(f"You have {len(filtered_todos)} incomplete tasks in total")
print(f"{work_projects}")