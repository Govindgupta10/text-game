# game.py

import random

# Character class
class Character:
    def _init_(self, name, health, skills):
        self.name = name
        self.health = health
        self.skills = skills
        self.inventory = []

    def _str_(self):
        return f"{self.name} (Health: {self.health}, Skills: {self.skills})"

# Story class
class Story:
    def _init_(self):
        self.story_path = []
        self.current_scene = 0

    def add_scene(self, scene):
        self.story_path.append(scene)

    def next_scene(self):
        self.current_scene += 1
        return self.story_path[self.current_scene]

    def previous_scene(self):
        self.current_scene -= 1
        return self.story_path[self.current_scene]

# Command class
class Command:
    def _init_(self, command, action):
        self.command = command
        self.action = action

    def execute(self, game):
        self.action(game)

# Game class
class Game:
    def _init_(self):
        self.character = Character("Player", 100, ["strength", "intelligence"])
        self.story = Story()
        self.commands = [
            Command("go", self.move),
            Command("take", self.take),
            Command("use", self.use),
            Command("inventory", self.show_inventory),
        ]

    def move(self, game):
        # Move to next scene
        scene = self.story.next_scene()
        print(scene)

    def take(self, game):
        # Take an item from the scene
        item = input("What do you want to take? ")
        self.character.inventory.append(item)
        print(f"You took {item}.")

    def use(self, game):
        # Use an item from inventory
        item = input("What do you want to use? ")
        if item in self.character.inventory:
            print(f"You used {item}.")
            self.character.inventory.remove(item)
        else:
            print("You don't have that item.")

    def show_inventory(self, game):
        # Show character's inventory
        print("Inventory:")
        for item in self.character.inventory:
            print(item)

    def play(self):
        print("Welcome to the game!")
        while True:
            command = input("> ")
            for cmd in self.commands:
                if command.startswith(cmd.command):
                    cmd.execute(self)
                    break
            else:
                print("Invalid command. Try again!")

# Create game instance and start playing
game = Game()
game.play()
