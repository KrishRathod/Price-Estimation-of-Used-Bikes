from tkinter import *
from tkinter.ttk import *
import mysql.connector

master = Tk()
master.title('Used Bike Price Estimation Software')
master.geometry("900x600")
base_frame = Frame(master)
base_frame.pack()

wrong_input_lable1 = Label(master)
wrong_input_lable2 = Label(master)
wrong_input_lable3 = Label(master)
wrong_input_lable4 = Label(master)
wrong_input_lable5 = Label(master)

purchase_value = 0

s = Style()
s.configure('My.TFrame', background='#c4dfe6')

sto = Style()
sto.configure('W.TButton', font=('Arial', 20, 'bold'),
              background='#66a5ad', foreground='#07575b')


bike_name_options = {"Please select brand": 0, "Bajaj": 4, "Hero": 3, "Honda": 5, "Royal Enfield": 3,
                     "Suzuki": 6, "TVS": 4, "Yamaha": 4, "Aprilia": 7,
                     "Avantura Choppers": 5, "Bajaj": 3, "Benelli": 4,
                     "BMW": 6, "Carberry": 8, "CFMoto": 5, "Ducati": 3,
                     "Global Automobiles": 6, "Harley-davson": 5,
                     "Husqvarna": 8, "Hyosung": 4, "Indian": 6,
                     "Jawa": 4, "Kawasaki": 7, "Kinetic": 8, "KTM": 6, "LML": 2,
                     "Mahindra": 6, "Moto Guzzi": 8, "Regal Raptor": 5,
                     "Revolt": 5, "Triumph": 4}

year_of_purchase_list = ['2000', '2001', '2002', '2003',
                         '2004', '2005', '2006', '2007',
                         '2008', '2009', '2010', '2011',
                         '2012', '2013', '2014', '2015',
                         '2016', '2017', '2018', '2019', ]

State_dictionary = {"Andhra Pradesh": 5, "Andaman Nicobar": 4, "Arunachal Pradesh": 3, "Assam": 5, "Bihar": 5,
                    "Chandigarh": 5, "Chhattisgarh": 4, "Dadra Nagar Haveli": 3, "Daman n Diu": 5, "Delhi": 5, "Goa": 4,
                    "Gujarat": 5, "Haryana": 4, "Himachal Pradesh": 3, "Jammu Kashmir": 5, "Jharkhand": 6, "Karnataka": 3,
                    "Kerala": 5, "Lakshadweep": 4, "Madhya Pradesh": 3, "Maharashtra": 5, "Manipur": 6, "Meghalaya": 4,
                    "Mizoram": 5, "Nagaland": 4, "Orissa": 3, "Pondicherry": 3, "Punjab": 5, "Rajasthan": 6, "Sikkim": 7,
                    "Tamil Nadu": 5, "Telangana": 4, "Tripura": 3, "Uttar Pradesh": 5, "Utarakhand": 6, "West Bengal": 6}


def Calculate():
    global buy_price, bike_manufacturer, year_purchase, state_from, Kms_driven, purchase_value
    purchase_value = buy_price
    buy_price = buy_price*((0.95)**(2020-int(year_purchase)))
    buy_price = buy_price - buy_price * \
        (bike_name_options[bike_manufacturer]/100)*2
    buy_price = buy_price - buy_price*(State_dictionary[state_from]/100)
    factor = 5
    if Kms_driven >= 500000:
        factor = 50
    elif Kms_driven >= 100000:
        factor = 25
    elif Kms_driven >= 50000:
        factor = 15
    elif Kms_driven >= 30000:
        factor = 10
    elif Kms_driven >= 20000:
        factor = 8
    elif Kms_driven >= 10000:
        factor = 6
    buy_price = buy_price - buy_price*(factor/100)
    buy_price = int(buy_price)


