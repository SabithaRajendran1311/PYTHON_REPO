import random
lower="abcdefghijklmnopqrstuvewxyz"
upper="ABCDEFGHIJKLMNOPQRTUVWXYZ"
numbers="1234567890"
symbols="!@#$%^&*()_+=<>"
all_chars=lower+upper+numbers+symbols
length=int(input("enter a lengeth:"))
password=''.join (random.sample(all_chars,length))
print("generated password:",password)
