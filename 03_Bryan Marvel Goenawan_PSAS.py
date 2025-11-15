import tkinter as tk
from tkinter import ttk
from datetime import datetime

CustomerData = []
loggeduser = ""

def openpage(frame):
    frame.tkraise()

def login():
    username = loginUser.get()
    password = loginPassword.get()
    if username == "Feianzach" and password == "12345":
        loginUser.delete(0, tk.END)
        loginPassword.delete(0, tk.END)
        loginstatus.config(text="")
        global loggeduser
        loggeduser = username
        openpage(hal2)
        try:
            hello.config(text=f"Hello, {loggeduser}")
        except NameError:
            pass
    elif not username or not password:
        loginstatus.config(text="All Data Must Be Filled", foreground="#d40707")
    else:
        loginstatus.config(text="Username or Password is Invalid", foreground="#d40707")
def logOut():
    darkmode.set(0)
    style.configure("TFrame", background="#F5DE76")
    style.configure("TLabel", background="#F5DE76", foreground="black")
    style.configure("TButton", background="#ececec", foreground="black")
    style.map("TButton", background=[("active", "white")])
    style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", foreground="black")
    style.configure("Treeview.Heading", background="#4682b4", foreground="white")
    openpage(hal1)


def priceCalculation():
    startingprice = priceEntry.get()
    totalnights = bookedNightsEntry.get()
    if startingprice.isdigit() and totalnights.isdigit():
        floatedprice = float(startingprice)
        intnights = int(totalnights)
        result.config(text=f"Total = ${floatedprice*intnights}", foreground="green")
    elif not startingprice.isdigit() or not totalnights.isdigit():
        result.config(text="Booked Nights and Starting Price Must be a digit", foreground="#d40707")
    else:
        result.config(text="Booked Nights and Starting Price Must Be Filled", foreground="#d40707")

def updateprice(event):
    roomtype = comboRoom.get()
    if roomtype in room_prices:
        price = room_prices[roomtype]
        priceEntry.config(state="normal")
        priceEntry.delete(0, tk.END)
        priceEntry.insert(0, price)
        priceEntry.config(state="readonly")

def datastore():
    customerName = nameEntry.get()
    checkInDate = checkInEntry.get()
    totalnights = bookedNightsEntry.get()
    roomType = comboRoom.get()
    startingprice = priceEntry.get()
    if not customerName or not checkInEntry or not totalnights or not roomType or not startingprice:
        confirmation.config(text="All Columns Must Be Filled", foreground="#d40707")
        return
    try:
        datetime.strptime(checkInDate, "%d/%m/%y")
    except ValueError:
        confirmation.config(text="Invalid Check-In Date Format (Use DD/MM/YY)", foreground="#d40707")
        return
    if not totalnights.isdigit() or not startingprice.isdigit():
        confirmation.config(text="Booked Nights and Starting Price Must Be A Digit", foreground="#d40707")
        return
    floatedprice = float(startingprice)
    intnights = int(totalnights)
    CustomerData.append({"name": customerName, "checkdate": checkInDate, "totalnights": totalnights, "roomtype": roomType, "price": floatedprice, "total": floatedprice*intnights})
    nameEntry.delete(0, tk.END)
    checkInEntry.delete(0, tk.END)
    bookedNightsEntry.delete(0, tk.END)
    priceEntry.config(state="normal")
    priceEntry.delete(0, tk.END)
    priceEntry.config(state="readonly")
    confirmation.config(text="Data Stored Successfully", foreground="green")
    result.config(text="Total =", foreground="green")

def datadisplay():
    for i in guestlistView.get_children():
        guestlistView.delete(i)
    if CustomerData:
        for s in CustomerData:
            guestlistView.insert("", tk.END, values = (s["name"], s["checkdate"], s["totalnights"], s["roomtype"], s["price"], s["total"]))
    else:
        guestlistView.insert("", tk.END, values=("NO DATA", "-", "-", "-", "-"))

def opendatastorage():
    openpage(hal4)
    datadisplay()

def datasearch():
    searchkey = searchEntry.get().lower()
    for i in guestlistSearch.get_children():
        guestlistSearch.delete(i)
    searchResult = [s for s in CustomerData if searchkey in s["name"].lower()]
    if searchResult:
        for s in searchResult:
            guestlistSearch.insert("", tk.END, values=(s["name"], s["checkdate"], s["totalnights"], s["roomtype"], s["price"], s["total"]))
    else:
        guestlistSearch.insert("", tk.END, values=("DATA NOT FOUND", "-", "-", "-", "-"))
    
def deleteThatRnGang(): 
    main.destroy()

