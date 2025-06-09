import tkinter as tk
from PIL import Image, ImageTk
import sys
import os

class StaticImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ВИОЛ МЬЮЗИК: Staff CRM")

        # Получаем правильный путь к файлу
        try:
            # Для собранного приложения (PyInstaller)
            base_path = sys._MEIPASS
        except AttributeError:
            # Для разработки (обычный запуск .py)
            base_path = os.path.dirname(os.path.abspath(__file__))

        # Путь к изображению (БЕЗ ПРОБЕЛОВ, lowercase)
        image_path = os.path.join(base_path, "frame22.png")
        
        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            # Экстренный fallback (если путь сломался)
            image = Image.new("RGB", (800, 600), "red")  # Заглушка
            print(f"Ошибка: файл {image_path} не найден!")

        self.bg_photo = ImageTk.PhotoImage(image)
        width, height = image.size
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(False, False)

        bg_label = tk.Label(self.root, image=self.bg_photo)
        bg_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    
    # Пробуем загрузить иконку (необязательно)
    try:
        icon_path = os.path.join(os.path.dirname(__file__), "wiol.icns")
        root.iconbitmap(icon_path)
    except:
        pass  # Игнорируем ошибку, если иконка не загрузилась

    app = StaticImageApp(root)
    root.mainloop()