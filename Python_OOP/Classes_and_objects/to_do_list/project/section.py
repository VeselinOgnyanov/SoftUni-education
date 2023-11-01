from task import Task


class Section:

    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {new_task}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details} is added to the section"

    def complete_task(self, task_name: str):
        for current_task in self.tasks:
            if task_name == current_task:
                current_task.completed_set = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        removed_tasks = len(self.tasks)
        self.tasks.clear
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        string_to_return = ""
        string_to_return += f"Section {self.name}:" + "/n"
        for current_task in self.tasks:
            string_to_return += current_task.details() + "/n"


#     • view_section()
#         ◦ Returns information about the section and its tasks in this format:
#     "Section {section_name}:
#      {details of the first task}
#      {details of the second task}
#      …
#      {details of the n task}"
