from db.connection import mysql_connect

def add_project(cursor, project_title, project_description, tasks):
    project_data = (project_title, project_description)
    cursor.execute("INSERT INTO projects(title, description) VALUES (%s, %s)", project_data)
    
    tasks_data = []
    for task in tasks:
        task_data = (cursor.lastrowid, task)
        tasks_data.append(task_data)

    cursor.executemany("INSERT INTO tasks(project_id, description) VALUES (%s, %s)", tasks_data)

def main():
    db = mysql_connect('projects')
    if db is not None:
        cursor = db.cursor()
    else:
        print("Could not connect to db.")
        return
    
    tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"]
    add_project(cursor, "Clean house", "Clean house by room", tasks)
    db.commit()

    cursor.execute("SELECT * FROM projects")
    project_records = cursor.fetchall()
    cursor.execute("SELECT * FROM tasks")
    tasks_records = cursor.fetchall()
    print(f"Projects: {project_records}\nTasks: {tasks_records}")

if __name__ == "__main__":
    main()