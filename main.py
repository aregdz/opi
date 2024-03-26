from list_html_generator import generate_list_html

# Создаем список строк
items = ['строка_1', 'строка_2', 'строка_3', 'строка_4', 'строка_5']

# Вызываем функцию из модуля, чтобы получить функцию-замыкание для генерации HTML списка
generate_html_list = generate_list_html(items, num_items=None)

# Вызываем внутреннюю функцию, чтобы получить многострочную строку HTML
html_list = generate_html_list()

# Выводим результат на экран
print(html_list)