'''word=raw_input("Enter Full Name with space")

for char in range(len(word) - 1, -1, -1):


  print(word[char])
print("\n")
'''

def reverse(s):
  str = ""
  for i in s:
   # print(i)
    str = i+" "+ str
    #print(str)
  return str

print("Hello World")
fval = raw_input("Enter your fname: ")
lval = raw_input("Enter your lname: ")

print("----------------------------------------")
print("reverse " + reverse(fval+lval))

