
def calculate(min, max, step):
    sum=0
    for n in range (min,max+1,step):
        sum=sum+n
        n+step
    print(sum)
               
calculate(1, 3, 1)
calculate(4,8,2)
calculate(-1,2,2) 

def avg(data):
    from collections import Counter
    employees = [{
     "name":"John", "salary":30000, "manager":False
    }, 
    {
    "name":"Bob", "salary":60000, "manager":True
    }, 
    { 
    "name":"Jenny", "salary":50000, "manager":False
    }, 
    { 
    "name":"Tony", "salary":40000, "manager":False
    } ]
    count_manager = lambda x:0 if x['manager'] else 1
    manager_list = map(count_manager, employees)
    ppl=(sum(manager_list))
   
    for entry in employees:
        count_salary = lambda x:0 if x['manager'] else entry["salary"]
        salary_list = map (count_salary, employees)
    total=(sum(salary_list)) 
    print(total/ppl)
            

    
avg({
"employees":[ 
{
"name":"John", "salary":30000, "manager":False
}, 
{
"name":"Bob", "salary":60000, "manager":True
}, 
{ 
"name":"Jenny", "salary":50000, "manager":False
}, 
{ 
"name":"Tony", "salary":40000, "manager":False
} 
]
})

def func(a):
    def func2(b,c):
        print(a)+(b*c)
    return func2


func(2)(3, 4)
func(5)(1, -5)
func(-3)(2, 9)

import sys
def maxProduct(nums):
    if len(nums) < 2:
        return
    max_product =  -sys.maxsize
    max_i = max_j = -1
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if max_product < nums[i] * nums[j]:
                max_product = nums[i] * nums[j]
                (max_i, max_j) = (i,j)
    print(nums[max_i]* nums[max_j])

maxProduct([5, 20, 2, 6])  
maxProduct([10, -20, 0, 3]) 
maxProduct([10, -20, 0, -3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2]) 
maxProduct([5,-1, -2, 0])  
maxProduct([-5, -2])
    
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            s=nums[i]+nums[j]
            if s==target:
                return[i,j] 

result=twoSum([2, 11, 7, 15], 9)
print(result) 

