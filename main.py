import customtkinter as cs
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os
import re
import datetime
from tkinter.font import nametofont


# Function For check for Data
def Check_data(data, data_type):
    if data_type == "Prix":
        # Check if Prix is int or float
        if re.match(r'^[1-9]\d*(\.\d+)?$', data):
            return True
        else:
            return False
    elif data_type == "Quantity":
        # Check if Quantity is int
        if re.match(r'^[1-9]\d*$', data):
            return True
        else:
            return False
    elif data_type == "ID":
        if re.match(r'^[1-9]\d*$', data):
            return True
        else:
            return False
    else:
        return False


# function to add data to json file
def add_json():
    # get data from entry
    product_id = Myid_entre.get()
    product_name = Name_entre.get()
    product_prix = prix_entre.get()
    product_Qnt = Quantity_entre.get()
    product_Date_exep = Date_entre.get()
    #Check If Data not Empty
    if not (product_id and product_name and product_prix and product_Qnt and product_Date_exep):
        messagebox.showerror("Error","Please fill in all fields.")
        return
    #Prix Should be numbers (int or float)
    if product_prix and not Check_data(product_prix,"Prix"):
        messagebox.showerror("Error","Please enter correct Prix")
        return
    #Quantity Should be numbers (only int)
    if product_Qnt and not Check_data(product_Qnt,"Quantity"):
        messagebox.showerror("Error","Please enter correct Quantity")
        return
    # id should be int
    if product_id and not Check_data(product_id,"ID"):
        messagebox.showerror("Error","Please enter correct Id")
        return






    #Put Data in entry
    Data_Entry = {
        'ID':product_id,
        'Name':product_name,
        'Prix':product_prix,
        'Quantity':product_Qnt,
        'Date Exep':product_Date_exep,
        'Total':f"{float(product_prix)*int(product_Qnt)} DH"
    }
    Myjson_file = 'products.json'
    #Checks if file json exists
    if os.path.exists(Myjson_file):
        with open(Myjson_file,'r') as file:
            data = json.load(file)
    else:
        data = []
    data.append(Data_Entry)

    with open(Myjson_file,'w') as file:
        json.dump(data,file,indent=2)
    #clear entrys
    Myid_entre.delete(0,tk.END)
    Name_entre.delete(0,tk.END)
    prix_entre.delete(0,tk.END)
    Quantity_entre.delete(0,tk.END)
    Date_entre.delete(0,tk.END)
    #add data to treeview
    add_to_treeview()
    #message box
    messagebox.showinfo("Info",'Data has Inserted')
# Function to insert data in treeView
def add_to_treeview():
    #Checks if file json exists
    Myjson_file='products.json'
    if os.path.exists(Myjson_file):
        with open(Myjson_file,'r') as file:
            data =json.load(file)
        #delete all data from treeview
        for item in tree.get_children():
            tree.delete(item)
        # insert new datas
        for item in data:
            tree.insert("","end",values=(
              item['ID'],item['Name'],item['Prix'],item['Quantity'],item['Date Exep'],item['Total']))
#Function For Update data
def Update_data():
    selected_item = tree.focus()
    #check if not selected any data
    if not selected_item:
        messagebox.showerror("Error","Please select item")
        return
    # get id of item who selected
    myid=tree.item(selected_item,'values')[0]
    # get all data from entrys
    product_id=Myid_entre.get()
    product_name=Name_entre.get()
    product_prix=prix_entre.get()
    product_Qnt=Quantity_entre.get()
    product_Date_exep=Date_entre.get()
    #handling error check if entrys empty
    if not (product_id or product_name or product_prix or product_Qnt or product_Date_exep):
        messagebox.showerror("Error","Please Entry Update Data.")
        return
    #Prix should be numbers
    if product_prix and not Check_data(product_prix,"Prix"):
        messagebox.showerror("Error","Please enter correct Prix")
        return

        # Quantity should be numbers
    if product_Qnt and not Check_data(product_Qnt,"Quantity"):
        messagebox.showerror("Error","Please enter correct Quantity")
        return
        #id should be number
    if product_id and not Check_data(product_id,"ID"):
        messagebox.showerror("Error","Please enter correct ID")
        return
    #json file read
    with open('products.json','r') as file:
        data=json.load(file)
    # I want to check if data from entrys not empty
    for item in data:
        if item['ID']==myid:
            #I want to check if id not exists
            if product_id and product_id != myid:
                if any(i['ID']==product_id for i in data):
                    messagebox.showerror("ID Error","Product ID already exists.")
                    return
                item['ID']=product_id
            if product_name:
               item['Name']=product_name
            if product_prix:
               item['Prix']=product_prix
            if product_Qnt:
               item['Quantity']=product_Qnt
            if product_Date_exep:
               item['Date Exep']=product_Date_exep
            item['Total']=f"{float(item['Prix'])*int(item['Quantity'])} DH"
            break
    with open('products.json','w') as file:
        json.dump(data,file,indent=2)
    add_to_treeview()
    Myid_entre.delete(0,tk.END)
    Name_entre.delete(0,tk.END)
    prix_entre.delete(0,tk.END)
    Quantity_entre.delete(0,tk.END)
    Date_entre.delete(0,tk.END)
    messagebox.showinfo("Info",'Data has updated')
