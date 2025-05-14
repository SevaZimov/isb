# main.py
import json
import argparse
from argparse import Namespace
from tests import freq_bit_test, identical_consecutive_test, most_ones_seq_test


def setup_arg_parser() -> Namespace:
    """Создает и настраивает парсер аргументов командной строки.

    :return: Настроенный экземпляр Namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'sequences',
        help="Путь к JSON-файлу с побитовыми последовательностями"
    )
    return parser.parse_args()


def load_sequences(file_path: str) -> dict[str, str]:
    """Загружает последовательности из JSON-файла.

    :param file_path: Путь к JSON-файлу с
    битовыми последовательностями
    :return: Словарь с побитовыми последовательностями и языками
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        sequences = json.load(f)
    if not isinstance(sequences, dict):
        raise ValueError("Файл последовательностей должен содержать JSON-объект")
    for lang, seq in sequences.items():
        if not isinstance(seq, str):
            raise ValueError(f"Последовательность для {lang} должна быть строкой")

        if len(seq) != 128:
            raise ValueError(
                f"Последовательность для {lang} должна содержать ровно 128 бит. "
                f"Получено: {len(seq)}"
            )

        if not all(c in '01' for c in seq):
            raise ValueError(
                f"Последовательность для {lang} содержит недопустимые символы. "
                "Допустимы только '0' и '1'"
            )
    return sequences


def main() -> None:
    try:
        args = setup_arg_parser()
        sequences = load_sequences(args.sequences)

        for language, sequence in sequences.items():
            print(f"\nРезультаты тестов для {language}:")

            # Тест на частоту битов
            p_freq = freq_bit_test(sequence)
            print(f"1. Тест на частоту битов: P = {p_freq:.6f}")

            # Тест на идентичные последовательности
            p_identical = identical_consecutive_test(sequence)
            print(f"2. Тест на идентичные последовательности: P = {p_identical:.6f}")

            # Тест на максимальные последовательности единиц
            x_square = most_ones_seq_test(sequence)
            print(f"3. Тест на максимальные последовательности единиц: χ^2 = {x_square:.6f}")
    except ValueError as e:
        print(f"Ошибка загрузки файла: {e}")


if __name__ == "__main__":
    main()