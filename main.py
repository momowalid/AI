# python exercise 1
# question 1
from typing import Dict

name=input()
# way 1
print(len(name))
# way 2
num=0
for i in range(0,len(name)):
    num=num+1
print(num)
#*******************************
# question 2
name2=input()
out=""
if len(name2)<2:
    print(out)
else:
    out=name2[0]+name2[1]+name2[-2]+name2[-1]
    print(out)
#*******************************
# question 3
name3=input()
if len(name3)<3 :
    print(name3)
else:
    if name3[-1]=="g" and name3[-2]=="n" and name3[-3]=="i":
        name3=name3+"ly"
    else:name3=name3+"ing"
    print(name3)
#******************************
# question 4

n=int(input("enter the number of words : "))
input4=[]
bigname=""
bigsize=0
i=0
while i<n:
 input4.append(input("enter the word: "))

 if len(input4[i])>bigsize:
     bigsize=len(input4[i])
     bigname=input4[i]
 i=i+1
print(bigname)
print(bigsize)
#********************************
# question 5
name5=input("enter a name: ")
last=name5[0]
first=name5[-1]
print(first+name5[1:-1]+last)
#********************************
# question 6
import sys
name6=input("enter a name: ")
i=0
while i<len(name6):
    sys.stdout.write(name6[i])
    i=i+2
print(" ")
#*******************************
# question 8
name8=input("Enter your name: ")
print(name8.upper())
print(name8.lower())
#*******************************
# question 9
string9=input("enter a string : ")
if len(string9)%4==0:
    string9=string9 [::-1]
print(string9)
#******************************
# question 10
string10=input("enter a string : ")
string10=string10.strip()
print(string10)
#*******************************
# question 11
string11=input("enter the string : ")
char11=input("enter the character : ")
if string11[0]==char11[0]:
    print("YES")
else:
    print("NO")
#********************************
# question 13
numbers = [30.92002, 4.101965, 12.12197, 27.51999]
for number in numbers:
    print("{:.2f}".format(number))
#*********************************
# question 14
numbers = [3.14159, -2.71828, 1.41421, -0.57721]

for number in numbers:
    print("{:+.2f}".format(number))
#*********************************
# question 15
number = 1234567890
formatted_number = "{:,}".format(number)
print(formatted_number)
#**********************************
# question 16
# first method in question number 9
# second method
string16=input(" enter your string : ")
i=len(string16)-1
out16=""
while i>=0:
    out16=out16+string16[i]
    i=i-1
print(out16)
#**********************************
# question 17
string17=input(" enter a string : ")
repeated=""
i=0
counter=0
out=0
while i<len(string17):
    j=0
    while j<len(string17):
        if(string17[j]==string17[i]):
            counter=counter+1
        j=j+1
    if counter>1 :
        out=out+1
        string17.replace('',string17[i])
    i=i+1
print(out)
#********************************
# question 18
string18=input("enter your string : ")
i=0
while i<len(string18):
    repeated=0
    for j in range(0,len(string18)):
        if(string18[i]==string18[j]):
            repeated=repeated+1
    if(repeated==1):
        print(string18[i])
        break
    i=i+1
#***********************************
# question 19
string19=input("enter a string:")
print(string19.replace(' ',''))
#*********************************
# question 20
string20=input("enter a string : ")
print(len(string20)*(len(string20)+1)/2)
#********************************
# question 21
list21=[1,3,8,9,'m','o']
last=list21[0]
list21[0]=list21[-1]
list21[-1]=last
print(list21)
#********************************
# question 22
list22=[23,65,19,90]
pos1=input("enter the first position : ")
pos2=input("enter the second position : ")
replace=list22[int(pos1)-1]
list22[int(pos1)-1] = list22[int(pos2)-1]
list22[int(pos2)-1] = replace
print(list22)
#********************************
# question 23
list23=[1,2,3,4,5,6,7,8,9]
print(len(list23))
#********************************
# question 24
list24=[23,57,89,23,45,67,89]
print(max(list24))
#*********************************
# question 25
list25=[89,45,23,12,3,456,78,8]
print(min(list25))
#********************************
# question 26
list26=[23,12,1,2,3,4,5,6,7,8,9]
element26=int(input("enter your element : "))
existing=list26.count(element26)
if existing>0 :
    print("YES")
else :
    print("NO")
print(existing)
#*********************************
# question 27
# first way
list27=[1,2,3,4,5,6,7,8,9,10]
list27.clear()
print(list27)
#*********************************
# question 28
list28=[1,2,3,4,3,3,2,2,1,5,6,5,7,9,8,8,7,6,8]
print(set(list28))
#********************************
#question 29
dictionary29={"name":"momo" , "id":"8" , "name":"walid" , "id":"12"}
print(dictionary29)
#*******************************
# question 30
list30=[1,21,3,33,4,5,4,4,4,5,6,7,7,7,8]
set30=set(list30)
print(len(set30))
#*********************************
# question 33
first=int(input("enter the first digit: "))
second=int(input("enter the second digit: "))
third=int(input("enter the third digit: "))
print(first,second,third)
print(first,third,second)
print(second,first,third)
print(second,third,first)
print(third,first,second)
print(third,second,first)
#********************************
# question 36
list36=[1,1,1,2,2,1,1,1,4,5,6,7,8]
removal=input("enter the element you want to remove : ")
i=0
out=[]
while i<len(list36):
    if list36[i]!=int(removal):
        out.append(list36[i])
    i=i+1
