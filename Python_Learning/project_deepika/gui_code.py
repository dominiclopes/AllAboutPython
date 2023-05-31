from tkinter import *


top = Tk(screenName="1", baseName="2", className="sequent peak algorithm", useTk=1, sync=0, use=None)

# Code to add widgets will go here...
L1 = Label(top, text="Range of year for calculation")
L1.pack()
start = Entry(top, bd=10)
start.insert(END, "2000")
start.pack()
end = Entry(top, bd=10)
end.insert(END, "2005")
end.pack()


def create_input_table():
    # Add Entry for the inflow and display cumulative inflow
    inflow_entry_list_dict = []
    for counter in range(int(end.get()) - int(start.get()) + 1):
        year_label = Label(top, text=int(start.get()) + counter)
        year_label.pack()
        new_entry = Entry(top, bd=2)
        new_entry.pack()
        cumulative_inflow_value_label = Label(top, text="I'll print something later")
        cumulative_inflow_value_label.pack()
        inflow_entry_list_dict.append({"label": year_label, "entry": new_entry,
                                       "cumulative": cumulative_inflow_value_label})




B = Button(top, text="Enter Data for these months", command=create_input_table)
B.pack()

top.mainloop()

