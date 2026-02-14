import os

Import("env")

# Путь к файлу Bruce, который не дает собрать прошивку
file_path = "lib/HAL/display/tftespi.h"

def patch_source(source, target, env):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # Перезаписываем файл, исключая строку со словом "sleep"
        with open(file_path, "w", encoding="utf-8") as f:
            for line in lines:
                if "using TFT_eSPI::sleep;" not in line:
                    f.write(line)
                else:
                    print("--- УСПЕХ: ОШИБКА SLEEP УДАЛЕНА ИЗ КОДА ---")

# Запускаем скрипт перед началом компиляции
env.AddPreAction("buildprog", patch_source)
