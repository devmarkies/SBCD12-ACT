#"The quick brown fox jumps over the lazy dog"
sentence = input("Enter a sentence:")
t1 = []
t2 = ""
for char in sentence:
    if char == " ":
        if t2:
            t1.append(t2)
            t2 = ""
    else:
        t2 += char
    
if t2:
    t1.append(t2)
print(t1)


