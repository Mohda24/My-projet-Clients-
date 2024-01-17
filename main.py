import customtkinter as cs
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os
from tkinter.font import nametofont


# Function For check for Data
def Check_data(y,z):
    for i in range(len(y)):
        if y[0] == "0" or y[i] not in ["0","1","2","3","4","5","6","7","8","9"] :
          messagebox.showerror("Error",f"Enter Correct {z}")
          return

# function to add data to json file
def add_json():
    product_id = Myid_entre.get()
    product_name = Name_entre.get()
    product_prix = prix_entre.get()
    product_Qnt = Quantity_entre.get()
    product_Date_exep = Date_entre.get()
    #Check If Data not Empty
    if not (product_id and product_name and product_prix and product_Qnt and product_Date_exep):
        messagebox.showerror("Error","Please fill in all fields.")
        return
    #Prix Should be numbers
    Check_data(product_prix,"Prix")
    Check_data(product_Qnt,"Quantity")
    #Quantity Should be numbers


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
    add_to_treeview()
    messagebox.showinfo("Info",'Data has Inserted')

def add_to_treeview():
    Myjson_file='products.json'
    if os.path.exists(Myjson_file):
        with open(Myjson_file,'r') as file:
            data =json.load(file)

        for item in tree.get_children():
            tree.delete(item)
        for item in data:
            tree.insert("","end",values=(
              item['ID'],item['Name'],item['Prix'],item['Quantity'],item['Date Exep'],item['Total']))
def Update_data():
    selected_item = tree.focus()

    if not selected_item:
        messagebox.showerror("Error","Please select item")
        return
    myid=tree.item(selected_item,'values')[0]
    product_id=Myid_entre.get()
    product_name=Name_entre.get()
    product_prix=prix_entre.get()
    product_Qnt=Quantity_entre.get()
    product_Date_exep=Date_entre.get()
    if not (product_id or product_name or product_prix or product_Qnt or product_Date_exep):
        messagebox.showerror("Error","Please fill in all fields.")
        return
    for i in range(len(product_prix)):
        if product_prix[0]=="0" or product_prix[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
            messagebox.showerror("Error","Enter Correct Prix")
            return
        #Quantity Should be numbers
    for i in range(len(product_Qnt)):
        if product_Qnt[0]=="0" or product_Qnt[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
            messagebox.showerror("Error","Enter Correct Prix")
            return
    #json file
    with open('products.json','r') as file:
        data=json.load(file)
    for item in data:
        if item['ID']==myid:
            if not product_name:
                pass
            else:
                item['Name']=product_name
            if not product_prix:
                pass
            else:
               item['Prix']=product_prix
            if not product_Qnt:
                pass
            else:
                item['Quantity']=product_Qnt
            if not product_Date_exep:
                pass
            else:
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
                    ,font=My_Fonts["Second_Font"],hover_color="#FF2400",text="Delete Products",fg_color="#ED2939",width=245,height=40)
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