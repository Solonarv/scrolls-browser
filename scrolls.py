# Library for dealing with scrolls

class Scroll(object):
    def __init__(self, id_, name, set_, type_, subtypes, rarity, cost, resource, attack, countdown, health, traits, ability, flavor):
        self.id = id_
        self.set = set_
        self.name = name
        self.type = type_
        self.subtypes = subtypes
        self.rarity = rarity
        self.cost = cost
        self.resource = resource
        self.attack = attack
        self.countdown = countdown
        self.health = health
        self.traits = traits
        self.ability = ability
        self.flavor = flavor
