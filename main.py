from psxdb import psxdb
import argparse
import os

# usage:
# blaat = psxdb.fetch_info('SLES_51815', 'PS2')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='The directory where the ISO or BIN/CUE files reside')
    parser.add_argument('platform', help='Platform. Currently PSX or PS2. Defaults to PS2', default='PS2')
    args = parser.parse_args()

    dir = args.directory
    platform = args.platform
    print(f'Checking {dir}...')
    print(f'Platform is {platform}')

    for count, filename in enumerate(os.listdir(dir)):
        print(f'Parsing file {count}: {filename}...')
        file = os.path.splitext(filename)[0]
        ext = os.path.splitext(filename)[1]
        print(f'The file is {file}, {ext}')
        dst_filename = psxdb.fetch_info(file, platform)
        if dst_filename is not None:
            src = dir + filename
            dst = dir + dst_filename + ext

            os.rename(src, dst)
        else:
            print('Game has not been found or has already been parsed...')
            print('')


if __name__ == '__main__':
    main()
