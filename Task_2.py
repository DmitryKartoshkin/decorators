from decorator import make_way_to_log
import os

FILE_NAME = 'log_2.txt'
FILE_LOG_DIR = 'logs'
ROOT_PATH = os.getcwd()
full_path = os.path.join(ROOT_PATH, FILE_LOG_DIR, FILE_NAME)

@make_way_to_log(path = full_path)
def factorial(n):
    fact = 1
    for f in range(1, n+1):
        fact *= f
    return fact


if __name__ == "__main__":
    f_6 = factorial(6)
    f_12 = factorial(12)
    factorial(100)
