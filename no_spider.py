class no_spider:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    
    def say_it(self):
        return f"The {self.name} says: {self.desc}"


sample =  no_spider("yam", "I am a yam")

print(sample.say_it())