def toggle_darkmode():
    if darkmode.get() == 1:
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TLabel", background="#1e1e1e", foreground="white")
        style.configure("TButton", background="#333333", foreground="white")
        style.map("TButton", background=[("active", "#444444")])
        style.configure("Treeview", background="#2d2d2d", fieldbackground="#2d2d2d", foreground="white")
        style.configure("Treeview.Heading", background="#444444", foreground="white")

    else:
        style.configure("TFrame", background="#F5DE76")
        style.configure("TLabel", background="#F5DE76", foreground="black")
        style.configure("TButton", background="#ececec", foreground="black")
        style.map("TButton", background=[("active", "white")])
        style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", foreground="black")
        style.configure("Treeview.Heading", background="#4682b4", foreground="white")


#Main Window Media
main = tk.Tk()
main.title("HOTEL LAND OF DAWN BOOKING AND REGISTRATION")
main.geometry("960x640")
main.configure(bg = "#a4d0f8")
darkmode = tk.IntVar()
#SEMUA HALAMAN
hal1 = ttk.Frame(main)
hal2 = ttk.Frame(main)
hal3 = ttk.Frame(main)
hal4 = ttk.Frame(main)
hal5 = ttk.Frame(main)
hal6 = ttk.Frame(main)
hal7 = ttk.Frame(main)
for frame in (hal1,hal2,hal3,hal4,hal5,hal6,hal7):
    frame.place(relx=0,rely=0,relheight=1,relwidth=1)

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#F5DE76")
style.configure("TLabel", background="#F5DE76", font=("Cambria", 10))
style.configure("TButton", font=("Britannic", 12, "bold"), padding=5)
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#4682b4", foreground="white")
style.configure("Treeview", background="#fafafa", fieldbackground="#ffffff", foreground="black")

#Halaman 1
ttk.Label(hal1, text = 'HOTEL LAND \n   OF DAWN', font = ("Felix Titling", 24, "bold")).pack()
ttk.Label(hal1, text = 'Room Booking and Registration', font = ("Courier New", 8)).pack()
ttk.Label(hal1, text = 'Employee Username', font = ("Castellar", 10, "bold", "italic")).pack(pady=5)
loginUser = ttk.Entry(hal1, width = 40)
loginUser.focus_set()
loginUser.pack()
ttk.Label(hal1, text = 'Employee Password', font = ("Castellar", 10, "bold", "italic")).pack(pady=5)
loginPassword = ttk.Entry(hal1, width=40, show="*")
loginPassword.pack()
loginstatus = ttk.Label(hal1, text="")
loginstatus.pack()
buttonframe = ttk.Frame(hal1)
buttonframe.pack()
logIn = ttk.Button(buttonframe, width=10, text = "LOG IN", command = login).grid(row=0,column=0,padx=5)
Exit = ttk.Button(buttonframe, width=10, text = "EXIT", command = deleteThatRnGang).grid(row=0,column=1,padx=5)

#Halaman 2 (PRIME MENU)
ttk.Label(hal2, text = "HOTEL LAND \nOF DAWN", font=('Felix Titling', 12, 'bold', 'italic')).place(x=0, y=0, anchor='nw')
ttk.Label(hal2, text = "HOTEL LAND \n   OF DAWN", font=('Felix Titling', 24, 'bold')).pack(pady=5)
ttk.Label(hal2, text = 'Room Booking and Registration', font = ("Courier New", 8)).pack()
hello = ttk.Label(hal2, text = f"", font = ("Gabriola", 18, 'bold'))
hello.pack(pady=5)
ttk.Label(hal2, text="· · ─ ·✶· ─ · ·· · ─ ·✶· ─ · ·· · ─ ·✶· ─ · ·· · ─ ·✶· ─ · ·· · ─ ·✶· ─ · ·").pack()
ttk.Button(hal2, text= "Make Room Booking Reservations", width=40, style="TButton", command=lambda: openpage(hal3)).pack(pady=10)
ttk.Button(hal2, text= "Stored Guest Data", width=40, style="TButton", command=opendatastorage).pack(pady=5)
ttk.Button(hal2, text= "Search Guest Data", width=40, style="TButton", command=lambda: openpage(hal5)).pack(pady=5)
buttonframe2 = ttk.Frame(hal2)
buttonframe2.pack(pady=10)
ttk.Button(buttonframe2, text="LOG OUT", style="TButton", command=logOut).grid(row=0, column=0, padx=5)
ttk.Button(buttonframe2, text="ACCOUNT SETTINGS", style="TButton", command=lambda: openpage(hal6)).grid(row=0, column=1, padx=5)

#Halaman 3
ttk.Label(hal3, text = "HOTEL LAND \nOF DAWN", font=('Felix Titling', 12, 'bold', 'italic')).place(x=0, y=0, anchor='nw')

