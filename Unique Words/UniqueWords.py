text="This is a simple text This is used  to demonstrate the counting of unique words."
words=text.split()
unique_words=set(words)
count=len(unique_words)
print("Number of unique words:",count)
