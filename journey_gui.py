import tkinter as tk
from tkinter import ttk
from utility import *
from table.bicycle_table import ProxyCreateTable
from table.bicycle_dao import *

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title("Bicycle sharing system")
create = ProxyCreateTable()
create.load_data(file_name=PATH_JOURNEY_CSV, columns=JOURNEY_COLUMN, tablename=JOURNEY_TABLE_NAME)
create.load_data(file_name=PATH_STATION_CSV, columns=STATION_COLUMN, tablename=STATION_TABLE_NAME)
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
my_tree['columns'] = JOURNEY_COLUMN
my_tree.column("#0", width=0, stretch=tk.NO)
my_tree.column(f"{JOURNEY_COLUMN[0]}", anchor=tk.W, width=100)
my_tree.column(f"{JOURNEY_COLUMN[1]}", anchor=tk.W, width=100)
my_tree.column(f"{JOURNEY_COLUMN[2]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[3]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[4]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[5]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[6]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[7]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[8]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[9]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[10]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[11]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[12]}", anchor=tk.CENTER, width=100)
my_tree.column(f"{JOURNEY_COLUMN[13]}", anchor=tk.CENTER, width=100)

my_tree.heading("#0", text="", anchor=tk.W)
my_tree.heading(f"{JOURNEY_COLUMN[0]}", text=f"{JOURNEY_COLUMN[0]}", anchor=tk.W)
my_tree.heading(f"{JOURNEY_COLUMN[1]}", text=f"{JOURNEY_COLUMN[1]}", anchor=tk.W)
my_tree.heading(f"{JOURNEY_COLUMN[2]}", text=f"{JOURNEY_COLUMN[2]}", anchor=tk.CENTER)
my_tree.heading(f"{JOURNEY_COLUMN[3]}", text=f"{JOURNEY_COLUMN[3]}", anchor=tk.CENTER)
my_tree.heading(f"{JOURNEY_COLUMN[4]}", text=f"{JOURNEY_COLUMN[4]}", anchor=tk.CENTER)
my_tree.heading(f"{JOURNEY_COLUMN[5]}", text=f"{JOURNEY_COLUMN[5]}", anchor=tk.W)
my_tree.heading(f"{JOURNEY_COLUMN[6]}", text=f"{JOURNEY_COLUMN[6]}", anchor=tk.W)
my_tree.heading(f"{JOURNEY_COLUMN[7]}", text=f"{JOURNEY_COLUMN[7]}", anchor=tk.CENTER)
my_tree.heading(f"{JOURNEY_COLUMN[8]}", text=f"{JOURNEY_COLUMN[8]}", anchor=tk.CENTER)
my_tree.heading(f"{JOURNEY_COLUMN[9]}", text=f"{JOURNEY_COLUMN[9]}", anchor=tk.CENTER)
my_tree.heading(f"{JOURNEY_COLUMN[10]}", text=f"{JOURNEY_COLUMN[10]}", anchor=tk.W)
my_tree.heading(f"{JOURNEY_COLUMN[11]}", text=f"{JOURNEY_COLUMN[11]}", anchor=tk.W)
my_tree.heading(f"{JOURNEY_COLUMN[12]}", text=f"{JOURNEY_COLUMN[12]}", anchor=tk.CENTER)
my_tree.heading(f"{JOURNEY_COLUMN[13]}", text=f"{JOURNEY_COLUMN[13]}", anchor=tk.CENTER)

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")
data_frame = tk.LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()
num4 = tk.StringVar()
num5 = tk.StringVar()
num6 = tk.StringVar()
num7 = tk.StringVar()
num8 = tk.StringVar()
num9 = tk.StringVar()
num10 = tk.StringVar()
num11 = tk.StringVar()
num12 = tk.StringVar()
num13 = tk.StringVar()

journey_id_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[0]}")
journey_id_label.grid(row=0, column=0, padx=10, pady=10)
journey_id_entry = tk.Entry(data_frame)
journey_id_entry.grid(row=0, column=1, padx=10, pady=10)

journey_duration_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[1]}")
journey_duration_label.grid(row=0, column=2, padx=10, pady=10)
journey_duration_entry = tk.Entry(data_frame, textvariable=num1)
journey_duration_entry.grid(row=0, column=3, padx=10, pady=10)

