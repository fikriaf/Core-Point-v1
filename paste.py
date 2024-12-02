import tkinter as tk

def paste_text():
    copied_text = app.clipboard_get()
    text_widget.insert("insert", copied_text)
    update_height()

def update_height(event=None):
    # Menghitung jumlah baris dalam widget Text
    num_lines = text_widget.get("1.0", "end-1c").count("\n")
    # Mengatur ulang tinggi widget Text sesuai jumlah baris, minimum 1
    if num_lines > 1:
        if num_lines > 6:
            text_widget.config(height=7)
        else:
            text_widget.config(height=num_lines + 1)
    else:
        text_widget.config(height=1)


app = tk.Tk()
app.title("Multi-line Paste")

canvas_coreflash = tk.Canvas(app, width=1000, height=500)
canvas_coreflash.pack()

text_widget = tk.Text(canvas_coreflash, width=60, height=1, fg="black", font=("arial", 12), wrap="none")
text_widget.place(x=20, y=50)

# Bind event untuk memantau perubahan teks
text_widget.bind("<KeyRelease>", update_height)

app.mainloop()
