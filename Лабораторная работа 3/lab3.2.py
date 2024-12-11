# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group,N = ","):
    first_group1 = first_group.split(N)
    second_group1 = second_group.split(N)
    general_members = list(set(first_group1).intersection(set(second_group1)))
    general_members.sort()

    return general_members

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(f"Общие участники групп:{find_common_participants(participants_first_group, participants_second_group, N="|")}")