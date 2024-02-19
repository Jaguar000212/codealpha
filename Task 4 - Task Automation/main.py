# Importing the required libraries
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import tempfile


# Function to move files from one folder to another
def cleanup_system():
    temp_folder = tempfile.gettempdir()
    for temp_file in os.listdir(temp_folder):
        try:
            os.remove(os.path.join(temp_folder, temp_file))
        except:
            messagebox.showerror("Error", f"Failed to remove '{temp_file}' from temp folder.")
            continue

    # Show a success message
    messagebox.showinfo("Success", "System cleaned successfully!")


def move_files():
    # Get the source and destination folder paths
    source_folder = filedialog.askdirectory(title="Select Source Folder")
    destination_folder = filedialog.askdirectory(title="Select Destination Folder")

    # Check if the source and destination folders are selected
    if source_folder and destination_folder:
        # Get the list of files in the source folder
        files = os.listdir(source_folder)

        # Move each file from the source folder to the destination folder
        for file in files:
            file_path = os.path.join(source_folder, file)
            if os.path.isfile(file_path):
                shutil.move(file_path, destination_folder)

        # Show a success message
        messagebox.showinfo("Success", "Files moved successfully!")
    else:
        # Show an error message if the folders are not selected
        messagebox.showerror("Error", "Please select source and destination folders.")


def clean_folder():
    # Get the folder path
    folder_path = filedialog.askdirectory(title="Select Folder")

    # Check if the folder is selected
    if folder_path:
        # Get the list of files in the folder
        files = os.listdir(folder_path)

        # Remove each file from the folder
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

        # Show a success message
        messagebox.showinfo("Success", "Folder cleaned successfully!")
    else:
        # Show an error message if the folder is not selected
        messagebox.showerror("Error", "Please select a folder.")


def clean_pycache():
    # Get the folder path
    folder_path = filedialog.askdirectory(title="Select Folder")

    # Check if the folder is selected
    if folder_path:
        # Get the list of files and subfolders in the folder
        for root, dirs, files in os.walk(folder_path):
            # Remove the __pycache__ folder
            if "__pycache__" in dirs:
                shutil.rmtree(os.path.join(root, "__pycache__"))

        # Show a success message
        messagebox.showinfo("Success", "__pycache__ cleaned successfully!")
    else:
        # Show an error message if the folder is not selected
        messagebox.showerror("Error", "Please select a folder.")


def rename_files():
    directory = filedialog.askdirectory(title="Select Folder")
    prefix = "My_File_"  # Replace with your prefix

    for filename in os.listdir(directory):
        new_name = prefix + filename
        source = os.path.join(directory, filename)
        destination = os.path.join(directory, new_name)

        try:
            os.rename(source, destination)
        except Exception as e:
            print(f"Error renaming file {filename}: {e}")

    # Show a success message
    messagebox.showinfo("Success", "Files renamed successfully!")


# Create the main window
window = tk.Tk()
window.title("Task Automation")

# Set the window size
window.geometry("300x300")

# Create the label for the title
title_label = tk.Label(window, text="Task Automation", font=("Helvetica", 16))
title_label.pack(pady=10)

# Create the buttons to run the scripts
cleanup_system_button = tk.Button(window, text="Cleanup System", command=cleanup_system)
cleanup_system_button.pack(pady=10)

move_files_button = tk.Button(window, text="Move Files", command=move_files)
move_files_button.pack(pady=10)

clean_folder_button = tk.Button(window, text="Clean Folder", command=clean_folder)
clean_folder_button.pack(pady=10)

clean_pycache_button = tk.Button(window, text="Clean Python Cache", command=clean_pycache)
clean_pycache_button.pack(pady=10)

rename_files_button = tk.Button(window, text="Rename Files", command=rename_files)
rename_files_button.pack(pady=10)

# Run the main loop

window.mainloop()
