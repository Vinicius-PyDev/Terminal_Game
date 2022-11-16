import rich.console
from random import randint
def ATK():
    atk = 20
    atkar = randint(atk/2, atk )
    return atkar
AAA = rich.console.Console()
for d in range(10):
    AAA.print("[#000099]" + str(ATK()) + "[/]", style="bold")
    input()
