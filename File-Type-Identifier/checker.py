import os

file_signatures = {
    "png": b"\x89PNG\r\n\x1a\n",
    "jpg": b"\xFF\xD8\xFF",
    "gif87": b"GIF87a",
    "gif89": b"GIF89a",
    "exe": b"MZ",
    "pdf": b"%PDF",
    "zip": b"PK\x03\x04",
    "elf": b"\x7FELF",
    "bmp": b"\x42\x4D",
    "mp3": b"ID3",
    "rar": b"\x52\x61\x72\x21\x1A\x07\x00",
    "doc": b"\xD0\xCF\x11\xE0",
    "ogg": b"OggS",
    "gz": b"\x1F\x8B"
}

file_path = input("Enter the path of the file: ")

if not os.path.isfile(file_path):
    print("File does not exist. Check the path and try again.")
    exit()

print("File found!")
split = file_path.split(".")
with open (file_path, "rb") as f:
    f_read = f.read()
    #print(f_read)
    for ext, mnum in file_signatures.items():
        if f_read.startswith(mnum):
            print(f"File detected as: {ext.upper()}")
            if split[1].upper() == ext.upper():
                print(f"The file is safe")
            else:
                print(f"The file might be unsafe")
            exit()
    print("Unknow file type")