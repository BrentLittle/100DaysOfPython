# Creating a class

class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(20060929, "Brent Littlefield")
print(user1.id)
print(user1.username)

user2 = User(20430927, "Matt Denny")
print(user2.id)
print(user2.username)

user1.follow(user2)

print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)