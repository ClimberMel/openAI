import tkinter as tk
from tkinter import scrolledtext
from ai_script import generate_text

def generate_content():
    # Get the user input
    prompt_text = query_input.get()

    # Use the generate_text function from ai_script.py
    try:
        generated_text = generate_text(prompt_text)
        output_display_area.insert(tk.INSERT, generated_text + "\n")
        status_bar.config(text="Generated successfully!")
    except Exception as e:
        output_display_area.insert(tk.INSERT, f"An error occurred: {e}\n")
        status_bar.config(text="Error generating.")

# The main window
root = tk.Tk()
root.title("AI Content Creation Tool")

# Query input
query_input = tk.Entry(root, width=50)
query_input.pack(pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate", command=generate_content)
generate_button.pack(pady=5)

# Output display
output_display_area = scrolledtext.ScrolledText(root, width=50, height=20)
output_display_area.pack(pady=10, padx=10)

# Status bar
status_bar = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Run the application
root.mainloop()
