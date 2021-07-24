class User:
    def __init__(self,name):
        self.name=name
        self.isLoggedIn = False

def isAuthenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].isLoggedIn:
            function(args[0])
    return wrapper

@isAuthenticated
def createBlogPost(user):
    print(f"This is {user.name}'s new blog post.")


newUser = User("Brent")
createBlogPost(newUser)

newUser.isLoggedIn = True
createBlogPost(newUser)