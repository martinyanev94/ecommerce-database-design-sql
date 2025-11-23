class User:
    def __init__(self, username):
        self.username = username
        self.friends = set()

    def add_friend(self, friend):
        self.friends.add(friend)

def suggest_friends(user):
    suggested = set()
    for friend in user.friends:
        suggested.update(friend.friends)
    suggested.discard(user)  # remove the user from suggestions
    return suggested

alice = User("Alice")
bob = User("Bob")
charlie = User("Charlie")

alice.add_friend(bob)
bob.add_friend(charlie)

print(suggest_friends(alice))  # will suggest Charlie
