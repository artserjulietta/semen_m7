import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters


def test_password_valid_and_correct_length():
    """Тест: пароль правильной длины и содержит только разрешённые символы"""
    
    length = 50
    password = generate_password(length)
    
    # Проверка длины
    assert len(password) == length, f"Длина пароля {len(password)}, ожидалось {length}"
    
    # Проверка символов
    allowed = set(string.ascii_letters + string.digits + string.punctuation)
    invalid = set(password) - allowed
    
    assert len(invalid) == 0, f"Недопустимые символы: {invalid}"


    import string

def test_password_contains_only_valid_characters():
    """Тест: пароль содержит ТОЛЬКО разрешённые символы (латиница, цифры, знаки)"""
    
    # Определяем, какие символы разрешены
    allowed_chars = set(string.ascii_letters + string.digits + string.punctuation)
    
    # Генерируем пароль
    password = generate_password(50)
    
    # Преобразуем пароль в множество символов (уникальные)
    password_chars = set(password)
    
    # Находим "плохие" символы — те, что не входят в allowed_chars
    invalid_chars = password_chars - allowed_chars
    
    # Проверяем: если есть недопустимые символы — ошибка
    assert len(invalid_chars) == 0, f"Найдены недопустимые символы в пароле: {invalid_chars}"


"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""