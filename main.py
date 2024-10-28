import os
from os import path
import shutil
import time
import datetime
import logging

logging.basicConfig(
    filename= "desktop_cleaner.log",
    level= logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode= 'a'
)


current_time = datetime.datetime.now()
date_int = int(str(current_time.year) + str(current_time.month) + str(current_time.day))


downloads_path = "C:\\Users\\sudha\\Downloads"
images_path = "C:\\Users\\sudha\\OneDrive\\Pictures"
docs_path = "C:\\Users\\sudha\\OneDrive\\Documents"
videos_path = "C:\\Users\\sudha\\Videos"
music_path = "C:\\Users\\sudha\\Music"
class_room_path = "D:\\Class_Room"

class desktop_cleaner:
    
    def __init__(self, downloads, images_path, docs_path, videos_path, music_path, class_room_path):
        self.downloads = downloads
        self.images = images_path
        self.docs = docs_path
        self.videos = videos_path
        self.music = music_path
        self.class_room = class_room_path
    
    def get_directory(self):
        
        lst_of_dir = os.listdir(self.downloads)
        i = 1
        for x in lst_of_dir:
            print(f'{i}. {x}')
            i += 1
        print('-----------------------')
        
        return lst_of_dir
            
    def exe_iso_zip_remover(self):
        file_count = 0
        lst_of_dir = cleaner.get_directory()
        for i in lst_of_dir:
            path = os.path.join(self.downloads, i)
            if '.exe' in i or '.zip' in i or '.iso' in i or '.rar' in i:
                os.path.join(self.downloads, i)
                print(f'{i} => Deleted')
                logging.info(f'{i} was removed from {path}')
                os.remove(path)
                file_count += 1
        if file_count == 0:
            print('Nothing Found')
            logging.info('Nothing was removed at the moment.')
            
    def older_file_remover(self):
        file_count = 0
        lst_of_dir = cleaner.get_directory()
        
        for i in lst_of_dir:
            path = os.path.join(self.downloads, i)
            m_time = os.path.getmtime(path)
            m_time = time.ctime(m_time)
            t_obj = time.strptime(m_time)
            time_stamp = time.strftime('%Y%m%d', t_obj)
            time_stamp = int(time_stamp)
            
            if date_int - time_stamp > 30:
                logging.info(f'{i} was removed from {path}')
                os.remove(path)
                file_count += 1
            else: print(f'{i} => {date_int - time_stamp}')
        if file_count == 0:
            logging.info('Nothing was removed at the moment.')
            
    def file_mover(self):
        
        lst_of_dir = cleaner.get_directory()
        file_count = 0
        for x in lst_of_dir:
            path = os.path.join(self.downloads, x)

            if '.pdf' in x or '.ppt' in x:
                shutil.copy(path, self.class_room)
                shutil.copy(path, self.docs)
                logging.info(f'{x} was moved to {self.class_room}')
                file_count += 1
                time.sleep(3)
                print(f'{x} => Moved to {self.class_room}')
                os.remove(path)
                
            elif ".jpg" in x or ".jpeg" in x or ".jfif" in x or ".pjpeg" in x or '.pjp' in x or '.png' in x:
                shutil.copy(path, self.images)
                file_count += 1
                logging.info(f'{x} was moved to {self.images}')
                time.sleep(3)
                print(f'{x} => Moved to {self.images}')
                os.remove(path)
        if file_count == 0:
            logging.info('Nothing was moved at the moment.')
            

if __name__ == '__main__':
    cleaner = desktop_cleaner(downloads_path, images_path, docs_path, videos_path, music_path, class_room_path)
    cleaner.get_directory()
    cleaner.exe_iso_zip_remover()
    cleaner.file_mover()
    cleaner.older_file_remover()