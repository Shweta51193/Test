from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup
import requests
from tkinter import filedialog
import pandas as pd
import xlsxwriter
root = Tk()


back = tk.Frame(master=root, width=5000, height=1000, bg='black')
# back.pack()
# Don't allow the widgets inside to determine the frame's width / height
back.pack_propagate(0)
back.pack(fill=tk.BOTH, expand=1)  # Expand the frame to fill the root window

# Changed variables so you don't have these set to None from .pack()
label_url = tk.Label(master=back, text='Enter URL:', height=2, fg="white",bg="black")
label_url.grid(row=2, column=0)
# label_1 = tk.Label(master=back, bg='black')
# label_1.grid(row=3, column=1)
entryBox = Entry(master=back, width=60)
entryBox.grid(row=2, column=1)

label_save=tk.Label(master=back,text="Save to directory:",height=2,fg="white",bg="black")
label_save.grid(row=3,column=0)

textvar=StringVar()
saveentry=Entry(master=back,text=textvar,width=60)
saveentry.grid(row=3,column=1)

def func_save(var1):
    dirlocation=filedialog.askdirectory(initialdir="/",title="Select Directory")
    # print(dirlocation)
    
    a = var1.split('.')
    print(a[1])
    b = var1.split('/')
    # print(b[2])

    func_submit.filename = "file_"+a[1]+".txt"
    # print(filename)
    file1 = func_submit.filename
    c=dirlocation+"/"+str(file1)
    print(c)
    textvar.set(c)

    f = open(c, "wb+")
    # for i in a:
    #     print(i)
    data = requests.get(var1)
    # print(data)
    soup = BeautifulSoup(data.text)
    # print(soup)


    txt_file = soup.prettify("utf-8")
    f.write(txt_file)
    
    # print("hello")

select_button=Button(master=back,text="..",command=lambda: func_save(entryBox.get()))
select_button.grid(row=3,column=2)
# url_text = entryBox.get()
# print(url_text)

label_2 = tk.Label(master=back, bg='black')
label_2.grid(row=5, column=1)


def func_submit(var1):
    # print(var1)
    a = var1.split('.')
    # print(a[1])
    b = var1.split('/')
    # print(b[2])

    func_submit.filename = "file_"+a[1]+".txt"
    # print(filename)
    file1 = func_submit.filename
    f = open(file1, "wb+")
    # for i in a:
    #     print(i)
    data = requests.get(var1)
    # print(data)
    soup = BeautifulSoup(data.text)
    # print(soup)
    title_tag = soup.findAll("a", {"class": "_2cLu-l"})
    # print(title_tag)
    for i in title_tag:
        p_name=i['title']
        p_url="https://"+b[2]+i['href']

    txt_file = soup.prettify("utf-8")
    f.write(txt_file)

btn_submit = tk.Button(master=back, text="Submit",
                       command=lambda: func_submit(entryBox.get()))

btn_submit.grid(row=5, column=1)

def func_export(var1):
    a = var1.split('.')
    b = var1.split('/')
    filename = "file_"+a[1]+".xlsx"
    # url=r"file_flipkart.txt"
    # page=open(url)
    # soup = BeautifulSoup(page.read())
    data = requests.get(var1)
    # print(data)   
    soup = BeautifulSoup(data.text)
    # print(soup)
    name_list=[]
    url_list=[]
    discount_list=[]
    price_list=[]
    price_details=soup.find_all("div",{"class":"_1uv9Cb"})
    # print(price_details)
    for i in price_details:
        discount_tag=i.find("div",{"class":"_1vC4OE"})
        discount_list.append(discount_tag.text)

        price_tag=i.find("div",{"class":"_3auQ3N"})
        # print(price_tag)
        price_list.append(price_tag.text)

        # offer_tag=i.find("")

        # print(discount_tag.text)
    title_tag = soup.findAll("a", {"class": "_2cLu-l"})
    # print(title_tag)
    

    for i in title_tag:
        p_name=i['title']
        name_list.append(p_name)
        p_url="https://"+b[2]+i['href']
        url_list.append(p_url)

    df=pd.DataFrame({
        'Price':[i for i in price_list],
        'Discount Price':[i for i in discount_list],
        'Product URL':[i for i in url_list],
        'Product name':[i for i in name_list]})

    writer = pd.ExcelWriter(filename,options={'strings_to_urls': False})
    df.to_excel(writer, startrow=0, startcol=0)
    worksheet = writer.sheets['Sheet1']
    writer.save()
    # workbook  = writer.book
    # worksheet = writer.sheets['Product_details']
    # writer=pd.ExcelWriter(filename,engine='xlsxwriter')
    # df.to_excel(writer, sheet_name='Product_details')
    
btn_export_excel_file=tk.Button(master=back,text ="Export Excel Sheet",command=lambda:func_export(entryBox.get()))
btn_export_excel_file.grid(row=5,column=2)

def func_file(a):
    # print(func_submit.filename)
    print("print file content")
    f = open(func_submit.filename, "r+")
    for i in f:

        print(i)

label_3 = tk.Label(master=back, bg='black').grid(row=7, column=1)
btn_get_file = tk.Button(master=back, text="Get File",
                         command=lambda: func_file("hello")).grid(row=8, column=1)


mainloop()
