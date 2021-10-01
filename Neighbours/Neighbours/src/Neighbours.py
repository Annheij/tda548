import random
from typing import List
from enum import Enum, auto
import numpy
import pygame as pg
import time


#  Program to simulate segregation.
#  See : http:#nifty.stanford.edu/2014/mccown-schelling-model-segregation/
#

# Enumeration type for the Actors
class Actor(Enum):
    BLUE = auto()
    RED = auto()
    NONE = auto()  # NONE used for empty locations


# Enumeration type for the state of an Actor
class State(Enum):
    BLUE_UNSATISFIED = auto()
    RED_UNSATISFIED = auto()
    NA = auto()  # Not applicable (NA), used for NONEs


World = List[List[Actor]]  # Type alias


SIZE = 100


def neighbours():
    pg.init()
    model = NeighborsModel(SIZE)
    _view = NeighboursView(model)
    model.run()


class NeighborsModel:

    # Tune these numbers to test different distributions or update speeds
    FRAME_RATE = 1000            # Increase number to speed simulation up
    DIST = [0.25, 0.25, 0.50]  # % of RED, BLUE, and NONE
    THRESHOLD = 0.7            # % of surrounding neighbours that should be like me for satisfaction
    UNSATISFIED_COUNTER = 0
    # ########### These following two methods are what you're supposed to implement  ###########
    # In this method you should generate a new world
    # using randomization according to the given arguments.
    @staticmethod
    def __create_world(size) -> World:
        time_start = time.time()
        amount_of_red = [1]*(round(((size * size)-1) * NeighborsModel.DIST[0]))
        blue = [2]*(round(((size * size)-1)*NeighborsModel.DIST[1]))
        none = [3]*(round(((size * size)-1)*NeighborsModel.DIST[2]))
        generated_world = amount_of_red + blue + none
        for placement in range(0, len(generated_world)):
            if generated_world[int(placement)] == 1:
                generated_world[placement] = Actor.BLUE
            elif generated_world[int(placement)] == 2:
                generated_world[int(placement)] = Actor.RED
            else:
                generated_world[placement] = Actor.NONE
        random.shuffle(generated_world)
        brave_new_world = []
        for _ in range(size):
            brave_new_world.append(generated_world[0:size])
            del generated_world[0:size]
        print(time.time()-time_start)
        return brave_new_world

    # This is the method called by the timer to update the world
    # (i.e move unsatisfied) each "frame".
    def __update_world(self):
        self.UNSATISFIED_COUNTER = 0
        for row in range(0, len(self.world)):
            for col in range(0, len(self.world)):
                if self.world[row][col] != Actor.NONE:
                    list_of_neighbours = self.check_neighbors(row, col)
                    self.calculate_satisfaction(list_of_neighbours, row, col)
        self.move_world()

    def check_neighbors(self, row, col):
        list_of_neighbours = []
        for n_row in range(-1, 2):
            for n_col in range(-1, 2):
                if is_valid_location(len(self.world), n_row, n_col, row, col):
                    list_of_neighbours.append(self.world[row-n_row][col-n_col])
        return list_of_neighbours

    def move_world(self):
        list_to_place = []
        place_to_place = self.find_empty()
        for row in range(0, len(self.world)):
            for col in range(0, len(self.world)):
                if self.world[row][col] == State.BLUE_UNSATISFIED:
                    place_to_place.append([row, col])
                    list_to_place.append(Actor.BLUE)
                    self.world[row][col] = Actor.NONE
                    self.UNSATISFIED_COUNTER -= 1
                elif self.world[row][col] == State.RED_UNSATISFIED:
                    place_to_place.append([row, col])
                    list_to_place.append(Actor.RED)
                    self.world[row][col] = Actor.NONE
                    self.UNSATISFIED_COUNTER -= 1
        random.shuffle(list_to_place)
        random.shuffle(place_to_place)
        i = 0
        for place in list_to_place:
            self.world[place_to_place[i][0]][place_to_place[i][1]] = place
            i += 1

    def calculate_satisfaction(self, n_list, row, col):

        if self.world[row][col] == Actor.BLUE:
            good_neighbours = n_list.count(Actor.BLUE) + n_list.count(State.BLUE_UNSATISFIED)
            bad_neighbours = n_list.count(Actor.RED) + n_list.count(State.RED_UNSATISFIED)
            if good_neighbours + bad_neighbours == 0:
                self.world[row][col] = State.BLUE_UNSATISFIED
            elif good_neighbours / (good_neighbours + bad_neighbours) > self.THRESHOLD:
                self.world[row][col] = Actor.BLUE
            else:
                self.world[row][col] = State.BLUE_UNSATISFIED
        elif self.world[row][col] == Actor.RED:
            bad_neighbours = n_list.count(Actor.BLUE) + n_list.count(State.BLUE_UNSATISFIED)
            good_neighbours = n_list.count(Actor.RED) + n_list.count(State.RED_UNSATISFIED)
            if good_neighbours + bad_neighbours == 0:
                self.world[row][col] = State.RED_UNSATISFIED
            elif good_neighbours / (good_neighbours + bad_neighbours) > self.THRESHOLD:
                self.world[row][col] = Actor.RED
            else:
                self.world[row][col] = State.RED_UNSATISFIED
        elif self.world[row][col] == Actor.NONE:
            self.world = Actor.NONE


    def threshold_pick(self, row, col, blue, red, x):
        if self.world[row][col] == Actor.BLUE:
            satisfaction = int((blue / (blue + red)))
            return satisfaction
        elif self.world[row][col] == Actor.RED:
            satisfaction = int((red / (red + blue)))
            return satisfaction
        return 1

    def state_pick(self, row, col, x):
        if x == 1:
            return self.world[row][col]
        if self.world[row][col] == Actor.BLUE:
            return State.BLUE_UNSATISFIED
        elif self.world[row][col] == Actor.RED:
            return State.RED_UNSATISFIED

    def find_empty(self):
        empty_spaces = []
        for row in range(0, len(self.world)):
            for col in range(0, len(self.world)):
                if self.world[row][col] == Actor.NONE:
                    empty_spaces.append([row, col])
        return empty_spaces

    # ########### the rest of this class is already defined, to handle the simulation clock  ###########
    def __init__(self, size):
        self.world: World = self.__create_world(size)
        self.observers = []  # for enabling discoupled updating of the view, ignore

    def run(self):
        clock = pg.time.Clock()
        running = True
        while running:
            running = self.__on_clock_tick(clock)
        # stop running
        print("Goodbye!")
        pg.quit()

    def __on_clock_tick(self, clock):
        clock.tick(self.FRAME_RATE)  # update no faster than FRAME_RATE times per second
        self.__update_and_notify()
        return self.__check_for_exit()

    # What to do each frame
    def __update_and_notify(self):
        self.__update_world()
        self.__notify_all()

    @staticmethod
    def __check_for_exit() -> bool:
        keep_going = True
        for event in pg.event.get():
            # Did the user click the window close button?
            if event.type == pg.QUIT:
                keep_going = False
        return keep_going

    # Use an Observer pattern for views
    def add_observer(self, observer):
        self.observers.append(observer)

    def __notify_all(self):
        for observer in self.observers:
            observer.on_world_update()