print(out)
#********************************
# question 37
list1=["gfg","is","best"]
list2=[0,1,2,1,0,0,0,2,1,1,2,0]
i=0
out=[]
while i<len(list2):
    out.append(list1[list2[i]])
    i=i+1
print(out)
#********************************
# question 38
list38=[(4,5,5,4),(5,4,3)]
k=int(input("enter the element : "))
n=int(input(" enter number of occurances : "))
i=0
while i<len(list38):
    if list38[i].count(k)==n:
        print(list38[i])
    i=i+1
#**********************************
#question 39
list39=[[1,3,3],[2,1,2],[3,2,1]]
i=0
j=0
out=[]
while i<3:
    while j<3:
        out.append(list39[list39[j][i]-1])
        j=j+1
    print("Sorted array specific to column",i,": ",out)
    out=[]
    j=0
    i=i+1
#********************************
# question 40
dictionary40={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(sorted(dictionary40))
#**********************************
# question 41
dictionary41={"Gfg":3 , "is" : 7, "best" : 10, "for" : 6, "geeks" : 8}
k=int(input("enter the maximum value: "))
i=0
list41=list(dictionary41)
out={}
out=dict(out)
while i<len(list41):
    if int(dictionary41[list41[i]])<=k:
        out[list41[i]]=dictionary41[list41[i]]
    i=i+1
print(out)
#*********************************
#question 42
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
add2=dic2.copy()
add3=dic3.copy()
dic1.update(add2)
dic1.update(add3)
print(dic1)
#****************************
# question 45
dict45={'a':9 , 'b':10 , 'c':12 , 'd':15}
print(max(dict45.values()))
print(min(dict45.values()))
#**************************
# question 46
dict46={'c1': 'Red', 'c2': 'Green', 'c3': None}
i=0
list46=list(dict46)
while i<len(dict46):
    if dict46[list46[i]] == None:
        dict46.pop(list46[i])
    i=i+1
print(dict46)
#****************************
# question 47
tuple1=(1,2,3,4,5,6,7,8,9)
print(tuple1[0])
#*****************************
# question 48
tuple2=('u',1,'q',2,'e',3,'h')
i=0
while i<len(tuple2):
    print(tuple2[i])
    i=i+1
#*****************************
# question 49
tuple3=(1,2,3,5,3,4,5,45,6,7,8)
add=input("enter your new element: ")
tuple3=tuple3+tuple(add)
print(tuple3)
#*****************************
# question 50
tuple4=('m','o','h','a','m','e','d')
i=0
out=""
while i<len(tuple4):
    out=out+tuple4[i]
    i=i+1
print(out)
#*******************************
# question 51
list51={1,2,3,4,5,6}
tuple51=tuple(list51)
print(tuple51)
#******************************
# question 52
tuple52=(2,3,4,5,6,7,8,9,10,443)
print(tuple52[::-1])
#******************************
# question 53
list53=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
replace=input("enter the new value : ")
i=0
while i<3:
    list1=list(list53[i])
    list1[2]=replace
    list53[i]=tuple(list1)
    i=i+1
print(list53)
#******************************
# question 54
ori=input("Enter the origial string : ")
print(tuple(ori))
#******************************
# question 55
tuple55=(22,56,23,5,78,9,1,4)
list1=list(tuple55)
sum=0
i=0
while i<len(list1):
    sum=sum+int(list1[i])
    i=i+1
print(sum/len(list1))
#******************************
# question 56
n=int(input("enter the number of numbers you will add : "))
set56={12,3,4,54,56,76}
set56=set(set56)
i=0
while i<n:
    add=int(input("enter number "))
    set56.add(add)
    i=i+1
print(set56)
#****************************
# question 57
set57={2,32,5,5,5,6,7,8,8,3,2,2,7,8,9}
print(set(set57))
#*************************
# question 59
set59={56,4,57,84,3,46,578,32,56,89,100}
print(max(set59))
print(min(set59))
#*****************************
# question 60
list60=[1,2,3,4,5,6,7,8,9,1]
set60=set(list60)
list60=list(set60)
sum=input("enter the summation value : ")
i=0
j=0
while i<len(list60):
    j=i+1
    while j<len(list60):
        if list60[i]+list60[j]==int(sum):
            print(list60[i])
            print(list60[j])
        j=j+1
    i=i+1
# *************************** end of the task ***************************************
