def find_missing_letter(chars):
    lst_full = list(range(ord(chars[0]), ord(chars[-1])+1))
    lst_chars = [ord(char) for char in chars]
    return [chr(el) for el in lst_full if not el in lst_chars][0]


def test_find_missing_letter():
    assert find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
    assert find_missing_letter(['O', 'Q', 'R', 'S']) == 'P'
