# Prompt: An animal shelter, which holds only dogs and cats, operates on a
# strictly "first in, first out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter, or they
# can select whether they prefer a dog or a cat (and will receive 
# the odlest of that type). They cannot select which specific animal they would
# like. Create the data structure to maintain this system and implement
# operations such as enqueue, dequeueAny, deqeueDog, and dequeueCat. You may use
# the build in LinkedList data structure.
from StacksAndQueues import Queue

class AnimalShelter:
    def __init__(self, animal_id, animal_type):
        if not animal_type in ['cat', 'dog']:
            raise ValueError("Animal must either be cat or dog")
        self.all_animals = Queue((animal_id, animal_id))
        if animal_type == 'cat':
            self.cats = Queue(animal_id)
            self.dogs = None
        else:
            self.dogs = Queue(animal_id)
            self.cats = None

    def enqueue(self, animal_id, animal_type):
        self.all_animals.add((animal_id, animal_type))
        if animal_type == 'cat':
            self.cats.push(animal_id)
        else:
            self.dogs.push(animal_id)

    def remove_specific(self, animal_type):
        if animal_type == 'cats':
            holding = []
            while True:
                n = self.cats.remove()
                if n == None or n[0] == return_val[0]:
                    break
                holding.append(n)

            for held in holding:
                self.cats.add(held)
        else:
            holding = []
            while True:
                n = self.dogs.remove()
                if n == None or n[0] == return_val[0]:
                    break
                holding.append(n)

            for held in holding:
                self.dogs.add(held)

    def dequeueAny(self):
        ret_val = self.all_animals.remove()
        self.remove_specific(ret_val[1])
        return ret_val[0]

    def dequeueDog(self):
        ret_val = self.dogs.remove()
        holding = []
        while True:
            n = self.all_animals.remove()
            if n == None or (n[0] == ret_val and n[1] == 'dogs'):
                break
            holding.append(n)
        for held in holding:
            self.dogs.add(held)
        return ret_val

    def dequeueCat(self):
        ret_val = self.catgs.remove()
        holding = []
        while True:
            n = self.all_animals.remove()
            if n == None or (n[0] == ret_val and n[1] == 'cat'):
                break
            holding.append(n)
        for held in holding:
            self.cats.add(held)
        return ret_val
