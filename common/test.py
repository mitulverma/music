# test file
from pitchspace import PitchSpace

c = PitchSpace([0,4,7,10])
print c

print len(c)

# for i in range(12):
#     c.rotate()
#     print c

c.flip()
print c


c.rotate(7)
print c