def save_record():
    global buy_price, bike_manufacturer, year_purchase, state_from, Kms_driven, purchase_value
    mydb = mysql.connector.connect(
        host="localhost", user="root", passwd="toor", database="price_estimation")
    mycursor = mydb.cursor()
    command = "insert into history(buy_price,bike_manufacturer,year_purchase,state_from,Kms_driven,purchase_price) values(%s,%s,%s,%s,%s,%s);"
    data = [(buy_price, bike_manufacturer, year_purchase,
             state_from, Kms_driven, purchase_value)]
    try:
        mycursor.executemany(command, data)
        mydb.commit()
    except:
        mydb.rollback()
        print('error')
    return


def show_new_price(curr_frame):
    global buy_price

    desc_label = Label(
        curr_frame, text='Condition', font=("Helvetica", 10, 'bold'), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=6, column=0, padx=10, pady=5, sticky=NSEW)
    desc_label = Label(
        curr_frame, text='Resale value', font=("Helvetica", 10, 'bold'), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=6, column=1, padx=0, pady=5, sticky=NSEW)

    desc_label = Label(
        curr_frame, text='Good', font=("Helvetica", 10, 'bold'), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=7, column=0, padx=10, pady=0, sticky=NSEW)
    desc_label = Label(
        curr_frame, text=str(buy_price), font=("Helvetica", 10, 'bold'), width=20, borderwidth=10, relief="sunken", anchor=CENTER, foreground="green")
    desc_label.grid(row=7, column=1, padx=0, pady=0, sticky=NSEW)

    desc_label = Label(
        curr_frame, text='Fair', font=("Helvetica", 10, 'bold'), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=8, column=0, padx=10, pady=0, sticky=NSEW)
    desc_label = Label(
        curr_frame, text=str(int(buy_price*0.95)), font=("Helvetica", 10, 'bold'), width=20, borderwidth=10, relief="sunken", anchor=CENTER, foreground="#E8AC41")
    desc_label.grid(row=8, column=1, padx=0, pady=0, sticky=NSEW)

    desc_label = Label(
        curr_frame, text='Bad', font=("Helvetica", 10, 'bold'), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=9, column=0, padx=10, pady=0, sticky=NSEW)
    desc_label = Label(
        curr_frame, text=str(int(buy_price*0.90)), font=("Helvetica", 10, 'bold'), width=20, borderwidth=10, relief="sunken", anchor=CENTER, foreground="red")
    desc_label.grid(row=9, column=1, padx=0, pady=0, sticky=NSEW)
    return


def check(curr_frame):
    global buy_price, bike_manufacturer, year_purchase, state_from, Kms_driven
    global wrong_input_lable1, wrong_input_lable2, wrong_input_lable3, wrong_input_lable4, wrong_input_lable5
    flag = TRUE
    wrong_input_lable1.grid_forget()
    wrong_input_lable2.grid_forget()
    wrong_input_lable3.grid_forget()
    wrong_input_lable5.grid_forget()
    wrong_input_lable4.grid_forget()

    try:
        buy_price = int(buy_price)
    except:
        wrong_input_lable1 = Label(
            curr_frame, text='*Wrong input', font=("Helvetica", 10), width=25, foreground="red",background='#c4dfe6')
        wrong_input_lable1.grid(row=1, column=2, padx=6, pady=10, sticky=NSEW)
        flag = FALSE

    try:
        Kms_driven = int(Kms_driven)
    except:
        wrong_input_lable2 = Label(
            curr_frame, text='*Wrong input', font=("Helvetica", 10), width=25, foreground="red",background='#c4dfe6')
        wrong_input_lable2.grid(row=5, column=2, padx=6, pady=10, sticky=NSEW)
        flag = FALSE

    if bike_manufacturer == 'Please select brand':
        wrong_input_lable3 = Label(
            curr_frame, text='*Wrong selection', font=("Helvetica", 10), width=25, foreground="red",background='#c4dfe6')
        wrong_input_lable3.grid(row=2, column=2, padx=6, pady=10, sticky=NSEW)
        flag = FALSE

    if year_purchase == 'Please select year':
        wrong_input_lable4 = Label(
            curr_frame, text='*Wrong selection', font=("Helvetica", 10), width=25, foreground="red",background='#c4dfe6')
        wrong_input_lable4.grid(row=3, column=2, padx=6, pady=10, sticky=NSEW)
        flag = FALSE

    if state_from == 'Please select State':
        wrong_input_lable5 = Label(
            curr_frame, text='*Wrong selection', font=("Helvetica", 10), width=25, foreground="red",background='#c4dfe6')
        wrong_input_lable5.grid(row=4, column=2, padx=6, pady=10, sticky=NSEW)
        flag = FALSE
    return flag


