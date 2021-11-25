
class Parrot:
    species = 'bird'
    vertebrae = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return f'{self.name} sings {song}.'

    def dance(self):
        return f'{self.name} is now dancing.'


tweety = Parrot('Tweety', 2)

print(tweety.__class__.species)
print(tweety.name)

print(tweety.sing('Happy birthday to you.'))
print(tweety.dance())

