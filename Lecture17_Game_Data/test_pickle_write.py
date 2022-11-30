import pickle

class NPC:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y
    def show(self):
        print(f'Name : {self.name}, Pos: {self.x ,self.y}')

yuri = NPC('Yuri', 100, 200)
tom = NPC('Tom', 200, 400)
npcs = [yuri, tom]
yuri.show()

with open('npcs.pickle', 'wb') as f:
    pickle.dump(npcs,f)