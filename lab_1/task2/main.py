import argparse
from argparse import Namespace
import json
from dec import decode_text, make_key, count_chars, load_frequencies


def setup_arg_parser() -> Namespace:
    """Создает и настраивает парсер аргументов командной строки.

    :return: Настроенный экземпляр Namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'frequency',
        help="Путь к JSON-файлу с частотами символов"
    )
    parser.add_argument(
        'input',
        help="Путь к файлу с исходным зашифрованным текстом"
    )
    parser.add_argument(
        'key',
        help="Путь к JSON-файлу для сохранения подобранного ключа шифрования"
    )
    parser.add_argument(
        'output',
        help="Путь для сохранения расшифрованного текста"
    )
    return parser.parse_args()


def save_result(output_path: str, content: str) -> None:
    """Сохраняет текст в файл.

    :param output_path: Путь для сохранения файла.
    :param content: Текст для записи.
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)


def read_file(filename: str) -> str:
    """Читает содержимое файла.

    :param filename: Путь к файлу для чтения
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def main() -> None:
    """Основная функция для выполнения дешифрования."""
    try:
        args = setup_arg_parser()
        print(f"Используются частоты из файла: {args.frequency}")
        frequencies = load_frequencies(args.frequency)
        encrypted_text = read_file(args.input)
        encrypted_counts = count_chars(encrypted_text)
        ####key = make_key(encrypted_counts, frequencies)
        key = load_frequencies(args.key)
        decrypted_text = decode_text(encrypted_text, key)
        save_result(args.output, decrypted_text)
        with open(args.key, 'w', encoding='utf-8') as f:
            json.dump(key, f, ensure_ascii=False, indent=4)
        print(f"Успешно! Дешифрованный текст сохранен в {args.output}")
        print(f"Ключ шифрования сохранен в {args.key}")
    except FileNotFoundError as e:
        print(f"Ошибка: Файл не найден - {e.filename}")
    except json.JSONDecodeError:
        print("Ошибка: Некорректный формат JSON-файла")
    except ValueError as e:
        print(f"Ошибка в данных: {str(e)}")
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")


if __name__ == "__main__":
    main()
