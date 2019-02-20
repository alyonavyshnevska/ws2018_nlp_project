import os
from pathlib import Path


def unicode_clean_up(input_file, output_file):
    with open(input_file, 'r') as f:
        with open(output_file, 'w', encoding="utf-8") as write_f:
            for line in f:
                fixed_line = bytes(line, 'utf-8').decode('unicode-escape')
                write_f.write(fixed_line)


def main():
    folder_path = os.path.join(Path(__file__).parents[1], 'dataset', 'raw')

    unicode_clean_up(os.path.join(folder_path, 'twitter-2013train-A.txt'),
                     os.path.join(folder_path, 'twitter-2013train-A.txt-fixed'))
    unicode_clean_up(os.path.join(folder_path, 'twitter-2013dev-A.txt'),
                     os.path.join(folder_path, 'twitter-2013dev-A.txt-fixed'))
    unicode_clean_up(os.path.join(folder_path, 'twitter-2015train-A.txt'),
                     os.path.join(folder_path, 'twitter-2015train-A.txt-fixed'))


if __name__ == "__main__":
    main()