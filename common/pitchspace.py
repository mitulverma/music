# The PitchSpace class
# Represents generalized 12-pitchspace elements which can be chords.

class PitchSpace:

    def __init__(self, notes):
        '''
        notes is a list (set) with integers between 0 and 11 (inclusive).
        '''
        notes.sort()
        self.notes = notes

    def __repr__(self):
        '''
        '''

        clock = ["      .\n", 
                 "   .\n", 
                 "     .\n", 
                 "      .\n", 
                 "     .\n", 
                 "   .\n", 
                 "      . ", 
                 "   .  ", 
                 " .    ", 
                 ".     ", 
                 " .    ", 
                 "   .  "]

        for note in self.notes:
            new_string = ""
            for c in clock[note]:
                if c == ".":
                    if note == 10:
                        new_string += 'a'
                    elif note == 11:
                        new_string += 'b'
                    else:
                        new_string += str(note)
                else:
                    new_string += c
            clock[note] = new_string

        new_clock = clock[0]
        for i in range(1,6):
            new_clock += clock[-i] + clock[i]
        new_clock += clock[6]

        return new_clock

    def __len__(self):
        '''
        '''
        return len(self.notes)


    def __eq__(self, other):
        '''
        '''
        return self.notes == other.notes

    def __ne__(self, other):
        '''
        '''
        return self.notes != other.notes


    def rotate(self, n=1):
        '''
        rotate clockwise by 30 degrees 
        transpose chord into key one half step higher
        can handle anti-clockwise rotations as well (enter negative n)
        '''
        n = n%12
        for j in range(n):
            for i in range(len(self.notes)):
                self.notes[i] = (self.notes[i] + 1) % 12

    def flip(self, n=0):
        '''
        flip about 0-6 (or any other) axis
        This musical operation is called "inversion"
        '''
        n = n%12
        for i in range(len(self.notes)):
            self.notes[i] = (-self.notes[i] + n) % 12

    # def normalize(self):
    #     '''
    #     '''
    #     min_diff = 12
    #     current_diff = max(self.notes) - min(self.notes)

    #     while 0 not in self.notes:
    #         self.rotate()
            


# Find out and code up normal, prime forms. chord equivalence classes,