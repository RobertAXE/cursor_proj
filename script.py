import random
import string
import sys


def generate_password(length: int) -> str:
    if length <= 0:
        raise ValueError("length must be a positive integer")

    alphabet = string.ascii_letters + string.digits + string.punctuation
    rng = random.SystemRandom()
    return "".join(rng.choice(alphabet) for _ in range(length))


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python script.py <length>", file=sys.stderr)
        print("Example: python script.py 12", file=sys.stderr)
        return 2

    try:
        length = int(argv[1])
        password = generate_password(length)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    print(password)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
