from pprint import pprint

class TestCase:

    def __init__(self, steps = {}, result = None):
        self.steps = steps # шаги тест-кейса (словарь)
        self.result = result # ожидаемый результат выполнения тест-кейса

    def set_step(self, step_number, step_text):
        # step_number - ключ (номер шага)
        # step_text - значение (текстовое описание шага)
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        # step_number - ключ (номер шага)
        self.steps.pop(step_number, 'Такого ключа нет в словаре')

    def set_result(self, result):
        self.result = result # ожидаемый результат выполнения тест-кейса

    def get_test_case(self):
        # {'Шаги': {<номер шага>: '<описание шага>'}, 'Ожидаемый результат': '<вывод ожидаемого результата>'}
        pprint({'Шаги' : self.steps, 'Ожидаемый результат' : self.result}, sort_dicts=False)


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()