x = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]

n = []

for i in x :
    if i not in n:
        n.append(i)

print(n)

s1 = [5,6,7,3,76,45,45,6,7,9]
s2 = s1[2]
s3 = s1.count(7)
s4 = s1.sort()
s5 = s1.sort(reverse=True)
print(s2)
print(s3)
print(s4)
print(s5)

new_list = [1,2,3,4,'a','b','c','a','b','c',1,2,3,4]

new = []
let = []
for i in new_list:
    if str(i).isdigit():
        if int(i) not in new:
            new.append(int(i))
    elif str(i).isalpha():
        if i not in let:
         let.append(i)

print(new)
print(let)

# input abcabc #output abc like given a string need to find substring length and substring

n= 'abcabc'
another = set()
left = 0
max_length = 0
for right in range(len(n)):
    while n[right] in another:
        another.remove(n[left])
        left +=1
    another.add(n[right])
    if max_length < right -left+1:
        max_length = right-left+1
        start=left
print(max_length,n[start:start+max_length])


#input [3,6,8,10,13,15,17,20] output= 3,6 8,10 13,15 15,17
#find dif in b/w 2 adjacent values
#use for loop to iterate and find diff
#use aother for loop and if loop to print

nums1 =[3,6,8,10,13,15,17,20]
min_diff = nums1[1]-nums1[0]
for i in range(len(nums1)-1):
    diff = nums1[i+1]-nums1[i]
    if diff < min_diff:
        min_diff = diff

for i in range(len(nums1)-1):
    if nums1[i+1]-nums1[i]== min_diff:
        print((nums1[i]),(nums1[i+1]))

#area of rectangle
#need to get 2 elements lenght and breadth need to multiply them
#swap variables
a,b = 2,3
b,a = 2,3
print(b,a)
#odd or even
'''number = int(input("enter a number to check even or odd"))
if number % 2 == 0:
    print("even")
else:
    print("odd")

#Check whether a character is vowel or consonant
character = input("enter a character to check weather it is vowel or not").lower()
vowels = "aeiou"
if character  in vowels:
    print("characters  contain vowels")
else:
        print("it has a vowel")'''

a = 10
b = 20
c = 30

if a>b and a>c:
    print("a is max")
elif b>a and b>c:
    print("b is max")
else:
    print("c is max")


'''def flower():
    name=input()
    city =input()

    output = f'{name}lives in{city}'
    print(output)
flower()'''


#slicing
a = "hii govindha"
print(a[4:])
#a.title will capitalize the first letter
def name(a):
    return a.title()

print(name("govindha"))
