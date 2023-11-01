from task import Task


class Section:
    tasks = []

    def __init__(self, name: str) -> None:
        self.name = name

    def add_task(self, new_task: Task):
        pass

    def complete_task(task_name: str):
        pass
# The Section class should also have four methods:
#     • add_task(new_task: Task)
#         ◦ Adds a new task to the collection and returns "Task {task details} is added to the section"
#         ◦ If the task is already in the collection, returns "Task is already in the section {section_name}"
#     • complete_task(task_name: str)
#         ◦ Changes the task to completed (True) and returns "Completed task {task_name}"
#         ◦ If the task is not found, returns "Could not find task with the name {task_name}"
#     • clean_section()
#         ◦ Removes all the completed tasks and returns "Cleared {amount of removed tasks} tasks."
#     • view_section()
#         ◦ Returns information about the section and its tasks in this format:
#     "Section {section_name}:
#      {details of the first task}
#      {details of the second task}
#      …
#      {details of the n task}"
