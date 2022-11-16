from random import choice
from random import randint
import rich.console as Cores
cor = Cores.Console()
import time

CLASSES = ["Assasino", "Guerreiro", "Mercenario", "Mago", "Necromante", "Invocador", "Caçador", "inventor", "Guardião", "Deus"]

CLASSES_INFOS = ["+15 AGI\n+15 DEX\n+30 Equilibrio", "+20 ATK\n+10 ATKMG\n+30 Força", "+10 ATK\n+10 ATKMG\n+10 DEX\n+5 Carisma\n+10 Equilibrio\n+5 Inteligencia\n+10 Força", "+15 ATKMG\n+15 DEFMG\n+10 Alquimia\n+20 Inteligencia", "Necromante", "Invocador", "Caçador", "inventor", "Guardião", "Deus"]


def Saves():
    open("aaa.txt", "w")
    write(aaa)


class Player():
    def __init__(self):#, nome="", classe=""):
        self.nome = ""
        self.classe = ""

        randint(0, 5)
        #Atributos de batalha
        #self.hp = randint(5, 30)
        self.mp = randint(1, 5)
        self.ATK = randint(1, 5)
        self.DEF = randint(1, 5)
        self.ATKMG = randint(1, 5)
        self.DEFMG = randint(1, 5)
        self.DEX = randint(1, 5)
        self.AGI = randint(1, 5)
        art = self.mp + self.ATK + self.DEF + self.ATKMG + self.DEFMG + self.DEX + self.AGI
        #basemax = 40
        self.hp = [40 - art, 40 - art]
        #print(str(self.hp[0]) + "/" + str(self.hp[1]))
        #Atributos de ação
        self.Equilibrio = randint(1, 5)
        self.Carisma = randint(1, 5)
        self.Inteligencia = randint(1, 5)
        self.Força = randint(1, 5)
        self.Imunidade = randint(1, 5)
        self.Alquimia = randint(1, 5)
        self.Aparencia = randint(1, 5)
        self.Nobreza = randint(1, 5)

    def Assasino(self):
        self.DEX += 15
        self.AGI += 15
        self.Equilibrio += 30
    
    def Guerreiro(self):
        self.ATK += 20
        self.ATKMG += 10
        self.Força += 30
        
    def PrintChar(self):
        cor.print("\n\n" + "[#4444ee]Nome: [#4444ff]" + self.nome + "\n" + "[#4444ee]Classe: [#4444ff]" + self.classe)
        
        cor.print("\nAtributos de Combate:\n", style="#4444dd")
        cor.print("[#4444ff]HP: " + str(self.hp[0]) + "/" + str(self.hp[1]))
        cor.print("[#4444ff]MP: " + str(self.mp))
        cor.print("[#4444ff]ATK: " + str(self.ATK))
        cor.print("[#4444ff]DEF: " + str(self.DEF))
        cor.print("[#4444ff]ATKMG: " + str(self.ATKMG))
        cor.print("[#4444ff]DEFMG: " + str(self.DEFMG))
        cor.print("[#4444ff]DEX: " + str(self.DEX))
        cor.print("[#4444ff]AGI: " + str(self.AGI))
        
        cor.print("\n\nAtributos de Ação:\n", style="#4444dd")
        cor.print("[#4444ff]Equilibrio: " + str(self.Equilibrio))
        cor.print("[#4444ff]Carisma: " + str(self.Carisma))
        cor.print("[#4444ff]Inteligencia: " + str(self.Inteligencia))
        cor.print("[#4444ff]Força: " + str(self.Força))
        cor.print("[#4444ff]Imunidade: " + str(self.Imunidade))
        cor.print("[#4444ff]Alquimia: " + str(self.Alquimia))
        cor.print("[#4444ff]Aparencia: " + str(self.Aparencia))
        cor.print("[#4444ff]Nobreza: " + str(self.Nobreza))
        input()


class Enemy():
    def __init__(self, nome, hp, ATK, DEF, ATKMG, DEFMG):
        self.nome = nome
        self.hp = hp
        self.ATK = ATK
        self.DEF = DEF
        self.ATKMG = ATKMG
        self.DEFMG = DEFMG

    def Ataque(self, alvo):
        alvo.hp[0] -= randint(int(self.ATK / 2), self.ATK)
        if alvo.hp[0] <= 0:
            while True:
                print("GAME OVER")
                input()
    
    def AtaqueMG(self, alvo):
        alvo.hp[0] -= randint(int(self.ATKMG/2), self.ATKMG )
        if alvo.hp[0] <= 0:
            while True:
                cor.print("[red]GAME OVER")
                input()
        
    def PrintChar(self):
        cor.print("\n\n" + "[orange4]Nome: " + self.nome)

        cor.print("[orange4]\nAtributos do Inimigo:\n")
        cor.print("[orange4]HP: " + str(self.hp))
        cor.print("[orange4]ATK: " + str(self.ATK))
        cor.print("[orange4]DEF: " + str(self.DEF))
        cor.print("[orange4]ATKMG: " + str(self.ATKMG))
        cor.print("[orange4]DEFMG: " + str(self.DEFMG))
    
    
def Evento():
    roleta = randint(1, 2)

    if roleta == 1:
        print("Voce esta em uma floresta")
        print("Voce escuta um barulho que parece ser algum tipo de animal")
        print("Voce percebe que se trata de um filhote de Lobo embaixo de um galho de arvore que esta o prendendo")
        print("Deseja ajudar o lobo e Levantar o galho")
        escolha = input("Digite 'sim' ou 'não' ")
        if escolha == "sim":
            galho = randint(5, 10)
            if player.Força >= galho:
                print("Voce ajudor um lobinho")
            else:
                print(f"para levantar esse galho você precisaria de pelo menos {galho} de Força")
    if roleta == 2:
        print("voce esta em uma caverna")
    
    
player = Player()

puppy_wolf = Enemy("Filhote de Lobo", 9, 2, 3, 2, 1)
wolf = Enemy("Lobo", 17, 7, 4, 20, 5)


print("Ola seja bem vindo ao jogo terminal\n")
time.sleep(3)
print("Aqui voce vai se aventurar matando monstros\nusando equipamentos e escolhendo uma classe\ne até vai poder se casar\n")
time.sleep(3)
print("mas antes de dar inicio a essa aventura vamos criar o seu personagem então\npor favor escolha seu nome\n")
time.sleep(2)


SEU_NOME = input("Escreva seu nome ")

while len(SEU_NOME) >= 15:
    print("por favor não insira um nome tão grande")
    SEU_NOME = input("Escreva seu nome ")
    
player.nome = SEU_NOME

print("\nok agora colha uma classe \n")
time.sleep(3)

for i in range(0, 9):
    print( f"[{str(i)}]" + " " + CLASSES[i] + ":" + "\n" + CLASSES_INFOS[i] + "\n")

while True:
    time.sleep(3)
    try:
        print("\nEscolha um numero de acordo com a classe que desejar")
        SUA_CLASSE = int(input("Escolha sua classe: "))
        if SUA_CLASSE <= 8:
            player.classe = CLASSES[int(SUA_CLASSE)]
            break
    except:
        pass
    print("Escolha apenas os numeros validos e sem adição de letras")


player.PrintChar()

player.Assasino()


time.sleep(3)
player.PrintChar()

while True:
    print()
    Evento()
    player.PrintChar()
    wolf.PrintChar()
    wolf.AtaqueMG(player)
    input()

