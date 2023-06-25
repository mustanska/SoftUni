from typing import List

from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: task_name == t.name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        completed_tasks_count = 0
        for task_number in range(len(self.tasks)):
            if self.tasks[task_number].completed:
                completed_tasks_count += 1
                self.tasks.remove(self.tasks[task_number])

        return f"Cleared {completed_tasks_count} tasks."

    def view_section(self) -> str:
        tasks = "\n".join([t.details() for t in self.tasks])

        return f"Section {self.name}:\n{tasks}"
