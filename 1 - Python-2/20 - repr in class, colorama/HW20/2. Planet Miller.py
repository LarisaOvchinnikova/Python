# 2. Planet Miller
# Представьте что вы приземлились на планету Миллер (из фильма Интерстеллар), где один час равен семи годам на Земле.
# # Посчитайте через сколько минут у вас наступит 2021 год.

from datetime import datetime
today = datetime.today()
new_year_2021 = datetime(2021, 1, 1, 0, 0, 0)
time_until_new_year = new_year_2021 - today
print(f"Our time until New Year: {time_until_new_year}")

q = 7 * 365 * 24

time_miller_until_new_year = time_until_new_year /q
print(f"Miller time until New Year: {time_miller_until_new_year}")