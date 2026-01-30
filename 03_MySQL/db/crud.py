from sqlalchemy import select
from sqlalchemy.orm import Session

from db.connection import Project, Task

def create_project(session: Session, title: str, description: str) -> Project:
    project = Project(title=title, description=description)
    session.add(project)
    return project

def get_projects(session: Session):
    return session.scalars(select(Project)).all()

def create_task(session: Session, project_id: int, description: str | list[str]) -> Task | list[Task]:
    if isinstance(description, list):
        tasks = [Task(project_id=project_id, description=desc) for desc in description]
        session.bulk_save_objects(tasks)
        return tasks
    task = Task(project_id=project_id, description=description)
    session.add(task)
    return task

def get_tasks_by_project(session: Session, project_id: int):
    return session.scalars(select(Task).where(Task.project_id == project_id)).all()

def update_task_status(session: Session, task_id: int, is_completed: bool) -> Task:
    task = session.get(Task, task_id)
    if task:
        task.completed = is_completed
    return task

def delete_task(session: Session, task_id: int) -> None:
    task = session.get(Task, task_id)
    if task:
        session.delete(task)