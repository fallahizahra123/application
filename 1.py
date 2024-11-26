#برنامه ای با پایتون بنویسید که 10 عدد تصادفی تولید و تعیین کند از هر کدام از اعداد چند بار تکرار میشود؟

import random
numbers = [random.randint(1, 10) for _ in range(10)]
count={}
for num in numbers:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
for num, count in count.items():
    print(f'عدد {num}، تعداد تکرار: {count}')

#برنامه ای بنویسید که یک لیست از اعداد از کاربر گرفته . موارد تکراری را حذف کند

list_input=input("Enter number:").split()
del_num=[]
for ii in list_input:
    if ii not in del_num:
        del_num.append(ii)
print(del_num)

#برنامه ای بنویسید که یک لیست حاوی متن و عدد از کاربر دریافت کند و متن ها و اعداد را جدا کرده و در دو لیست مجزا بریزد

list_input_digi= input("please Enter input: ").split(".")
list_num=[]
list_str=[]
for item_digi in list_input_digi:
    if item_digi.isdigit():
        list_num.append(item_digi)
    else:
        list_str.append(item_digi)
print("text=",list_str)
print("number=",list_num)

#برنامه ای بنویسید که یک متن از فایل بخواند و تمام حروف آن را به صورت captal  نوشته و در همان فایل بریزد

sam_file="2.txt"
sam_open=open(sam_file,"+r")
sam_uper=sam_open.read().upper()
sam_open.write(sam_uper)

#برنامه ای بنویسید که یک فایل را باز کرده  و خطوط فرد آن را حذف کند
odd_open=open("22.txt","r")
lineee=odd_open.readlines()
out_file=open("3.txt","w")
for i in range(len(lineee)):
    if i%2==1:
        out_file.write(lineee[i])

#حتویات لیست های A، B و C 
ListA=[random.randint(10,100) for _ in range(50)]
ListB=[random.randint(10,100) for _ in range(50)]
#listA=random.sample(range(1,100),50)
#ListB=random.sample(range(1.100),50)
ListC=[]
for ii in range(len(ListA)):
    if ListA[ii] > ListB[ii]:
        ListC.append(1)
    elif ListA[ii] < ListB[ii]:
        ListC.append(-1)
    else:
        ListC.append(0)
print("ListA=",ListA)
print("ListB=",ListB)
print("ListC=",ListC)
