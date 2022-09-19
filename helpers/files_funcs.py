import os.path
import zipfile
from zipfile import ZipFile
from os.path import basename
from definitions import ROOT_DIR


def generate_absolute_path(source):
    path = os.path.join(ROOT_DIR, source)
    return path


def add_files_to_zip(dir_name, zip_file_name, file_types):
    with ZipFile(zip_file_name, 'x') as zip_file:
        for folderName, subfolders, filenames in os.walk(dir_name):
            for filename in filenames:
                if filename.split(".")[-1] in file_types:
                    filePath = os.path.join(folderName, filename)
                    zip_file.write(filePath, basename(filePath))


def extract_all_files_from_zip(dir_name, zip_file_name):
    with zipfile.ZipFile(zip_file_name) as zf:
        zf.extractall(dir_name)
