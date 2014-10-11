# Each note has a value. S = 0, r = 1, R = 2 etc stored in dictionaries
# Functions will work with scales, used as lists. smash and smoosh will allow me to use strings

import math

notevalue = {'S':0, 'r':1, 'R':2, 'g':3, 'G':4, 'm':5, 'M':6, 'P':7, 'd':8, 'D':9, 'n':10, 'N':11}
valuenote = {0:'S', 1:'r', 2:'R', 3:'g', 4:'G', 5:'m', 6:'M', 7:'P', 8:'d', 9:'D', 10:'n', 11:'N'}

chordid = {"SGP":"maj", "SgP":"min", "SgM":"dim", "SGd":"aug", "SRP":"sus2", "SmP":"sus4"}

def convert(scale):
    '''Converts from note to numeric code and back'''
    result = []
    if type(scale[0]) is str:
        for s in scale:
            t = notevalue[s]
            result.append(t)
    else:
        for i in scale:
            j = valuenote[i]
            result.append(j)
    return result

def spitscale(root, start):
    '''Gives the output scale from input location on input scale'''
    diff = notevalue[start]
    for n in root:
        if n == start:
            newScale = root
        else:
            reject = root[0]
            root = root[1:]
            root.append(reject)
    
    newNum = convert(newScale)
    newNum[:] = [(x-diff)%12 for x in newNum] # Normalizing the new scale
    output = convert(newNum)
    return output
        
def smash(s):
    '''Converts a string input to a list'''
    L = []
    for i in range(len(s)):
        L.append(s[i])
    return L

def smoosh(L):
    '''Converts a list input to a string'''
    s = ''
    for i in L:
        s+=i
    return s

def freqscale(scale, freq):
    '''Converts the sargam scale to a frequency scale'''
    output = []
    for n in scale:
        note = freq * math.pow(2, (notevalue[n]/12.0))
        output.append(note)
    output.append(freq*2)
    return output

def getthaatspace(scale):
    '''Gets the thaatspace/raagspace of the input scale'''
    ts = [scale]
    s1 = scale
    s2 = []
    while s2!=scale:
        s2=spitscale(s1, s1[1])
        s1=s2
        ts.append(s1)
    return ts

def chord(scale):
    '''Returns the 1-3-5 chord of the input scale'''
    otf = smoosh(scale[0] + scale[2] + scale[4])
    if otf in chordid:
        return chordid[smoosh(otf)] # Use when all possible chords are identified in dict
    else:
        return smoosh(otf)
    

def chord7(scale):
    '''Returns the 1-3-5 plus 3-5-7 of the input scale'''
    otf = chord(scale)
   # print(otf)
    tfs = chord(spitscale(scale, scale[2]))
    return otf + ' ' + '+' + ' ' + tfs

def majorscale(start):
    '''Start on any note of the bansuri and get major scale'''
    startval = notevalue[start]
    valscale = [startval, startval+2, startval+4, startval+5, startval+7, startval+9, startval+11]
    output = []
    for n in valscale:
        p = n % 12
        q = valuenote[p]
        output.append(q)
    return output

#if __name__ == "__main__":


