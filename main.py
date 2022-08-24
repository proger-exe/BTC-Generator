"I'm idk what i doing."
import random
from typing import List


def generate(how_many: int) -> List[str]:
    """Receipts Function-generator

    Args:
        how_many (int): how many receipts create.

    Returns:
        List[str]: a result
    """

    total_receipt = []

    for _ in range(how_many):
        total_receipt.append(
            "".join([random.choice("aedfgc1234567890") for _ in range(32)])
        )

    return total_receipt


def main() -> None:
    "Main function"

    how_many = ""
    stdout = input("Enter count of receipts > ")

    while True:
        if stdout.isdigit():
            how_many = int(stdout)
            break

        
        stdout = input("[Incorrent output]\nEnter count of receipts > ")

    res = generate(how_many=how_many)
    for receipt in res:
        print(f"https://t.me/BTC_CHANGE_BOT?start=c_{receipt}")


if __name__ == "__main__":
    main()
