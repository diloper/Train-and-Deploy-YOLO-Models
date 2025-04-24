
with open('ag', 'r') as f:
    for linea in f:
        print(linea)
        line = linea.replace('\n', '')
# Open the source file for reading and the destination file for writing
        with open('import.json', 'r', encoding='utf-8') as infile, open(line+'.json', 'w', encoding='utf-8') as outfile:
            for lineg in infile:
                # Replace occurrences of 'old_keyword' with 'new_keyword'
                new_line = lineg.replace('82ddf823-screenshot_20250420_181246.png', line)
                outfile.write(new_line)
