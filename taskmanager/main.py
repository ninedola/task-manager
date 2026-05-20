from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Удалить задачу")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            task = input("Введите задачу: ")
            manager.add_task(task)

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            manager.show_tasks()

            try:
                index = int(input("Введите номер задачи: "))
                manager.remove_task(index - 1)
            except ValueError:
                print("Ошибка ввода")

        elif choice == "4":
            break

        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()