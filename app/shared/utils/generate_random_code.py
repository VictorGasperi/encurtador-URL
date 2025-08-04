import random
import string


def generate_random_code(length: int) -> str:
    alpha_num = string.ascii_lowercase + string.digits
    result = ''.join(random.choices(alpha_num, k=length))
    return result

    
    