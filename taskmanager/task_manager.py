class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task.strip():
            self.tasks.append(task)
            print("Задача добавлена")
        else:
            print("Пустая задача")

    def show_tasks(self):
        if not self.tasks:
            print("Задач нет")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Удалена задача: {removed}")
        else:
            print("Неверный индекс")