#counting vowels


vowel=['a','e','i','o','u']
word='mohanraj'
count=0
for i in word:
    if i in vowel:
        count=count+1
print(count)


word='mohanraj'
cha='a'
count=0
for i in word:
    if i == cha:
        count=count+1
print(count)