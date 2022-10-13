#wf1.py
import sys

freq = {}

for word in input("Enter string \n").split(" "):
    if word in freq:
        freq[word] = 1 + freq[word]
        
    else:
        freq[freq] = 1
        
print(freq)

#----
#wf2.py
import sys
freq = {}     
for word in input().split(" "):
    freq[word] = 1 + freq.get(word,0)
print (freq)

#----
#wf3.py
import sys

freq = {}

for word in input().split(" "):
        freq[word] = 1 + freq.get(word,0)
for w in sorted(freq.keys()):
    print(w,freq[w])

