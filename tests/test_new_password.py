import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_characters2(password, password_length = 10, password_max = 20):
    """ Тест, что длина пароля соответствует заданной """
    if password_length <= len(password) <= password_max:
        return True
    else:
        return False

def test_password_characters3():
    """Тест, что два сгенерированных подряд пароля различаются"""
    if generate_password != generate_password:
        print("Пароли различаются")
    else:
        print("Пароли одинаковые")