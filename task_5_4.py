# Задача 4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1, Two — 2, Three — 3, Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open("task_5_4.txt", encoding="utf-8") as f_obj:
    out_f = open('new_task_5_4.txt', 'w', encoding='utf-8')
    for txt in f_obj.readlines():
        txt = txt.replace("One", "Один")
        txt = txt.replace("Two", "Два")
        txt = txt.replace("Three", "Три")
        txt = txt.replace("Four", "Четыре")
        out_f.write(txt)
    out_f.close()





