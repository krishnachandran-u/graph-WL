import os
import gzip
import shutil

output_dir = "extracted_text_files"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

gzipped_files = [f for f in os.listdir() if f.endswith('.txt.gz')]

for gz_file in gzipped_files:
    output_file = os.path.join(output_dir, gz_file.replace('.txt.gz', '.txt'))
    
    with gzip.open(gz_file, 'rt') as gz, open(output_file, 'w') as out_file:
        shutil.copyfileobj(gz, out_file)
    
    print(f"Extracted: {gz_file} -> {output_file}")

print("Decompression completed.")
