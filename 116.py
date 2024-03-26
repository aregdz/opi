def generate_list_html(items):
    # Внутренняя функция, которая формирует многострочную строку с элементами списка в формате HTML
    def inner_function():
        # Начинаем строку с открывающегося тега <ol>
        result = '<ol>\n'
        # Добавляем каждый элемент из списка в тег <li>...</li> и добавляем их в результирующую строку
        for item in items:
            result += f'<li>{item}</li>\n'
        # Заканчиваем строку закрывающимся тегом </ol>
        result += '</ol>'
        return result

    # Возвращаем внутреннюю функцию, чтобы можно было вызвать ее позднее
    return inner_function

# Создаем список строк
items = ['строка_1', 'строка_2', 'строка_3']

# Вызываем внешнюю функцию, чтобы получить функцию-замыкание для генерации HTML списка
generate_html_list = generate_list_html(items)

# Вызываем внутреннюю функцию, чтобы получить многострочную строку HTML
html_list = generate_html_list()

# Выводим результат на экран
print(html_list)