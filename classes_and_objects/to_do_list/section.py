from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return  f"Could not find task with the name {task_name}"
        task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        count = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                count += 1
        return f"Cleared {count} tasks."

    def view_section(self):
        result = '\n'.join(t.details() for t in self.tasks)
        return f"""Section {self.name}:
{result}"""

