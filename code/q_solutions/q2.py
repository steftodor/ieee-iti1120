# Remove the vowels from any given string s

string = "hippopotamus"
# hppptms

def removeVowels(s):
    vowels = 'aeiou'

    result = ""

    for i in s:
        if i not in vowels:
            result = result + i

    return result

print(removeVowels(string))