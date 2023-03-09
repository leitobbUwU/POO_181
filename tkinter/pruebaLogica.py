import random
import string

def generate_password(length, include_uppercase, include_special_chars):
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_special_chars:
        chars += string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def check_password_strength(password):
    length_ok = len(password) >= 8
    uppercase_ok = any(c.isupper() for c in password)
    special_chars_ok = any(c in string.punctuation for c in password)
    if length_ok and uppercase_ok and special_chars_ok:
        return 'Strong'
    elif length_ok and uppercase_ok:
        return 'Moderate'
    else:
        return 'Weak'

def generate_password_and_check_strength(length, include_uppercase, include_special_chars):
    password = generate_password(length, include_uppercase, include_special_chars)
    strength = check_password_strength(password)
    return password, strength