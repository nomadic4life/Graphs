import random
import math


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship nondirectional
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential ( start from 0 and increment id by 1 for the next new users) integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for user in range(numUsers):
            self.addUser(f'user-{user}')

        # randomly distributed friendships
        # between those users
        possibleFriendships = []

        # Create friendships
        for userID in self.users:
            for frinedID in range(userID + 1, self.lastID + 1):
                # append in tuple
                possibleFriendships.append((userID, frinedID))
        random.shuffle(possibleFriendships)
        # The number of users must be greater than the average number of friendships
        for i in range(0, math.floor(numUsers * avgFriendships / 2)):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # Create an empty Queue and enqueue the starting vertex
        q = Queue()
        q.enqueue([userID])
        # While the queue is not empty ...
        while q.size() > 0:
            # Dequeue the first vertex
            path = q.dequeue()
            v = path[-1]
            # If that vertex has not been visisted ...
            if v not in visited:
                # Mark it as visisted
                visited[v] = path

                # Then add all of its neighbors to the back of the queue
                for friend in self.friendships[v]:
                    # Copy the path
                    path_copy = list(path)
                    # Append neighbor to the back of the copy
                    path_copy.append(friend)
                    # Enqueue copy to the queue
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    # sg.populateGraph(10, 2)
    sg.friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {
        8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

    # {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
