# test file
from pitchspace import PitchSpace

c = PitchSpace([0,4,7])
print c

# for i in range(12):
#     c.rotate()
#     print c

c.flip()
print c


print "\n ------------------------------------------- \n"

c.minimizeRange()

print c
print c.flips
print c.rotations