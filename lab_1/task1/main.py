import argparse
from argparse import Namespace

from enc import load_key, encrypt_text


def setup_arg_parser() -> Namespace:
    """Создает и настраивает парсер аргументов командной строки.

    :return: Настроенный экземпляр ArgumentParser.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'key',
        help="Путь к JSON-файлу с ключом шифрования"
    )
    parser.add_argument(
        'input',
        help="Путь к файлу с исходным текстом"
    )
    parser.add_argument(
        'output',
        help="Путь для сохранения зашифрованного текста"
    )
    return parser.parse_args()


def save_result(output_path: str, content: str) -> None:
    """Сохраняет текст в файл.

    :param output_path: Путь для сохранения файла.
    :param content: Текст для записи.
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)


def main() -> None:
    """Основная функция"""
    args = setup_arg_parser()
    try:
        with open(args.input, 'r', encoding='utf-8') as file:
            text = file.read()
        key = load_key(args.key)
        encrypted_text = encrypt_text(text, key)
        save_result(args.output, encrypted_text)
        print(f"Текст успешно зашифрован и сохранен в {args.output}")
    except Exception:
        print("Проверьте входные данные и попробуйте снова.")


if __name__ == "__main__":
    main()
