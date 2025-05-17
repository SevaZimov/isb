import math


def freq_bit_test(sequence: str) -> float:
    """
    Выполняет частотный побитовый тест NIST.

    :param sequence: Битовая строка для тестирования
    :return: P значение теста
    """
    s_n = ((sequence.count("1") - sequence.count("0"))
           / math.sqrt(len(sequence)))
    p = math.erfc(abs(s_n) / math.sqrt(2))
    return p


def identical_consecutive_test(sequence: str) -> float:
    """
    Тест на идентичные подряд идущие биты (Runs Test).
    :param sequence: Битовая строка для тестирования
    :return: P значение теста
    """
    q = sequence.count("1") / len(sequence)
    if abs(q - 0.5) >= 2 / math.sqrt(len(sequence)):
        return 0.0
    v_n = 0
    for i in range(len(sequence) - 1):
        if sequence[i] != sequence[i + 1]:
            v_n += 1
    p = math.erfc(
        abs(v_n - 2 * len(sequence) * q * (1 - q)) /
        (2 * math.sqrt(2 * len(sequence)) * q * (1 - q))
    )
    return p


def most_ones_seq_test(sequence: str, block : int, pi : list[float]) -> float:
    """
    Тест на самую длинную последовательность единиц в блоке.
    :param pi: Список вероятностных констант
    :param block: Размер блока
    :param sequence: Битовая строка для тестирования
    :return: Значение статистики χ² (хи-квадрат)
    для последующего получения P на стороннем сайте
    """

    stat = {"v1": 0, "v2": 0, "v3": 0, "v4": 0}
    for i in range(0, len(sequence), block):
        sub_seq = sequence[i:i + block]
        one_dupl = "1"
        while one_dupl in sub_seq:
            one_dupl += "1"
        max_ones_seq = len(one_dupl)
        key = f"v{max(min(max_ones_seq, 4), 1)}"
        stat[key] += 1
    sqr_x = 0
    for i in range(4):
        sqr_x += pow((stat[f"v{i + 1}"] - 16 * pi[i]), 2) / (16 * pi[i])
    return sqr_x
