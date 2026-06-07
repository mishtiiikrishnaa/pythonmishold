import tkinter as tk
from tkinter import messagebox
import mysql.connector as mc

# establish connection
var = mc.connect(host="localhost", user="root", passwd="123456", database="meghnanair")
cursor = var.cursor()

def create_table():
    tn = entry_table_name.get()
    if tn:
        try:
            st = f"CREATE TABLE {tn} (bookid VARCHAR(20), bookname VARCHAR(20), price INTEGER, qty INTEGER)"
            cursor.execute(st)
            var.commit()
            messagebox.showinfo("Success", f"Table '{tn}' created successfully.")
        except mc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "Please enter a table name.")

def add_record():
    t = entry_table_name.get()
    bid = entry_book_id.get()
    bkn = entry_book_name.get()
    pri = entry_price.get()
    qty = entry_quantity.get()
    
    if t and bid and bkn and pri and qty:
        try:
            pri = float(pri)
            qty = int(qty)
            m = f"INSERT INTO {t} (bookid, bookname, price, qty) VALUES ('{bid}', '{bkn}', {pri}, {qty})"
            cursor.execute(m)
            var.commit()
            messagebox.showinfo("Success", "Record added successfully.")
        except mc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

def display_all_records():
    t = entry_table_name.get()
    if t:
        try:
            st = f"SELECT * FROM {t}"
            cursor.execute(st)
            records = cursor.fetchall()
            display_records(records)
        except mc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "Please enter a table name.")

def display_price_records():
    t = entry_table_name.get()
    if t:
        try:
            st = f"SELECT * FROM {t} WHERE price > 500"
            cursor.execute(st)
            records = cursor.fetchall()
            display_records(records)
        except mc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "Please enter a table name.")

def display_qty_records():
    t = entry_table_name.get()
    if t:
        try:
            st = f"SELECT * FROM {t} WHERE qty < 100"
            cursor.execute(st)
            records = cursor.fetchall()
            display_records(records)
        except mc.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
    else:
        messagebox.showwarning("Input Error", "Please enter a table name.")

def display_records(records):
    result_window = tk.Toplevel(root)
    result_window.title("Records")
    for record in records:
        record_label = tk.Label(result_window, text=str(record))
        record_label.pack()

root = tk.Tk()
root.title("Library Management")

# table name
label_table_name = tk.Label(root, text="Table Name:")
label_table_name.pack()
entry_table_name = tk.Entry(root)
entry_table_name.pack()

# book id
label_book_id = tk.Label(root, text="Book ID:")
label_book_id.pack()
entry_book_id = tk.Entry(root)
entry_book_id.pack()

# book name
label_book_name = tk.Label(root, text="Book Name:")
label_book_name.pack()
entry_book_name = tk.Entry(root)
entry_book_name.pack()

# price
label_price = tk.Label(root, text="Price:")
label_price.pack()
entry_price = tk.Entry(root)
entry_price.pack()

# quantity
label_quantity = tk.Label(root, text="Quantity:")
label_quantity.pack()
entry_quantity = tk.Entry(root)
entry_quantity.pack()

# buttons
button_create_table = tk.Button(root, text="Create Table", command=create_table)
button_create_table.pack()

button_add_record = tk.Button(root, text="Add Record", command=add_record)
button_add_record.pack()

button_display_all = tk.Button(root, text="Display All Records", command=display_all_records)
button_display_all.pack()

button_display_price = tk.Button(root, text="Display Records with Price > 500", command=display_price_records)
button_display_price.pack()

button_display_qty = tk.Button(root, text="Display Records with Quantity < 100", command=display_qty_records)
button_display_qty.pack()

root.mainloop()
cursor.close()
var.close()
