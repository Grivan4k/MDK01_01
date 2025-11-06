class Rival:
    def __init__(self, life):
        self.life = life
    
    def attack(self):
        print("Ouch!")
        self.life -= 1
    
    def checkLife(self):
        if self.life <= 0:
            print("You won!")
        else:
            print(self.life)

thanos = Rival(3)
magneto = Rival(5)

thanos.checkLife()  
magneto.checkLife() 

thanos.attack()     
thanos.attack()     
thanos.attack()    

thanos.checkLife()  
magneto.checkLife() 

while magneto.life > 0:
    magneto.attack()
magneto.checkLife() 