
def stringSwap(str):
    words = str.split(" ")
    tmp = words[-1]
    words[-1] = words[0]
    words[0] = tmp
    sentence = " ".join(words)
    return sentence

