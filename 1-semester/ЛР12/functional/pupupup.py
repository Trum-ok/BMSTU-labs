def is_alternating_vowel_consonant(word: str) -> bool:
    """Проверяет, чередуются ли гласные и согласные в слове."""
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZбвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ"

    for i in range(len(word) - 1):
        if (word[i] in vowels and word[i + 1] in vowels) or \
           (word[i] in consonants and word[i + 1] in consonants):
            return False
    return True


def get_sentence_by_idx(lines: list[str], idx: int) -> str:
    """Извлекает предложение с индексом `idx` из списка строк."""
    current_idx = 0
    sentence_parts = []

    for line in lines:
        words = line.split()
        for word in words:
            if current_idx == idx:
                sentence_parts.append(word)
            if word.endswith((".", "?", "!", ";")):
                if current_idx == idx:
                    return ' '.join(sentence_parts)
                sentence_parts = []
                current_idx += 1

    return "\nИскомое предложение не найдено.\n"


def find_sentence_idx(lines: list[str]) -> int:
    cnt = {}
    idx = 0
    for line in lines:
        for word in line.split():
            if is_alternating_vowel_consonant(word):
                if idx in cnt.keys():
                    cnt[idx] += 1
                else:
                    cnt[idx] = 1
            if word.endswith(".") or word.endswith('?') or word.endswith("!") or word.endswith(";"):
                idx += 1

    max_idx = max(cnt, key=cnt.get, default=-1)
    return max_idx


def del_sentence(lines: list[str], idx: int) -> list[str]:
    """Удаляет предложение с индексом idx из списка строк."""
    current_idx = 0
    sentence_start = None
    sentence_end = None

    for line_idx, line in enumerate(lines):
        words = line.split()
        for word_idx, word in enumerate(words):
            if current_idx == idx and sentence_start is None:
                sentence_start = (line_idx, word_idx)
            if current_idx == idx and (word.endswith((".", "?", "!", ";"))):
                sentence_end = (line_idx, word_idx)
                break
            if word.endswith((".", "?", "!", ";")):
                current_idx += 1
        if sentence_end:
            break

    if sentence_start and sentence_end:
        start_line, start_word = sentence_start
        end_line, end_word = sentence_end
        if start_line == end_line:
            lines[start_line] = ' '.join(
                lines[start_line].split()[:start_word] +
                lines[start_line].split()[end_word + 1:]
            )
        else:
            lines[start_line] = ' '.join(lines[start_line].split()[:start_word])
            for i in range(start_line + 1, end_line):
                lines[i] = ''
            lines[end_line] = ' '.join(lines[end_line].split()[end_word + 1:])
        lines = [line for line in lines if line.strip()]

    return lines


def find_and_remove_max_sentence(lines: list[str]) -> list[str]:
    """
    Находит и удаляет предложение с максимальным количеством слов,
    где гласные чередуются с согласными.
    """
    max_sentence_idx = find_sentence_idx(lines)
    print(max_sentence_idx)
    res = get_sentence_by_idx(lines, max_sentence_idx)
    if "\nИскомое предложение не найдено.\n" not in res:
        print("Искомое предложение:\n", res, len(res.split()))
    else:
        print(res)
    return del_sentence(lines, max_sentence_idx)


if __name__ == "__main__":
    from _text import t
    print("\nОбновленный текст:")
    print('\n'.join(find_and_remove_max_sentence(t)))
