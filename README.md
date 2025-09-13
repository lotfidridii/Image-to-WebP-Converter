## Image to WebP Converter
This Python script converts all **PNG**, **JPG**, and **JPEG** images inside a given directory (and its subfolders) into the modern **WebP format**.
It also gives you the option to **delete the original images after conversion** and shows a nice progress bar during processing.
## Features
* Converts .png, .jpg, .jpeg images to .webp
* Optimized WebP compression (quality=85, method=6, optimize=True)
* Keeps transparency for PNG images
* Interactive confirmation: choose whether to delete originals after conversRequirementsion
* Progress bar with conversion status
* Works on the current directory or any folder you specify

## Requirements
Make sure you have Python 3.8+ installed.
Install the required packages:
```shell
pip install pillow tqdm
```
## Usage
#### 1. Run in the current directory
If you place the script in the folder containing your images:
```
python converter.py
```
#### 2. Run on a specific directory
You can pass a path as an argument:
```
python converter.py "path\to\directory"
```
#### 3. Interactive prompt
The script will ask:
```
Do you want to delete originals after conversion? (y/n):
```
* Enter `y` → originals are deleted only if WebP is smaller
* Enter `n` → originals are kept, WebP files are saved alongside

## Example Output
```
Do you want to delete originals after conversion? (y/n): y
Converting images: 100%|██████████████████████████| 25/25 [00:12<00:00,  2.03file/s]

✅ Converted 20 image(s) in: C:\Users\YourName\Pictures
⚠️ Skipped 5 image(s) because WebP was larger.
```
## Notes
* Originals are never **deleted automatically** unless you confirm with `y`.
* WebP may sometimes be **larger** than the original (especially for simple PNGs). Those are skipped when deletion is enabled.
* Supports recursive conversion in all **subfolders**.
