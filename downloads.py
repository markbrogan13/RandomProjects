from os import scandir, rename
from os.path import exists, join, splitext
from shutil import move

import logging

downloads_dir = "D:\\Downloads"
exe_dir = "D:\\Downloads\\Applications"
documents_dir = "D:\\Downloads\\Documents"
images_dir = "D:\\Downloads\\Images"
media_dir = "D:\\Downloads\\Media"
misc_dir = "D:\\Downloads\\Misc"
pcap_dir = "D:\\Downloads\\pcaps"

exe_extensions = [".exe", ".msi"]
documents_extensions = [".doc", ".docx", ".odt", ".pdf", ".PDF", ".xls", ".xlsx", ".ppt", ".pptx", ".html", ".csv"]
images_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", 
                     ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", 
                    ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", 
                    ".svg", ".svgz", ".ai", ".eps", ".ico"]

media_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd",
                    ".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]

misc_extensions = [".ttf", ".otf", ".rar", ".application", ".tar.gz", ".stl", ".jar", ".ics", ".bix",
                   ".CT", ".mid", ".tar.xz", ".img", ".eml", ".mobileconfig", ".sfk", ".ckpt", ".yaml",
                   ".toml", ".dat", ".m", ".vsix", ".bin", ".hex", ".jff"]

pcap_extensions = [".pcap", ".pcapng"]

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1

    while exists(f"{dest}/{name}"):
        name = f"{filename}{str(counter)}{extension}"
        counter += 1
    
    return name

def move_file(dest, file, name):
    if exists(F"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        rename(old_name, new_name)
    move(file, dest)

def download_cleaner():
    with scandir(downloads_dir) as files:
        for file in files:
            name = file.name
            filename, extension = splitext(name)

            if extension in exe_extensions:
                sort_exe(file, name)
            elif extension in documents_extensions:
                sort_documents(file, name)
            elif extension in images_extensions:
                sort_images(file, name)
            elif extension in media_extensions:
                sort_media(file, name)
            elif extension in pcap_extensions:
                sort_pcap(file, name)
            elif extension in misc_extensions:
                sort_misc(file, name)

def sort_exe(file, name):
    try:
        move_file(exe_dir, file, name)
    except Exception:
        print(Exception)

def sort_documents(file, name):
    try:
        move_file(documents_dir, file, name)
    except TypeError:
        print(Exception)

def sort_images(file, name):
    try:
        move_file(images_dir, file, name)
    except Exception:
        print(Exception)
    
def sort_media(file, name):
    try:
        move_file(media_dir, file, name)
    except Exception:
        print(Exception)

def sort_misc(file, name):
    try:
        move_file(misc_dir, file, name)
    except Exception:
        print(Exception)

def sort_pcap(file, name):
    try:
        move_file(pcap_dir, file, name)
    except Exception:
        print(Exception)

if __name__ == "__main__":
    download_cleaner()

