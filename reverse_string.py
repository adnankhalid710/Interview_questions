'''
str1 = 'I Love HK'
str2 = str1.split()
str3 = str2[::-1]
str4 =" ".join(str3)
print(str4)
'''

def Reverse_string(s1):
    s2 = s1.split()
    s3 = s2[::-1]
    s4 =" ".join(s3)
    return s4
str1 = 'I Love HongKong'
print(Reverse_string(str1))
