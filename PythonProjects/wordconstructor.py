""" Solution 1
def canConstruct(fro: str, to: str) -> bool:
    for c in fro:
        res = to.find(c)

        # if we found the letter in the 'to' string,
        # remove the letter from the to variable
        if res != -1:
            to = to.replace(to[res], '', 1)

            if to.__len__() == 0:
                return True

    return False
            
"""

def canConstruct(fro: str, to: str) -> bool:
    for c in to:
        if c not in fro:
            return False
        fro = fro.replace(c, '', 1)
    return True

    

print(canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))