digi = ['A','b','c',1,2,'A','b','c',1,2,]

new = list(set())

for i in digi:
    if i not in new:
        new.append(i)
print(new)


class Animal:
    def sound(self):
        print("geberic")
class Dog(Animal):
    def sound(self):
        print("wool")
class Cat(Animal):
    def sound(self):
        print("meow")

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()