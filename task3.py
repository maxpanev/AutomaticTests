def count_vowels(s):
    # Создаем множество гласных букв (включая как строчные, так и прописные)
    vowels = set("aeiouAEIOU")
    # Инициализируем счетчик количества гласных
    count = 0
    # Проходим по каждому символу в строке
    for char in s:
        # Если символ является гласной, увеличиваем счетчик
        if char in vowels:
            count += 1
    # Возвращаем общее количество гласных
    return count