from convert_time import get_military

def test_get_military_AM():
   assert get_military("12:30 AM") == "00:30"
   assert get_military("11:30 AM") == "11:30"


def test_get_military_PM():
   assert get_military("12:30 PM") == "12:30"
   assert get_military("11:30 PM") == "23:30"


def test_get_military():
   assert get_military("12:30 PM") == "12:30"
   assert get_military("11:30 PM") == "23:30"