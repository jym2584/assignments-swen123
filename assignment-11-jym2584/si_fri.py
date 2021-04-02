class characters:
    __slots__ = ["name", "description", "health", "skills"]

    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.health = 100
        self.skills = ["Flee"]
0
char1 = characters("Patrick", "The best man")
char2 = characters("Bryce", "The best student")
char3 = characters("Prof. Herring", "The best professor")

def set_attributes():
    char1.health = 150
    char1.skills = ["Swear"]

    char2.skills.append("Study")
    char2.skills.append("Shoot") # Open to interpretations

    char3.health = 999999
    char3.skills.append("Fail")
    char3.skills.append("Teach")

def print_char(character):
    print("** ",character.name," **", "\n(", character.description, ")\n  Health: ", character.health, "\n  Skills:", character.skills, sep="")
    print()


set_attributes()

print_char(char1)
print_char(char2)
print_char(char3)