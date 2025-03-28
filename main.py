import tkinter as tk
from tkinter import filedialog, messagebox

def filter_file_by_keyword(input_file, keyword, output_file):
    with open(input_file, 'r', encoding='utf8bom') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if keyword in line]

    with open(output_file, 'w', encoding='utf8bom') as file:
        file.writelines(filtered_lines)

def select_and_filter():
    """Функція для вибору файлу та фільтрації його вмісту."""
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        messagebox.showwarning("Помилка", "Не обрано файл.")
        return
    
    keyword = keyword_entry.get().strip()
    if not keyword:
        messagebox.showwarning("Помилка", "Введіть ключове слово.")
        return
    
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not save_path:
        messagebox.showwarning("Помилка", "Не обрано місце для збереження.")
        return

    filter_file_by_keyword(file_path, keyword, save_path)
    messagebox.showinfo("Готово", f"Фільтрований вміст збережено у '{save_path}'.")

# Запуск GUI тільки якщо файл запущений напряму
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Фільтрація TXT файлу")
    root.geometry("400x200")

    tk.Label(root, text="Введіть ключове слово:").pack(pady=5)
    keyword_entry = tk.Entry(root, width=40)
    keyword_entry.pack(pady=5)

    tk.Button(root, text="Вибрати файл та фільтрувати", command=select_and_filter).pack(pady=10)

    root.mainloop()