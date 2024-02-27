import os
import shutil
from tkinter import Tk, filedialog, messagebox, ttk, Frame
from tkinter import *
from PIL import ImageTk, Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import tkinter as tk


# AES encryption function
def encrypt_data(data):
    # Generated key and IV
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))

    return encrypted_data

# Obfuscate file
def obfuscate_file():
    file_path = file_entry.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file.")
        return

    if not techniques_combobox.get():
        messagebox.showerror("Error", "Please select an obfuscation technique.")
        return

    selected_technique = techniques_combobox.get()
    obfuscated_data = ""

    with open(file_path, 'r') as file:
        data = file.read()

        if selected_technique == "Masking":
            obfuscated_data = mask_letters(data)

        elif selected_technique == "Tokenization":
            obfuscated_data = tokenize_data(data)

        elif selected_technique == "Encryption":
            obfuscated_data = encrypt_data(data)
            # Convert bytes to hexadecimal string
            obfuscated_data = obfuscated_data.hex()
        elif selected_technique == "Generalization":
            obfuscated_data = generalize_data(data)

    if obfuscated_data:
        base_name = os.path.basename(file_path)
        download_path = os.path.join(os.path.expanduser("~"), "Downloads", "obfuscated_" + base_name)

        with open(download_path, 'wb') as obfuscated_file:
            obfuscated_file.write(obfuscated_data.encode('utf-8'))

        messagebox.showinfo("Obfuscation", "File obfuscated successfully!")
        file_entry.delete(0, END)

        # Enable the download button
        download_button.config(state=NORMAL)

        # Set the path of the obfuscated file
        obfuscate_file.obfuscated_file_path = download_path

def download_file():
    download_path = filedialog.asksaveasfilename(initialfile="obfuscated_file.txt", defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
    
    if download_path:
        obfuscated_file_path = obfuscate_file.obfuscated_file_path
        
        try:
            shutil.copy2(obfuscated_file_path, download_path)
            messagebox.showinfo("Download", "File downloaded successfully!")
        except IOError:
            messagebox.showerror("Error", "Failed to download the file.")

# AES encryption function
def encrypt_data(data):
    # Generated key and IV
    key = get_random_bytes(16)
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))

    return encrypted_data

# Mask every next letter
def mask_letters(data):
    obfuscated_data = ""
    for i, char in enumerate(data):
        if i % 2 == 0:
            obfuscated_data += char
        else:
            obfuscated_data += "*"
    return obfuscated_data

# Tokenization technique
def tokenize_data(data):
    words = data.split()
    obfuscated_words = []
    for word in words:
        if len(word) > 0:
            obfuscated_words.append(word[0])
    obfuscated_data = " ".join(obfuscated_words)
    return obfuscated_data

# Generalization technique
def generalize_data(data):
    obfuscated_data = ""
    for char in data:
        if char.isalpha():
            obfuscated_data += "X"
        else:
            obfuscated_data += char
    return obfuscated_data

# Create the main window
window = Tk()
window.title("File Obfuscation Tool")

# Set the background image
background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\shashank singh\OneDrive\Desktop\python\cyber-image.jpg"))
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()
# Set the window size and position
window_width = int(window.winfo_screenwidth() * 0.8)
window_height = int(window.winfo_screenheight() * 0.8)
window_x = int((window.winfo_screenwidth() - window_width) / 2)
window_y = int((window.winfo_screenheight() - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Create a label for file selection
# Create a label for file selection
file_label = Label(window, text="*browse file foe obfuscation*", font=("Arial", 18), bg="black", fg="white", borderwidth=0, relief="solid", padx=5, pady=5)
file_label.pack(pady=(250,10))

# Create an entry field for file path
# Create a frame for the entry field
entry_frame = Frame(window, bg="black", padx=10, pady=10)
entry_frame.pack()

# Create an entry field for file path
file_entry = Entry(window, width=50, font=("Arial", 12), bg="black", fg="white", borderwidth=0, relief="solid")
file_entry.pack(pady=(0, 10)) 

# Configure the frame for rounded shape
entry_frame.config(highlightbackground="black", bd=0)



# Create a button to browse for a file
browse_button = ttk.Button(window, text="Browse", command=lambda: file_entry.insert(END, filedialog.askopenfilename()), style="Custom.TButton")
browse_button.pack(pady=10)



# Create a label for obfuscation technique
technique_label = tk.Label(window, text="Select obfuscation technique:", font=("Arial", 18), background="black", foreground="white")
technique_label.pack(pady=10)


# Create a combobox for technique selection
techniques_combobox = ttk.Combobox(window, values=["Masking", "Tokenization", "Encryption", "Generalization"], state="readonly", font=("Arial", 14))
techniques_combobox.pack()

s = ttk.Style()
s.theme_create("custom_style", parent="alt", settings={
    "TCombobox": {
        "configure": {
            "background": "black",
            "foreground": "white",
        }
    }
})
s.theme_use("custom_style")



# Create a button to start the obfuscation process
obfuscate_button = tk.Button(window, text="Obfuscate", command=obfuscate_file, font=("Arial", 14), fg="white", bg="black", relief=tk.FLAT)
obfuscate_button.pack(side="left", padx=(515,0), pady=0)

# Create a download button (initially disabled)
download_button = tk.Button(window, text="Download", command=download_file, font=("Arial", 14), fg="white", bg="black", relief=tk.FLAT, state=tk.DISABLED)
download_button.pack(side="left", padx=10, pady=0)



# Define the custom style for the buttons
s = ttk.Style()
s.configure("Custom.TButton", font=("Arial", 14), foreground="white", padding=5, roundness=8)
s.configure("Custom.TButton",
            background="black",
            lightcolor="black",
            darkcolor="black",
            bordercolor="black",
            arrowcolor="black",
            highlightbackground="black",
            troughcolor="black")


# Run the main event loop
window.mainloop()
