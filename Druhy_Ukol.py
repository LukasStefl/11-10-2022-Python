string = "Python is a high-level, general-purpose programming language. Python is dynamically-typed and garbage-collected."
word = "Python"
words = string.split()
count = 0
for w in words:
   if w == word:
      count += 1
print(count)