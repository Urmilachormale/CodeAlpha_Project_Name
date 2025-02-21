import os
import shutil

# Define the directory to organize
directory = "C:/Users/YourUsername/Downloads"  # Change this to your target directory

# Define file type categories
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
}

# Create categorized folders if they don't exist
for category in file_categories.keys():
    category_path = os.path.join(directory, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Move files to respective category folders
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, category, filename))
                print(f"Moved: {filename} -> {category}")
                break

print("File organization complete!")
