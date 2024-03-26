def generate_list_html(items, num_items=None):
    # Внутренняя функция, которая формирует многострочную строку с элементами списка в формате HTML
    def inner_function():
        # Начинаем строку с открывающегося тега <ol>
        result = '<ol>\n'
        # Проверяем, если задано количество строк, иначе используем все строки
        if num_items is not None:
            items_to_use = items[:num_items]
        else:
            items_to_use = items
        # Добавляем каждый элемент из списка в тег <li>...</li> и добавляем их в результирующую строку
        for item in items_to_use:
            result += f'<li>{item}</li>\n'
        # Заканчиваем строку закрывающимся тегом </ol>
        result += '</ol>'
        return result

    # Возвращаем внутреннюю функцию, чтобы можно было вызвать ее позднее
    return inner_function