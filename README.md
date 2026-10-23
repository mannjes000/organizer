# Downloads Organizer

A Python script that sorts my Downloads folder into subfolders by file type (images, documents, installers, archives).

## How to run


python3 organize.py


## How it works

It loops through every file in `~/Downloads`, checks the file extension against a dictionary of categories, and moves matching files into the right folder. Folders are created automatically if they don't exist.

## Ideas to add

- More categories (scripts, class files)
- Skip files modified in the last hour
- Add dates to filenames