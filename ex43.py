from sys import exit
from random import randint

class Scene(object):
    
    def enter(self):
        print "Scene not made. Exiting."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        final_scene = self.scene_map.next_scene('end')

        while current_scene != final_scene:
            print "While-loop ran!"
            next_scene_ID = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_ID)

        #TODO: No idea why this one isn't working at the end.
        current_scene.enter()
        
        
class Death(Scene):

    def enter(self):
        print "You died. Game over."
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print ("You are the last person left alive after the Gothons from"
               " Planet Percal #25 have overtaken your ship. You have been on"
               " the run since your captain sent out a shipwide call early in"
               " your shift. To prevent your ship from falling into Gothon "
               "control, you need to get to the armory to get a neutron bomb to"
               " set off. This is the starting point and has a Gothon already "
               "standing there they have to defeat with a joke before continuing."
        )
        answer = raw_input('> ')
        if answer == 'yes':
            return 'armory'
        else:
            return 'death'


class LaserWeaponArmory(Scene):

    def enter(self):
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

    def enter(self):
        print ("Another battle scene with a Gothon where the hero places the"
               " bomb."
        )
        answer = raw_input('> ')
        if answer == 'yes':
            return 'escape'
        else:
            return 'death'


class EscapePod(Scene):

    def enter(self):
        print ("Where the hero escapes but only after guessing the right"
               " escape pod."
        )
        answer = raw_input('> ')
        if answer == 'yes':
            return 'end'
        else:
            return 'death'

class Map(object):


    setmap = { 'central_corridor' : CentralCorridor(),
               'armory' : LaserWeaponArmory(),
               'bridge' : TheBridge(),
               'escape' : EscapePod(),
               'death' : Death(),
               'end' : 'You win!'
    }


    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        onward = Map.setmap.get(scene_name)
        return onward

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
