from models import Task, Base, engine, SessionLocal

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

class TaskRepository:
    def __init__(self):
        self.session = SessionLocal()

    def add_task(self, title: str):
        new_task = Task(title=title)
        self.session.add(new_task)
        self.session.commit()
        return new_task

    def list_tasks(self):
        return self.session.query(Task).all()

    def complete_task(self, task_id: int):
        task = self.session.query(Task).filter(Task.id == task_id).first()
        if task:
            task.completed = True
            self.session.commit()
            return task
        return None

    def delete_task(self, task_id: int):
        task = self.session.query(Task).filter(Task.id == task_id).first()
        if task:
            self.session.delete(task)
            self.session.commit()
            return True
        return False
