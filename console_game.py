"""
This Console Game personal project is for Corban to be able to test some of the basic
features of Python. Here are the basic minimum things that the program should include:
-Follow all of the PEP 8 style guidelines
-Import at least one module
-Use at least the following basic types: int, float, str, set, list, dict
-Have at least one class
-Use at least one custom generator
-Raise at least one exception
-Handle at least one exception
-Use at least one comprehension, either list, set, dict, or generator
-Read and write to a save file
-
"""

from item import Item
from enemy import Enemy
import random


save_file_name = "console_game_save.txt"
player_name = ""
player_health = 100
player_score = 0
player_money = 100
player_num_kills = 0
player_quest_progress = 0
player_inventory = []

item_attr_front = ["Old", "Rusty", "Well-used *wink wink*", "New", "High Quality", "Refurbished", "Just-Like-New",
                   "Expensive", "Cheap", "Bargin", "Worthless", "Imported", "Fancy", "Fair", "Sleek", "Smooth",
                   "Stylish"]
item_attr_thing = ["Baseball Bat", "Relic", "Cloak", "Sword", "Mittins", "Toothpaste", "Desktop Moniter", "Juice",
                   "Bow and Arrow", "Axe", "Pumpkin Pie", "Door Frame", "Moonshine", "Root Beer", "Go-Go Juice"]

