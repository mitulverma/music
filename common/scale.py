# The scale class

from main import music

class Scale:

    def __init__(self, notes):
        """
        """
        if type(notes) == str:
            notes = music.convert(music.smash(notes))
        self.notes = notes

    def __repr__(self):
        """
        """
        return music.smoosh(music.numToAlpha(self.notes))
## Add all the other functionality
## complete this class dammit