end_date_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[2]}")
end_date_label.grid(row=0, column=4, padx=10, pady=10)
end_date_entry = tk.Entry(data_frame, textvariable=num2)
end_date_entry.grid(row=0, column=5, padx=10, pady=10)

end_month_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[3]}")
end_month_label.grid(row=0, column=6, padx=10, pady=10)
end_month_entry = tk.Entry(data_frame, textvariable=num3)
end_month_entry.grid(row=0, column=7, padx=10, pady=10)

end_year_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[4]}")
end_year_label.grid(row=0, column=8, padx=10, pady=10)
end_year_entry = tk.Entry(data_frame, textvariable=num4)
end_year_entry.grid(row=0, column=9, padx=10, pady=10)

end_hour_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[5]}")
end_hour_label.grid(row=0, column=10, padx=10, pady=10)
end_hour_entry = tk.Entry(data_frame, textvariable=num5)
end_hour_entry.grid(row=0, column=11, padx=10, pady=10)

end_minute_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[6]}")
end_minute_label.grid(row=1, column=0, padx=10, pady=10)
end_minute_entry = tk.Entry(data_frame, textvariable=num6)
end_minute_entry.grid(row=1, column=1, padx=10, pady=10)

end_station_id_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[7]}")
end_station_id_label.grid(row=1, column=2, padx=10, pady=10)
end_station_id_entry = tk.Entry(data_frame, textvariable=num7)
end_station_id_entry.grid(row=1, column=3, padx=10, pady=10)

start_date_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[8]}")
start_date_label.grid(row=1, column=4, padx=10, pady=10)
start_date_entry = tk.Entry(data_frame, textvariable=num8)
start_date_entry.grid(row=1, column=5, padx=10, pady=10)

start_month_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[9]}")
start_month_label.grid(row=1, column=6, padx=10, pady=10)
start_month_entry = tk.Entry(data_frame, textvariable=num9)
start_month_entry.grid(row=1, column=7, padx=10, pady=10)

start_year_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[10]}")
start_year_label.grid(row=1, column=8, padx=10, pady=10)
start_year_entry = tk.Entry(data_frame, textvariable=num10)
start_year_entry.grid(row=1, column=9, padx=10, pady=10)

start_hour_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[11]}")
start_hour_label.grid(row=1, column=2, padx=10, pady=10)
start_hour_entry = tk.Entry(data_frame, textvariable=num11)
start_hour_entry.grid(row=1, column=3, padx=10, pady=10)

start_minute_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[12]}")
start_minute_label.grid(row=1, column=2, padx=10, pady=10)
start_minute_entry = tk.Entry(data_frame, textvariable=num12)
start_minute_entry.grid(row=1, column=3, padx=10, pady=10)

start_station_id_label = tk.Label(data_frame, text=f"{JOURNEY_COLUMN[13]}")
start_station_id_label.grid(row=1, column=2, padx=10, pady=10)
start_station_id_entry = tk.Entry(data_frame, textvariable=num13)
start_station_id_entry.grid(row=1, column=3, padx=10, pady=10)

create_record = FactoryDAO(CreateJourneyDao)

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
    journey_id_entry.delete(0, tk.END)
    journey_duration_entry.delete(0, tk.END)
    end_date_entry.delete(0, tk.END)
    end_month_entry.delete(0, tk.END)
    end_year_entry.delete(0, tk.END)
    end_hour_entry.delete(0, tk.END)
    end_minute_entry.delete(0, tk.END)
    end_station_id_entry.delete(0, tk.END)
    start_date_entry.delete(0, tk.END)
    start_month_entry.delete(0, tk.END)
    start_year_entry.delete(0, tk.END)
    start_hour_entry.delete(0, tk.END)
    start_minute_entry.delete(0, tk.END)
    start_station_id_entry.delete(0, tk.END)

