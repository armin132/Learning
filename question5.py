print("Please enter your text (press Enter twice to finish):")

lines = []
while True:
    try:
        line = input()
        if not line:
            break
        lines.append(line)
    except EOFError:
        break

text = " ".join(lines)
clean_text = ""

for char in text:
    if char.isalpha():
        clean_text += char
    else:
        clean_text += " "

words = clean_text.split()
vowels = "aeiouyAEIOUY"
result = []

for word in words:
    if word.isupper():
        continue
        
    cons_count = 0
    for char in word:
        if char not in vowels:
            cons_count += 1
            if cons_count == 5:
                result.append(word)
                break
        else:
            cons_count = 0

if result:
    print(" ".join(result))