from tkinter import *

# Quit subroutine
def quit_app():
    main_window.destroy()

# Print details of all the items in the inventory
def print_inventory_details():
    item_count = 0
    # Create the column headings
    Label(main_window, font=("Helvetica 10 bold"), text="Row").grid(column=0, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Name").grid(column=1, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="").grid(column=2, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Quantity").grid(column=3, row=7)
    Label(main_window, font=("Helvetica 10 bold"), text="Price").grid(column=4, row=7)
    # Add each item in the list into its own row
    while item_count < counters['total_entries']:
        Label(main_window, text=item_count).grid(column=0, row=item_count+8)
        Label(main_window, text=(inventory_details[item_count][0])).grid(column=1, row=item_count+8)
        Label(main_window, text=(inventory_details[item_count][1])).grid(column=2, row=item_count+8)
        Label(main_window, text=(inventory_details[item_count][2])).grid(column=3, row=item_count+8)
        Label(main_window, text=(inventory_details[item_count][3])).grid(column=4, row=item_count+8)
        item_count += 1
        counters['item_count'] = item_count

# Check the inputs are all valid
def check_inputs():
    input_check = 0
    Label(main_window, text="               ").grid(column=2, row=0)
    Label(main_window, text="               ").grid(column=2, row=1)
    Label(main_window, text="               ").grid(column=2, row=2)
    Label(main_window, text="               ").grid(column=2, row=3)
    # Check that customer name is not blank, set error text if blank
    if len(entry_product_name.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=0)
        input_check = 1
    # Check that category is not blank, set error text if blank
    if len(entry_category.get()) == 0:
        Label(main_window, fg="red", text="Required").grid(column=2, row=1)
        input_check = 1
    # Check the quantity is not blank and is a positive integer, set error text if blank or invalid
    if (entry_quantity.get().isdigit()):
        if int(entry_quantity.get()) <= 0:
            Label(main_window, fg="red", text="Positive number only").grid(column=2, row=2)
            input_check = 1
    else:
        Label(main_window, fg="red", text="Positive number only").grid(column=2, row=2)
        input_check = 1
    # Check that price is not blank and is a valid number, set error text if blank or invalid
    try:
        price = float(entry_price.get())
        if price <= 0:
            raise ValueError
    except ValueError:
        Label(main_window, fg="red", text="Valid price required").grid(column=2, row=3)
        input_check = 1

    if input_check == 0:
        append_item()

# Add the next item to the inventory list
def append_item():
    # Append each item to its own area of the list
    inventory_details.append([entry_product_name.get(), entry_category.get(), entry_quantity.get(), entry_price.get()])
    # Clear the input boxes
    entry_product_name.delete(0, 'end')
    entry_category.delete(0, 'end')
    entry_quantity.delete(0, 'end')
    entry_price.delete(0, 'end')
    counters['total_entries'] += 1

# Delete a row from the inventory list
def delete_row():
    # Find which row is to be deleted and delete it
    del inventory_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    item_count = counters['item_count']
    delete_item.delete(0, 'end')
    # Clear the last item displayed on the GUI
    Label(main_window, text="       ").grid(column=0, row=item_count+7)
    Label(main_window, text="       ").grid(column=1, row=item_count+7)
    Label(main_window, text="       ").grid(column=2, row=item_count+7)
    Label(main_window, text="       ").grid(column=3, row=item_count+7)
    Label(main_window, text="       ").grid(column=4, row=item_count+7)
    # Print all the items in the list
    print_inventory_details()

# Create the buttons and labels
def setup_buttons():
    # Create all the empty and default labels, buttons, and entry boxes. Put them in the correct grid location
    Label(main_window, text="Customer Name").grid(column=0, row=0, sticky=E)
    Label(main_window, text="Item customer has hired").grid(column=0, row=1, sticky=E)
    Button(main_window, text="Quit", command=quit_app, width=10, bnBg="snow2").grid(column=4, row=0, sticky=E)
    Button(main_window, text="Append Details", command=check_inputs, bg="snow2").grid(column=3, row=1)
    Button(main_window, text="Print Details", command=print_inventory_details, width=10, bg="snow2").grid(column=4, row=1, sticky=E)
    Label(main_window, text="How many items the customer has hired").grid(column=0, row=2, sticky=E)
    Label(main_window, text="Row #").grid(column=3, row=2, sticky=E)
    Button(main_window, text="Delete Row", command=delete_row, width=10, bg="snow2").grid(column=4, row=3, sticky=E)
    Label(main_window, text="               ").grid(column=2, row=0)

# Start the program running
def main():
    # Set window border color and thickness
    main_window.configure(bg='dark slate gray')
    main_window['highlightbackground'] = 'dark slate gray'
    main_window['highlightcolor'] = 'dark slate gray'
    main_window['highlightthickness'] = 10
   
    # Start the GUI
    setup_buttons()
    main_window.mainloop()

# Create empty list for inventory details and empty variable for entries in the list
counters = {'total_entries': 0, 'item_count': 0}
inventory_details = []
main_window = Tk()
entry_product_name = Entry(main_window)
entry_product_name.grid(column=1, row=0)
entry_category = Entry(main_window)
entry_category.grid(column=1, row=1)
entry_quantity = Entry(main_window)
entry_quantity.grid(column=1, row=2)
entry_price = Entry(main_window)
entry_price.grid(column=1, row=3)
delete_item = Entry(main_window)
delete_item.grid(column=3, row=3)
main()


