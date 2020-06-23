from unittest import TestCase
# по умолчанию после клика на названии функциии ctrl+shift+T
# образовался unittest. Этоне совсем удобно.
# Изменим дефолтные настройки pycharm на pytest: File -> Settings ->
# или в поиске(лупа) напишем test
# внизу выбрать default test runner
# в появившемся окне Settings в области Testing выбираем
# Default test runner ---> pytest (вместо Unittests)


class Test(TestCase):
    def test_is_prime(self):
        self.fail()
