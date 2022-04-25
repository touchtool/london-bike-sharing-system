import tkinter as tk
from tkinter import ttk
from utility import *

from table.bicycle_dao import *

root = tk.Tk()
root.title("Bicycle sharing system")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

create_record = FactoryDAO(STATION_TABLE_NAME)
create_record.load_data(file_name=PATH_JOURNEY_CSV, columns=JOURNEY_COLUMN, tablename=JOURNEY_TABLE_NAME)
create_record.load_data(file_name=PATH_STATION_CSV, columns=STATION_COLUMN, tablename=STATION_TABLE_NAME)
create = create_record.get_create_dao()

root.geometry(f"{width}x{height}")
style = ttk.Style()
style.theme_use('default')
style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")
style.map('Treeview',
	background=[('selected', "#347083")])

tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)
tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()
tree_scroll.config(command=my_tree.yview)
my_tree['columns'] = STATION_COLUMN
my_tree.column("#0", width=0, stretch=tk.NO)
my_tree.column(f"{STATION_COLUMN[0]}", anchor=tk.W, width=140)
my_tree.column(f"{STATION_COLUMN[1]}", anchor=tk.W, width=140)
my_tree.column(f"{STATION_COLUMN[2]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{STATION_COLUMN[3]}", anchor=tk.CENTER, width=140)
my_tree.column(f"{STATION_COLUMN[4]}", anchor=tk.CENTER, width=300)
my_tree.heading("#0", text="", anchor=tk.W)
my_tree.heading(f"{STATION_COLUMN[0]}", text=f"{STATION_COLUMN[0]}", anchor=tk.W)
my_tree.heading(f"{STATION_COLUMN[1]}", text=f"{STATION_COLUMN[1]}", anchor=tk.W)
my_tree.heading(f"{STATION_COLUMN[2]}", text=f"{STATION_COLUMN[2]}", anchor=tk.CENTER)
my_tree.heading(f"{STATION_COLUMN[3]}", text=f"{STATION_COLUMN[3]}", anchor=tk.CENTER)
my_tree.heading(f"{STATION_COLUMN[4]}", text=f"{STATION_COLUMN[4]}", anchor=tk.CENTER)
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")
data_frame = tk.LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()
str1 = tk.StringVar()
station_id_label = tk.Label(data_frame, text=f"{STATION_COLUMN[0]}")
station_id_label.grid(row=0, column=0, padx=10, pady=10)
station_id_entry = tk.Entry(data_frame)
station_id_entry.grid(row=0, column=1, padx=10, pady=10)

capacity_label = tk.Label(data_frame, text=f"{STATION_COLUMN[1]}")
capacity_label.grid(row=0, column=2, padx=10, pady=10)
capcity_entry = tk.Entry(data_frame, textvariable=num1)
capcity_entry.grid(row=0, column=3, padx=10, pady=10)

latitude_label = tk.Label(data_frame, text=f"{STATION_COLUMN[2]}")
latitude_label.grid(row=0, column=4, padx=10, pady=10)
latitude_entry = tk.Entry(data_frame, textvariable=num2)
latitude_entry.grid(row=0, column=5, padx=10, pady=10)

longitude_label = tk.Label(data_frame, text=f"{STATION_COLUMN[3]}")
longitude_label.grid(row=1, column=0, padx=10, pady=10)
longitude_entry = tk.Entry(data_frame, textvariable=num3)
longitude_entry.grid(row=1, column=1, padx=10, pady=10)

station_name_label = tk.Label(data_frame, text=f"{STATION_COLUMN[4]}")
station_name_label.grid(row=1, column=2, padx=10, pady=10)
station_name = tk.Entry(data_frame, textvariable=str1)
station_name.grid(row=1, column=3, padx=10, pady=10)

def create_tree_record():
	count = 0
	records = create.get_query()
	for record in records:
		if count % 2 == 0:
			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('evenrow',))
		else:
			my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4]), tags=('oddrow',))
		# increment counter
		count += 1
	root.update()

def up():
	rows = my_tree.selection()
	for row in rows:
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Move Rown Down
def down():
	rows = my_tree.selection()
	for row in reversed(rows):
		my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Remove one record
def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)

# Remove Many records
def remove_many():
	x = my_tree.selection()
	for record in x:
		my_tree.delete(record)

# Remove all records
def remove_all():
	for record in my_tree.get_children():
		my_tree.delete(record)

# Clear entry boxes
def clear_entries():
	# Clear entry boxes
	station_id_entry.delete(0, tk.END)
	capcity_entry.delete(0, tk.END)
	latitude_entry.delete(0, tk.END)
	longitude_entry.delete(0, tk.END)
	station_name.delete(0, tk.END)


# Select Record
def select_record(e):
	# Clear entry boxes
	clear_entries()

	# Grab record Number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')

	# outpus to entry boxes
	station_id_entry.insert(0, values[0])
	capcity_entry.insert(0, values[1])
	latitude_entry.insert(0, values[2])
	longitude_entry.insert(0, values[3])
	station_name.insert(0, values[4])

# Update record
def update_record():
	# Update record
	find_record = create.get_query_by_id(station_id_entry.get())
	if capcity_entry.get() == "":
		num1.set(f"{find_record[0][1]}")
	if latitude_entry.get() == "":
		num2.set(f"{find_record[0][2]}")
	if longitude_entry.get() == "":
		num3.set(f"{find_record[0][3]}")
	if station_name.get() == "":
		str1.set(f"{find_record[0][4]}")
	for item in my_tree.get_children():
		my_tree.delete(item)
	
	create.update_by_id(station_id_entry.get(), capacity=int(capcity_entry.get()), latitude=float(latitude_entry.get()), longitude=float(longitude_entry.get()), station_name=str(station_name.get()))
	create_tree_record()
	root.update()
	my_tree.see(station_id_entry.get())
	my_tree.selection_toggle(int(station_id_entry.get())-1)
	# Clear entry boxes
	clear_entries()

#Search
prev = None

def searh():
	global prev
	if prev is not None:
		my_tree.selection_toggle(prev)
	my_tree.see(station_id_entry.get())
	my_tree.move(station_id_entry.get(), my_tree.parent(station_id_entry.get()), my_tree.index(int(station_id_entry.get())-1))
	my_tree.selection_toggle(int(station_id_entry.get())-1)
	prev = int(station_id_entry.get())-1
	find_id = create.get_query_by_id(int(station_id_entry.get()))
	find_label = tk.Label(search_frame, text=f"{find_id[0]}")
	find_label.grid(row=0, column=5, padx=10, pady=10)

search_frame = tk.LabelFrame(root, text="Search")
search_frame.pack(fill="x", expand="yes", padx=20)
search_button = tk.Button(search_frame, text="Find ", command=searh)
search_button.grid(row=0, column=0, padx=10, pady=10)

# Add Buttons
button_frame = tk.LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = tk.Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

move_up_button = tk.Button(button_frame, text="Move Up", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

move_down_button = tk.Button(button_frame, text="Move Down", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<Return>", select_record)


create_tree_record()

root.mainloop()