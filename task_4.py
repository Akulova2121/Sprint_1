new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Тестировщик только что завершил задачу task_005. Перенеси её из списка new_tasks в список completed_tasks. Сделай это в одно действие.
completed_tasks.append(new_tasks.pop(-1))

# Запрос task_007 заказчик убрал из плана, потому что нужно доработать требования. Удали его из списка new_tasks.
new_tasks.remove('task_007')


# В последней задаче из списка new_tasks заказчик поднял приоритет, поэтому её нужно будет взять в работу следующей. Выведи её на экран.
print(new_tasks[-1])