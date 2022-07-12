from datetime import datetime
now = datetime.now()


def logger(func):
    def new_function(*args, **kwargs):
        with open('log.txt', 'w', encoding='utf-8') as log_file:
            log_file.write(f'Дата и время вызова функции: {now.strftime("%m/%d/%Y, %H:%M:%S")}\n')
            log_file.write(f'Имя функции: {func.__name__}\n')
            if args and kwargs:
                log_file.write(f'Аргументы функции: {args, kwargs}\n')
            elif args:
                log_file.write(f'Аргументы функции: {args}\n')
            else:
                log_file.write(f'Аргументы функции: {kwargs}\n')
            something = func(*args, **kwargs)
            log_file.write(f'Результат выполнения функции: {something}')

        return something
    return new_function


def path_logger(path):
    def decorator(func):
        def new_path_function(*args, **kwargs):
            with open(path + 'log.txt', 'w', encoding='utf-8') as log_file:
                log_file.write(f'Дата и время вызова функции: {now.strftime("%m/%d/%Y, %H:%M:%S")}\n')
                log_file.write(f'Имя функции: {func.__name__}\n')
                if args and kwargs:
                    log_file.write(f'Аргументы функции: {args, kwargs}\n')
                elif args:
                    log_file.write(f'Аргументы функции: {args}\n')
                else:
                    log_file.write(f'Аргументы функции: {kwargs}\n')
                something = func(*args, **kwargs)
                log_file.write(f'Результат выполнения функции: {something}')
            return something
        return new_path_function
    return decorator


@logger
def mul(a, b):
    return a * b


@path_logger(path='C:/Users/Public/')
def power(a, b):
    return a ** b


print(mul(2, 6))
print(power(5, 4))
