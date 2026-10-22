###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

# Count vowels in the text
ktora = 0
while ktora < len(text):
    char = text[ktora]
#for char in text:
    if char in vowels:
        vowel_count += 1
    ktora += 1

print(f"The number of vowels in the text is: {vowel_count}")