def console_game():
    print("Welcome to Corban's Adventure game in Python!")
    print("Loading...")

    random.seed()
    _load_data()
    _print_player_stats()
    print()

    while True:
        _print_quest_map()
        user_input = input("Ready to start your next quest (y/n)?")
        if user_input == "y" or user_input == "Y":
            _do_quest(player_quest_progress)
            print("Congrats! You are now {0}% complete!".format(player_quest_progress * 100 // 10))
            print("\nSaving...")
            _save_data()
        elif user_input == "n" or user_input == "N":
            break;
    print("Goodbye!")


def _load_data():
    global player_name, player_health, player_score, player_money, player_num_kills, player_quest_progress
    try:
        with open(save_file_name, mode="rt", encoding="utf-8") as f:
            player_name = f.readline().strip()
            player_health = int(f.readline().strip())
            player_score = int(f.readline().strip())
            player_money = int(f.readline().strip())
            player_num_kills = int(f.readline().strip())
            player_quest_progress = int(f.readline().strip())

            try:
                # keep reading until we run into an error
                while True:
                    # TODO low key there's got to be a better way to do this, but whatever
                    it_name = f.readline().strip()
                    it_des = f.readline().strip()
                    it_cost = int(f.readline().strip())
                    it_att = int(f.readline().strip())
                    it_heal = int(f.readline().strip())
                    it_dur = int(f.readline().strip())

                    player_inventory.append(Item(it_name, it_des, it_cost, it_att, it_heal, it_dur))

            except (StopIteration, ValueError) as error:
                # We've reached the end of the file
                pass

    except FileNotFoundError:
        print("\nIt appears this is your first game!")
        player_name = input("Welcome stranger, what's your name? ")
        print("Welcome to Shirlock Forest, " + player_name + "!")
        print("Saving...")
        _save_data()


def _save_data():
    try:
        with open(save_file_name, mode="wt", encoding="utf-8") as f:
            f.write(player_name + "\n")
            f.write(str(player_health) + "\n")
            f.write(str(player_score) + "\n")
            f.write(str(player_money) + "\n")
            f.write(str(player_num_kills) + "\n")
            f.write(str(player_quest_progress) + "\n")

            for it in player_inventory:
                f.write(it.name + "\n")
                f.write(it.description + "\n")
                f.write(str(it.cost) + "\n")
                f.write(str(it.attack) + "\n")
                f.write(str(it.health) + "\n")
                f.write(str(it.durability) + "\n")

    except (FileNotFoundError, FileExistsError) as error:
        print("There was a problem saving the file!")
        print(error)


def _print_player_stats():
    print("=" * 60)
    print("Corban's Adventure Game in Python!")
    print("=" * 60)

    global player_name, player_health, player_score, player_money, player_num_kills, player_quest_progress
    print("Player Name:", player_name)
    print("Health:", player_health)
    print("Score:", player_score)
    print("Money: $", player_money)
    print("Number of Kills:", player_num_kills)
    print("Quest Progress: {0}%".format(int(player_quest_progress) * 100 // 10))

    _print_player_inventory()
    print("\n")


def _print_quest_map():

    quest_list = [str(x + 1) + " " for x in range(10)]
    quest_list[0] += "-Trading Post-"
    quest_list[1] += "The Forbidden Forest"
    quest_list[2] += "-Trading Post-"
    quest_list[3] += "Night of the Phoenix"
    quest_list[4] += "-Trading Post-"
    quest_list[5] += "Bridge of Death"
    quest_list[6] += "An Unexpected Visitor"
    quest_list[7] += "Into the Caves"
    quest_list[8] += "-Trading Post-"
    quest_list[9] += "Your Worst Nightmare"

    if int(player_quest_progress) < 10:
        quest_list[int(player_quest_progress)] = "**" + quest_list[int(player_quest_progress)] + "**"

    print("Welcome to your quest!\nYou are {0}% complete!".format(int(player_quest_progress) * 100 // 10))
    for quest in quest_list:
        print(quest)
    print()


def _do_quest(quest):
    global player_inventory, player_score, player_num_kills, player_health, player_quest_progress, player_money
    print("Loading Quest!")

    room_enemies = []

    if quest == 0 or quest == 2 or quest == 4 or quest == 8:
        _trading_post((quest + 1) * 2, (quest + 3) ** 3)
    elif quest == 1:

        room_enemies.append(Enemy("Skeleton", 10, 5, 3))
        room_enemies.append(Enemy("Zombie", 20, 0, 1))

        _enter_fight("Forbidden Forest", room_enemies)
    elif quest == 3:

        room_enemies.append(Enemy("Phoenix", 35, 10, 5))
        room_enemies.append(Enemy("Fireling", 10, 0, 2))
        room_enemies.append(Enemy("Fireling", 10, 0, 2))
        room_enemies.append(Enemy("Fireling", 10, 0, 2))
        room_enemies.append(Enemy("Fireling", 10, 0, 2))

        _enter_fight("Night of the Phoenix", room_enemies)
    elif quest == 5:

        room_enemies.append(Enemy("Troll", 15, 10, 5))
        room_enemies.append(Enemy("Fat Troll", 20, 25, 3))
        room_enemies.append(Enemy("Lazy Troll", 10, 4, 1))
        room_enemies.append(Enemy("Smart Troll", 20, 0, 10))

        _enter_fight("Bridge of Death", room_enemies)
    elif quest == 6:
        room_enemies.append(Enemy("Your mom", 50, 50, 5))
        _enter_fight("An Unexpected Visitor", room_enemies)
    elif quest == 7:

        room_enemies.append(Enemy("Batman", 35, 10, 7))

        for _ in range(20):
            room_enemies.append(Enemy("Bat", 5, 0, 2))

        _enter_fight("Into the Caves", room_enemies)
    elif quest == 9:

        room_enemies.append(Enemy("Lucy Furr", 50, 25, 15))
        room_enemies.append(Enemy("Baby Devil", 15, 7, 5))
        room_enemies.append(Enemy("Baby Devil", 15, 7, 5))

        _enter_fight("Your Worst Nightmare", room_enemies)
    else:
        print("Sorry that quest doesn't exist")

    player_quest_progress += 1

    if player_health <= 0:
        print("Try again!")
        player_health = 100
        player_score = 0
        player_money = 100
        player_num_kills = 0
        player_quest_progress = 0
        player_inventory = []


def _enter_fight(room_name, list_enemies):
    global player_inventory, player_score, player_num_kills, player_health, player_quest_progress, player_money

    print("You have entered the", room_name)
    print("Suddenly out of no where, appears some horrible enemies!\n")

    def ___print_monster_stats():
        print("Here are the enemies in the room:")
        print(_phil("Enemy", 40), _phil("Hlth", 10), _phil("Armor", 10), _phil("Atk", 10))
        for en in list_enemies:
            print(_phil(en.name, 40), _phil(en.health, 10), _phil(en.armor, 10), _phil(en.attack, 10))

    user_moves = 3
    while True:
        if len(list_enemies) == 0:
            break
        if user_moves > 0:
            print("\nYou have", user_moves, "move(s) left, what would you like to do?")
            print("0: View enemies in room (1 move)\n1: View your stats (1 move)\n"
                  "2: Attack! (1 move per attack)\n3: Use a potion (1 move)\n4: Retreat")
            user_input = input("What would you like to do? ")
            if user_input == "0":
                print()
                ___print_monster_stats()
                user_moves -= 1
                print()
            elif user_input == "1":
                print()
                _print_player_stats()
                user_moves -= 1
                print()
            elif user_input == "2":
                print("Attack!")

                while user_moves > 0:
                    if len(list_enemies) == 0:
                        break
                    print("\nYou have " + str(user_moves) + " move(s) left")
                    print("Here are the enemies in the room:")
                    x = 0
                    for en in list_enemies:
                        print(_phil(str(x) + ":", 4), en.name)
                        x += 1

                    user_input = input("Which enemy would you like to attack (q to cancel)? ")

                    try:
                        if user_input == "q":
                            break

                        user_input = int(user_input)

                        if user_input < 0 or user_input >= len(list_enemies):
                            print("Incorrect input")
                            continue
                        print()

                        x = 0
                        for i in player_inventory:
                            print(_phil(str(x) + ":", 4), _phil(i.name, 40), i.attack)
                            x += 1

                        user_weapon = input("Which item would you like to use to attack with? ")
                        user_weapon = int(user_weapon)
                        if user_weapon < 0 or user_weapon >= len(player_inventory):
                            print("Incorrect input")
                            continue

                        list_enemies[user_input].receive_attack(player_inventory[user_weapon].attack)
                        player_score += player_inventory[user_weapon].attack * 2
                        player_inventory[user_weapon].durability -= 1
                        print("\n" + str(list_enemies[user_input].name), "now has", list_enemies[user_input].health, "health left")

                        if list_enemies[user_input].health <= 0:
                            print()
                            print("#" * 50)
                            print("You have killed", str(list_enemies[user_input].name) + "!!!")
                            print("#" * 50)

                            player_num_kills += 1
                            player_score += 50

                            money_won = 25 + random.randint(25, 26 + 50 * player_num_kills)
                            print("You got", money_won, "money from", str(list_enemies[user_input].name) + "!")
                            print("Score increased by 50")
                            player_money = int(player_money) + money_won
                            del list_enemies[user_input]
                        if player_inventory[user_weapon].durability <= 0:
                            print("Your weapon", player_inventory[user_weapon].name, "has been exhausted")
                            del player_inventory[user_weapon]

                        user_moves -= 1
                    except (ValueError, TypeError) as err:
                        print("Sorry I didn't get that")
                        print(err)
                        raise err

                if len(list_enemies) == 0:
                    break
            elif user_input == "3":
                print("Select the potion you would like to use:")
                user_moves -= 1

                x = 0
                for i in player_inventory:
                    print(_phil(str(x) + ":", 4), _phil(i.name, 40), i.health)
                    x += 1

                while True:
                    user_input = input("Which potion would you like to drink (q to cancel)? ")
                    if user_input == "q":
                        break
                    else:
                        try:
                            if int(user_input) < 0 or int(user_input) >= len(player_inventory):
                                print("Incorrect input")

                            player_health += player_inventory[int(user_input)].health
                            player_inventory[int(user_input)].durability -= 1
                            print("Your health has increased by", player_inventory[int(user_input)].health, "to",
                                  player_health)
                            if player_inventory[int(user_input)].durability <= 0:
                                print("Item", player_inventory[int(user_input)].name, "has been exhausted")
                                del player_inventory[int(user_input)]
                            break
                        except (ValueError, TypeError):
                            print("Didn't get that, try again")

            elif user_input == "4":
                player_score -= 500
                player_quest_progress -= 3
                if player_quest_progress < 0:
                    player_quest_progress = 0

                if player_health < 100:
                    player_health = 100

                print("You wimp out and leave the fight")
                break
            else:
                print("Sorry, your input was not recognized")
        else:
            print()
            print("&" * 60)
            print("& ENEMIES TURN")
            print("&" * 60)

            print()
            for en in list_enemies:

                print(en.name + " attacked you for " + str(en.attack))
                player_health -= int(en.attack)

            print("The enemies are done!")
            print("Your health is now", player_health)
            if player_health <= 0:
                print("You died! Good try!")
                print("You got a score of", player_score)
                break
            print()
            user_moves = 3


def _print_player_inventory():
    """This function will print the player's inventory to the console"""
    global player_inventory
    print("\nInventory (", len(player_inventory), "):")
    print(_phil("Item", 40), _phil("Atk", 10), _phil("Hth", 10), _phil("Dur", 10))
    for i in player_inventory:
        print(_phil(i.name, 40), _phil(i.attack, 10), _phil(i.health, 10), _phil(i.durability, 10))


def _trading_post(min_cost, max_cost):
    global player_money, player_inventory, player_score
    print("$" * 80)
    print("T R A D I N G   P O S T")
    print("$" * 80, "\n")

    post_items = [next(_item_generator(min_cost, max_cost)) for _ in range(15)]

    def ___print_store_items():
        print(_phil("Here are the items available:", 44), _phil("Cost", 10), _phil("Atk", 10), _phil("Hlth", 10),
              _phil("Dur", 10))
        j = 0
        for i in post_items:
            print(_phil(str(j) + ":", 3), _phil(i.name, 40), _phil(i.cost, 10), _phil(i.attack, 10), _phil(i.health, 10),
                  _phil(i.durability, 10))
            j += 1

    ___print_store_items()

    while True:
        print("\nWhat would you like to do?\n0: See items in store\n1: Buy an item\n2: See my stats\n3: Leave store")
        user_input = input("Choice: ")
        if user_input == "0":
            # See the items in the store
            ___print_store_items()
        elif user_input == "1":
            user_input = input("Which item would you like to buy? ")

            try:
                if post_items[int(user_input)].cost <= int(player_money):
                    print("Thank you for purchasing this item!")
                    player_money -= post_items[int(user_input)].cost
                    player_inventory.append(post_items[int(user_input)])
                    del post_items[int(user_input)]
                    player_score += 10

                    ___print_store_items()
                else:
                    print("You do not have enough money for this item, you have", player_money)
            except (IndexError, TypeError) as err:
                print("Invalid input, try again")
                print(err)
        elif user_input == "2":
            _print_player_stats()
        elif user_input == "3":
            break
        else:
            print("Sorry, your input was not recognized")


def _item_generator(min, max):
    """A generator that generates random items
    min is the minimum cost
    max is the maximum cost, the general value of the items is determined based on the min and max values
    """
    item_cost = random.randint(min, max)
    balancer = 2 * item_cost / max
    if random.random() <= 0.35:
        # we'll give a random potion
        yield Item(get_rand_item_name() + " Potion", "", cost=item_cost, attack=0,
                health=int(random.randint(min, min + 10) * balancer), durability=1)
    else:
        yield Item(get_rand_item_name() + " Weapon", "", cost=item_cost,
                attack=int(random.randint(min, min + min // 2) * balancer), health=0,
                   durability=int(random.randint(max, max * 2) * balancer))


def get_rand_item_name():
    """A generator to get random names"""
    return str(item_attr_front[random.randint(0, len(item_attr_front) - 1)]) + " " + \
        str(item_attr_thing[random.randint(0, len(item_attr_thing) - 1)])


def _phil(st, length):
    filler = " " * (length - len(str(st)))
    return str(st) + filler


if __name__ == "__main__":
    console_game()
