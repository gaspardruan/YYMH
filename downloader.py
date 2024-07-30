import requests
import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor

URL = "https://yymh.app/home/api/chapter_list/tp/{}-1-1-1000"
BASE_SRC = "https://yyxx.xiumm.top/public"
HEADERS = {
    'Referer': 'https://yymh.app/'
}


def download_all(url, name):
    response = requests.get(url)
    if response.status_code == 200:
        folder_path = './' + name
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
        os.makedirs(folder_path)

        data = response.json()
        chapters = data['result']['list']

        with ThreadPoolExecutor(max_workers=16) as pool:
            for chapter_num, chapter in enumerate(chapters, 1):
                image_list = chapter['imagelist'].split(',')
                for image_num, image in enumerate(image_list, 1):
                    image_url = BASE_SRC + image
                    pool.submit(download_image, image_url,
                                chapter_num, image_num, folder_path)


def download_image(image_url, chapter_num, image_num, folder_path):
    image_data = requests.get(image_url, headers=HEADERS)
    image_name = 'ch{}-{}.jpg'.format(chapter_num, image_num)
    with open(folder_path + '/' + image_name, 'wb') as f:
        f.write(image_data.content)


def compress_to_zip(result_path, src_path):
    shutil.make_archive(result_path, 'zip', src_path)
    os.rename('./' + result_path + '.zip', './' + result_path + '.cbz')


def delete_folder(folder_path):
    if not os.path.isdir(folder_path):
        return
    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        print("Error: {}".format(e.strerror))


def main():
    parser = argparse.ArgumentParser(description="Download the YYMH comics by comic id.")
    parser.add_argument("id", type=int, help="comic id")
    parser.add_argument("name", type=str, help="comic name", default='undefined')
    args = parser.parse_args()

    url = URL.format(args.id)
    name = args.name

    print("Start Downloading")
    download_all(url, name)
    print("Downloading Done")

    print("Start Compressing")
    compress_to_zip(name, './' + name)
    print("Compressing Over")

    print("Start Deleting")
    delete_folder('./' + name)
    print("Deleting Done")


main()
