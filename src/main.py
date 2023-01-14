from manager import *

def q1(turtle):

    passed_column = 0
    # ^ Total number of columns the turtle got out of.

    while passed_column < 1:
    # ^ Stops execution when the total number of columns passed is more than or equal to 2.

        if not is_facing_wall(turtle):
            fd(turtle, 30)
            fd(turtle, 30)
            passed_column += 1
        # ^ This is basically the code for getting out of the maze. It is supposed to be towards east direction. So,
        # it adds 1 to passed_column.

        else:
            lt(turtle, 90)
        # ^ If the turtle is not in front of the exit. This is the start of searching for an exit.

            if not is_facing_wall(turtle):
                fd(turtle, 30)
                rt(turtle, 90)
            # ^ Searching continues. This is a single step of searching.

            else:
                lt(turtle, 180)
            # ^ When the turtle reaches most north or south, it has to turn back.

                while passed_column < 1:
                # ^ This part is like a copy of the code above. It is meant to move the turtle towards the opposite
                # direction, though.

                    if not is_facing_wall(turtle):
                        fd(turtle, 30)
                        lt(turtle, 90)

                        if not is_facing_wall(turtle):
                            fd(turtle, 30)
                            fd(turtle, 30)
                            passed_column += 1

                        else:
                            rt(turtle, 90)

                    else:
                        break
                    # ^ I guess turtle is in a box here. Or the exit is on the left wall. This part of the code
                    # will never be used in normal conditions.

# ————————————————————————————————————————————————————————————————————————————————————————————————————

def q2(turtle, no_of_columns):

    while no_of_columns > 0:
    # ^ Stops the execution when no_of_columns decreases to 0. It is for repeating the movement done for getting out
    # of a column of the maze no_of_columns times.

        if not is_facing_wall(turtle):
            fd(turtle, 30)
            fd(turtle, 30)
            no_of_columns -= 1
        # ^ The code for getting out of a single column. Each column exited, decreases no_of_columns by 1.

        else:
            lt(turtle, 90)
        # ^ The start of searching for an exit.

            if not is_facing_wall(turtle):
                fd(turtle, 30)
                rt(turtle, 90)
            # ^ Searching.

            else:
                lt(turtle, 180)  # < The turtle is at the most north or south of the column. It turns back.
                while no_of_columns > 0:
                # ^ Almost the same code above but towards the opposite direction.

                    if not is_facing_wall(turtle):
                        fd(turtle, 30)
                        lt(turtle, 90)

                        if not is_facing_wall(turtle):
                            fd(turtle, 30)
                            fd(turtle, 30)
                            no_of_columns -= 1

                        else:
                            rt(turtle, 90)

                    else:
                        break
                    # ^ The turtle is in a box or the exit is on the left wall.

# ————————————————————————————————————————————————————————————————————————————————————————————————————

def q3(turtle, max_treasure_count):

    total_vertical = 0  # < Total movement on the vertical line. Resets when turtle vertically turns back.
    collected_treasure = 0  # < Total treasure collected by the turtle.

    lt(turtle, 90)
    # ^ In order to start to search for treasures along a column, the turtle has to be positioned vertically at the
    # beginning.

    while total_vertical < 3:
    # ^ Stops execution when the turtle moves 3 times without turning back. That means it moved all along the column.
    # This is a key factor for q3. If the maze's vertical length changes, this whole code will not work.

        if not is_facing_wall(turtle):  # The turtle moves along the column. Each move increases the total_vertical.
            fd(turtle, 30)
            total_vertical += 1

            if is_over_treasure(turtle):
                pick_treasure(turtle)
                collected_treasure += 1
            # ^ The code for noticing and collecting treasures. Each treasure collected, increases collected_treasure
            # by 1.

                if collected_treasure == max_treasure_count:
                    break
                # ^ If the turtle reaches the maximum treasure it can carry, which is given as an input by the user,
                # it immediately stops.

        else:
            lt(turtle, 180)
            total_vertical = 0
            # ^ If the turtle moved vertically but there is/are still block(s) it didn't check for treasures, it has
            # to turn back and move all along the column.

    if collected_treasure < max_treasure_count:
        lt(turtle, 90)
        q1(turtle)  # < q1 is just enough for the turtle to get out of the maze. It's almost the same maze anyway.
    # ^ If the turtle didn't reach the maximum treasure it can carry, it should get out of the maze. If it did, it
    # must stop. This piece of code will not work if it collected treasures as many as the limit.

    return collected_treasure
    # ^ This command returns the number of collected treasures as a value to this function. Thus, it is printed
    # afterwards.

# ————————————————————————————————————————————————————————————————————————————————————————————————————

