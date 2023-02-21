def stringSwap(str):
    words = str.split(" ")
    tmp = words[-1]
    words[-1] = words[0]
    words[0] = tmp
    sentence = " ".join(words)
    return sentence


def len_joke():
    joke = get_joke()
    return len(joke)

def get_joke():
    return "This is a joke haha"
