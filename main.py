import math
import random
import zlib

txt = open("exempeltext.txt").read()

print(len(txt))

byteArr = bytearray(txt, "UTF-8")

print(len(byteArr))


def makeHisto(data):
    history = [0] * 256
    for value in data:
        history[value] += 1
    return history


histo = makeHisto(byteArr)
print(histo)


# The string has 29091 symbols but the UTF-8 encoding makes some symbols take two bytes and there for the byteArr has 30390 bytes

def makeProb(data):
    probability = []
    total = sum(data)
    for value in data:
        probability.append(value / total)
    return probability


prob = makeProb(histo)
print(prob)


def entropi(data):
    entropy = 0
    for value in data:
        if value != 0:
            entropy += value * math.log2(1 / value)
    return entropy


entr = entropi(prob)
print(entr)

# entropy is 5.58 which means...  stuff goes here

theCopy = byteArr.copy()
random.shuffle(theCopy)

compressedShuffle = zlib.compress(theCopy)

print(len(compressedShuffle))

# The zipped array is 19663 bytes and 157304 bits long
# That's 12842 bytes smaller. The array is now 58% of its original size

compressed = zlib.compress(byteArr)

print(len(compressed))

# The zipped array is 12842 bytes and 102736 bits long
# That's 17548 bytes smaller. The array is now 42% of its original size

# Despite the entropy being the same between bytearray and the shuffled copy the rates of compression is different which indicates a memory source.
# E.G not only symbols are compressed but words and other patterns too.

t1 = """I hope this lab never ends because
it is so incredibly thrilling!"""
t10 = 10*t1

b1 = bytearray(t1, "UTF-8")
b10 = bytearray(t10, "UTF-8")

print(len(b1))
print(len(b10))

c1 = zlib.compress(b1)
c10 = zlib.compress(b10)

print(len(c1))
print(len(c10))

# t1 compressed to 68 from 65 (-3) and t10 to 78 from 650 (572)
# The reason the compressed t10 is not 10 times longer than t1 is because the repeating pattern was exploited as a source of compression.
