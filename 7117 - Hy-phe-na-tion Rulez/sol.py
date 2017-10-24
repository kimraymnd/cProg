from sys import stdin, stdout
import itertools


def main():

    vowel = {"a","e","i","o","u","y"}
    nope = {"qu", "tr", "br", "str", "st", "sl", "bl", "cr", "ph", "ch"}
    cons = set()
    for i in range(26):
        if chr(65+i).lower() not in vowel:
            cons.add(chr(65+i).lower())

    for phrase in stdin:
        if phrase.strip() == "===": return 0
        words = phrase.split()
        for x in words:
            n = len(x)
            i = 0
            count = 0
            offset = 0
            while(i<n):
                # print(i, x[:i+1], end=' ')
                if count==0:
                    if x[i].lower() in vowel:
                        count = 1
                elif count == 1:
                    if x[i].lower() in vowel: count = 1
                    elif x[i:i+2].lower() in nope:
                        offset += 1
                        count += 1
                        i += 1
                    elif x[i].lower() in cons: count += 1
                elif count == 2:
                    if x[i].lower() in vowel:
                        if x[i] == 'e' and i == n-1:
                            break
                        x = x[:i-1-offset]+"-"+x[i-1-offset:]
                        n = len(x)
                        i += 0
                        count = 1
                        offset = 0
                    elif x[i:i+2].lower() in nope:
                        offset += 1
                        count += 1
                        i += 1
                    elif x[i].lower() in cons: count += 1
                elif count == 3:
                    if x[i].lower() in vowel:
                        x = x[:i-1-offset]+"-"+x[i-1-offset:]
                        n = len(x)
                        i += 1
                        count = 1
                    else:
                        count = 0
                # print(count)
                i += 1
            stdout.write("%s\n"%x)

if __name__=="__main__":
    main()
