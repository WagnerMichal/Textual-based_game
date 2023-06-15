class Player:
    """
    Class to represent a player and his location
    """
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname
        self.current_location = None

    def __str__(self):
        """
        Returns:
            str: Name of the player
        """
        return self.name + ' alias ' + self.nickname

    def move_to_node(self, destination):
        """
        Changes players current location to his selected destination

        Args:
            destination (int): Converted index of location in array of available nodes 
        """
        self.current_location = self.current_location.connected_nodes[destination]


class Node:
    """
    Class to represent node and his connections.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_nodes = []

    def add_connection(self, node):
        """
        Creates connection between two nodes 

        Args:
            node (object): Node that will be connected to our current node
        """
        if node not in self.connected_nodes:
            self.connected_nodes.append(node)

    def add_two_way_connection(self, node):
        """
        Creates two way connection between two nodes

        Args:
            node (object): Node that will be connected to our current node
        """
        if node not in self.connected_nodes:
            self.connected_nodes.append(node)
            node.connected_nodes.append(self)

    def get_choices(self):
        """
        Creates a string with available paths (nodes) for current node.
        Assigns letter computed by using index of node.

        Returns:
            str: Available nodes with letters for choosing.
        """
        string = ''
        for i, choice in enumerate(self.connected_nodes):
            string += f"{chr(65 + i)} - {choice.name}\n"
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
            return self.connected_nodes[choice]


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

    beach.add_connection(jungle)
    beach.add_connection(cave_entrance)
    jungle.add_connection(campsite)
    jungle.add_two_way_connection(tunnel)
    cave_entrance.add_connection(underground_lake)
    cave_entrance.add_connection(tunnel)
    underground_lake.add_connection(spider_lair)
    underground_lake.add_connection(catacombs)
    catacombs.add_two_way_connection(crystal_cave)
    catacombs.add_two_way_connection(cavern)
    cavern.add_two_way_connection(tunnel)
    cavern.add_two_way_connection(labyrinth)
    cavern.add_connection(riverside)
    campsite.add_connection(waterfall)
    campsite.add_two_way_connection(cliffs)
    waterfall.add_connection(labyrinth)
    labyrinth.add_connection(cliffs)
    labyrinth.add_connection(riverside)
    riverside.add_connection(ruins)
    ruins.add_connection(treasure)

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
            print('\nYou found the treasure!.')
            break


if __name__ == "__main__":
    main()
