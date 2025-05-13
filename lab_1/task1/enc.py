import json
from typing import Dict


def load_key(key_path: str) -> Dict[str, str]:
    """Загружает ключ шифрования из JSON-файла.

    :param key_path: Путь к файлу с ключом в формате JSON.
    :return: Словарь вида {'исходный_символ': 'заменяющий_символ'}.
    """
    with open(key_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def encrypt_text(text: str, key: Dict[str, str]) -> str:
    """Шифрует текст методом простой подстановки.

    :param text: Исходный текст для шифрования.
    :param key: Словарь замены символов (например, {'А': 'Щ', 'Б': 'Ъ'}).
    :return: Зашифрованная строка. Символы, отсутствующие в ключе,
    остаются без изменений.
    """
    if not text or not key:
        raise ValueError("Текст и ключ не могут быть пустыми.")

    encrypted = []
    for char in text.upper():
        encrypted.append(key.get(char, char))
    return ''.join(encrypted)
