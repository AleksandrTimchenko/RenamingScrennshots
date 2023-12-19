import datetime as dt
import os
import natsort
import shutil
import re

start_directory = r'D://Ionki/Screen/'
end_directory = r'D://Ionki/'

while True:
    
    try:
        # Если папка со скриншотами пустая, программа дальше не выполняется
        if len(os.listdir(start_directory)) == 0:
            print("Папка со скриншотами пуста. Ошибка: 005")
            break
        
        screenshots = os.listdir(start_directory)
        screenshots = natsort.natsorted(screenshots)
        
        j=0
        for scshot in screenshots:
            if(scshot.endswith('.gif')):
                j=j+1
        if(j == 0):
            print('Остутствуют файлы с расширением .gif. Ошибка: 006')
            break

       
        date = input('Введите год начала в формате YYYY-MM-DD: ')

        if(date == 'exit'):
            print('Пока :(')
            break
        
        time = input('Введите время начала в формате HH-mm: ')
        
        if(time == 'exit'):
            print('Пока :(')
            break
        
        # Маска формата даты и времени. УУУУ-ММ-ДД и ЧЧ-мм
        date_mask = r'^[0-9]{4}[-][0-9]{2}[-][0-9]{2}$'
        time_mask = r'^[0-9]{2}[-][0-9]{2}$'
        
        # Проверка введённых значений
        check_date = re.fullmatch(date_mask, date)
        check_time = re.fullmatch(time_mask, time)
        
        # Условия, если формат даты и времени не прошёл проверку
        if(check_date == None):
            print('Введённая дата не соответствует формату. Ошибка: 002')
            break
        if(check_time == None):
            print('Введённое время не соответствует формату. Ошибка: 003')
            break        
        
        # Выделение года, месяца, дня и времени из введённых значений 
        Year_s = date.split('-')[0]
        Month_s = date.split('-')[1]
        Day_s = date.split('-')[2]
        
        Hour_s = time.split('-')[0]
        Minute_s = time.split('-')[1]
        
        
        
        print(date, time)
        
        # Создание даты и времени первого скриншота
        start_datetime = dt.datetime(year = int(Year_s), month = int(Month_s), 
                                day = int(Day_s), hour = int(Hour_s), minute = int(Minute_s))
        print('start_datetime: ', start_datetime)
        
        scshot_datetime = start_datetime
        
        iteration_time = dt.timedelta(minutes = 15)
              

        print(screenshots[:3], screenshots[-3:])

        for scshot in screenshots:
            # Условие, которое говорит использовать только файлы с расширением .gif
            if(scshot.endswith('.gif')):
                old_name = start_directory + scshot
                
                if(scshot_datetime.year > start_datetime.year):
                    start_datetime = scshot_datetime
                    
                    year_dir = r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/'
                    month_dir = (r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/')
                    final_dir = (r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%d') + '_' + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/')
                    
                    if(os.path.exists(year_dir) != True):
                        os.mkdir(year_dir)
                        os.mkdir(month_dir)
                        os.mkdir(final_dir)
                    elif(os.path.exists(month_dir) != True):
                        os.mkdir(month_dir)
                        os.mkdir(final_dir)
                    elif(os.path.exists(final_dir) != True):
                        os.mkdir(final_dir)
                        
                    new_name = final_dir + '   lon_' + scshot_datetime.strftime('%Y_%m_%d_%H%M') + '.gif'
                    
                    if os.path.exists(new_name):
                        print("Невозможно переименовать из %s в %s, такой файл уже существует" % (old_name,new_name))
                        print('Ошибка: 004')
                        continue

                    else:
                        print("Переименовано из %s в %s" % (old_name, new_name))
                        os.rename(old_name, new_name)
                
                elif(scshot_datetime.month > start_datetime.month):
                    start_datetime = scshot_datetime
                    
                    year_dir = r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/'
                    month_dir = (r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/')
                    final_dir = (r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%d') + '_' + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/')
                    
                    if(os.path.exists(year_dir) != True):
                        os.mkdir(year_dir)
                        os.mkdir(month_dir)
                        os.mkdir(final_dir)
                    elif(os.path.exists(month_dir) != True):
                        os.mkdir(month_dir)
                        os.mkdir(final_dir)
                    elif(os.path.exists(final_dir) != True):
                        os.mkdir(final_dir)
                        
                    new_name = final_dir + '   lon_' + scshot_datetime.strftime('%Y_%m_%d_%H%M') + '.gif'
                    
                    if os.path.exists(new_name):
                        print("Невозможно переименовать из %s в %s, такой файл уже существует" % (old_name,new_name))
                        print('Ошибка: 004')
                        continue

                    else:
                        print("Переименовано из %s в %s" % (old_name, new_name))
                        os.rename(old_name, new_name)
                        
                elif(scshot_datetime.day > start_datetime.day):
                    start_datetime = scshot_datetime
                    
                    year_dir = r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/'
                    month_dir = (r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/')
                    final_dir = (r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%d') + '_' + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/')
                    
                    if(os.path.exists(year_dir) != True):
                        os.mkdir(year_dir)
                        os.mkdir(month_dir)
                        os.mkdir(final_dir)
                    elif(os.path.exists(month_dir) != True):
                        os.mkdir(month_dir)
                        os.mkdir(final_dir)
                    elif(os.path.exists(final_dir) != True):
                        os.mkdir(final_dir)
                        
                    new_name = final_dir + '   lon_' + scshot_datetime.strftime('%Y_%m_%d_%H%M') + '.gif'
                    
                    if os.path.exists(new_name):
                        print("Невозможно переименовать из %s в %s, такой файл уже существует" % (old_name,new_name))
                        print('Ошибка: 004')
                        continue

                    else:
                        print("Переименовано из %s в %s" % (old_name, new_name))
                        os.rename(old_name, new_name)

                    
                else:
                    
                    year_dir = r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/'
                    month_dir = (r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/')
                    final_dir = (r'D://Ionki/' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/' 
                         + scshot_datetime.strftime('%d') + '_' + scshot_datetime.strftime('%m') + '_' + scshot_datetime.strftime('%Y') + '/')
                    
                    if(os.path.exists(year_dir) != True):
                        os.mkdir(year_dir)
                        os.mkdir(month_dir)
                        os.mkdir(final_dir)
                    elif(os.path.exists(month_dir) != True):
                        os.mkdir(month_dir)
                        os.mkdir(final_dir)
                    elif(os.path.exists(final_dir) != True):
                        os.mkdir(final_dir)
                        
                    new_name = final_dir + '   lon_' + scshot_datetime.strftime('%Y_%m_%d_%H%M') + '.gif'
                    
                    if os.path.exists(new_name):
                        print("Невозможно переименовать из %s в %s, такой файл уже существует" % (old_name,new_name))
                        print('Ошибка: 004')
                        continue

                    else:
                        print("Переименовано из %s в %s" % (old_name, new_name))
                        os.rename(old_name, new_name)
           
            scshot_datetime = scshot_datetime + iteration_time     
        
        break

    except:
        print('Ошибка: 001')
        break

