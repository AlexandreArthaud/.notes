import os
import sys

def get_markdown_files(root_folder):
    markdown_files = []

    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.md'):
                relative_path = os.path.relpath(os.path.join(root, file), root_folder)
                markdown_files.append(relative_path)

    return markdown_files

if __name__ == '__main__':
    markdown_list = get_markdown_files(sys.argv[1])
    in_logm_section = False
    
    for path in markdown_list:
        print(f"On {path}:")
        with open(f'{sys.argv[1]}/{path}', 'r', encoding='utf-8') as markdown_input:
            for index, line in enumerate(markdown_input.readlines()):
                if '```' in line:
                    if not in_logm_section and '```logm' in line:
                        in_logm_section = True
                        continue
                    else:
                        in_logm_section = False
                        continue

                if not in_logm_section:
                    continue

                if not line.isspace(): # not an empty line
                    if not line.strip().startswith('#'): # not a heading
                        if ' : ' not in line: # line has no separator (it should):
                                print(f"\tLine {index}: No separator: {line}", end='')



