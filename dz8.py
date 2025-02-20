import time
import unittest

def measure_time(func, *args, **kwargs):
    """
    Функція для вимірювання часу виконання іншої функції.
    :param func: Функція, час виконання якої потрібно виміряти
    :param args: Позиційні аргументи для функції
    :param kwargs: Іменовані аргументи для функції
    :return: Кортеж (результат виконання функції, час виконання у секундах)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time


def example_function(n):
    time.sleep(n)
    return n

class TestMeasureTime(unittest.TestCase):
    def test_execution_time(self):
        _, exec_time = measure_time(example_function, 1)
        self.assertAlmostEqual(exec_time, 1, delta=0.1)

    def test_function_result(self):
        result, _ = measure_time(example_function, 2)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()
