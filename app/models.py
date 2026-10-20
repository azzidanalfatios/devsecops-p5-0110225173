from dataclasses import dataclass


@dataclass
class Task:
    title: str
    completed: bool = False

    def mark_completed(self):
        self.completed = True