ttk.Label(hal3, text = "Guest Name", font = ("OCR A Extended", 10, 'bold')).pack(pady=10)
nameEntry = ttk.Entry(hal3, width=50)
nameEntry.pack(pady=5)

ttk.Label(hal3, text = "Check-In Date (DD/MM/YY)", font = ("OCR A Extended", 10, 'bold')).pack(pady=10)
checkInEntry = ttk.Entry(hal3, width=50)
checkInEntry.pack(pady=5)

ttk.Label(hal3, text = "Total Booked Nights", font = ("OCR A Extended", 10, 'bold')).pack(pady=10)
bookedNightsEntry = ttk.Entry(hal3, width=50)
bookedNightsEntry.pack(pady=5)

ttk.Label(hal3, text = "Standard = $100.00/night\nExecutive = $150.00/night\nDeluxe = $200.00/night\nSuite = $250.00/night", font=("OCR A Extended", 10, 'bold')).pack(pady=10)
ttk.Label(hal3, text = "Room Type", font=("OCR A Extended", 10, 'bold')).pack(pady=10)
selected_option = tk.StringVar()
comboRoom = ttk.Combobox(hal3, textvariable=selected_option, state="readonly")
comboRoom['values'] = ("Standard", "Executive", "Deluxe", "Suite")
comboRoom.set("Standard")
comboRoom.pack(pady=5)
ttk.Label(hal3, text="Price Per Night", font=("OCR A Extended", 10, 'bold')).pack(pady=10)
priceEntry = ttk.Entry(hal3, width=50, state="readonly")
priceEntry.pack(pady=5)
room_prices = {
    "Standard": 100,
    "Executive": 150,
    "Deluxe": 200,
    "Suite": 250
}
comboRoom.bind("<<ComboboxSelected>>", updateprice)

result = ttk.Label(hal3, text="Total = ",font=("OCR A Extended", 10, 'bold'), foreground="green")
result.pack(pady=5)

confirmation = ttk.Label(hal3, text="")
confirmation.pack(pady=5)

ttk.Button(hal3, text="CALCULATE PRICE", command=priceCalculation).pack(pady=5)

buttonframe3 = ttk.Frame(hal3)
buttonframe3.pack()
ttk.Button(buttonframe3, text="STORE DATA", command=datastore).grid(row=0, column=0, padx=5)
ttk.Button(buttonframe3, text="Back", command=lambda: openpage(hal2)).grid(row=0, column=1, padx=5)

#Halaman 4
ttk.Label(hal4, text = "HOTEL LAND \nOF DAWN", font=('Felix Titling', 12, 'bold', 'italic')).place(x=0, y=0, anchor='nw')
ttk.Label(hal4, text = "Guest List", font=('Felix Titling', 18, 'bold')).pack(pady=5)
data = ("Guest Name","Check In Date","Booked Nights","Room","Price per Night","Total Price")
guestlistView = ttk.Treeview(hal4, columns=data, show="headings")
for i in data:
    guestlistView.heading(i, text=i)
guestlistView.pack(pady=15)
ttk.Button(hal4, text="BACK", width=40, command=lambda: openpage(hal2)).pack(pady=70)

#Halaman 5
ttk.Label(hal5, text = "HOTEL LAND \nOF DAWN", font=('Felix Titling', 12, 'bold', 'italic')).place(x=0, y=0, anchor='nw')
ttk.Label(hal5, text = "Search Guest List", font=('Felix Titling', 18, 'bold')).pack(pady=5)
searchEntry = ttk.Entry(hal5, width=40)
searchEntry.pack(pady=5)
ttk.Button(hal5, text = "Search", command=datasearch).pack()
searchData = ("Guest Name","Check In Date","Booked Nights","Room","Price per Night","Total Price")
guestlistSearch = ttk.Treeview(hal5, columns=searchData, show="headings")
for i in searchData:
    guestlistSearch.heading(i, text=i)
guestlistSearch.pack()
ttk.Button(hal5, text="BACK", command=lambda: openpage(hal2)).pack(pady=5)

#Halaman 6
ttk.Label(hal6, text = "HOTEL LAND \nOF DAWN", font=('Felix Titling', 12, 'bold', 'italic')).place(x=0, y=0, anchor='nw')
ttk.Label(hal6, text="Display Settings", font=("Felix Titling", 18, "bold")).pack(pady=20)
ttk.Checkbutton(hal6,text="Enable Dark Mode",variable=darkmode,command=toggle_darkmode).pack(pady=10)
ttk.Button(hal6, text="BACK", command=lambda: openpage(hal2)).pack(pady=20)

# #Halaman 7
# ttk.Label(hal7, text = "HOTEL LAND \nOF DAWN", font=('Felix Titling', 12, 'bold', 'italic')).place(x=0, y=0, anchor='nw')

openpage(hal1)
main.mainloop()