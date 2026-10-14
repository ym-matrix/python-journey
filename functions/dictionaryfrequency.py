str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for achar in str1:
    if achar not in freq:
        freq[achar]=0
    freq[achar]+=1
print(freq)