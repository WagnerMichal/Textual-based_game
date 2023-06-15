class Player:
    """
    Class to represent a player and his location
    """
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname
        self.current_location = None
        self.distance_traveled = 0

    def __str__(self):
        """
        Returns:
            str: Name of the player
        """
        return self.name + ' alias ' + self.nickname

    def move_to_node(self, destination):
        """
        Changes players current location to his selected destination.
        Counts the distance traveled to each node.

        Args:
            destination (int): Converted index of location in array of available nodes 
        """
        edge = self.current_location.connected_nodes[destination]
        self.current_location = edge.node
        self.distance_traveled += edge.distance


class Edge:
    """
    Class to represent an edge between nodes along with its distance.
    """
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class Node:
    """
    Class to represent node and his connections.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_nodes = []

    def add_connection(self, node, distance):
        """
        Creates connection between two nodes and holds information about distance

        Args:
            node (object): Node that will be connected to our current node
            distance (int): distance between nodes
        """
        edge = Edge(node, distance)
        if edge not in self.connected_nodes:
            self.connected_nodes.append(edge)

    def add_two_way_connection(self, node, distance):
        """
        Creates two way connection between two nodes and holds information about distance

        Args:
            node (object): Node that will be connected to our current node
            distance (int): distance between nodes
        """
        edge = Edge(node, distance)
        if edge not in self.connected_nodes:
            self.connected_nodes.append(edge)
            edge.node.connected_nodes.append(Edge(self, distance))

    def get_choices(self):
        """
        Creates a string with available paths (nodes) for current node and distance.
        Assigns letter computed by using index of node.

        Returns:
            str: Available nodes with letters for choosing.
        """
        string = ''
        for i, choice in enumerate(self.connected_nodes):
            string += f"{chr(65 + i)} - {choice.node.name} (Distance: {choice.distance} km)\n"
        return string

    def get_node(self, choice):
        """
        Checks if node exists.

        Args:
            choice (int): Index of chosen node in array of available nodes
        Returns:
            object: Node on chosen index.
        """
        if choice < len(self.connected_nodes):
            return self.connected_nodes[choice].node


def create_world():
    """
    Creates a gaming world with all the connections.

    Returns:
        object: starting and ending node.
    """
    beach = Node("Beach",
                 "You woke up on a sandy beach with no recollection of how you got there.")
    jungle = Node("Jungle",
                  "Dense vegetation surrounds you as you enter the mysterious jungle.")
    cave_entrance = Node("Cave Entrance",
                         "A dark cave entrance beckons you to explore its depths.")
    underground_lake = Node("Underground lake",
                            "A tranquil underground lake shimmers with beauty.")
    spider_lair = Node("Spider lair",
                       "You encounter a web-filled lair inhabited by a giant spider.")
    catacombs = Node("Catacombs",
                     "A network of underground catacombs stretches before you.")
    crystal_cave = Node("Crystal cave",
                        "A cave decorated with shining crystals radiates an otherworldly glow.")
    cavern = Node("Cavern",
                  "A vast cavern stretches before you, filled with stalactites and stalagmites.")
    tunnel = Node("Tunnel",
                  "You venture into an underground tunnel that leads you deeper into the island.")
    campsite = Node("Campsite",
                    "You stumble upon an old campsite, abandoned and overgrown.")
    waterfall = Node("Waterfall", "A magnificent waterfall stands before you.")
    cliffs = Node("Cliffs",
                  "You reach a cliff that offers a view of the surrounding ocean.")
    labyrinth = Node("Labyrinth", "You stand in a mysterious labyrinth.")
    riverside = Node("Riverside", "You arrive at a peaceful riverside.")
    ruins = Node("Ruins",
                 "Ancient ruins rise from the ground, weathered by time.")
    treasure = Node("Treasure",
                    "You have discovered a hidden chamber filled with gold and jewels.")

    beach.add_connection(jungle, 2)
    beach.add_connection(cave_entrance, 1)
    jungle.add_connection(campsite, 3)
    jungle.add_two_way_connection(tunnel, 2)
    cave_entrance.add_connection(underground_lake, 4)
    cave_entrance.add_connection(tunnel, 5)
    underground_lake.add_connection(spider_lair, 2)
    underground_lake.add_connection(catacombs, 2)
    catacombs.add_two_way_connection(crystal_cave, 1)
    catacombs.add_two_way_connection(cavern, 4)
    cavern.add_two_way_connection(tunnel, 2)
    cavern.add_two_way_connection(labyrinth, 3)
    cavern.add_connection(riverside, 5)
    campsite.add_connection(waterfall, 3)
    campsite.add_two_way_connection(cliffs, 2)
    waterfall.add_connection(labyrinth, 4)
    labyrinth.add_connection(cliffs, 10)
    labyrinth.add_connection(riverside, 7)
    riverside.add_connection(ruins, 2)
    ruins.add_connection(treasure, 1)

    return beach, treasure


def main():
    """
    Main logic of application
    """
    player_name = input('Enter your name: ')
    player_nickname = input('Enter your nickname: ')
    player = Player(player_name, player_nickname)
    starting_location, ending_location = create_world()
    player.current_location = starting_location
    print(f"\nWelcome, {player.nickname}!")
    while True:
        print(f"You are currently at {player.current_location.name}.")
        print(player.current_location.description)
        if not player.current_location.connected_nodes:
            print("You are forgotten and lost forever.")
            break
        print("Where do you want to go")
        print(player.current_location.get_choices())
        choice = input("Enter your choice: ").upper()

        index = ord(choice) - 65
        if player.current_location.get_node(index):
            player.move_to_node(index)
        else:
            print("\nYou can't go there. Choose another way.")

        if player.current_location == ending_location:
            print(f'\nYou found the treasure! You traveled {player.distance_traveled} km.')
            break


if __name__ == "__main__":
    main()
