from tkinter import Tk, Label
import time

# Create the main window
clk = Tk()
clk.title("Clock")  # Set the title of the window
clk.geometry("1350x700+0+0")  # Set the size and position of the window
clk.config(bg="#0C1E28")  # Set the background color of the window

def clock():
    # Get the current time
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))

    # Determine whether it's AM or PM
    if int(hr) > 12 and int(mn) > 0:
        lb_dn.config(text="PM")
    else:
        lb_dn.config(text="AM")

    # Convert 24-hour time to 12-hour time
    if int(hr) > 12:
        hr = str(int(hr) - 12)

    # Update the labels with the current time
    lb_hr.config(text=hr)
    lb_mn.config(text=mn)
    lb_sc.config(text=sc)

    # Schedule the clock function to run again after 200 milliseconds
    lb_hr.after(200, clock)

# Create and place the hour label
lb_hr = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#087587", fg="white")
lb_hr.place(x=350, y=200, width=150, height=150)

# Create and place the hour text label
lb_hr_text = Label(clk, text="HOUR", font=("Times 20 bold", 20, 'bold'), bg="#087587", fg="white")
lb_hr_text.place(x=350, y=360, width=150, height=50)

# Create and place the minute label
lb_mn = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#008EA4", fg="white")
lb_mn.place(x=520, y=200, width=150, height=150)

# Create and place the minute text label
lb_mn_text = Label(clk, text="MINUTE", font=("Times 20 bold", 20, 'bold'), bg="#008EA4", fg="white")
lb_mn_text.place(x=520, y=360, width=150, height=50)

# Create and place the second label
lb_sc = Label(clk, text="12", font=("Times 20 bold", 75, 'bold'), bg="#06B4BB", fg="white")
lb_sc.place(x=690, y=200, width=150, height=150)

# Create and place the second text label
lb_sc_text = Label(clk, text="SECOND", font=("Times 20 bold", 20, 'bold'), bg="#06B4BB", fg="white")
lb_sc_text.place(x=690, y=360, width=150, height=50)

# Create and place the AM/PM label
lb_dn = Label(clk, text="AM", font=("Times 20 bold", 70, 'bold'), bg="#9F0646", fg="white")
lb_dn.place(x=860, y=200, width=150, height=150)

# Create and place the AM/PM text label
lb_dn_text = Label(clk, text="NOON", font=("Times 20 bold", 20, 'bold'), bg="#9F0646", fg="white")
lb_dn_text.place(x=860, y=360, width=150, height=50)

# Start the clock function
clock()

# Run the main event loop
clk.mainloop()