#Fuction for delete data
def Delete_data():
    selected_item=tree.focus()
    #Check if not selected any data
    if not selected_item:
        messagebox.showerror("Error","Please select item")
        return
    # get id of element who I want to delete it
    myid=tree.item(selected_item,'values')[0]
    with open('products.json','r') as file:
        data=json.load(file)
        for item in data:
            if item["ID"]==myid:
                data.remove(item)
    with open('products.json','w') as file:
        json.dump(data,file,indent=2)
    add_to_treeview()
    messagebox.showinfo("Delete","The product has been successfully deleted.")


#Create Root (Window)
root = cs.CTk()
root.title("MyProgram")
root.config(background="#393939")
root.geometry("1000x550")



#Fonts
My_Fonts = {
    "Primary_Font":("Roboto",20, "bold"),
    "Second_Font": ("Open Sans",16, 'bold')
}
#Create Place For Entre data
#Id
Myid = cs.CTkLabel(root,text="ID :",font=My_Fonts["Primary_Font"],bg_color="#393939",text_color="white")
Myid.place(x=20,y=20)
Myid_entre = cs.CTkEntry(root,font=My_Fonts["Second_Font"],corner_radius=5,bg_color="#393939",border_width=1,width=100)
Myid_entre.place(x=120,y=20)
#Name
Name = cs.CTkLabel(root,text="Name :",font=My_Fonts["Primary_Font"],bg_color="#393939",text_color="white")
Name.place(x=20,y=70)
Name_entre = cs.CTkEntry(root,font=My_Fonts["Second_Font"],bg_color="#393939")
Name_entre.place(x=120,y=70)
#Prix
prix = cs.CTkLabel(root,text="Prix :",font=My_Fonts["Primary_Font"],bg_color="#393939",text_color="white")
prix.place(x=20,y=120)
prix_entre = cs.CTkEntry(root,font=My_Fonts["Second_Font"],corner_radius=5,bg_color="#393939",border_width=1)
prix_entre.place(x=120,y=120)
#Quantity
Quantity = cs.CTkLabel(root,text="Quantity :",font=My_Fonts["Primary_Font"],bg_color="#393939",text_color="white")
Quantity.place(x=20,y=170)
Quantity_entre = cs.CTkEntry(root,font=My_Fonts["Second_Font"],corner_radius=5,bg_color="#393939",border_width=1)
Quantity_entre.place(x=120,y=170)
#DateExper
Date = cs.CTkLabel(root,text="Date Exep :",font=My_Fonts["Primary_Font"],bg_color="#393939",text_color="white")
Date.place(x=20,y=220)
Date_entre = cs.CTkEntry(root,font=My_Fonts["Second_Font"],corner_radius=5,bg_color="#393939",border_width=1)
Date_entre.place(x=120,y=220)
#Add Button
add = cs.CTkButton(root,corner_radius=15,border_width=2,bg_color="#393939",text_color="white",cursor='hand2'
                   ,font=My_Fonts["Second_Font"],hover_color="#3B7A57",text="Add Products",fg_color="#29AB87",width=245,height=40,command=add_json)
add.place(x=20,y=280)
#Update Buttun
Update = cs.CTkButton(root,corner_radius=15,border_width=2,bg_color="#393939",text_color="white",cursor='hand2'
                      ,font=My_Fonts["Second_Font"],hover_color="#FFA836",text="Update Products",fg_color="#F5761A",width=245,height=40,command=Update_data)
Update.place(x=20,y=340)
#Sell Product
Sell = cs.CTkButton(root,corner_radius=15,border_width=2,bg_color="#393939",text_color="white",cursor='hand2'
                    ,font=My_Fonts["Second_Font"],hover_color="#FFA836",text="Sell Products",fg_color="#F5761A",width=245,height=40)
Sell.place(x=20,y=400)
#Delete Products
Delete = cs.CTkButton(root,corner_radius=15,border_width=2,bg_color="#393939",text_color="white",cursor='hand2'
                    ,font=My_Fonts["Second_Font"],hover_color="#FF2400",text="Delete Products",fg_color="#ED2939",width=245,height=40,command=Delete_data)
Delete.place(x=20,y=460)
#  i will create treeview
style = ttk.Style(root)
style.theme_use('clam')
style.configure('Treeview', foreground='black', font=('Open Sans', 18, 'bold'), fieldbackground='#313837',rowheight=35,bordercolor='gray',border=4, lightcolor='gray', darkcolor='gray')
style.map('Treeview', background=[('selected', 'red'),],)
tree = ttk.Treeview(root,height=22)

tree['show'] = 'headings'  # This removes the empty first column
tree['padding'] = [0, 0]
#Create Columns
tree['columns'] = ('ID','Name','Prix','Quantity','Date Exep','Total')
#Create Header of treeview
TkHeadingFont = nametofont("TkHeadingFont")
TkHeadingFont.configure(size=20)
style.configure("Treeview.Heading", foreground="black",font=('Open Sans', 20, 'bold'))

tree.column('#0',width=0,stretch=tk.NO)
for column in tree['columns']:
    tree.column(column, anchor=tk.CENTER, width=160,)

for column in tree['columns']:
    tree.heading(column,text=column)


tree.place(x=430,y=20)
add_to_treeview()







root.mainloop()