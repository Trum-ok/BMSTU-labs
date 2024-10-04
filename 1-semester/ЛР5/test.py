def filter_elements(elements):
    # Определяем крайние значения
    first = elements[0]
    last = elements[-1]
    
    # Считаем количество нулей
    zeros = elements.count(0)
    
    # Формируем начальный список оставшихся элементов
    remaining = [first] + [0] * zeros + [last]
    
    # Считаем, сколько элементов у нас сейчас
    count = len(remaining)
    
    # Если у нас меньше 4 элементов, добавляем дополнительные крайние элементы
    if count < 4:
        remaining = remaining[:1] + elements[1:-1] + remaining[-1:]  # добавляем элементы из середины
        remaining = remaining[:4]  # оставляем не более 4 элементов
    
    # Если у нас больше 8 элементов, обрезаем лишние
    elif count > 8:
        remaining = remaining[:8]  # оставляем не более 8 элементов
    
    return remaining

# Пример использования
elements = [1, 0, 2, 3, 0, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 13, 0, 14, 15, 16]
result = filter_elements(elements)
print(result)