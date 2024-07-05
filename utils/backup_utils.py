import os
import subprocess
from config.config import Config
from datetime import datetime

def create_backup(filename):
    # Create a backup file with a specific name or make it a hidden system file
    if filename.startswith('.'):
        backup_file = filename
    else:
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        backup_file = f'.{Config.DB_NAME}_{timestamp}.sql'

    # Create the backup directory if it doesn't exist
    backup_dir = os.path.abspath(Config.BACKUP_DIR)
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Create the backup file
    backup_file = os.path.join(backup_dir, backup_file)
    dump_cmd = ['mysqldump', '-u', Config.DB_USERNAME, '-p' + Config.DB_PASSWORD, Config.DB_NAME]
    try:
        with open(backup_file, "w") as f:
            subprocess.run(dump_cmd, stdout=f, check=True)
        print(f"Backup created: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating backup: {e}")

def restore_backup(backup_file):
    # Validate the backup file
    if not os.path.exists(backup_file):
        print(f"Error: Backup file '{backup_file}' does not exist")
        return

    # Restore the backup
    restore_cmd = ['mysql', '-u', Config.DB_USERNAME, '-p' + Config.DB_PASSWORD, Config.DB_NAME]
    try:
        with open(backup_file, "r") as f:
            subprocess.run(restore_cmd, stdin=f, check=True)
        print(f"Backup restored from: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error restoring backup: {e}")