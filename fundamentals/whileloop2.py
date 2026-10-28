def beginning(str):
    sublist=[]
    idx=0
    while idx<10 and str[idx]!='bye':
        sublist.append(str[idx])
        idx+=1
    return sublist
print(beginning(['Hi','My','Name','Is','Jack','Sparow','What','Do','you','want','that','i','have','bye']))