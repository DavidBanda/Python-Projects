from statistics import *

exec("print('this works like eval')")

list_str = "[5, 6, 2, 9, 0]"
list_str = exec(list_str)
print(list_str)

exec("list_str2 = [5, 6, 2, 9, 0]")
#print(list_str2)

exec("def test(): "
     "print(list_str2)")
test()

exec("""
def test2():
    example = [1, 5, 7, 9, 8, 3, 3, 5, 6, 8, 2, 4]
    c = mean(example)
        
    print(c)
""")

test2()