# Select Record
def select_record(e):
	# Clear entry boxes
    journey_id_entry.delete(0, tk.END)
    journey_duration_entry.delete(0, tk.END)
    end_date_entry.delete(0, tk.END)
    end_month_entry.delete(0, tk.END)
    end_year_entry.delete(0, tk.END)
    end_hour_entry.delete(0, tk.END)
    end_minute_entry.delete(0, tk.END)
    end_station_id_entry.delete(0, tk.END)
    start_date_entry.delete(0, tk.END)
    start_month_entry.delete(0, tk.END)
    start_year_entry.delete(0, tk.END)
    start_hour_entry.delete(0, tk.END)
    start_minute_entry.delete(0, tk.END)
    start_station_id_entry.delete(0, tk.END)

	# Grab record Number
    selected = my_tree.focus()
	# Grab record values
    values = my_tree.item(selected, 'values')

	# outpus to entry boxes
    journey_id_entry.insert(0, values[0])
    journey_duration_entry.insert(0, values[1])
    end_date_entry.insert(0, values[2])
    end_month_entry.insert(0, values[3])
    end_year_entry.insert(0, values[4])
    end_hour_entry.insert(0, values[5])
    end_minute_entry.insert(0, values[6])
    end_station_id_entry.insert(0, values[7])
    start_date_entry.insert(0, values[8])
    start_month_entry.insert(0, values[9])
    start_year_entry.insert(0, values[10])
    start_hour_entry.insert(0, values[11])
    start_minute_entry.insert(0, values[12])
    start_station_id_entry.insert(0, values[13])

# Update record
def update_record():
    # Grab the record number
    selected = my_tree.focus()
	# Update record
    find_record = create_record.find_id(journey_id_entry.get())
    if journey_duration_entry.get() == "":
        num1.set(f"{find_record[0][1]}")
    if end_date_entry.get() == "":
        num2.set(f"{find_record[0][2]}")
    if end_month_entry.get() == "":
        num3.set(f"{find_record[0][3]}")
    if end_year_entry.get() == "":
        num4.set(f"{find_record[0][4]}")
    if end_hour_entry.get() == "":
        num5.set(f"{find_record[0][5]}")
    if end_minute_entry.get() == "":
        num6.set(f"{find_record[0][6]}")
    if end_station_id_entry.get() == "":
        num7.set(f"{find_record[0][7]}")
    if start_date_entry.get() == "":
        num8.set(f"{find_record[0][8]}")
    if start_month_entry.get() == "":
        num9.set(f"{find_record[0][9]}")
    if start_year_entry.get() == "":
        num10.set(f"{find_record[0][10]}")
    if start_hour_entry.get() == "":
        num11.set(f"{find_record[0][11]}")
    if start_minute_entry.get() == "":
        num12.set(f"{find_record[0][12]}")
    if start_station_id_entry.get() == "":
        num13.set(f"{find_record[0][13]}")
    print(f"{find_record[0][3]}")
    print(f"{end_month_entry.get()}")
    my_tree.item(selected, text="", values=(journey_id_entry.get(), journey_duration_entry.get(), end_date_entry.get(), end_month_entry.get(), end_year_entry.get(), end_hour_entry.get(), end_minute_entry.get(), end_station_id_entry.get(), start_date_entry.get(), start_month_entry.get(), start_year_entry.get(), start_hour_entry.get(), start_minute_entry.get(), start_station_id_entry.get()))
    
    create_record.update_journey_by_id(journey_id_entry.get(), journey_duration=int(journey_duration_entry.get()), end_date=int(end_date_entry.get()), end_month=int(end_month_entry.get()), end_year=int(end_year_entry.get()), end_hour=int(end_hour_entry.get()), end_minute=int(end_minute_entry.get()), end_station_id=int(end_station_id_entry.get()), start_date=int(start_date_entry.get()), start_month=int(start_month_entry.get()), start_year=int(start_year_entry.get()), start_hour=int(start_hour_entry.get()), start_minute=int(start_minute_entry.get()), start_station_id=int(start_station_id_entry.get()))
    
    # Clear entry boxes
    journey_id_entry.delete(0, tk.END)
    journey_duration_entry.delete(0, tk.END)
    end_date_entry.delete(0, tk.END)
    end_month_entry.delete(0, tk.END)
    end_year_entry.delete(0, tk.END)
    end_hour_entry.delete(0, tk.END)
    end_minute_entry.delete(0, tk.END)
    end_station_id_entry.delete(0, tk.END)
    start_date_entry.delete(0, tk.END)
    start_month_entry.delete(0, tk.END)
    start_year_entry.delete(0, tk.END)
    start_hour_entry.delete(0, tk.END)
    start_minute_entry.delete(0, tk.END)
    start_station_id_entry.delete(0, tk.END)

#Search
def searh():
    find_id = create_record.find_id(int(journey_id_entry.get()))
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

count = 0
records = create_record.find_all()
for record in records:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13]), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11], record[12], record[13]), tags=('oddrow',))
	# increment counter
	count += 1

root.mainloop()