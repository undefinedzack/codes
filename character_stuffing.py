def char_stuffing(text,flag):
    knt = 0
    i = 0
    while i < len(text) :
        if text[i] == flag:
            text = text[:i] + flag + text[i:]
            i += 2
            knt += 1
        i += 1
    print('flag character\'s added: {}'.format(knt+2))
    return flag+text+flag

def char_destuffing(text,flag):
    knt = 0
    text = text[1:len(text)-1]  #removing starting and ending flag

    for i in range(len(text)-2):
        if text[i:i+2] == flag+flag :
            text = text[:i] + text[i+1:]
            knt += 1

    print('flag characters removed: {}'.format(knt+2))
    return text

if __name__ == '__main__':
    text = str(input("Enter text: "))
    flag = str(input("Enter flag: "))

    stuffed_text = char_stuffing(text, flag)
    print('Data after character stuffing: {}'.format(stuffed_text))

    destuffed_text = char_destuffing(stuffed_text, flag)
    print('Data after De Dtuffing: {}'.format(destuffed_text))



