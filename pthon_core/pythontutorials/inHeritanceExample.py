#Base Class
class Character(object):
    def __init__(self):
        self.health = 100


class BlackSmith(Character):
    def __init__(self):
        super(BlackSmith,self).__init__()


bs = BlackSmith()
print (bs.health)