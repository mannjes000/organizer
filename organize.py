from pathlib import Path
import shutil

downloads = Path.home() / "Downloads"

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Installers": [".dmg", ".pkg"],
    "Archives": [".zip", ".tar", ".gz"],
}

for item in downloads.iterdir():
    if not item.is_file():
        continue
    for folder, extensions in folders.items():
        if item.suffix.lower() in extensions:
            dest = downloads / folder
            dest.mkdir(exist_ok=True)
            print(f"Moving {item.name} -> {folder}")
            shutil.move(str(item), str(dest / item.name))
            break