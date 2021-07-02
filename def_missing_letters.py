l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def missing_letter(s):
    for letter in s:
            if not  l[(l.index(letter))+1] == s[(s.index(letter))+1]:
                return print(l[(l.index(letter))+1])
s1 =['d','e','f','h','i']
s2 =['H','I','J','L','M']                
missing_letter(s1)
missing_letter(s2)
                