import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase

# create all upper and lowercase combinations
combinations = []
for i in range(len(upper)):
    combinations.append(lower[i]+upper[i])
    combinations.append(upper[i]+lower[i])

def reduce_string(string):
    old = ''
    while old != string:
        old = string
        for sub in combinations:
            string = string.replace(sub, '')
    return string

# string = 'dabAcCaCBAcCcaDA'  # test string
with open('./input05.txt') as infile:
    string = infile.read().splitlines()[0]
original = string

string = reduce_string(string)

# Part I:
print(len(string))

## Part II
best_len = len(original)
for i in range(len(upper)):
    # preprocess the string by removing all ls/us
    string = original
    string = string.replace(lower[i], '')
    string = string.replace(upper[i], '')

    string = reduce_string(string)
    if len(string) < best_len:
        best_len = len(string)

print(best_len)
