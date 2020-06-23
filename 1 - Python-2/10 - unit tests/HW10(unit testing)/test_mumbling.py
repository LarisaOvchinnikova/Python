from mumbling import accum
def test_accum():
    assert accum("ZpglnRxqenU") == "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu"
    assert accum("abcd") == "A-Bb-Ccc-Dddd"
    assert accum("a") == "A"