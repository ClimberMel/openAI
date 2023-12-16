import subprocess
import tkinter as tk

def run_ai_script():
    #subprocess.run(['python', 'code/ai_script.py'])
    import code.ai_script

def main():
    root = tk.Tk()
    root.title("Tkinter Desktop Application")
    root.geometry("300x300")

    # Button
    run_button = tk.Button(root, text="Run AI Script", command=run_ai_script)

    # Center the button
    run_button.pack(expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()
