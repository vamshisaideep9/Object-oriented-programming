# Multilevel inheritance


class Grandparent:
    def __init__(self, name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")

class parent(Grandparent):
    def work(self):
        print(f"{self.name} is working")

class child(parent):
    def play(self):
        print(f"{self.name} is playing.")


child = child("vamshi")
child.tell_story()
child.work()
child.play()