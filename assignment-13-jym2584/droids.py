PROTOCOL = "Procotol Droid"
ASTROMECH = "Astromech Droid"

PROTO_PARTS = ["p_head", "p_chassis", "p_left_arm", "p_right_arm", 
                "p_left_leg", "p_right_leg"]

ASTRO_PARTS = ["a_dome", "a_body", "a_left_leg", "a_center_leg",
                "a_right_leg"]

class Droid:
    __slots__ = ["__serial", "__droid_type", "__parts"]

    def __init__(self, serial, droid_type):
        self.__serial = serial
        self.__droid_type = droid_type
        self.__parts = dict()

        if droid_type == PROTOCOL:
            for part in PROTO_PARTS:
                self.__parts[part] = "missing"
        else:
            for part in ASTRO_PARTS:
                self.__parts[part] = "missing"

    def need_parts(self, a_part):
        if a_part in self.__parts:
            return self.__parts[a_part] == "missing"
        else:
            return False

    def install(self, a_part):
        if self.need_parts(a_part):
            self.__parts[a_part] = "installed"
        else:
            raise ValueError ("Part " + a_part + " not needed")

    def is_complete(self):
        for status in self.__parts.values():
            if status == "missing":
                return False
            else:
                return True
    
    def __repr__(self):
        string = ""
        string += str(self.__droid_type) + ":\n"
        string += "  serial number: " + str(self.__serial) + "\n"
        string += "  PARTS:" + "\n"
        for part in self.__parts:
            string += "    " + part + ": " + self.__parts[part] + "\n"
        return string

    def __str__(self):
        completed = "Unfinished"
        if self.is_complete():
            completed = "Assembled"
        string = self.__serial + " " + completed
        return string

if __name__ == "__main__":
    droid = Droid("R4-D2", ASTROMECH)
    print(droid)
    for part in ASTRO_PARTS:
        if droid.need_parts(part):
            droid.install(part)
    print(repr(droid))
    print(droid)
