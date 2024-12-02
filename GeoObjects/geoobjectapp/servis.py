import os

def get_path_upload_photos(base_dir='upload'):
    upload_path = os.path.join(os.getcwd(), base_dir)
    return upload_path