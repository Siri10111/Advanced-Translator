import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
from gtts import gTTS
import os
import threading
import json

# Function to perform translation
def translate_text():
    input_text = input_text_box.get("1.0", tk.END).strip()
    target_lang = target_lang_box.get()
    
    if not input_text:
        messagebox.showerror("Input Error", "Please enter some text to translate!")
        return
    if not target_lang:
        messagebox.showerror("Language Error", "Please select a target language!")
        return
    
    threading.Thread(target=perform_translation, args=(input_text, target_lang)).start()

# Function to perform the actual translation
def perform_translation(input_text, target_lang):
    try:
        response = requests.get(f"https://api.mymemory.translated.net/get?q={input_text}&langpair=en|{target_lang}")
        if response.status_code == 200:
            translated = response.json()["responseData"]["translatedText"]
            output_text_box.delete("1.0", tk.END)
            output_text_box.insert(tk.END, translated)
            
            # Text-to-Speech
            save_and_play_tts(translated, target_lang)
            save_translation(input_text, translated)  # Save to history
        else:
            raise Exception("Failed to retrieve translation.")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Translation Error", f"Request failed: {str(e)}")
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {str(e)}")

# Function to save translation to history
def save_translation(input_text, translated_text):
    history_entry = {"input": input_text, "translated": translated_text}
    translation_history.append(history_entry)
    update_history_display()

# Function to update history display
def update_history_display():
    history_text_box.delete("1.0", tk.END)
    for entry in translation_history:
        history_text_box.insert(tk.END, f"Input: {entry['input']}\nTranslated: {entry['translated']}\n\n")

# Function to clear all fields
def clear_fields():
    input_text_box.delete("1.0", tk.END)
    output_text_box.delete("1.0", tk.END)
    target_lang_box.set('')
    
# Function to save translation to a file
def save_to_file():
    with open("translations_history.json", "w") as file:
        json.dump(translation_history, file, ensure_ascii=False, indent=4)
    messagebox.showinfo("Save Successful", "Translation history saved successfully!")

# Function to handle text-to-speech
def save_and_play_tts(translated, target_lang):
    tts = gTTS(translated, lang=target_lang)
    tts.save("translation.mp3")
    os.system("start translation.mp3")  # Play the sound

# Create the main window
root = tk.Tk()
root.title("Advanced Language Translator")
root.geometry("700x700")
root.configure(bg="#1e1e1e")  # Dark background

# Initialize translation history
translation_history = []

# Create and place widgets
input_label = tk.Label(root, text="Input Text:", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
input_label.pack(pady=5)

input_text_box = scrolledtext.ScrolledText(root, height=8, width=60, font=("Arial", 12), bg="#2e2e2e", fg="#ffffff")
input_text_box.pack(pady=5)

target_lang_label = tk.Label(root, text="Select Target Language:", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
target_lang_label.pack(pady=5)

languages = ["en", "es", "fr", "de", "it", "zh", "ja", "pt", "ru", "ar"]
target_lang_box = ttk.Combobox(root, values=languages, font=("Arial", 12), state="readonly")
target_lang_box.pack(pady=5)

translate_button = tk.Button(root, text="Translate", command=translate_text, font=("Arial", 12), bg="#4CAF50", fg="#ffffff")
translate_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_fields, font=("Arial", 12), bg="#f44336", fg="#ffffff")
clear_button.pack(pady=5)

output_label = tk.Label(root, text="Translated Text:", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
output_label.pack(pady=5)

output_text_box = scrolledtext.ScrolledText(root, height=8, width=60, font=("Arial", 12), bg="#2e2e2e", fg="#ffffff")
output_text_box.pack(pady=5)

history_label = tk.Label(root, text="Translation History:", font=("Arial", 12), bg="#1e1e1e", fg="#ffffff")
history_label.pack(pady=5)

history_text_box = scrolledtext.ScrolledText(root, height=8, width=60, font=("Arial", 12), bg="#2e2e2e", fg="#ffffff")
history_text_box.pack(pady=5)

save_button = tk.Button(root, text="Save History", command=save_to_file, font=("Arial", 12), bg="#2196F3", fg="#ffffff")
save_button.pack(pady=10)

# Start the main event loop
root.mainloop()

# Add this function to your existing translator.py code

def main():
    root = tk.Tk()
    root.title("Advanced Language Translator")
    root.geometry("700x700")
    root.configure(bg="#1e1e1e")  # Dark background
    
    # Initialize translation history
    translation_history = []
    
    # Create and place widgets (as in the previous code)
    # ... (the rest of your code here)

if __name__ == "__main__":
    main()
