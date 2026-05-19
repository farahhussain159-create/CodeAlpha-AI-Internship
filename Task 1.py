import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src = src_lang.get()
    dest = dest_lang.get()
    result = GoogleTranslator(source=src, target=dest).translate(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("600x400")

tk.Label(root, text="Enter Text:").pack()
input_text = tk.Text(root, height=5)
input_text.pack()

tk.Label(root, text="Source Language:").pack()
src_lang = ttk.Combobox(root, values=["en", "ur", "fr", "ar", "de", "es"])
src_lang.set("en")
src_lang.pack()

tk.Label(root, text="Target Language:").pack()
dest_lang = ttk.Combobox(root, values=["en", "ur", "fr", "ar", "de", "es"])
dest_lang.set("ur")
dest_lang.pack()

tk.Button(root, text="Translate", command=translate_text, bg="blue", fg="white").pack(pady=5)

tk.Label(root, text="Translated Text:").pack()
output_text = tk.Text(root, height=5)
output_text.pack()

root.mainloop()
