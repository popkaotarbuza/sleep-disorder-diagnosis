import kagglehub
import os
import shutil

# Handle датасета
dataset_handle = "uom190346a/sleep-health-and-lifestyle-dataset"

# Папка в проекте, куда сохранить датасет
project_dir = "./data"

# Скачиваем датасет (возвращает путь к временной папке)
temp_path = kagglehub.dataset_download(dataset_handle)
print("Временный путь к датасету:", temp_path)

# Копируем содержимое в папку проекта
for item in os.listdir(temp_path):
    src = os.path.join(temp_path, item)
    dst = os.path.join(project_dir, item)
    if os.path.isfile(src):
        shutil.copy(src, dst)
    else:
        shutil.copytree(src, dst, dirs_exist_ok=True)