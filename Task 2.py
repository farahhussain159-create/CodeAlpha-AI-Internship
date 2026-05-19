import tkinter as tk
from tkinter import scrolledtext

faqs = {
    "hello": "Hi there! How can I help you?",
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to think like humans.",
    "what is python": "Python is a popular programming language used for AI, web development and more.",
    "who made you": "I was created as part of CodeAlpha AI Internship project.",
    "bye": "Goodbye! Have a great day!",
    "help": "You can ask me about AI, Python, or say hello!"
}

def get_response(user_input):
    user_input = user_input.lower().strip()
    for key in faqs:
        if key in user_input:
            return faqs[key]
    return "Sorry, I don't have an answer for that. Try asking about AI or Python!"

def send_message():
    user_msg = entry.get()
    if not user_msg:
        return
    chat_box.insert(tk.END, f"You: {user_msg}\n")
    response = get_response(user_msg)
    chat_box.insert(tk.END, f"Bot: {response}\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("FAQ Chatbot - CodeAlpha")
root.geometry("500x500")

chat_box = scrolledtext.ScrolledText(root, height=20)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10)

tk.Button(root, text="Send", command=send_message, bg="blue", fg="white").pack(side=tk.LEFT)

root.mainloop()
