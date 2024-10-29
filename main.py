import os
import shutil
import time
import datetime
from tkinter import *
from tkinter import messagebox, filedialog
import logging

logging.basicConfig(
    filename= "desktop_cleaner.log",
    level= logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode= 'a'
)


current_time = datetime.datetime.now()
date_int = int(str(current_time.year) + str(current_time.month) + str(current_time.day))




class desktop_cleaner():
    
    def __init__(self, file_path, images_path, docs_path, videos_path, music_path, class_room_path):
        self.directory = file_path
        self.images = images_path
        self.docs = docs_path
        self.videos = videos_path
        self.music = music_path
        self.class_room = class_room_path
        self.lst_of_dir = os.listdir(self.directory) if os.path.exists(self.directory) else []
    
    # def get_directory(self):
        
    #     i = 1
    #     for x in self.lst_of_dir:
    #         print(f'{i}. {x}')
    #         i += 1
    #         desktop_cleaner.lst_of_dir.append(x)
    #     print('-----------------------')
            
    def remove_file_extensions(self, extensions):
        file_count = 0
        for file in self.lst_of_dir:
            path = os.path.join(self.directory, file)
            if any(file.endswith(ext) for ext in extensions):
                os.path.join(self.directory, file)
                print(f'{file} => Deleted')
                logging.info(f'{file} was removed from {path}')
                os.remove(path)
                file_count += 1
        if file_count == 0:
            print('Nothing Found')
            logging.info('Nothing was removed at the moment.')
            
    def older_file_remover(self, days_old = 30):
        file_count = 0
        
        for file in self.lst_of_dir:
            path = os.path.join(self.directory, file)
            m_time = os.path.getmtime(path)
            m_time = time.ctime(m_time)
            t_obj = time.strptime(m_time)
            time_stamp = time.strftime('%Y%m%d', t_obj)
            time_stamp = int(time_stamp)
            
            if date_int - time_stamp > days_old:
                logging.info(f'{file} was removed from {path}')
                os.remove(path)
                file_count += 1
            else: print(f'{file} => {date_int - time_stamp}')
        if file_count == 0:
            logging.info('Nothing was removed at the moment.')
            
    def move_files(self, target_directory, extensions):
        
        file_count = 0
        for file in self.lst_of_dir:
            path = os.path.join(self.directory, file)

            if any(file.endswith(ext) for ext in extensions):
                shutil.move(path, target_directory)
                logging.info(f'{file} was moved to {target_directory}')
                file_count += 1
                print(f'{file} => Moved to {self.class_room}')
                
        if file_count == 0:
            logging.info('Nothing was moved at the moment.')
        
class graphics():
    def __init__(self,root):
        self.root = root
        self.file_path = ''
    
    def program_executor(self):
        
        images_path = "C:\\Users\\sudha\\OneDrive\\Pictures"
        docs_path = "C:\\Users\\sudha\\OneDrive\\Documents"
        videos_path = "C:\\Users\\sudha\\Videos"
        music_path = "C:\\Users\\sudha\\Music"
        class_room_path = "D:\\Class_Room"
        
        cleaner = desktop_cleaner(self.file_path, images_path, docs_path, videos_path, music_path, class_room_path)
        # cleaner.get_directory()
        cleaner.remove_file_extensions({".exe", ".iso", ".zip", ".rar"})
        cleaner.move_files(docs_path, {".pdf", ".docx", ".ppt", ".txt"})
        cleaner.move_files(images_path, {".jpg", ".jpeg", ".png"})
        cleaner.older_file_remover(30)   
        Label(self.root, text= "Everything Logged In...", font=("Ariel", 15, 'bold')).pack()
        logging.info("---Done---")
        
    def path_input(self):
        
        path = filedialog.askdirectory()
        
        if path:
            self.file_path = path
            Label(self.root, text=f"Selected Directory: {self.file_path}", font=("Arial", 12)).pack()
            messagebox.showinfo("", "File Path set!")
            
    
    
    def working_gui(self):
        
        self.root.title('Desktop Cleaner')
        self.root.geometry('800x800')

        Label(self.root, text='Welcome to Desktop Cleaner', font=("Montserrat", 25)).pack()
        Label(self.root, text='A solution to organizing your space\n\n', font=("Montserrat", 20)).pack()
        
        Button(self.root, text='\nChoose File Path\n',font=("Ariel", 15, 'bold'), width=25, command=graphics.path_input).pack()
        
        
        Label(self.root, text='\nClicking the button will delete all the packages or zip files,\ndocuments will be moved to Documents Folder and Images to Images Folder.\n',font=("Ariel", 15, 'bold') ).pack()
        Button(self.root, text='\nRun the Program\n',font=("Ariel", 15, 'bold'), width=25, command=graphics.program_executor).pack()
        
        self.root.mainloop()
                
                
if __name__ == '__main__':
    
    tk = Tk()
  
    
    
    
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    logging.info(dt_string)
    images_path = "C:\\Users\\sudha\\OneDrive\\Pictures"
    docs_path = "C:\\Users\\sudha\\OneDrive\\Documents"
    videos_path = "C:\\Users\\sudha\\Videos"
    music_path = "C:\\Users\\sudha\\Music"
    class_room_path = "D:\\Class_Room"

    graphics = graphics(tk)
    
    
    
    graphics.working_gui()
    
    
    
    