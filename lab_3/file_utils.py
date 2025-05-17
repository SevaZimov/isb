def save_binary(path: str, data: bytes) -> None:
    """
    Сохраняет binary файл
    :param data: Данные для записи
    :param path: Путь к файлу
    :return:
    """
    with open(path, 'wb') as f:
        f.write(data)

def read_binary(path: str) -> bytes:
    """
    Читает binary файл
    :param path: Путь к файлу
    :return:
    """
    with open(path, 'rb') as f:
        return f.read()

def save_txt(path: str, content: str) -> None:
    """
    Сохраняет текстовый файл
    :param path: Путь к файлу
    :param content: Данные для записи
    :return:
    """
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def read_txt(path: str) -> str:
    """
    Сохраняет текстовый файл
    :param path: Путь к файлу
    :return:
    """
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()