class User():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.followers = 0


    def follow(self):
        self.followers += 1



user_1 = User("mike", 1)
user_2 = User("Paul", 2)

print(user_1.name.title())
print(user_2.name.title())

