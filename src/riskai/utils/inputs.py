import traceback

def int_input(prompt:str) -> int:
    val:int
    while True:
        try:
            val = int(input(prompt))
            break
        except ValueError:
            print("Bad int value")
            traceback.print_exc()
    return val
