# This program is for reverse given string 
# This program is also generate Palindrome word.
# Palindrome is a word which have the same equence of character from both side (left to right and right to left are same)
#from audioop import reverse
def reverse_str(str1):
    str2 = list(str1)
    str3 = str2[::-1]
    str4 = "".join(str3)  
    return str4

def palnidrom(str1):
    str2 = list(str1)
    del str2[0]
    str3 = "".join(str2)
    return str3
str11 = "google"
str4 = reverse_str(str11)
#print(f"Original word is :{str11}")
print("Original word is :{:>20} and".format(str11))    # {:>20} its padding here
#print(f"After reverse it :{str4}")
print("After reverse it :{:20} and".format(str4))
#exit()
str5 = palnidrom(str11)
print(str5)

str6 = str4+str5
print(f"After palindom it :{str6}")
'''
st1 = 'muhammad'                           
st2 = 'adnan'
st3 = st1 + st2
print(st3)
'''