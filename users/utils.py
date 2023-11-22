import secrets


def generate_otp_code() -> int:
    """
    The function of generating a random six-digit OTP code.
    """
    return secrets.randbelow(900000) + 100000
