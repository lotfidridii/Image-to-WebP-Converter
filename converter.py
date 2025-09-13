from PIL import Image
import os
import sys
from tqdm import tqdm

# Get directory from command-line argument if provided, else use current directory
if len(sys.argv) > 1:
    directory = os.path.normpath(sys.argv[1].strip("'\""))
else:
    directory = os.getcwd()

# File extensions to convert (case-insensitive)
extensions = (".png", ".jpg", ".jpeg")

# Ask user confirmation
delete_originals = input("Do you want to delete originals after conversion? (y/n): ").strip().lower() == "y"

# Gather all image files first
image_files = []
for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.lower().endswith(extensions):
            image_files.append(os.path.join(root, filename))

converted_count = 0
skipped_count = 0

# Progress bar
for filepath in tqdm(image_files, desc="Converting images", unit="file"):
    try:
        with Image.open(filepath) as img:
            # Convert to WebP-compatible mode
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGBA")
            else:
                img = img.convert("RGB")

            # WebP file path
            webp_filename = os.path.splitext(os.path.basename(filepath))[0] + ".webp"
            webp_filepath = os.path.join(os.path.dirname(filepath), webp_filename)

            # Save optimized WebP
            img.save(
                webp_filepath,
                "webp",
                quality=85,
                method=6,
                optimize=True,
            )

        # Handle deletion
        if delete_originals:
            if os.path.exists(webp_filepath):
                if os.path.getsize(webp_filepath) < os.path.getsize(filepath):
                    os.remove(filepath)
                    converted_count += 1
                else:
                    skipped_count += 1
        else:
            converted_count += 1  # counted as converted, but originals kept

    except Exception as e:
        print(f"\n❌ Failed to process {filepath}: {e}")

# Final summary message
if converted_count > 0:
    print(f"\n✅ Converted {converted_count} image(s) in: {directory}")
if skipped_count > 0 and delete_originals:
    print(f"⚠️ Skipped {skipped_count} image(s) because WebP was larger.")
if converted_count == 0 and skipped_count == 0:
    print(f"\nℹ️ No images found to convert in: {directory}")
