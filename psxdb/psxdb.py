import re
import requests
from bs4 import BeautifulSoup


# Region code arrays
pal = ['SCES', 'SLES']
ntsc_j = ['SLPM', 'SLPS', 'GN', 'SLKA']
ntsc_u = ['SLUS']


def check_region(filename):
    prefix = re.split('-|_', filename)[0].upper()
    if prefix in pal:
        print('Filename suggests PAL region')
        return 'PAL'

    elif prefix in ntsc_j:
        print('Filename suggests NTSC-J region')
        return 'NTSC-J'

    elif prefix in ntsc_u:
        print('Filename suggests NTSC-U region')
        return 'NTSC-U'

    else:
        print('Filename has no known region prefix.')
        return None


def fetch_info(filename, platform):
    region = check_region(filename)
    # prefix = re.split('.', filename)[0].upper()

    print(f'Fetching data for {filename}({region})...')
    list_url = None
    if region == 'PAL':
        if platform == 'PS2':
            list_url = 'https://psxdatacenter.com/psx2/plist2.html'
        elif platform == 'PSX':
            list_url = 'http://psxdatacenter.com/plist.html'
    elif region == 'NTSC-U':
        if platform == 'PS2':
            list_url = 'https://psxdatacenter.com/psx2/plist2.html'
        elif platform == 'PSX':
            list_url = 'http://psxdatacenter.com/plist.html'
    elif region == 'NTSC-J':
        if platform == 'PS2':
            list_url = 'https://psxdatacenter.com/psx2/plist2.html'
        elif platform == 'PSX':
            list_url = 'http://psxdatacenter.com/plist.html'

    page = requests.get(list_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    names = soup.find_all('tr')
    filename_serial = re.sub('_', '-', filename)
    for name in names:

        if len(name.find_all(['td'])) >= 1:
            info = name.find_all(['td'])[0]
            serial = name.find_all(['td'])[1].get_text()
            game_name = name.find_all(['td'])[2].get_text()

            # filename_serial = re.sub('_', '-', prefix)

            if filename_serial.upper() == serial:
                print(f'Game identified as {serial} - {game_name}!')
                # print(info.get_text())
                return f'{serial}-{game_name.lstrip()}'
