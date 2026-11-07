types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_dubl(c):
    tickets_clean = {}
    used = []
    for key, values in c.items():
        unique_values =[]
        for i in values:
            if i not in used:
                used.append(i)
                unique_values.append(i)
        tickets_clean[key] = unique_values
    return tickets_clean

def merge_dicts(a, b):
    tickets_merged = {}
    for key_a, values_a in a.items():
        for key_b, values_b in b.items():
            if key_a == key_b:
                tickets_merged[values_a] = values_b
    return tickets_merged



cleaned = delete_dubl(tickets)
print(cleaned)

merge = merge_dicts(types, cleaned)
print(merge)
