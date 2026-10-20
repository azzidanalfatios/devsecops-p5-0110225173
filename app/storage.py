import json
from dataclasses import asdict
from pathlib import Path

from app.models import Task


DEFAULT_FILE = Path("tasks.json")


def save_tasks(tasks, path=DEFAULT_FILE):
    data = [asdict(task) for task in tasks]
    Path(path).write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )


def load_tasks(path=DEFAULT_FILE):
    file_path = Path(path)

    if not file_path.exists():
        return []

    data = json.loads(file_path.read_text(encoding="utf-8"))
    return [Task(**item) for item in data]