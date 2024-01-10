from datetime import timedelta as td

from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    date = td(microseconds=100)
    calculate_salary()
    get_employees()
    time = date.total_seconds()
    print('Программа отработала за: ', time, 'сек.')
