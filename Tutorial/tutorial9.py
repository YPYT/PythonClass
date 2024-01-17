import tkinter as tk
def fahrenhet_to_celsius():
    f_value = float(f_entry.get())
    c_value = (f_value-32)*5/9
    c_entry.delete(0,tk.END)
    c_entry.insert(0, f"{c_value:.2f}")
def celsius_to_fahrenhet():
    c_value = float(c_entry.get())
    f_value = c_value*5/9+32
    f_entry.delete(0,tk.END)
    f_entry.insert(0, f"{f_value:.2f}")
# Create window
window = tk.Tk()
window.title("Temperature Converter")
# F Entry and Lavel
f_label = tk.Label(window, text="Fahrenhet:")
f_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
f_entry = tk.Entry(window, width=10)
f_entry.insert(0,"32.0")
f_entry.grid(row=1, column=0, padx=10, pady=10)
# C Entry and Lavel
c_label = tk.Label(window, text="Celsius:")
c_label.grid(row=0, column=1, padx=10, pady=10, sticky=tk.E)
c_entry = tk.Entry(window, width=10)
c_entry.insert(0,"0.0")
c_entry.grid(row=1, column=1, padx=10, pady=10)
# Create Buttons
to_c_button = tk.Button(window, text="Convert to Celsius >>", command=fahrenhet_to_celsius)
to_c_button.grid(row=2,column=0,padx=10,pady=10)
to_f_button = tk.Button(window, text="Convert to Fahrenhet <<", command=celsius_to_fahrenhet)
to_f_button.grid(row=2,column=1,padx=10,pady=10)
# Run the main loop
window.mainloop()