def Calculation_page(curr_frame):
    s = Style()
    s.configure('My.TFrame', background='#c4dfe6')

    sto = Style()
    sto.configure('W.TButton', font=('Arial', 20, 'bold'),
                  background='#66a5ad', foreground='#07575b')
    curr_frame.forget()

    def Submit_details():
        global buy_price, bike_manufacturer, year_purchase, state_from, Kms_driven
        buy_price = price_entry.get()
        bike_manufacturer = bike_name_list.get()
        year_purchase = year_purchase_list.get()
        state_from = state_from_list.get()
        Kms_driven = kms_entry.get()
        if check(calculation_page):
            Calculate()
            save_record()
            show_new_price(calculation_page)

    curr_frame.forget()
    calculation_page = Frame(master, style='My.TFrame')
    calculation_page.pack(fill=BOTH, expand=True)

    info_lable = Label(
        calculation_page, text='Please provide correct details for proper evaluation', font=("Helvetica", 16), background='#66a5ad')
    info_lable.grid(row=0, column=0, pady=30, padx=10, columnspan=10, sticky=W)

    purchase_price_lable = Label(
        calculation_page, text='Please enter purchase price :', font=("Helvetica", 10), width=35, background='#66a5ad')
    purchase_price_lable.grid(row=1, column=0, padx=10, pady=5, sticky=W)

    price_entry = Entry(calculation_page, width=23)
    price_entry.grid(row=1, column=1, pady=5, padx=0, sticky=W)

    bike_name_lable = Label(calculation_page, text='Please Select Brand :', font=(
        "Helvetica", 10), width=35, background='#66a5ad')
    bike_name_lable.grid(row=2, column=0, padx=10, pady=5, sticky=W)

    bike_name_list = Combobox(
        calculation_page, values=list(bike_name_options), state="readonly")
    bike_name_list.set('Please select brand')
    bike_name_list.grid(row=2, column=1, pady=10, sticky=W)

    year_purchase_lable = Label(
        calculation_page, text='Please Select year of purchase :', font=("Helvetica", 10), width=35, background='#66a5ad')
    year_purchase_lable.grid(row=3, column=0, padx=10, pady=5, sticky=W)

    year_purchase_list = Combobox(
        calculation_page, values=year_of_purchase_list, state="readonly")
    year_purchase_list.set('Please select year')
    year_purchase_list.grid(row=3, column=1, pady=10, sticky=W)

    year_purchase_lable = Label(
        calculation_page, text='Please select state :', font=("Helvetica", 10), width=35, background='#66a5ad')
    year_purchase_lable.grid(row=4, column=0, padx=10, pady=5, sticky=W)

    state_from_list = Combobox(calculation_page, values=list(
        State_dictionary), state="readonly")
    state_from_list.set('Please select State')
    state_from_list.grid(row=4, column=1, pady=10, sticky=W)

    kms_lable = Label(calculation_page, text='Please enter KM\'s Driven :', font=(
        "Helvetica", 10), width=35, background='#66a5ad')
    kms_lable.grid(row=5, column=0, padx=10, pady=5, sticky=W)

    kms_entry = Entry(calculation_page, width=23)
    kms_entry.grid(row=5, column=1, pady=5, padx=0, sticky=W)

    Button_back = Button(
        calculation_page, text='Previous', style='W.TButton', width=8, command=lambda: main_page(calculation_page))
    Button_back.grid(row=10, column=0, pady=20, padx=10, sticky=W)

    Button_calculate_price = Button(
        calculation_page, text='Submit', style='W.TButton', width=8, command=Submit_details)
    Button_calculate_price.grid(row=10, column=1, pady=20, sticky=E)


