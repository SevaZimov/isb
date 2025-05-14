import json


def load_frequencies(file_path: str) -> dict[str, float]:
    """Загружает частоты символов из JSON-файла.

    :param file_path: Путь к JSON-файлу с частотами
    :return: Словарь с частотами символов
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        frequencies = json.load(f)

    if not isinstance(frequencies, dict):
        raise ValueError("Файл частот должен содержать JSON-объект (словарь)")

    return frequencies


def save_key_to_json(key: dict[str, str], filename: str) -> None:
    """Сохраняет ключ шифрования в JSON-файл.

    :param key: Словарь с ключом шифрования
    :param filename: Имя файла для сохранения
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(key, f, ensure_ascii=False, indent=4)


def count_chars(text: str) -> dict[str, int]:
    """Подсчитывает частоту встречаемости символов в тексте.

    :param text: Анализируемый текст
    """
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


def make_key(encrypted_counts: dict[str, int],
             lang_freq: dict[str, float]) -> dict[str, str]:
    """Создаёт ключ для расшифровки на основе частотного анализа.

    :param encrypted_counts: Частоты символов в зашифрованном тексте
    :param lang_freq: Эталонные частоты символов языка
    """
    enc_sorted = sorted(encrypted_counts.items(), key=lambda x: -x[1])
    lang_sorted = sorted(lang_freq.items(), key=lambda x: -x[1])
    key = {}
    used_chars = set()
    for i in range(min(len(enc_sorted), len(lang_sorted))):
        enc_char = enc_sorted[i][0]
        lang_char = lang_sorted[i][0]
        if lang_char not in used_chars:
            key[enc_char] = lang_char
            used_chars.add(lang_char)
    for char, _ in enc_sorted:
        if char not in key:
            key[char] = "?"
    return key


def decode_text(text: str, key: dict[str, str]) -> str:
    """Дешифрует текст с использованием ключа замены символов.

    :param text: Зашифрованный текст
    :param key: Словарь замены символов
    """
    decrypted = [key.get(char, char) for char in text]
    result = ''.join(decrypted)
    return result
