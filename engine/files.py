# =========================================================
# AP AI V4 Stable
# Created by : Amarchand Meghwal
# =========================================================

"""
File Utilities
"""

import os
import shutil


class FileManager:

    @staticmethod
    def exists(path):
        """
        Check whether file or folder exists.
        """
        return os.path.exists(path)

    @staticmethod
    def create_folder(path):
        """
        Create folder if it does not exist.
        """
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def create_file(path):
        """
        Create an empty file.
        """
        folder = os.path.dirname(path)

        if folder:
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(path):
            open(path, "w", encoding="utf-8").close()

    @staticmethod
    def delete(path):
        """
        Delete file or folder.
        """
        if os.path.isfile(path):
            os.remove(path)
            return True

        if os.path.isdir(path):
            shutil.rmtree(path)
            return True

        return False

    @staticmethod
    def copy(source, destination):
        """
        Copy file.
        """
        folder = os.path.dirname(destination)

        if folder:
            os.makedirs(folder, exist_ok=True)

        shutil.copy2(source, destination)

    @staticmethod
    def move(source, destination):
        """
        Move file.
        """
        folder = os.path.dirname(destination)

        if folder:
            os.makedirs(folder, exist_ok=True)

        shutil.move(source, destination)

    @staticmethod
    def rename(source, new_name):
        """
        Rename file.
        """
        folder = os.path.dirname(source)
        destination = os.path.join(folder, new_name)

        os.rename(source, destination)

        return destination

    @staticmethod
    def list_files(path):
        """
        Return file list.
        """
        if not os.path.isdir(path):
            return []

        return sorted(os.listdir(path))

    @staticmethod
    def size(path):
        """
        Return file size.
        """
        if not os.path.exists(path):
            return 0

        return os.path.getsize(path)

    @staticmethod
    def extension(path):
        """
        Return file extension.
        """
        return os.path.splitext(path)[1].lower()

    @staticmethod
    def filename(path):
        """
        Return file name only.
        """
        return os.path.basename(path)

    @staticmethod
    def parent(path):
        """
        Return parent directory.
        """
        return os.path.dirname(path)


files = FileManager()
