import secrets


def generate_otp_code() -> int:
    """
    Функция генерации случайного шестизначного OTP-кода.
    """
    return secrets.randbelow(900000) + 100000
