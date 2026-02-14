import os

Import("env")

# Путь к файлу, вызывающему ошибку в библиотеке Bruce
file_path = "lib/HAL/display/tftespi.h"

def patch_bruce(source, target, env):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.read()
        
        # Если находим проблемную строку, закомментируем её
        if "using TFT_eSPI::sleep;" in content:
            print("--- ПРИМЕНЯЕМ ИСПРАВЛЕНИЕ ОШИБКИ SLEEP ---")
            new_content = content.replace("using TFT_eSPI::sleep;", "// using TFT_eSPI::sleep;")
            with open(file_path, "w") as f:
                f.write(new_content)
            print("--- ГОТОВО: ОШИБКА УСТРАНЕНА ---")

env.AddPreAction("buildprog", patch_bruce)
