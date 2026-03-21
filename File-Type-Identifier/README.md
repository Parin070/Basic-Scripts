# File Type Identifier

A Python script that identifies the true type of a file using **magic numbers** (file signatures) rather than trusting the file extension. Useful for detecting mislabeled or potentially unsafe files.

---

## What are Magic Numbers?

Magic numbers are fixed byte sequences at the start of a file that identify its format. Unlike file extensions (which can be renamed by anyone), magic numbers are embedded in the file's actual binary content and are much harder to fake accidentally.

For example, every valid PNG file begins with the bytes `89 50 4E 47 0D 0A 1A 0A`, regardless of what the file is named.

---

## Features

- Detects file type from binary content, not the file name
- Cross-references detected type against the file's extension
- Flags mismatches as potentially unsafe
- Supports 14 common file formats

---

## Supported File Types

| Extension | Description         |
|-----------|---------------------|
| PNG       | PNG image           |
| JPG       | JPEG image          |
| GIF87     | GIF image (87a)     |
| GIF89     | GIF image (89a)     |
| BMP       | Bitmap image        |
| MP3       | MP3 audio           |
| OGG       | OGG audio           |
| PDF       | PDF document        |
| DOC       | MS Office document  |
| ZIP       | ZIP archive         |
| RAR       | RAR archive         |
| GZ        | Gzip compressed     |
| EXE       | Windows executable  |
| ELF       | Linux executable    |

---

## Requirements

- Python 3.x
- No external libraries required

---

## Usage

```bash
python checker.py
```

You will be prompted to enter a file path:

```
Enter the path of the file: /path/to/file.png
```

### Example Output

**Matching extension:**
```
File found!
File detected as: PNG
The file is safe
```

**Mismatched extension (e.g., an EXE renamed to .txt):**
```
File found!
File detected as: EXE
The file might be unsafe
```

**Unrecognized file type:**
```
File found!
Unknown file type
```

---

## Notes

- A "might be unsafe" result means the file's true type does not match its extension — this could indicate a renamed file or an attempt to disguise malicious content.
- A "safe" result only means the extension matches the detected signature. It does not guarantee the file is free of malicious content.
- If the file type is not in the supported list, the script will report it as unknown rather than guessing.

---

## Planned Improvements

- [ ] Double extension detection (e.g., `malware.exe.txt`)
- [ ] Recursive scanning of a directory
- [ ] Output results to a log file
- [ ] Support for additional file signatures