# ---------------- Helper methods ---------------------

# Check if inside world
def is_valid_location(size: int, row: int, col: int, p_row: int, p_col: int):
    if p_row-row == p_row and p_col-col == col:
        return False
    else:
        return 0 <= p_row-row < size and 0 <= p_col-col < size


# ------- Testing -------------------------------------

# Here you run your tests i.e. call your logic methods
# to see that they really work
def test():
    # A small hard coded world for testing
    test_world = [
        [Actor.RED, Actor.RED, Actor.NONE],
        [Actor.NONE, Actor.BLUE, Actor.NONE],
        [Actor.RED, Actor.NONE, Actor.BLUE]
    ]

    th = 0.5  # Simpler threshold used for testing

    size = len(test_world)
    print(is_valid_location(size, 0, 0, 0, 0))
    print(not is_valid_location(size, -1, 0, 0, 0))
    print(not is_valid_location(size, 0, 3, 0, 0))
    print(is_valid_location(size, 2, 2, 0, 0))

    # TODO More tests

    exit(0)


# Helper method for testing
def count(a_list, to_find):
    the_count = 0
    for a in a_list:
        if a == to_find:
            the_count += 1
    return the_count


# ###########  NOTHING to do below this row, it's pygame display stuff  ###########
# ... but by all means have a look at it, it's fun!
class NeighboursView:
    # static class variables
    WIDTH = 800   # Size for window
    HEIGHT = 800
    MARGIN = 1

    WHITE = (255, 255, 255)
    RED   = (255,   0,   0)
    BLUE  = (  0,   0, 255)

    # Instance methods

    def __init__(self, model: NeighborsModel):
        pg.init()  # initialize pygame, in case not already done
        self.dot_size = self.__calculate_dot_size(len(model.world))
        self.screen = pg.display.set_mode([self.WIDTH, self.HEIGHT])
        self.model = model
        self.model.add_observer(self)

    def render_world(self):
        # # Render the state of the world to the screen
        self.__draw_background()
        self.__draw_all_actors()
        self.__update_screen()

    # Needed for observer pattern
    # What do we do every time we're told the model had been updated?
    def on_world_update(self):
        self.render_world()

    # private helper methods
    def __calculate_dot_size(self, size):
        return max((self.WIDTH - 2 * self.MARGIN) / size, 2)

    @staticmethod
    def __update_screen():
        pg.display.flip()

    def __draw_background(self):
        self.screen.fill(NeighboursView.WHITE)

    def __draw_all_actors(self):
        for row in range(len(self.model.world)):
            for col in range(len(self.model.world[row])):
                self.__draw_actor_at(col, row)

    def __draw_actor_at(self, col, row):
        color = self.__get_color(self.model.world[row][col])
        xy = self.__calculate_coordinates(col, row)
        pg.draw.circle(self.screen, color, xy, self.dot_size / 2)

    # This method showcases how to nicely emulate 'switch'-statements in python
    @staticmethod
    def __get_color(actor):
        return {
            Actor.RED: NeighboursView.RED,
            Actor.BLUE: NeighboursView.BLUE
        }.get(actor, NeighboursView.WHITE)

    def __calculate_coordinates(self, col, row):
        x = self.__calculate_coordinate(col)
        y = self.__calculate_coordinate(row)
        return x, y

    def __calculate_coordinate(self, offset):
        x: float = self.dot_size * offset + self.MARGIN
        return x


if __name__ == "__main__":
    neighbours()
