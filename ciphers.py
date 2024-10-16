# ----------------------Index Sub Cipher----------------------
def encryptIndexSubstitutionCipher(text):
    last = ''
    for t in text:
        x = int(ord(t)) - 96
        if x < 10:
            last += '0'
            last += str(x) + ' '
        else:
            last += str(x) + ' '
    last = last[0: len(last) - 1]
    return last

def decryptIndexSubstitutionCipher(text):
    last = ''
    out = ''
    for cur in text:
        if (cur == ' '):
            x = int(last)
            x += 96
            out += chr(x)
            last = ''
        elif (cur == '0'):
            last += ''
        else:
            last += cur
    out += chr(int(last) + 96)
    return out


# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}

def encryptMorseCode(text):
    pr = ""
    for i in text:
        t = i
        pr += morseCode[t]
        pr += ' '
    return pr

def decryptMorseCode(text):
    morse = {
        '._' : 'a',
        '_...':'b',
        '_._.' : 'c',
        '_..' : 'd',
        '.' : 'e',
        '.._.' : 'f',
        '__.' : 'g',
        '....' : 'h',
        '..' : 'i',
        '.___' : 'j',
        '_._' : 'k',
        '._..' : 'l',
        '__' : 'm',
        '_.' : 'n',
        '___' : 'o',
        '.__.' : 'p',
        '__._' : 'q',
        '._.' : 'r',
        '...' : 's',
        '_' : 't',
        '.._' : 'u',
        '..._' : 'v',
        '.__' : 'w',
        '_.._' : 'x',
        '_.__' : 'y',
        '__..' : 'z'
    }
    pr = ''
    t = ''
    for i in text:
        if i == ' ':
            pr += morse[t]
            t = ''
        else:
            t += i
    pr += morse[t]
    return pr



# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    l = ""
    for cur in text:
        x = int(ord(cur)) - 97
        y = (a * x + b) % 26
        l += chr(y + 97)
    return l

def decryptAffineCipher(text, a, b):
    l = ""
    for cur in text:
        x = int(ord(cur)) - 97
        y = int(pow(a, -1, 26) * (x - b)) % 26
        l += chr(y + 97)
    return l




# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    l = ''
    t = 0
    for cur in text:
        x = ord(cur)
        if (x < 65 or (x > 90 and x < 97) or x > 122) and (x < 48 or x > 57):
            t+=1
            l += cur
        elif x > 64 and x < 91:
            if(t % 2 == 0):
                t+=1
                k = key1 % 26
                i = ord(cur)
                if (i + k) < 91:
                    l += chr(i + k)
                else:
                    r = 91 - i
                    l += chr(65 + k - r)
            else:
                t+=1
                k = key2 % 26
                i = ord(cur)
                if (i + k) < 91:
                    l += chr(i + k)
                else:
                    r = 91 - i
                    l += chr(65 + k - r)
        elif x > 95 and x <123:
            if (t % 2 == 0):
                t += 1
                k = key1 % 26
                i = ord(cur)
                if (i + k) < 123:
                    l += chr(i + k)
                else:
                    r = 122 - i
                    l += chr(97 + k - r)
            else:
                t += 1
                k = key2 % 26
                i = ord(cur)
                if (i + k) < 123:
                    l += chr(i + k)
                else:
                    r = 122 - i
                    l += chr(97 + k - r)
        else:
            d = ord(cur)
            f = 0
            if t % 2 == 0:
                f = key1 % 10
            else:
                f = key2 % 10

            if d + f > 57:
                l += chr(48 + d + f - 57)
                t+=1
            else:
                l += chr(d + f)
                t+=1
    return l

def decryptCaesarCipher(text, key1, key2):
    l = ''
    t = 0
    for cur in text:
        x = ord(cur)
        if (x < 65 or (x > 90 and x < 97) or x > 122) and (x < 48 or x > 57):
            t += 1
            l += cur
        elif x > 64 and x < 91:
            if (t % 2 == 0):
                t += 1
                k = key1 % 26
                i = ord(cur)
                if (i - k) > 64:
                    l += chr(i - k)
                else:
                    r = i - 65
                    l += chr(91 - k + r)
            else:
                t += 1
                k = key2 % 26
                i = ord(cur)
                if (i - k) > 64:
                    l += chr(i - k)
                else:
                    r = i - 65
                    l += chr(91 - k + r)
        elif x > 95 and x < 123:
            if (t % 2 == 0):
                t += 1
                k = key1 % 26
                i = ord(cur)
                if (i - k) > 95:
                    l += chr(i - k)
                else:
                    r = i - 96
                    l += chr(123 - k + r)
            else:
                t += 1
                k = key2 % 26
                i = ord(cur)
                if (i - k) > 95:
                    l += chr(i - k)
                else:
                    r = i - 96
                    l += chr(123 - k + r)
        else:
            d = ord(cur)
            f = 0
            if t % 2 == 0:
                f = key1 % 10
            else:
                f = key2 % 10

            if d - f < 48:
                l += chr(-(48 + d + f - 57))
                t += 1
            else:
                l += chr(d - f)
                t += 1
    return l


# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    list = []
    n = 0
    temp = ""
    for i in text:
        if n == key:
            list.append(temp)
            temp = ""
            temp += i
            n = 1
        else:
            temp += i
            n += 1
    list.append(temp)
    out = ""
    for i in range(key):
        for st in list:
            str = st
            if len(str) < (i + 1):
                out += ""
            else:
                out += str[i:i + 1]
    return out

def decryptTranspositionCipher(text, key):
    n = 0
    list = []
    # x = int ( len(text) / key ) + len(text) % key
    t = int(len(text) / key) + 1
    for i in range(len(text) % key):
        list.append(text[i * t: (i + 1) * t])
    temp = ""
    y = 0
    for i in text:
        if y >= t * (len(text) % key):
            if n == int(len(text) / key):
                list.append(temp)
                temp = ""
                temp += i
                n = 1
            else:
                temp += i
                n += 1
        y += 1
    list.append(temp)

    out = ""
    ln = len(list[0])

    for i in range(ln):
        for st in list:
            str = st
            if len(str) < (i + 1):
                out += ""
            else:
                out += str[i:i + 1]
    return out
