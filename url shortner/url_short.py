import tkinter as tk
from tkinter import messagebox
import pyshorteners
from pyshorteners.exceptions import ShorteningErrorException

def shorten_url():
    long_url = entry.get()
    if long_url:
        try:
            s = pyshorteners.Shortener()
            shortened_url = s.tinyurl.short(long_url)
            result_text.config(state=tk.NORMAL)  
            result_text.delete("1.0", tk.END)  
            result_text.insert(tk.END, "Shortened URL: " + shortened_url)
            result_text.config(state=tk.DISABLED) 
        except ShorteningErrorException as e:
            messagebox.showerror("Error", "Failed to shorten URL: " + str(e))
    else:
        messagebox.showwarning("Warning", "Please enter a URL to shorten.")

# Create the main window
root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x200")
root.configure(bg='green')

# Labels
label = tk.Label(root, text="Enter the URL to shorten:", font=("Arial", 12), bg='green',fg='white')
label.pack()

# Entry field
entry = tk.Entry(root, width=40)
entry.pack()

# Shorten button
shorten_button = tk.Button(root, text="Shorten", command=shorten_url, bg="blue", fg="white")
shorten_button.pack()

# Result text widget
result_text = tk.Text(root, height=3, width=40)
result_text.config(state=tk.DISABLED)  # Make the text widget read-only
result_text.pack()

# Run the GUI application
root.mainloop()
