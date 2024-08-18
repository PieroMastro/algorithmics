class Task:
    def __init__(self, description: str, importance: int, completion_month: str, completion_date: int):
        """
        Initialize a Task object.

        :param description: The description of the task.
        :param importance: The importance of the task (1-5).
        :param completion_month: The month in which the task should be completed.
        :param completion_date: The date on which the task should be completed.
        """
        
        self.description = description
        self.importance = importance
        self.completion_month = completion_month
        self.completion_date = completion_date

def create_task() -> Task:
    """
    Create and return a new Task object with user input.

    :return: A new Task object.
    """
    
    description = input("Ingresar descripción de tarea: ")
    importance = int(input("Ingresar importancia de tarea (del 1 al 5): "))
    
    while importance < 1 or importance > 5:
        print("Importancia debe ser entre 1 y 5")
        importance = int(input("Ingresar importancia de tarea (del 1 al 5): "))
        
    completion_month = input("Ingresar mes de realización: ")
    completion_date = int(input("Ingresar fecha de realización: "))

    while completion_date < 1 or completion_date > 31:
        print("Fecha de realización debe ser entre 1 y 31")
        completion_date = int(input("Ingresar fecha de realización: "))

    return Task(description, importance, completion_month, completion_date)

def find_most_important_task(task_list: list) -> Task:
    """
    Find and return the task with the highest importance in the given list.

    :param task_list: The list of tasks to search.
    :return: The task with the highest importance.
    """
    return max(task_list, key=lambda x: x.importance)

def find_most_urgent_task(task_list: list) -> Task:
    """
    Find and return the task with the earliest completion date in the given list.

    :param task_list: The list of tasks to search.
    :return: The task with the earliest completion date.
    """
    return min(task_list, key=lambda x: x.completion_date)

def main():
    task_list = []
    
    for i in range(3):
        task = create_task()
        task_list.append(task)

    most_important_task = find_most_important_task(task_list)
    most_urgent_task = find_most_urgent_task(task_list)

    print(f"La tarea más importante: {most_important_task.description}, importancia-{most_important_task.importance}, mes de realización-{most_important_task.completion_month}, fecha de realización-{most_important_task.completion_date}")
    print(f"La tarea más urgente: {most_urgent_task.description}, importancia-{most_urgent_task.importance}, mes de realización-{most_urgent_task.completion_month}, fecha de realización-{most_urgent_task.completion_date}")

if __name__ == "__main__":
    main()