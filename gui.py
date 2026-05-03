import tkinter as tk
from tkinter import messagebox
from pdf_maker import excel_to_pdf
window = tk.Tk()
window.title("PDF Maker!")
window.geometry("600x400")
label1 = tk.Label(window, text="Enter Input File Name.(Don't Add .xlsx)")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()
label2 = tk.Label(window, text="Enter Output File Name.(Don't Add .pdf)")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()
def button_click():
    text1 = entry1.get()
    text2 = entry2.get()
    try:
        excel_to_pdf(text1 + ".xlsx", text2 + ".pdf")
        tk.messagebox.showinfo("Done!", "PDF Generated Successfully!")
    except (FileExistsError, FileNotFoundError):
        tk.messagebox.showerror("Error!", "File not exists or not found in path.")
button = tk.Button(window, text="Generate PDF", command=button_click)
button.pack()
window.mainloop()