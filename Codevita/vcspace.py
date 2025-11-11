def vowel_conso_spaces(s):
    low = s.lower()
    v = ['a','e','i','o','u']
    Vowels = 0
    Consonants = 0
    White_spaces = 0
    for i in low:
        if i == " ":
            White_spaces += 1
        elif i in v:
            Vowels += 1
        else:
            Consonants += 1
    print("Vowels:",Vowels)
    print("Consonants:",Consonants)
    print("White spaces:",White_spaces)

s = input()
vowel_conso_spaces(s)