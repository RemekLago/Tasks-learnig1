sentence = "ABC for the purpose of LetterCounting program"
print(sentence)

words = 1
letters = 0
hash_table = {}

for x in sentence:
    x = x.lower() # downgrade all characters to string
    if x == " ":
        words +=1
    else:
        letters +=1
        if x in hash_table:
            hash_table[x] +=1
        else:
            hash_table[x] =1

print ("Words:", words)
print("Letters:", letters )
print ("Frequency:", hash_table)