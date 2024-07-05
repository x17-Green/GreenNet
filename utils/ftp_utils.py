# ftp_utils.py
import os
import glob
import pathlib
from ftplib import FTP
from config.config import Config

class FTPConnection:
    def __init__(self):
        self.local_file_dir = Config.BACKUP_DIR
        self.remote_file_path = Config.REMOTE_FILE_PATH

        if not os.path.exists(self.local_file_dir):
            raise ValueError(f"Directory {self.local_file_dir} does not exist")
        if not os.listdir(self.local_file_dir):
            raise ValueError(f"Directory {self.local_file_dir} is empty")

        self.ftp = FTP()
        self.ftp.connect(Config.FTP_SERVER, int(Config.FTP_PORT))
        self.ftp.login(Config.FTP_USERNAME, Config.FTP_PASSWORD)

    def get_latest_backup_file(self):
        print("Directory contents:")
        print(os.listdir(self.local_file_dir))
        backup_files = list(pathlib.Path(self.local_file_dir).glob('**/*.sql'))
        print(f"Found {len(backup_files)} files in {self.local_file_dir}")
        if not backup_files:
            raise ValueError(f"No.sql files found in {self.local_file_dir}")
        latest_backup_file = max(backup_files, key=lambda x: x.stat().st_ctime)
        print(latest_backup_file)
        return str(latest_backup_file)

    def upload_file(self):
        local_file_path = self.get_latest_backup_file()
        filename = os.path.basename(local_file_path)
        remote_file_path = os.path.join(self.remote_file_path, filename)
        with open(local_file_path, 'rb') as file:
            self.ftp.storbinary('STOR ' + remote_file_path, file)

    def close_connection(self):
        self.ftp.quit()