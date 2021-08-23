mystring = input("Enter the string : ")


def most_frequent(string):
    x = dict()
    for key in string:
        if key not in x:
            x[key] = 1
        else:
            x[key] += 1
    return x


output = (most_frequent(mystring))
print(output)
