from sqlalchemy import Engine
from sqlalchemy.orm import Session

from db import crud
from db.connection import engine

def add_new_project_with_task(
    engine: Engine,
    project_title: str,
    project_description: str,
    task_description: str | list[str],
) -> None:
    with Session(engine) as session:
        try:
            new_project = crud.create_project(session, project_title, project_description)
            session.flush()

            new_task = crud.create_task(session, new_project.project_id, task_description)

            session.commit()

            print(f"Project: {new_project}\nTask: {new_task}")
        except Exception as e:
            session.rollback()
            print(f"Error ocurred {e}")

if __name__ == "__main__":
    tasks = [
        "Decide what clothes to donate",
        "Organize summer clothes",
        "Organize winter clothes",
    ]

    add_new_project_with_task(
        engine=engine,
        project_title="Organize closet",
        project_description="Organize closet by color and style",
        task_description=tasks
    )