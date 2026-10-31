def test(num, condition=True, dict1={2: 3, 4: 5, 6: 8}):
    if condition:
        if num in dict1:
            return dict1[num]
    else:
        return False
print(test(4))