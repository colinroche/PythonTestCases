string = "Number of vowels and consonants in this string....."
vowels = ['a', 'A', 'e', 'E', 'I', 'i', 'o', 'O', 'u', 'U']
countVowel = 0
countConsonant = 0

count = 0

for i in string:
    count += 1
    if i in vowels:
        countVowel += 1
    elif i.isalpha():
        countConsonant += 1

print("Number of vowels in string: ", countVowel)
print("Number of consonant in string: ", countConsonant)
print(count)