def History_page(curr_frame):
    curr_frame.forget()
    history_page = Frame(master, style='My.TFrame')
    history_page.pack(fill=BOTH, expand=True)

    Button_back = Button(
        history_page, text='Previous', style='W.TButton', width=8, command=lambda: main_page(history_page))
    Button_back.grid(row=0, column=0, padx=10, pady=20, sticky=W)

    Button_calculate_price = Button(
        history_page, text='Exit', style='W.TButton', width=6, command=master.quit)
    Button_calculate_price.grid(row=0, column=5, pady=20, sticky=E)

    desc_label = Label(
        history_page, text="Resale Price", font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=1, column=0, padx=10, pady=5, sticky=NSEW)
    desc_label = Label(
        history_page, text="Purchase Price", font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=1, column=1, padx=0, pady=5, sticky=NSEW)
    desc_label = Label(
        history_page, text="Company", font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=1, column=2, padx=0, pady=5, sticky=NSEW)
    desc_label = Label(
        history_page, text="Purchase Year", font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=1, column=3, padx=0, pady=5, sticky=NSEW)
    desc_label = Label(
        history_page, text="State", font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=1, column=4, padx=0, pady=5, sticky=NSEW)
    desc_label = Label(
        history_page, text="KM Driven", font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
    desc_label.grid(row=1, column=5, padx=0, pady=5, sticky=NSEW)
    

    mydb = mysql.connector.connect(
        host="localhost", user="root", passwd="toor", database="price_estimation")
    mycursor = mydb.cursor()

    mycursor.execute("select * from history")
    result = mycursor.fetchall()

    for i in range(len(result)):
        buy_price, bike_manufacturer, year_purchase, state_from, Kms_driven, purchase_value = result[
            i]
        desc_label = Label(
            history_page, text=str(buy_price), font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER,foreground="green")
        desc_label.grid(row=i+2, column=0, padx=10,
                        pady=5, sticky=NSEW)
        desc_label = Label(
            history_page, text=str(purchase_value), font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER,foreground="red")
        desc_label.grid(row=i+2, column=1, padx=0,
                        pady=5, sticky=NSEW)
        desc_label = Label(
            history_page, text=bike_manufacturer, font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
        desc_label.grid(row=i+2, column=2, padx=0,
                        pady=5, sticky=NSEW)
        desc_label = Label(
            history_page, text=year_purchase, font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
        desc_label.grid(row=i+2, column=3, padx=0,
                        pady=5, sticky=NSEW)
        desc_label = Label(
            history_page, text=state_from, font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
        desc_label.grid(row=i+2, column=4, padx=0,
                        pady=5, sticky=NSEW)
        desc_label = Label(
            history_page, text=str(Kms_driven), font=("Helvetica", 10), width=20, borderwidth=10, relief="sunken", anchor=CENTER)
        desc_label.grid(row=i+2, column=5, padx=0,
                        pady=5, sticky=NSEW)
        


def main_page(curr_frame):
    s = Style()
    s.configure('My.TFrame', background='#c4dfe6')
    sto = Style()
    sto.configure('W.TButton', font=('Arial', 20, 'bold'),
                  background='#66a5ad', foreground='#07575b')
    curr_frame.forget()
    main_page = Frame(master, style='My.TFrame')
    main_page.pack(fill=BOTH, expand=True)
    lable = Label(main_page, text='Welcome to bike price estimation software', anchor=CENTER, background="#66a5ad",
                  foreground="#003b46", font="arial 15 bold")
    lable.pack(pady=20, fill=BOTH)

    Button_calculate_price = Button(
        main_page, text='Check Price', style='W.TButton', command=lambda: Calculation_page(main_page))
    Button_calculate_price.pack(pady=10)

    Button_View_History = Button(
        main_page, text='History', style='W.TButton', command=lambda: History_page(main_page))
    Button_View_History.pack(pady=10)

    Button_exit = Button(main_page, text='Exit',
                         style='W.TButton', command=master.quit)
    Button_exit.pack(pady=10)


main_page(base_frame)
master.mainloop()
