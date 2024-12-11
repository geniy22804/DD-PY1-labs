# TODO  Напишите функцию count_letters
def count_letters(text):
    text_with_low_symbols = str(text).lower()
    low_symbols = list(text_with_low_symbols)
    low_letters = []
    for i in low_symbols:
        if i.isalpha() == True:
            low_letters.append(i)
    str_of_unique_letters = set(low_letters)
    dict_list = {}
    for j in str_of_unique_letters:
        dict = {j: low_letters.count(j)}
        dict_list.update(dict)
    return dict_list
# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_of_letters):
    count_of_letters = sum(dict_of_letters.values())
    finished_dict = {}
    for letter, count in dict_of_letters.items():
        frequency = round(count / count_of_letters, 2)
        dict = {letter: frequency}
        finished_dict.update(dict)
    return finished_dict
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
for letter, freq in calculate_frequency(count_letters(main_str)).items():
        print(f"{letter}: {freq}")
# TODO Распечатайте в столбик букву и её частоту в тексте
