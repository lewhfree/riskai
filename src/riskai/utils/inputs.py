import traceback


def int_input(prompt: str) -> int:
    val: int
    while True:
        try:
            val = int(input(prompt))
            break
        except ValueError:
            print("Bad int value")
            traceback.print_exc()
    return val


def bool_input(prompt: str) -> bool:
    val: bool
    while True:
        try:
            val = bool(input(prompt).lower == "true")
            break
        except ValueError:
            print("bad bool value")
            traceback.print_exc()
    return val
