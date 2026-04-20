a = input("Type the sentence: ").split()
word_count = { }

ignore  = ['the', 'is', 'and', 'a', 'an', 'was']

for word in a:
    word = word.lower()
    
    clean = ""
    
    for ch in word:
        if ch.isalpha():
            clean += ch
            
    if clean:
        if clean in word_count:
            word_count[clean] += 1
        else:
            word_count[clean] = 1
    
print(word_count)

