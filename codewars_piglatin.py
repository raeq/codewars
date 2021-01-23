import string


print(string.punctuation)


def pig_it(text):
    if not text.strip():
        return None

    returnstr = ""

    for word in text.split():
        if word[-1:] in string.punctuation:
            if len(word) == 1:
                returnstr += word[1:-1] + add_ay(word[0])
            else:
                returnstr += word[1:-1] + add_ay(word[0]) + word[-1]
        else:
            returnstr += word[1:] + add_ay(word[0])
        returnstr += " "
    print(returnstr)
    return returnstr.rstrip()


def add_ay(w):
    if w.strip():
        if not w in string.punctuation:
            return w + "ay"
    return w


assert (pig_it('Quis custodiet ipsos custodes ?') == 'uisQay ustodietcay psosiay ustodescay ?')
assert (pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay')
assert (pig_it('This is my string.') == 'hisTay siay ymay tringsay.')
assert (pig_it('O tempora o mores !') == 'Oay emporatay oay oresmay !')
assert (pig_it('Quis custodiet ipsos custodes ?') == 'uisQay ustodietcay psosiay ustodescay ?')
