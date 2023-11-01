class Task():
    comments = []
    completed_set = False

    def __init__(self, name: str, due_date: str) -> None:
        self.name = name
        self.due_date = due_date

    def change_name(self, new_name: str):
        if new_name == self.name:
            return "Name cannot be the same."
        else:
            self.name = new_name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."
        else:
            self.due_date = new_date

    def add_comment(self, comment: str):
        Task.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number > len(Task.comments):
            return "Cannot find comment."
        else:
            Task.comments[comment_number - 1] = new_comment
            string_to_print = ", ".join(Task.comments)
            return string_to_print

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"
