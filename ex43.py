from sys import exit
from random import randint


class Scene(object):

    ''' General scene information '''
    def enter(self):
        print "Scene not made. Exiting."
        exit(1)


class Engine(object):

    ''' Setting up game engine '''
    def __init__(self, scene_map):
        self.scene_map = scene_map

    ''' Defines pathway through self.play() '''
    def play(self):
        # Sets first scene as a blank scene to get the game started
        current_scene = self.scene_map.opening_scene()
        # Sets final scene as the scene mapped to end
        final_scene = self.scene_map.next_scene('end')

        # While loop to keep engine running so long as the current scene does
        # not match the final scene
        while current_scene != final_scene:
            # testing criteria only
            print "While-loop ran!"
            # After the scene runs, change the current scene to the next scene
            # after using the function self.enter() defined in the meta class
            next_scene_id = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_id)

        # enters the scene defined in the while loop
        current_scene.enter()
        
        
class Death(Scene):

    ''' Sets up quips to provide after death scenes '''
    deaths = {"1": "You died. That sucks. Game over.",
              "2": "Wow, that was impressive. Game over.",
              "3": "I tried to help you, but you wouldn't listen. Game over.",
              "4": "Wait... Nope, still dead. Game over.",
              "5": "Insert witty quip here. Game over.",
              "6": "Dude, try harder. Game over.",
              "7": "Ooh, that one had to hurt. Game over.",
              "8": "Why did the gamer cross the Styx? Game over.",
              "9": "So many yo mama jokes, but you have no time. Game over.",
              "10": "Infinity death. Game over."
              }

    ''' Redefines self.enter() as pulling from the quips at random '''
    def enter(self):
        # Gets a random number from 1 to 10, changes it to a string, and
        # returns the related quip
        print Death.deaths[str(randint(1, 10))]
        # game over
        exit(1)


class CentralCorridor(Scene):

    ''' Defines self.enter() with storyline for the central corridor '''
    def enter(self):
        # TODO: Write up starting story.
        print ("This is the starting point and has a Gothon already standing"
               " there they have to defeat with a joke before continuing."
               )
        answer = raw_input('> ')
        if answer == 'yes':
            return 'armory'
        else:
            return 'death'


class LaserWeaponArmory(Scene):

    ''' Defines self.enter() with storyline for the armory '''
    def enter(self):
        # TODO: Write up story.
        print ("This is where the hero gets a neutron bomb to blow up the ship"
               " before getting to the escape pod. It has a keypad the hero"
               " has to guess the number for."
               )
        answer = raw_input('> ')
        if answer == 'yes':
            return 'bridge'
        else:
            return 'death'


class TheBridge(Scene):

    ''' Defines self.enter() with storyline for the bridge '''
    def enter(self):
        # TODO: Write up story.
        print ("Another battle scene with a Gothon where the hero places the"
               " bomb."
               )
        answer = raw_input('> ')
        if answer == 'yes':
            return 'escape'
        else:
            return 'death'


class EscapePod(Scene):

    ''' Defines self.enter() with storyline for the escape pod '''
    def enter(self):
        # TODO: Write up story.
        print ("Where the hero escapes but only after guessing the right"
               " escape pod."
               )
        answer = raw_input('> ')
        if answer == 'yes':
            return 'end'
        else:
            return 'death'


class Ending(Scene):

    ''' Defines self.enter() with storyline for the winning scenario '''
    def enter(self):
        # TODO: Write up story.
        print "Winning scenario."
        exit()


class Map(object):

    ''' Maps the story '''
    setmap = {'central_corridor': CentralCorridor(),
              'armory': LaserWeaponArmory(),
              'bridge': TheBridge(),
              'escape': EscapePod(),
              'death': Death(),
              'end': Ending()
              }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        onward = Map.setmap.get(scene_name)
        return onward

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')  # instance of Map class
a_game = Engine(a_map)  # instance of Engine class
a_game.play()
