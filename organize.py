from pathlib import Path
import shutil
import time

downloads = Path.home() / "Downloads"

folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx", ".csv"],
    "Installers": [".dmg", ".pkg"],
    "Archives": [".zip", ".tar", ".gz"],
    "Scripts": [".py", ".sh", ".js"],
}

moved = 0
now = time.time()

for item in downloads.iterdir():
    if not item.is_file():
        continue

    # skip anything changed in the last hour (3600 seconds)
    if now - item.stat().st_mtime < 3600:
        continue

    for folder, extensions in folders.items():
        if item.suffix.lower() in extensions:
            dest = downloads / folder
            dest.mkdir(exist_ok=True)

            target = dest / item.name
            if target.exists():
                target = dest / f"{item.stem}_{int(now)}{item.suffix}"

            print(f"Moving {item.name} -> {folder}")
            shutil.move(str(item), str(target))
            moved += 1
            break

print(f"Done. Moved {moved} files.")