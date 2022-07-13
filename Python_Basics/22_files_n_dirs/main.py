from pathlib import Path

path = Path("emails")

# create 'emails' directory if not exists
if not path.exists():
    path.mkdir()

# remove 'emails' directory if  exists
if path.exists():
    path.rmdir()

# glob - is an advanced method to search files and driectories
path2 = Path()
for file in path2.glob("*"):
    print(file)
