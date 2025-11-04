# class c1:
#     def  __init__(self):
#         print("c1")
# class c2():
#     def __init__(self):
#         print("c2")
        
# class c3(c1,c2):
#     def __init__(self):
#         print("c3")
#         super().__init__()
#         super().__init__()
       
# obj=c3()
# upword
    
# class c1:
#     num=120
#     def banna(self,a):
#         print(a)
# class c2(c1):
#     def banna(self):
#         print("b2")
#         print(c1.num)
#         super().banna("banna2")
# class c3(c1):
#     def banna(self):
#         print("b3")
#         super().banna("banna3")
      
# obj=c3()
# obj2=c2()
# obj.banna()
# obj2.banna()
# down world 

# obj.banna()
# class c1:
#     def banna(self):
#         print("b1")
# class c2():
#     def banna(self):
#         print("b2")
# class c3(c1,c2):
#     def banna(self):
#         print("b3")
#         super().banna()
#         super().banna()
# obj=c3()
# obj.banna()

# class c2:

#     def banna(self,a):
#         print("one",a)
#     def banna(self,a,b):
#         print("two",a,b)
#     def banna(self):
#         print("bn")
#     def banna(self,a,b):
#         print("two",a,b)
# obj=c2()
# obj.banna(1, 2)
# class c1:
#     def banna(self,a=0,b=0,c=0):
#         if b==0 and c==0:
#             print("one argument")
#         elif a!=0 and b!=0 and c!=0:
#             print("three argument ")
#         elif c==0:
#             print("three argument")
#         else:
#             print("no")
# obj=c1()
# obj.banna(1,2)
class c1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __mul__(self,other):
        n1=self.a*other.a
        n2=self.b*on
        