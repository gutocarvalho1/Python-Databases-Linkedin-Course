from sqlalchemy import select
from sqlalchemy.orm import Session

from db.connection import engine, Project, Task


def get_project_by_title(session: Session, project_title: str) -> Project:
    smt = select(Project).where(Project.title == project_title)
    # result = session.execute(smt)
    # return result.scalar()
    return session.scalar(smt)

def get_tasks_by_project_id(session: Session, project_id: int):
    smt = select(Task).where(Task.project_id == project_id)
    # result = session.execute(smt)
    # return result.scalars().all()
    return session.scalars(smt).all()

def main():
    with Session(engine) as session:
        project = get_project_by_title(session, "Organize closet")
        tasks = get_tasks_by_project_id(session, project.project_id)

        for task in tasks:
            print(task)

if __name__ == "__main__":
    main()