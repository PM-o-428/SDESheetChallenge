# Solution - 1
# Problem Link - https://www.codingninjas.com/codestudio/problems/decode-string_696319?topList=top-string-coding-interview-questions&leftPanelTab=0
# Challege Start Date - 04.06.2022
# Date - 17.08.2022
# Day 72
def decodeString(s):

    # Write your code here.
    numStack = []
    strStack = []
    k = ''
    seq = ''
    for c in s:
        if c.isdigit():
            if seq: # string that need to be muitplied with other string
                strStack.append(seq)
                seq = ''
            k += c
        elif c == '[':
            numStack.append(int(k))
            strStack.append('[') # must put '[' in stack to know when to stop popping
            k = ''
        elif c == ']':
            while True: # pop until met the corresponding '['
                elem = strStack.pop()
                if elem == '[':
                    break
                seq = elem + seq
            seq *= numStack.pop()
            strStack.append(seq)
            seq = ''
        else:
            seq += c
    result = ''
    while len(strStack) != 0:
        result = strStack.pop() + result

    return result + seq

s = 'ab2[c3[b]]'
print(decodeString(s))