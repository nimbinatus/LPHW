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
            next_scene_id = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_id)

        current_scene.enter()
        
        
class Death(Scene):

    deaths = {"1": "You died. Game over.",
              "2": "You died 2. Game over.",
              "3": "You died 3. Game over.",
              "4": "You died 4. Game over.",
              "5": "5. Game over.",
              "6": "6. Game over.",
              "7": "7. Game over.",
              "8": "8. Game over.",
              "9": "9. Game over.",
              "10": "Infinity death. Game over."
              }

    def enter(self):
        print Death.deaths[str(randint(1, 10))]
        exit(1)


class CentralCorridor(Scene):

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

    def enter(self):
        # TODO: Write up story.
        print "Winning scenario."
        exit()


class Map(object):

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


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
