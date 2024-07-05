text=input("enter a text:")
word_count=lambda text:len(text.split())
char_count=lambda text:len(text)
reverse_text=lambda text:text[::-1]
print("word count:",word_count(text))
print("character count:",char_count(text))
print("reversed text:",reverse_text(text))
