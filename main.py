import os
from os import path
import shutil
import time
import datetime


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
        return lst_of_dir
            
    def exe_iso_zip_remover(self):
        lst_of_dir = cleaner.get_directory()
        
        for i in lst_of_dir:
            if '.exe' in i or '.zip' in i or '.iso' in i or '.rar' in i:
                os.remove(path)
            else:
                print('Nothing Found')

    def older_file_remover(self):
        lst_of_dir = cleaner.get_directory()
        
        for i in lst_of_dir:
            path = f'{self.downloads}\\{i}'
            m_time = os.path.getmtime(path)
            m_time = time.ctime(m_time)
            t_obj = time.strptime(m_time)
            time_stamp = time.strftime('%Y%m%d', t_obj)
            time_stamp = int(time_stamp)
            
            if date_int - time_stamp > 30:
                os.remove(path)
            else: print(f'{i} => {date_int - time_stamp}')
                
    def file_mover(self):
        
        lst_of_dir = cleaner.get_directory()
        
        for x in lst_of_dir:
            path = f'{self.downloads}\\{x}'
            
            if '.pdf' or '.ppt' in x:
                shutil.copy(path, self.class_room)
                shutil.copy(path, self.docs)
                time.sleep(3)
                os.remove(path)
                
            elif ".jpg" in x or ".jpeg" in x or ".jfif" in x or ".pjpeg" in x or '.pjp' in x or '.png' in x:
                shutil.copy(path, self.images)
                time.sleep(3)
                os.remove(path)
                

if __name__ == '__main__':
    cleaner = desktop_cleaner(downloads_path, images_path, docs_path, videos_path, music_path, class_room_path)
    # cleaner.get_directory()
    # cleaner.exe_iso_zip_remover()
    # cleaner.file_mover()
    cleaner.older_file_remover()