def q4(turtle, max_treasure_count, no_of_columns):

    collected_treasure = 0  # < Total number of treasures collected by the turtle.
    total_south = 0  # < Total movement towards the south direction.

    for all_columns in range(no_of_columns, 0, -1):
    # ^ The loop for repeating the whole function no_of_columns times.


        # MOVING TO NORTH

        if collected_treasure < max_treasure_count:
        # ^ Prevents the turtle from turning around itself a few times after reaching the treasure carry limit.

            lt(turtle, 90)
            # ^ In order to start to search for treasures along a column, the turtle has to be positioned vertically
            # at the beginning.

            while collected_treasure < max_treasure_count:
            # ^ This loop is actually for the turtle to reach the most north wall of the current column. The turtle
            # shouldn't move after it reached the maximum treasure number, though.

                if is_over_treasure(turtle):
                    pick_treasure(turtle)
                    collected_treasure += 1
                # ^ The turtle notices that it is on a treasure and collects it. collected_treasure increases by one
                # for each treasure collected. It is placed before as many things as possible to prevent the turtle
                # from doing things, like turning around itself, after collecting the last treasure.

                    if collected_treasure == max_treasure_count:
                        break
                    # ^ When the turtle reached the maximum number of treasure it can carry, it immediately stops.

                else:
                    if not is_facing_wall(turtle):
                        fd(turtle, 30)
                # ^ If the turtle is not over a treasure, and if it didn't reach the treasure carry limit, it should
                # start or continue searching.

                    else:
                        if is_over_treasure(turtle):
                            pick_treasure(turtle)
                            collected_treasure += 1
                        # ^ Treasure collecting before all because of the same reason above.
                    # ^ In searching part, if the turtle isn't facing a wall.

                            if collected_treasure == max_treasure_count:
                                break
                            # ^ If the turtle reaches maximum treasure number, it must stop.

                        else:
                            lt(turtle, 180)
                            break
                        # ^ When the turtle reaches the most north wall, it should turn back and finish this loop.


            # MOVING TO SOUTH

            while total_south < 4 and collected_treasure < max_treasure_count:
                if is_over_treasure(turtle):
                    pick_treasure(turtle)
                    collected_treasure += 1
                # ^ Always starts with collecting treasures. ^ This loop is for the turtle to go to the most south
                # wall. It should stop as soon as it vertically moved 4 times. If it reached the maximum treasure
                # number, this loop will not start at all. This is a key code for q4. If the vertical length of the
                # maze changes, it will not work.

                else:
                    fd(turtle, 30)
                # ^ When the turtle is not on a treasure, it will start to search for one.

                    if is_over_treasure(turtle):
                        pick_treasure(turtle)
                        collected_treasure += 1
                        total_south += 1
                    # ^ Picking treasures. total_south increase is split to this if-else instead of being placed
                    # above (after fd(turtle, 30)) in order to prevent the turtle from stopping before collecting the
                    # treasures it ought to collect.

                    else:
                        total_south += 1

            total_south = 0
            # ^ total_south is reset after every column in order it to be able to execute after that column too.


        # EXITING A SINGLE COLUMN

        if collected_treasure < max_treasure_count:
        # ^ Prevents the turtle from turning around itself a few times after reaching the treasure carry limit.

            total_east = 0
            # ^ Total movement towards east direction.

            lt(turtle, 90)

            while total_east < 2 and collected_treasure < max_treasure_count:
            # ^ The turtle shouldn't exit the column when it reached the maximum treasure carry limit. And it should
            # stop when it got out of a single column.

                if not is_facing_wall(turtle):
                    fd(turtle, 30)
                    fd(turtle, 30)
                    total_east += 2
                # ^ This piece of code makes the turtle exit a single column.

                else:
                    lt(turtle, 90)
                    fd(turtle, 30)
                    rt(turtle, 90)
                # ^ This piece of code helps the turtle to search for the exit.

            total_east = 0
            # ^ total_east resets after every column.

    return collected_treasure
    # ^ Returns collected_treasure as a number to this function in order to print it afterwards.

# ————————————————————————————————————————————————————————————————————————————————————————————————————
# This piece of code code was written by Hasan Tarık Yumbul until here.
# Student Number: 219171247
# ————————————————————————————————————————————————————————————————————————————————————————————————————

manager = WorldManager()
is_facing_wall = manager.is_facing_wall
is_over_treasure = manager.is_over_treasure
pick_treasure = manager.pick_treasure

if __name__ == '__main__':

    print(40 * "*" + " Welcome " + 40 * "*" + "\n")
    delay = 0.4

    while True:
        world = TurtleWorld()
        world.geometry("600x400")
        for i in range(1, 5):
            print(i, "-", "Question", i)
        print(0, "-", "Exit")
        choice = int(input("Choose Question Number: "))
        if choice == 1:
            manager.read_world("maze1.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            q1(bob)
            wait_for_user()
        elif choice == 2:
            no_of_columns = int(input(
                "Enter the number of columns your maze will have: "))
            manager.read_world("maze2.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            q2(bob, no_of_columns)
            wait_for_user()
        elif choice == 3:
            max_treasure_count = int(input(
                "Enter the maximum number of treasures the turtle can pick up: "))
            manager.read_world("maze3.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            print("# of treasures collected:" + str(q3(bob, max_treasure_count)))
            wait_for_user()
        elif choice == 4:
            no_of_columns = int(input(
                "Enter the number of columns your maze will have: "))
            max_treasure_count = int(input(
                "Enter the maximum number of treasures the turtle can pick up: "))
            manager.read_world("maze4.txt")
            spx, spy, s = manager.spx, manager.spy, manager.s
            bob = manager.turtles[0]
            bob.set_delay(delay)
            print("# of treasures collected:" + str(
                q4(bob, max_treasure_count, no_of_columns)))
            wait_for_user()
        elif choice == 0:
            exit()
