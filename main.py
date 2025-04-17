# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pychar

print("hi")

print("hello"*2)
s="abcdefghi"
print(s[1:6:2])# 1 is starting,6 is ending, 2 is the gap so that it  will print evrey second element of the list


if([]):# if the block is empty then it will move to next block
    print("Anjan")
else:
    print("govindha")

my_list = [3,4,5,6,7]

for i in my_list:
    my_list.remove(i) #removes3 and moves to 4-is become1st element andcontinues
print(my_list)

a= frozenset([1,2,3,4,5,5,6,2])
#immutable sets are frozensets
print(a)


txt=["a", "b," ,"c"]
print(*txt,sep="-->")










