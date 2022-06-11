#Working with classes and objects

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def run(self):
        print("run")
        return 0

player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 20)

print(player1)
print(player2)

print(player1.name)
print(player2.name)

print(player1.age)
print(player2.age)

print(f"{player1.name} has {player1.age} years old.")
print(f"{player2.name} has {player2.age} years old.")

print(player1.run())
