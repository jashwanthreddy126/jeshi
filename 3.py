n=str(raw_input())
m=('a','e','i','o','u')
if n.isalpha():
     if n in m:
         print("vowel")
     else:
         print("Consonant")
else:
     print("invalid")
