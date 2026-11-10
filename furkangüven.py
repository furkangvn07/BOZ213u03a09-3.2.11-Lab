user_word = input("Enter a word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEİIOUÖÜ":  # Türkçe ve İngilizce sesli harfler
        continue
    print(letter)
