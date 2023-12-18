import datetime as dt
import os
import natsort
import shutil
import re

start_directory = r'D://Ionki/Screen/'
end_directory = r'D://Ionki/'

while True:
    
    try:
        
        if len(os.listdir(start_directory)) == 0:
            print("Папка со скриншотами пуста. Ошибка: 005")
            break

        # Данная версия может обработать только одни сутки

        date = input('Введите год начала в формате YYYY-MM-DD: ')

        if(date == 'exit'):
            print('Пока :(')
            break
        
        time = input('Введите время начала в формате HH-mm: ')
        
        if(time == 'exit'):
            print('Пока :(')
            break
        
        date_mask = r'^[0-9]{4}[-][0-9]{2}[-][0-9]{2}$'
        time_mask = r'^[0-9]{2}[-][0-9]{2}$'
                
        check_date = re.fullmatch(date_mask, date)
        check_time = re.fullmatch(time_mask, time)
        
        # Проверка введённых значений
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
        
        iteration_time = dt.timedelta(minutes = 15)
        
        final_directory = (r'D://Ionki/' + Year_s + '/' + Month_s + '_' + Year_s + '/' 
                           + Day_s + '_' + Month_s + '_' + Year_s + '/')
        print('Конечная папка для сохранения переименнованых скринов: ', final_directory)
        
        year_dir = r'D://Ionki/' + Year_s + '/'
        month_dir = r'D://Ionki/' + Year_s + '/' + Month_s + '_' + Year_s + '/'
        
        print('Папка года и месяца: ', year_dir, month_dir)

        # Проверка наличия папки для сохранения скриншотов и создания такой
        if(os.path.exists(year_dir) != True):
            os.mkdir(year_dir)
            os.mkdir(month_dir)
            os.mkdir(final_directory)
        elif(os.path.exists(month_dir) != True):
            os.mkdir(month_dir)
            os.mkdir(final_directory)
        elif(os.path.exists(final_directory) != True):
            os.mkdir(final_directory)
#        else:
#            continue
        
        screenshots = os.listdir(start_directory)
        screenshots = natsort.natsorted(screenshots)
        
        print(screenshots[:3], screenshots[-3:])

        for scshot in screenshots:
            new_name = final_directory + '   lon_' + start_datetime.strftime('%Y_%m_%d_%H%M') + '.gif'
            old_name = start_directory + scshot
            print(old_name)
            if os.path.exists(new_name):
                print("Невозможно переименовать из %s в %s, такой файл уже существует" % (old_name,new_name))
                print('Ошибка: 004')
                continue

            else:
                print("Переименовано из %s в %s" % (old_name, new_name))
                os.rename(old_name, new_name)
            
            start_datetime = start_datetime + iteration_time
        
        break

    except:
        print('Ошибка: 001')
        break

