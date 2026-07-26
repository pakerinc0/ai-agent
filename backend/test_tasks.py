from app.core.task_manager import TaskManager



manager = TaskManager()



task = manager.add_task(
    "Создать тестовый проект"
)


print(
    "Добавлена задача:"
)

print(task)



next_task = manager.get_next_task()


print(
    "Следующая задача:"
)

print(next_task)



manager.update_status(
    task["id"],
    "completed"
)



print(
    "Все задачи:"
)

print(
    manager.get_all()
)
