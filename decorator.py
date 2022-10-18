import datetime

def timer(func):
    def time_work(*args, **kwargs):
        datetime_start_of_work = datetime.datetime.now()
        result = func(*args, **kwargs)
        s = f'Время вызова функции: {datetime_start_of_work}, ' \
            f'Имя функции: {func}, ' \
            f'Аргументы функции: {args}, {kwargs}, ' \
            f'Результат работы функции: {result}'
        with open('log_1.txt', "a", encoding='utf-8') as f:
            f.write(f'{s} \n')
        return result
    return time_work


def make_way_to_log(path):
    def timer(func):
        def time_work(*args, **kwargs):
            datetime_start_of_work = datetime.datetime.now()
            result = func(*args, **kwargs)
            s = f'Время вызова функции: {datetime_start_of_work}, ' \
                f'Имя функции: {func}, ' \
                f'Аргументы функции: {args}, {kwargs}, ' \
                f'Результат работы функции: {result}'
            with open(path, "a", encoding='utf-8') as f:
                f.write(f'{s} \n')
            return result
        return time_work
    return timer
