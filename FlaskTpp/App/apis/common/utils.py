import uuid
import os

from App.settings import UPLOADS_MOVIE_PIC, FILE_BACKGROUND_PIC_PATH


def filename_transfer(filename):
    ext_name = filename.rsplit(".")[1]

    new_filename = uuid.uuid4().hex + "." + ext_name

    save_path = os.path.join(UPLOADS_MOVIE_PIC, new_filename)

    upload_path = os.path.join(FILE_BACKGROUND_PIC_PATH, new_filename)

    return save_path, upload_path
