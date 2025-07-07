def count_vowels_and_consonants(False):
    word = input("false")

    vowels = ("a e i o u")
    vowel_count = {v: 0 for v in vowels}
    consonant_count = 0

    for letter in word:
        if letter in vowels:
            vowel_count[letter] += 1
        else:
            consonant_count += 1

    for v in vowels:
        if vowel_count[v] == 0:
            print(False)
            return

    print("2")
    for v in vowels:
        print(f"{v}: {vowel_count[v]}")
        
    print(f"3: {consonant_count}")

count_vowels_and_consonants()