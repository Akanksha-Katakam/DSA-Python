def vowels_consonants(str):
    vowels=""
    consonants=""
    for i in str:
        if i in 'aeiouAEIOU':
            vowels+=i
        else:
            consonants+=i
    return vowels,consonants
str=input()
vowels,consonants=vowels_consonants(str)
print("vowels : ",vowels)
print("consonants : ",consonants)