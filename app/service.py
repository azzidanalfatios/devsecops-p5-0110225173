from app.models import Task
from app.validator import validate_task_title


def add_task(tasks, title):
    title = validate_task_title(title)
    task = Task(title=title)
    tasks.append(task)
    return task


def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        raise IndexError("Nomor tugas tidak ditemukan")

    tasks[index].mark_completed()
    return tasks[index]


def list_tasks(tasks):
    return [
        f"[{'x' if task.completed else ' '}] {task.title}"
        for task in tasks
    ]