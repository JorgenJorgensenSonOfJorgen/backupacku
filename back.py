class Backpack():
    def __init__(self, colour,size):
        self.colour = colour
        self.size = size
        self.items = []
        self.open = False
    def openBag(self):
        self.open = True
    def closeBag(self):
        self.close = True
    def putIn(self,item):
        if self.open:
            self.items.append(item)
            print('"{}" has been put into the backpack.'.format(item))
        else:
            print('Backpack must be open to add items.')
    def takeOut(self,item):
        if self.open:
            for i in range(len(self.items)):
                if self.items[i] == item:
                    self.items.pop(i)
                    return print('"{}" has been removed from the backpack.'.format(item))
                    
            return print('"{}" was not found in the backpack, therefore it was not removed.'.format(item))
        else:
            print('Backpack must be open to remove items.')

bPack1 = Backpack('blue', 'small')
bPack2 = Backpack('red', 'medium')
bPack3 = Backpack('green', 'large')

bPack2.openBag()
bPack2.putIn('lunch')
bPack2.putIn('jacket')
bPack2.closeBag()
bPack2.openBag()
bPack2.takeOut('jacket')
bPack2.closeBag()