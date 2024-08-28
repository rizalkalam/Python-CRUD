import random
import string

def random_string(long:int) -> str:
    str_result = ''.join(random.choice(string.ascii_letters) for i in range(6))
    return str_result