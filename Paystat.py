import re
from typing import Generator, Callable

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генератор, що ідентифікує всі дійсні числа у тексті та повертає їх.
    Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
    """
    for match in re.finditer(r' (?P<number>\d+\.\d+) ', text):
        yield float(match.group("number"))

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальний прибуток, використовуючи функцію генератора чисел.
    """
    return sum(func(text))

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний прибуток: {total_income}")

if __name__ == "__main__":
    main()
