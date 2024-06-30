import customtkinter as ctk
import ollama
import threading

# Global variable to store context
context = ''

# Define the function to interact with Ollama API
def chat_with_ollama(prompt, context):
    return ollama.generate(model="llama3", prompt=prompt, context=context, stream=True)

# Function to handle sending messages and receiving responses
def send_message(event=None):
    global context  # Declare the context as global to modify it

    user_input = input_entry.get("1.0", ctk.END).strip()

    # Display user message in chat history with 'user_message' tag
    chat_history.configure(state=ctk.NORMAL)
    chat_history.insert(ctk.END, f"You: {user_input}\n", 'user_message')
    chat_history.see(ctk.END)  # Scroll to the bottom
    chat_history.configure(state=ctk.DISABLED)

    input_entry.delete("1.0", ctk.END)

    def get_response(user_input, context, callback):
        output = chat_with_ollama(user_input, context)
        response = ""
        for chunk in output:
            chat_history.configure(state=ctk.NORMAL)
            response_chunk = chunk["response"]
            chat_history.insert(ctk.END, response_chunk, 'bot_response')
            chat_history.see(ctk.END)  # Scroll to the bottom
            chat_history.configure(state=ctk.DISABLED)
            response += response_chunk
            if chunk["done"]:
                context = chunk["context"]

        chat_history.configure(state=ctk.NORMAL)
        chat_history.insert(ctk.END, "\n")
        chat_history.see(ctk.END)  # Scroll to the bottom
        chat_history.configure(state=ctk.DISABLED)

        # Invoke the callback function with the new context
        callback(context)

    def update_context(new_context):
        global context
        context = new_context

    def start_threaded_response(user_input, current_context):
        threading.Thread(target=lambda: get_response(user_input, current_context, update_context)).start()

    # Start the threaded response
    start_threaded_response(user_input, context)

# Initialize the customtkinter application
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Techbeard the pirate chat bot")
app.geometry("500x600")

# Chat history TextBox
chat_history = ctk.CTkTextbox(app, width=480, height=400, wrap="word")
chat_history.pack(pady=(10, 5))
chat_history.configure(state=ctk.DISABLED)  # Make chat history read-only

# Configure tags for user and bot messages
chat_history.tag_config('user_message', background='lightgray', foreground='black')
chat_history.tag_config('bot_response', background='darkgray', foreground='black')

# Input TextBox with placeholder
input_entry = ctk.CTkTextbox(app, width=480, height=100)
input_entry.pack(pady=(5, 10))

# Add placeholder text
input_entry.insert("1.0", "write here")

def clear_placeholder(event):
    if input_entry.get("1.0", ctk.END).strip() == "write here":
        input_entry.delete("1.0", ctk.END)

def add_placeholder(event):
    if input_entry.get("1.0", ctk.END).strip() == "":
        input_entry.insert("1.0", "write here")

input_entry.bind("<FocusIn>", clear_placeholder)
input_entry.bind("<FocusOut>", add_placeholder)

# Bind Enter key to send message
input_entry.bind("<Return>", send_message)

# Send Button
send_button = ctk.CTkButton(app, text="Send", command=send_message)
send_button.pack(pady=(5, 10))

# Start the customtkinter event loop
app.mainloop()
