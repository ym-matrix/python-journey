numbers= "1, 4, 20,  52"

# strip()remove any trailing spaces and split() cuts the string at the commas 
cleannumbers=[int(num.strip()) for num in numbers.split(",")] 

print("cleanlist:",cleannumbers)

character=["Hello","I","am","Watt","Hello","I"]
#unique list to hold the unique values
unique_list=[] 

for char in character:
    if char not in unique_list:
#to add the unique characters in the end of the list 
        unique_list.append(char)

print("Unique list:",unique_list)