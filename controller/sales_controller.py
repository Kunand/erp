
from model.sales import sales
from view import terminal as view
from model import util

"""
def list_transactions(file_name):
    view.print_error_message("Not implemented yet.")
    print(sales.read_table_from_file(file_name, separator=';'))
"""

def add_transaction():
    view.print_error_message("Not implemented yet.")
    added_new = []
    gen_id = util.generate_id()
    added_new.append(gen_id)
    for i in range(1, len(sales.HEADERS)):
        if i == 1:
            get_costumer = input(sales.HEADERS[i])
            added_new.append(get_costumer)
        elif i == 2:
            get_product = input(sales.HEADERS[i])
            added_new.append(get_product)
        elif i == 3:
            get_price = input(sales.HEADERS[i])
            added_new.append(get_price)
        elif i == 4:
            get_date = input(sales.HEAREDS[i])
            added_new.append(get_date)

    with open("/Documents/erp/model/sales.csv", "a") as fil:
        append_row = csv.writer(fil)
        append_row.writerow(added_new)

    return added_new


def update_transaction():
    view.print_error_message("Not implemented yet.")
    with open("/Documents/erp/model/sales.csv", "w") as fil:
        find_id = input("Enter the id")
        for line in fil:
            if find_id in line:
                headers_element = input("Enter a number from 1 to 4")
                update = input("Enter the changes")
                if headers_element == "1":
                    line[1] = headers_element
                elif headers_element == "2":
                    line[2] = headers_element
                elif headers_element == "3":
                    line[3] = headers_element
                elif headers_element == "4":
                    line[4] = headers_element
    return fil

"""
def delete_transaction():
    view.print_error_message("Not implemented yet.")
    with open("/Documents/erp/model/sales.csv", "w") as fil:
        delet = input("Enter an ID")
        for line in fil:
            if

"""
def get_biggest_revenue_transaction():
    view.print_error_message("Not implemented yet.")


def get_biggest_revenue_product():
    view.print_error_message("Not implemented yet.")


def count_transactions_between():
    view.print_error_message("Not implemented yet.")


def sum_transactions_between():
    view.print_error_message("Not implemented yet.")


def run_operation(option):
    if option == 1:
        list_transactions(DATAFILE)
    elif option == 2:
        add_transaction()
    elif option == 3:
        update_transaction()
    elif option == 4:
        delete_transaction()
    elif option == 5:
        get_biggest_revenue_transaction()
    elif option == 6:
        get_biggest_revenue_product()
    elif option == 7:
        count_transactions_between()
    elif option == 8:
        sum_transactions_between()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List transactions",
               "Add new transaction",
               "Update transaction",
               "Remove transaction",
               "Get the transaction that made the biggest revenue",
               "Get the product that made the biggest revenue altogether",
               "Count number of transactions between",
               "Sum number of transactions between"]
    view.print_menu("Sales", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)