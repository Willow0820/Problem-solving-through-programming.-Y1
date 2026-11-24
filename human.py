#class stuff
class Human:
    MAX_ENERGY = 100

    def __init__(self, name = "Human"):
        self.name = name
        self.energy = Human.MAX_ENERGY
        self.age = 0

    def display(self):
        print(f'I am {self.name}')

if __name__ == "__main__":
     human = Human()
     human.display()






