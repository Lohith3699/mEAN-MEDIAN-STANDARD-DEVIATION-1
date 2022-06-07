import statistics
lst = []
  

n = int(input("Enter number of elements : "))

for i in range(0, n):
    print("Enter your number: ")
    ele = int(input())
  
    lst.append(ele) 
      
print(lst)
x = statistics.mean(lst)
print("Mean is :", x)
#Median
import statistics
lst = []
  

n = int(input("Enter number of elements : "))

for i in range(0, n):
   ele = int(input("Enter elements : "))
  
   lst.append(ele) 
      
print(lst)
x = statistics.median(lst)
print("Median is :", x)
#Standard Deviation
import statistics
lst = []
  

n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("Enter elements : "))
  
    lst.append(ele) 
      
print(lst)
x = statistics.stdev(lst)
print("Standard Deviation is :", x)