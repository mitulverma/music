# The PitchSpace class
# Represents generalized 12-pitchspace elements which can be chords.

import copy

class PitchSpace:

    def __init__(self, notes):
        '''
        notes is a list (set) with integers between 0 and 11 (inclusive).
        '''
        notes.sort()
        self.notes = notes
        
        self.rotations = 0
        self.flips = 0

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
        return self.notes == other.notes and self.rotations == other.rotations and self.flips == other.flips

    def __ne__(self, other):
        '''
        '''
        return not self == other


    def rotate(self, n=1):
        '''
        rotate clockwise by 30 degrees 
        transpose chord into key a half step higher
        can handle anti-clockwise rotations as well (enter negative n)
        '''
        n = n % 12
        for j in range(n):
            self.notes[:] = [(note + 1) % 12 for note in self.notes]
            self.rotations = (self.rotations + 1) % 12
        
        self.notes.sort() ## put notes in ascending order
        ## PRONE TO CONFLICT WITH "NORMAL" FORM

    def flip(self, n=0):
        '''
        flip about 0-6 (or any other) axis
        This musical operation is called "inversion"
        '''
        n = n % 12
        self.notes[:] = [(-note + n) % 12 for note in self.notes]
        self.flips = (self.flips + 1) % 2

        self.notes.sort()

    def range(self):
        '''
        '''
        return max(self.notes) - min(self.notes)

    def minimizeRange(self):
        '''
        FIXME: Please make this function less shitty. it is really shitty.
        thanks.
        '''
        copies = []

        if 0 in self.notes:
            orig = copy.deepcopy(self)
            copies.append(orig)

        for i in range(11):
            self.rotate()
            if 0 in self.notes:
                valid_copy = copy.deepcopy(self)
                copies.append(valid_copy)

        self.rotate()

        min_range = 12

        for item in copies:
            #print item, item.range()
            if item.range() < min_range:
                min_range = item.range()
                rotate_by = item.rotations

        self.rotate(rotate_by)



        
# Find out and code up normal, prime forms. chord equivalence classes,

# Write printInfo method


    # def __init__(self, orig=None, notes=[]):
    #     '''
    #     notes is a list (set) with integers between 0 and 11 (inclusive).
    #     '''
    #     if orig is None:
    #         self.defaultConstructor(notes)

    #     else:
    #         self.copyConstructor(orig)
        
    # def defaultConstructor(self, notes):
    #     '''
    #     '''
    #     notes.sort()
    #     self.notes = notes
        
    #     self.rotations = 0
    #     self.flips = 0


    # def copyConstructor(self, orig):
    #     '''
    #     '''
    #     self = copy.deepcopy(orig)