#!/usr/bin/python
# vim: set fileencoding=utf-8:
##******************************************************************************************************
## MODULES IMPORT
##******************************************************************************************************
#-------------------------------------------------------------------------------------------------------
import os
import os.path
import re
import shelve
import shutil
import glob
import sys
from glob import *
import tkinter
from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import *
import tkinter.messagebox
from tkinter.messagebox import *
import tkinter.ttk
from tkinter.ttk import *
import PIL
from PIL import *
from PIL import Image , ImageTk
#-------------------------------------------------------------------------------------------------------
#*******************************************************************************************************



##
##
##



##******************************************************************************************************
## CONSTANTS AND VARIABLES
##******************************************************************************************************
#-------------------------------------------------------------------------------------------------------
## Directories constants and variables
#-------------------------------------------------------------------------------------------------------
officefiletypes = [('Text files (.txt .guide .rtf .odt .sxw .tex .texi .wpd .lwp)' , '.txt .guide .rtf .odt .sxw .tex .texi .wpd .lwp'),
                   ('Microsoft Word (.docx .docm .doc .dotx .dotm .dot)' , '.docx .docm .doc .dotx .dotm .dot'),
                   ('Microsoft Excel (.xlsx .xlsm .xls .xltx . xltm .xlt .xlsb .xlam .xla)' , '.xlsx .xlsm .xls .xltx . xltm .xlt .xlsb .xlam .xla'),
                   ('Microsoft PowerPoint (.pptx .pptm .ppt .ppsx .ppsm .pps .potx .potm .pot .ppam .ppa)' , '.pptx .pptm .ppt .ppsx .ppsm .pps .potx .potm .pot .ppam .ppa'),
                   ('Microsoft Access (.accdb .mdb)' , '.accdb .mdb'),
                   ('Все файлы (.*)' , '.*')]
                   
pdffiletypes = [('Adobe PDF (.pdf)' , '.pdf'),
                ('Все файлы (.*)' , '.*')]

imagefiletypes = [('Bitmap Picture (.bmp .dib .rle)' , '.bmp .dib .rle'),
                  ('JPEG Picture (.jpeg .jpg .jfif .jpe .jpf .jpx .jp2 .j2c .j2k .jpc .jps)' , '.jpeg .jpg .jfif .jpe .jpf .jpx .jp2 .j2c .j2k .jpc .jps'),
                  ('Portable Network Graphics (.png .mng .apng .pns)' , '.png .mng .apng .pns'),
                  ('Graphics Interchange Format (.gif)' , '.gif'),
                  ('Targa (.tga .vba .icb .vst)' , '.tga .vba .icb .vst'),
                  ('Wireles Bitmap (.wbm .wbmp)' , '.wbm .wbmp'),
                  ('Portable Bit Map (.pbm .pgm .ppm .pnm .pfm .pam)' , '.pbm .pgm .ppm .pnm .pfm .pam'),
                  ('Windows Icon (.ico)' , '.ico'),
                  ('Все файлы (.*)' , '.*')]

archivefiletypes = [('Archive (.rar .zip .7z .tar .gzip .bzip2 .arj .lzh .uc2 .gz .cab .ace .iso .uue)' , '.rar .zip .7z .tar .gzip .bzip2 .arj .lzh .uc2 .gz .cab .ace .iso .uue'),
                    ('Все файлы (.*)' , '.*')]

htmlfiletypes = [('Web Page (.html .php .jsp)' , '.html .php .jsp'),
                 ('Все файлы (.*)' , '.*')]

audiofiletypes = [('Uncompressed audio (.aiff .au .cdda .dsd .dxd .raw .wav)' , '.aiff .au .cdda .dsd .dxd .raw .wav'),
                  ('Lossles audio (.flac .ape .alac .la .pac .m4a .ofr .rka .shn .wv)' , '.flac .ape .alac .la .pac .m4a .ofr .rka .shn .wv'),
                  ('Lossy audio (.mp3 .mp2 .mpeg .ogg .aac .wma .mp4 .m4p .mpc .vqf .ra .rm .ots .swa)' , '.mp3 .mp2 .mpeg .ogg .aac .wma .mp4 .m4p .mpc .vqf .ra .rm .ots .swa'),
                  ('Other audio (.gym .imf .it .mid .midi .mt2 .mng .mod .nsf .niff .org .psf .s3m .spc .vgm)' , '.gym .imf .it .mid .midi .mt2 .mng .mod .nsf .niff .org .psf .s3m .spc .vgm'),
                  ('Все файлы (.*)' , '.*')]
                  
videofiletypes = [('Video (.mp4 .3gp .mpeg .avi .264 .3gpp .aac .avc .f4v .flv .m4v .mov .mpe .mpg .mts .mxf .r3d .ts .vob .wm)' , '.mp4 .3gp .mpeg .avi .264 .3gpp .aac .avc .f4v .flv .m4v .mov .mpe .mpg .mts .mxf .r3d .ts .vob .wm'),
                  ('Все файлы (.*)' , '.*')]
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## Welcome Window constants and variables
#-------------------------------------------------------------------------------------------------------
WELCOME_WINDOW_WIDTH = 400
WELCOME_WINDOW_HEIGHT = 300
WELCOME_WINDOW_TITLE = 'Вход в программу'
TITLE_LAB1 = 'Portfolio Manager'
TITLE_LAB1_FONT = 'tahoma 16 bold'
WELCOME_WINDOW_CBOX1_1 = 'Просмотр'
WELCOME_WINDOW_CBOX1_2 = 'Редактирование'
BUT_COME_TEXT = 'Войти'
BUT_START_CANCEL_TEXT = 'Выход'
LOGIN_LAB_TEXT = 'Введите логин'
PASSWORD_LAB_TEXT = 'Введите пароль' 
BUT_CREATE_PROJECT_TEXT = 'Создать новое портфолио'
WELCOME_LABEL_IMAGE = 'RE3NEM.png'
WELCOME_PROJECTS_LISTBOX_LAB_TEXT = 'Список доступных портфолио:'
loginnumber = -1
passwordnumber = -2
namesarray = []
sectionsarray = []
lpnvglobalarray = []
globalarraysave = []
project_view_right_panel_listbox_list = []
BUT_WELCOME_DELETE_PROJECT_TEXT = 'Удалить портфолио'
BUT_WELCOME_ADD_PROJECT_TEXT = 'Загрузить портфолио'
lookmode = ''
lookprojecttype = ''
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## Project View Window constants and variables
#-------------------------------------------------------------------------------------------------------
PROJECT_VIEW_WINDOW_WIDTH = 800
PROJECT_VIEW_WINDOW_HEIGHT = 600
PROJECT_VIEW_PROJECT_TYPE_TEXT = 'Тип портфолио'
PROJECT_VIEW_TEXT1_FONT = 'arial 14 bold'
PROJECT_VIEW_RIGHT_PANEL_LISTBOX_LAB = 'Разделы портфолио:'
PIGHT_PANEL_LISTBOX_COUNT = str(100)
PROJECT_VIEW_PROPERTIES_BAR_PANEL_PROGRAMM_NAME_TEXT = 'Portfolio Manager'
PROJECT_VIEW_PROPERTIES_BAR_PANEL_PROGRAMM_VERSION = 'v1.0.0'
PROJECT_VIEW_PROPERTIES_BAR_PANEL_ITEM_SELECTED = 'Выбран элемент:'
ITEM_SELECTED = 'item_selected_element'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## Project Create Window constants and variables
#-------------------------------------------------------------------------------------------------------
PROJECT_CREATE_WINDOW_WIDTH = 600
PROJECT_CREATE_WINDOW_HEIGHT = 400
USER_LOGIN_REGISTER_LAB_TEXT = 'Введите ваш новый логин'
USER_PASSWORD_REGISTER_LAB_TEXT = 'Введите ваш новый пароль'
PROJECT_CREATE_NAME_LAB_TEXT = 'Введите название вашего портфолио'
TEMPLATE_CHOISE_LIST_LABEL_TEXT = 'Выберите шаблон для портфолио'
TEMPLATE_CHOISE_LIST_ITEM1_TEXT = 'Пустое портфолио'
TEMPLATE_CHOISE_LIST_ITEM1_TEXT_ATTRIBUTE1 = 'Создает полностью пустой\n'
TEMPLATE_CHOISE_LIST_ITEM1_TEXT_ATTRIBUTE2 = 'портфолио\n'
TEMPLATE_CHOISE_LIST_ITEM2_TEXT = 'Стандартный шаблон'
TEMPLATE_CHOISE_LIST_ITEM2_TEXT_ATTRIBUTE1 = 'По умолчанию заданы поля под\n'
TEMPLATE_CHOISE_LIST_ITEM2_TEXT_ATTRIBUTE2 = 'Ф.И.О., возраст и прочее\n'
TEMPLATE_CHOISE_LIST_ITEM3_TEXT = 'Расширенный шаблон'
TEMPLATE_CHOISE_LIST_ITEM3_TEXT_ATTRIBUTE1 = 'Тот же "Стандартный шаблон",\n'
TEMPLATE_CHOISE_LIST_ITEM3_TEXT_ATTRIBUTE2 = 'дополненный новыми полями\n'
PROJECT_CREATE_CREATE_BUTTON_TEXT = 'Создать портфолио'
PROJECT_CREATE_CANCEL_BUTTON_TEXT = 'Отмена'
PROJECT_CREATE_PROJECT_TYPE_1 = 'Педагог'
PROJECT_CREATE_PROJECT_TYPE_2 = 'Ученик(ца)'
PROJECT_CREATE_PROJECT_TYPE_LAB_TEXT = 'Выберите тип портфолио'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## Project Options Window constants and variables
#-------------------------------------------------------------------------------------------------------
PROJECT_OPTIONS_WINDOW_WIDTH = 400
PROJECT_OPTIONS_WINDOW_HEIGHT = 300
PROJECT_OPTIONS_WINDOW_TITLE = 'Настройки'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## About Window constants and variables
#-------------------------------------------------------------------------------------------------------
ABOUT_WINDOW_WIDTH = 500
ABOUT_WINDOW_HEIGHT = 600
ABOUT_WINDOW_TITLE_TEXT = 'О программе'
ABOUT_WINDOW_LAB1 = 'Portfolio Manager v 1.0.0'
ABOUT_WINDOW_LAB2 = 'Программа была написана на языке Python 3.x.x'
ABOUT_WINDOW_LAB3 = 'Были использованы модули TKinter, os, glob, shelve, PIL, re'
ABOUT_WINDOW_LAB4 = ''
ABOUT_WINDOW_LAB5 = '5'
ABOUT_WINDOW_LAB6 = '6'
ABOUT_WINDOW_LAB7 = '7'
ABOUT_WINDOW_LAB8 = '8'
ABOUT_WINDOW_LAB9 = '9'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## Help Window constants and variables
#-------------------------------------------------------------------------------------------------------
HELP_WINDOW_WIDTH = 500
HELP_WINDOW_HEIGHT = 600
HELP_WINDOW_TITLE_TEXT = 'Помощь'
HELP_WINDOW_LAB1 = '1'
HELP_WINDOW_LAB2 = '2'
HELP_WINDOW_LAB3 = '3'
HELP_WINDOW_LAB4 = '4'
HELP_WINDOW_LAB5 = '5'
HELP_WINDOW_LAB6 = '6'
HELP_WINDOW_LAB7 = '7'
HELP_WINDOW_LAB8 = '8'
HELP_WINDOW_LAB9 = '9'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_project_save" Message Box
#-------------------------------------------------------------------------------------------------------
SAVE_PROJECT_MSGBOX_WIDTH = 300
SAVE_PROJECT_MSGBOX_HEIGHT = 300
SAVE_PROJECT_MSGBOX_TITLE_TEXT = 'Сохранить Портфолио'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_load_text_file" Message Box
#-------------------------------------------------------------------------------------------------------
LOAD_TEXT_FILE_MSGBOX_WIDTH = 500
LOAD_TEXT_FILE_MSGBOX_HEIGHT = 190
LOAD_TEXT_FILE_MSGBOX_TITLE_TEXT = 'Загрузить Текстовый/Microsoft office файл'
LOAD_TEXT_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT = 'Выберите файл:'
LOAD_TEXT_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT = 'Выберите раздел:'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_load_pdf_file" Message Box
#-------------------------------------------------------------------------------------------------------
LOAD_PDF_FILE_MSGBOX_WIDTH = 500
LOAD_PDF_FILE_MSGBOX_HEIGHT = 190
LOAD_PDF_FILE_MSGBOX_TITLE_TEXT = 'Загрузить PDF файл'
LOAD_PDF_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT = 'Выберите файл:'
LOAD_PDF_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT = 'Выберите раздел'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_load_image_file" Message Box
#-------------------------------------------------------------------------------------------------------
LOAD_IMAGE_FILE_MSGBOX_WIDTH = 500
LOAD_IMAGE_FILE_MSGBOX_HEIGHT = 190
LOAD_IMAGE_FILE_MSGBOX_TITLE_TEXT = 'Загрузить изображение'
LOAD_IMAGE_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT = 'Выберите файл:'
LOAD_IMAGE_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT = 'Выберите раздел'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_load_archive_file" Message Box
#-------------------------------------------------------------------------------------------------------
LOAD_ARCHIVE_FILE_MSGBOX_WIDTH = 500
LOAD_ARCHIVE_FILE_MSGBOX_HEIGHT = 190
LOAD_ARCHIVE_FILE_MSGBOX_TITLE_TEXT = 'Загрузить архив'
LOAD_ARCHIVE_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT = 'Выберите файл:'
LOAD_ARCHIVE_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT = 'Выберите раздел'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_load_html_file" Message Box
#-------------------------------------------------------------------------------------------------------
LOAD_HTML_FILE_MSGBOX_WIDTH = 500
LOAD_HTML_FILE_MSGBOX_HEIGHT = 190
LOAD_HTML_FILE_MSGBOX_TITLE_TEXT = 'Загрузить HTML страницу'
LOAD_HTML_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT = 'Выберите файл:'
LOAD_HTML_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT = 'Выберите раздел'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_load_audio_file" Message Box
#-------------------------------------------------------------------------------------------------------
LOAD_AUDIO_FILE_MSGBOX_WIDTH = 500
LOAD_AUDIO_FILE_MSGBOX_HEIGHT = 190
LOAD_AUDIO_FILE_MSGBOX_TITLE_TEXT = 'Загрузить аудио файл'
LOAD_AUDIO_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT = 'Выберите файл:'
LOAD_AUDIO_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT = 'Выберите раздел'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_load_video_file" Message Box
#-------------------------------------------------------------------------------------------------------
LOAD_VIDEO_FILE_MSGBOX_WIDTH = 500
LOAD_VIDEO_FILE_MSGBOX_HEIGHT = 190
LOAD_VIDEO_FILE_MSGBOX_TITLE_TEXT = 'Загрузить видео файл'
LOAD_VIDEO_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT = 'Выберите файл:'
LOAD_VIDEO_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT = 'Выберите раздел'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_delete_any_file" Message Box
#-------------------------------------------------------------------------------------------------------
DELETE_ANY_FILE_MSGBOX_WIDTH = 300
DELETE_ANY_FILE_MSGBOX_HEIGHT = 300
DELETE_ANY_FILE_MSGBOX_TITLE_TEXT = 'Удалить какой-либо файл'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_add_file_field" Message Box
#-------------------------------------------------------------------------------------------------------
ADD_FILE_FIELD_MSGBOX_WIDTH = 300
ADD_FILE_FIELD_MSGBOX_HEIGHT = 140
ADD_FILE_FIELD_MSGBOX_TITLE_TEXT = 'Добавить раздел портфолио'
ADD_FILE_FIELD_MSGBOX_NAME_LAB_TEXT = 'Введите название раздела:'
ADD_FILE_FIELD_MSGBOX_TYPE_LAB_TEXT = 'Выберите тип раздела:'
FIELD_TYPE_1 = 'Поле объектов'
FIELD_TYPE_2 = 'Поле файлов'
BUT_ADD_FILE_FIELD_MSGBOX_CREATE_TEXT = 'Создать'
BUT_ADD_FILE_FIELD_MSGBOX_CANCEL_TEXT = 'Отмена'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_add_label_field" Message Box
#-------------------------------------------------------------------------------------------------------
ADD_LABEL_FIELD_MSGBOX_WIDTH = 300
ADD_LABEL_FIELD_MSGBOX_HEIGHT = 300
ADD_LABEL_FIELD_MSGBOX_TITLE_TEXT = 'Добавить текстовое поле (резюме)'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_add_image_field" Message Box
#-------------------------------------------------------------------------------------------------------
ADD_IMAGE_FIELD_MSGBOX_WIDTH = 300
ADD_IMAGE_FIELD_MSGBOX_HEIGHT = 300
ADD_IMAGE_FIELD_MSGBOX_TITLE_TEXT = 'Добавить поле для изображения (резюме)'
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
## "but_project_view_delete_any_field" Message Box
#-------------------------------------------------------------------------------------------------------
DELETE_ANY_FIELD_MSGBOX_WIDTH = 300
DELETE_ANY_FIELD_MSGBOX_HEIGHT = 140
DELETE_ANY_FIELD_MSGBOX_TITLE_TEXT = 'Удалить поле или раздел'
DELETE_ANY_FILE_MSGBOX_OBJECT_LIST_LAB_TEXT = 'Разделы портфолио'
BUT_DELETE_ANY_FIELD_MSGBOX_DELETE_TEXT = 'Удалить'
BUT_DELETE_ANY_FIELD_MSGBOX_CANCELE_TEXT = 'Отмена'
#-------------------------------------------------------------------------------------------------------
##******************************************************************************************************



##
##
##



##******************************************************************************************************
## FUNCTIONS AND CLASSES
##******************************************************************************************************
#-------------------------------------------------------------------------------------------------------
## Tooltips class
#-------------------------------------------------------------------------------------------------------
class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 1000     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify='left',
                       background="#B6C3FF" , font = 'arial 8 bold' , relief='flat', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
#-------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------
##------------------------------------------------------------------------------------------------------
## MouseClick events
##------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
## Welcome Window Come Button event
def but_come_event(event):
    if event.num == 1:
        def loadsectionslist():
            loaddataproject = shelve.open('Projects/' + namesarray[loginnumber - 1][:len(namesarray[loginnumber - 1]) - 1] + '/data' , flag = 'c')
            print(loaddataproject['sectionsdata'])
            global project_view_right_panel_listbox_list
            project_view_right_panel_listbox_list = loaddataproject['sectionsdata']
            global lookprojecttype
            lookprojecttype = loaddataproject['projecttype']
            project_view_project_type_viewer['text'] = PROJECT_VIEW_PROJECT_TYPE_TEXT + ' : ' + lookprojecttype
            project_view_right_panel_listbox.delete(0 , END)
            for i in project_view_right_panel_listbox_list:
                project_view_right_panel_listbox.insert(END , i)
            print(project_view_right_panel_listbox_list)
            loaddataproject.close()
            
        logintag = r'^'+login_entry.get()+'$'
        
        global loginnumber

        loginsfileopen = open('Data/logins.pmlpnf' , 'r')
        loginsarray = loginsfileopen.readlines()
        print(loginsarray)
        for num11,line11 in enumerate(loginsarray,1):
            if re.match(logintag , line11):
                print('Value: ' + line11 + str(num11))
                loginnumber = num11
                print(loginnumber)
        loginsfileopen.close()

        passwordtag = r'^'+password_entry.get()+r'$'

        passwordsfileopen = open('Data/passwords.pmlpnf' , 'r')
        passwordsarray = passwordsfileopen.readlines()
        print(passwordsarray)
        for num22,line22 in enumerate(passwordsarray,1):
            if re.match(passwordtag , line22):
                print('Value: ' + line22 + str(num22))
                global passwordnumber
                passwordnumber = num22
                print(passwordnumber)
        passwordsfileopen.close()

        namesfileopen = open('Data/names.pmlpnf' , 'r')
        global namesarray
        namesarray = namesfileopen.readlines()
        if loginnumber == passwordnumber:
            print(namesarray[loginnumber - 1])
            infolpnarray = [loginsarray[loginnumber-1],passwordsarray[passwordnumber-1],namesarray[loginnumber-1]]
            print(infolpnarray)
            project_view_window.deiconify()
            welcome_window.withdraw()
        else:
            showwarning('Вход в программу' , 'Неверный логин или пароль!')
        namesfileopen.close()

        global lpnvglobalarray
        lpnvglobalarray = []
        
        loadsectionslist()
        project_view_window.update_idletasks()
        project_view_window.update()
        
        if welcome_cbox.get() == 'Просмотр':
            but_project_view_project_save['state'] = 'disabled'
            but_project_view_project_save.unbind('<Button-1>')
            but_project_view_load_text_file['state'] = 'disabled'
            but_project_view_load_text_file.unbind('<Button-1>')
            but_project_view_load_pdf_file['state'] = 'disabled'
            but_project_view_load_pdf_file.unbind('<Button-1>')
            but_project_view_load_image_file['state'] = 'disabled'
            but_project_view_load_image_file.unbind('<Button-1>')
            but_project_view_load_archive_file['state'] = 'disabled'
            but_project_view_load_archive_file.unbind('<Button-1>')
            but_project_view_load_html_file['state'] = 'disabled'
            but_project_view_load_html_file.unbind('<Button-1>')
            but_project_view_load_audio_file['state'] = 'disabled'
            but_project_view_load_audio_file.unbind('<Button-1>')
            but_project_view_load_video_file['state'] = 'disabled'
            but_project_view_load_video_file.unbind('<Button-1>')
            but_project_view_delete_any_file['state'] = 'disabled'
            but_project_view_delete_any_file.unbind('<Button-1>')
            but_project_view_add_file_field['state'] = 'disabled'
            but_project_view_add_file_field.unbind('<Button-1>')
            but_project_view_add_label_field['state'] = 'disabled'
            but_project_view_add_label_field.unbind('<Button-1>')
            but_project_view_add_image_field['state'] = 'disabled'
            but_project_view_add_image_field.unbind('<Button-1>')
            but_project_view_delete_any_field['state'] = 'disabled'
            but_project_view_delete_any_field.unbind('<Button-1>')
            lookmode = 'Просмотр'
            project_view_project_opening_type['text'] = lookmode
            project_view_window.update_idletasks()
            
        if welcome_cbox.get() == 'Редактирование':
            but_project_view_project_save['state'] = 'enabled'
            but_project_view_project_save.bind('<Button-1>', but_project_view_project_save_event)
            but_project_view_load_text_file['state'] = 'enabled'
            but_project_view_load_text_file.bind('<Button-1>', but_project_view_load_text_file_event)
            but_project_view_load_pdf_file['state'] = 'enabled'
            but_project_view_load_pdf_file.bind('<Button-1>', but_project_view_load_pdf_file_event)
            but_project_view_load_image_file['state'] = 'enabled'
            but_project_view_load_image_file.bind('<Button-1>', but_project_view_load_image_file_event)
            but_project_view_load_archive_file['state'] = 'enabled'
            but_project_view_load_archive_file.bind('<Button-1>', but_project_view_load_archive_file_event)
            but_project_view_load_html_file['state'] = 'enabled'
            but_project_view_load_html_file.bind('<Button-1>', but_project_view_load_html_file_event)
            but_project_view_load_audio_file['state'] = 'enabled'
            but_project_view_load_audio_file.bind('<Button-1>', but_project_view_load_audio_file_event)
            but_project_view_load_video_file['state'] = 'enabled'
            but_project_view_load_video_file.bind('<Button-1>', but_project_view_load_video_file_event)
            but_project_view_delete_any_file['state'] = 'enabled'
            but_project_view_delete_any_file.bind('<Button-1>', but_project_view_delete_any_file_event)
            but_project_view_add_file_field['state'] = 'enabled'
            but_project_view_add_file_field.bind('<Button-1>', but_project_view_add_file_field_event)
            but_project_view_add_label_field['state'] = 'enabled'
            but_project_view_add_label_field.bind('<Button-1>', but_project_view_add_label_field_event)
            but_project_view_add_image_field['state'] = 'enabled'
            but_project_view_add_image_field.bind('<Button-1>', but_project_view_add_image_field_event)
            but_project_view_delete_any_field['state'] = 'enabled'
            but_project_view_delete_any_field.bind('<Button-1>', but_project_view_delete_any_field_event)
            lookmode = 'Редактирование'
            project_view_project_opening_type['text'] = lookmode
            project_view_window.update_idletasks()
            
        login_entry.delete(0 , END)
        password_entry.delete(0 , END)
        
        arraysfileopen = open('Data/arrays.pmlpnf' , 'r')
        arraysarray = arraysfileopen.readlines()
        for aavalue in arraysarray:
            aavaluearray = aavalue.split('|')
            lpnvglobalarray.append(aavaluearray)
            print(aavaluearray)
        print(lpnvglobalarray)
        arraysfileopen.close()
        return namesarray
        
##

## Welcome Window Cancel Button event
def but_start_cancel_event(event):
    if event.num == 1:
        welcome_window.destroy()
        project_create_window.destroy()
        project_view_window.destroy()
        sys.exit()

##

## Welcome Window Create Project Button event
def but_create_project_event(event):
    if event.num == 1:
        project_create_window.deiconify()
        welcome_window.withdraw()
        
##

## Project Create Window Cancel Button event
def but_project_create_cancel_event(event):
    if event.num == 1:
        welcome_window.deiconify()
        project_create_window.withdraw()

##

## Project Create Window Create Button event
def but_project_create_create_event(event):
    if event.num == 1:
        print(user_login_register_entry.get())
        print(user_password_register_entry.get())
        print(project_create_name_entry.get())
#        print(template_choise_list.get())
#        print(project_create_project_type_cbox.get())
        userprojectlist = [user_login_register_entry.get(),user_password_register_entry.get(),project_create_name_entry.get()]

        writelogins = open(loginsfile , 'a')
        writelogins.write(user_login_register_entry.get() + '\n')
        writelogins.close()
        
        writepasswords = open(passwordsfile , 'a')
        writepasswords.write(user_password_register_entry.get() + '\n')
        writepasswords.close()
        
        writenames = open(namesfile , 'a')
        writenames.write(project_create_name_entry.get() + '\n')
        writenames.close()
        
        writearray = shelve.open('Data/arrays.txt' , flag = 'c')
        writearray['savedata'] = userprojectlist
        writearray.close()
        
        os.mkdir('Projects/' + project_create_name_entry.get())
        
        newprojectlogin = open('Projects/' + project_create_name_entry.get() + '/' + project_create_name_entry.get() + '_login.pmlpnf' , 'w' , encoding = 'utf-8')
        newprojectlogin.write(user_login_register_entry.get())
        newprojectlogin.close()
        newprojectpassword = open('Projects/' + project_create_name_entry.get() + '/' + project_create_name_entry.get() + '_password.pmlpnf' , 'w' , encoding = 'utf-8')
        newprojectpassword.write(user_password_register_entry.get())
        newprojectpassword.close()
        newprojectname = open('Projects/' + project_create_name_entry.get() + '/' + project_create_name_entry.get() + '_name.pmlpnf' , 'w' , encoding = 'utf-8')
        newprojectname.write(project_create_name_entry.get())
        newprojectname.close()
        
        global lookprojecttype
        lookprojecttype = project_create_project_type_cbox.get()
        project_view_project_type_viewer['text'] = PROJECT_VIEW_PROJECT_TYPE_TEXT + ' : ' + lookprojecttype
        project_view_window.update_idletasks()
        
        newprojectarray = shelve.open('Projects/' + project_create_name_entry.get() + '/' + project_create_name_entry.get() + '_array.pmlpnf' ,flag = 'c')
        userprojectlist.append(sectionsarray)
        newprojectarray['dataproject'] = userprojectlist
        newprojectarray.close()
        
        opendatasavefile = shelve.open('Projects/' + project_create_name_entry.get() + '/data' , flag = 'c')
        opendatasavefile['sectionsdata'] = ['Данные о владельце портфолио']
        os.mkdir('Projects/' + project_create_name_entry.get() + '/' + opendatasavefile['sectionsdata'][0] + '_section')
        opendatasavefile['projecttype'] = project_create_project_type_cbox.get()
        print('\n')
        print(opendatasavefile['projecttype'])
        opendatasavefile.close()
        
        
        welcome_window.update_idletasks()
#        project_view_right_panel_listbox_list = ['Данные о пользователе']
#        for project_view_right_panel_listbox_list_item in project_view_right_panel_listbox_list:
#            project_view_right_panel_listbox.insert(END , project_view_right_panel_listbox_list_item)
#        project_create_window.update_idletasks()
        project_create_window.withdraw()
        welcome_window.deiconify()
        
##

## Options Window Show event        
def but_project_view_options_event(event):
    if event.num == 1:
        project_options_window = Toplevel(welcome_window , width = PROJECT_OPTIONS_WINDOW_WIDTH ,
                                          height = PROJECT_OPTIONS_WINDOW_HEIGHT)
        project_options_window.title(PROJECT_OPTIONS_WINDOW_TITLE)
        project_options_window.resizable(False , False)
        project_options_window.iconbitmap('icon.ico')
        
##
        
##Project View Window Change User Button event
def but_project_view_change_user_event(event):
    if event.num == 1:
        welcome_window.deiconify()
        project_view_window.withdraw()
 
##

## Help Window Show event
def but_project_view_help_event(event):
    if event.num == 1:
        help_window = Toplevel(welcome_window , width = HELP_WINDOW_WIDTH , height = HELP_WINDOW_HEIGHT)
        help_window.title(HELP_WINDOW_TITLE_TEXT)
        help_window.resizable(False , False)
        help_window.iconbitmap('icon.ico')
        help_window_lab1 = Label(help_window , text = HELP_WINDOW_LAB1 , font = 'arial 12 bold')
        help_window_lab1.place(x = 20 , y = 20 , width = 460 , height = 30)
        help_window_lab2 = Label(help_window , text = HELP_WINDOW_LAB2 , font = 'arial 12 bold')
        help_window_lab2.place(x = 20 , y = 50 , width = 460 , height = 30)
        help_window_lab3 = Label(help_window , text = HELP_WINDOW_LAB3 , font = 'arial 12 bold')
        help_window_lab3.place(x = 20 , y = 80 , width = 460 , height = 30)
        help_window_lab4 = Label(help_window , text = HELP_WINDOW_LAB4 , font = 'arial 12 bold')
        help_window_lab4.place(x = 20 , y = 110 , width = 460 , height = 30)
        help_window_lab5 = Label(help_window , text = HELP_WINDOW_LAB5 , font = 'arial 12 bold')
        help_window_lab5.place(x = 20 , y = 140 , width = 460 , height = 30)
        help_window_lab6 = Label(help_window , text = HELP_WINDOW_LAB6 , font = 'arial 12 bold')
        help_window_lab6.place(x = 20 , y = 170 , width = 460 , height = 30)
        help_window_lab7 = Label(help_window , text = HELP_WINDOW_LAB7 , font = 'arial 12 bold')
        help_window_lab7.place(x = 20 , y = 200 , width = 460 , height = 30)
        help_window_lab8 = Label(help_window , text = HELP_WINDOW_LAB8 , font = 'arial 12 bold')
        help_window_lab8.place(x = 20 , y = 230 , width = 460 , height = 30)
        help_window_lab9 = Label(help_window , text = HELP_WINDOW_LAB9 , font = 'arial 12 bold')
        help_window_lab9.place(x = 20 , y = 260 , width = 460 , height = 30)
        
##

## About Window Show event
def but_project_view_about_event(event):
    if event.num == 1:
        about_window = Toplevel(welcome_window , width = ABOUT_WINDOW_WIDTH , height = ABOUT_WINDOW_HEIGHT)
        about_window.title(ABOUT_WINDOW_TITLE_TEXT)
        about_window.resizable(False , False)
        about_window.iconbitmap('icon.ico')        
        about_window_lab1 = Label(about_window , text = ABOUT_WINDOW_LAB1 , font = 'arial 12 bold')
        about_window_lab1.place(x = 20 , y = 20 , width = 460 , height = 30)
        about_window_lab2 = Label(about_window , text = ABOUT_WINDOW_LAB2 , font = 'arial 10 bold')
        about_window_lab2.place(x = 20 , y = 50 , width = 460 , height = 30)
        about_window_lab3 = Label(about_window , text = ABOUT_WINDOW_LAB3 , font = 'arial 10 bold')
        about_window_lab3.place(x = 20 , y = 80 , width = 460 , height = 30)
        about_window_lab4 = Label(about_window , text = ABOUT_WINDOW_LAB4 , font = 'arial 10 bold')
        about_window_lab4.place(x = 20 , y = 110 , width = 460 , height = 30)
        about_window_lab5 = Label(about_window , text = ABOUT_WINDOW_LAB5 , font = 'arial 10 bold')
        about_window_lab5.place(x = 20 , y = 140 , width = 460 , height = 30)
        about_window_lab6 = Label(about_window , text = ABOUT_WINDOW_LAB6 , font = 'arial 10 bold')
        about_window_lab6.place(x = 20 , y = 170 , width = 460 , height = 30)
        about_window_lab7 = Label(about_window , text = ABOUT_WINDOW_LAB7 , font = 'arial 10 bold')
        about_window_lab7.place(x = 20 , y = 200 , width = 460 , height = 30)
        about_window_lab8 = Label(about_window , text = ABOUT_WINDOW_LAB8 , font = 'arial 10 bold')
        about_window_lab8.place(x = 20 , y = 230 , width = 460 , height = 30)
        about_window_lab9 = Label(about_window , text = ABOUT_WINDOW_LAB9 , font = 'arial 10 bold')
        about_window_lab9.place(x = 20 , y = 260 , width = 460 , height = 30)
        about_window_ok_but = Button(about_window , text = 'OK')
        about_window_ok_but.place(x = 200 , y = 550 , width = 100 , height = 30)
        
##
        
## Project View Window Change View Type Button event
def but_project_view_change_view_type_event(event):
    if event.num == 1:
        pass

##

## Project View Window Quit From Programm Button event
        
def but_project_view_quit_event(event):
    if event.num == 1:
        quitbox = askquestion('Выход из программы' , 'Вы правда хотите выйти из программы?')
        if quitbox == 'yes':
            welcome_window.destroy()
            project_create_window.destroy()
            project_view_window.destroy()
            sys.exit()
        
##

## Project View Window Project Save Button event
def but_project_view_project_save_event(event):
    if event.num == 1:
        saveprojectaskbox = askquestion('Сохранить портфолио' , 'Вы правда хотите сохранить изменения?')
        print('\n')
        if saveprojectaskbox == 'yes':
            datasavepath = namesarray[loginnumber - 1]
            savedataproject = shelve.open('Projects/' + datasavepath[:len(datasavepath) - 1] + '/data' , flag = 'c')
            print('\n')
            print(project_view_right_panel_listbox_list)
            savedataproject['sectionsdata'] = project_view_right_panel_listbox_list
            print(savedataproject['sectionsdata'])
            savedataproject.close()
        
##

## Project View Window Load Text File Button event
def but_project_view_load_text_file_event(event):
    if event.num == 1:
        def click_load_event(event): 
            load_text_file_msgbox_choise_file_entry['text'] = askopenfilename(filetypes = officefiletypes)
            but_project_view_load_text_file_msgbox.update_idletasks()
            print(load_text_file_msgbox_choise_file_entry['text'])
        def click_create_event(event):
            pass
        def click_cancel_event(event):
            but_project_view_load_text_file_msgbox.destroy()
        but_project_view_load_text_file_msgbox = Toplevel(welcome_window , width = LOAD_TEXT_FILE_MSGBOX_WIDTH ,
                                                            height = LOAD_TEXT_FILE_MSGBOX_HEIGHT)
        but_project_view_load_text_file_msgbox.title(LOAD_TEXT_FILE_MSGBOX_TITLE_TEXT)
        but_project_view_load_text_file_msgbox.resizable(False , False)
        but_project_view_load_text_file_msgbox.iconbitmap('Data\Icons\load_text_file_but.ico')
        load_text_file_msgbox_choise_file_lab = Label(but_project_view_load_text_file_msgbox ,
                                                      text = LOAD_TEXT_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT ,
                                                      font = 'arial 10 bold')
        load_text_file_msgbox_choise_file_lab.place(x = 20 , y = 20 , width = 460 , height = 20)
        load_text_file_msgbox_choise_file_entry = Label(but_project_view_load_text_file_msgbox , 
                                                        font = 'arial 10 bold' ,
                                                        text = '')
        load_text_file_msgbox_choise_file_entry.place(x = 20 , y = 40 , width = 460 , height = 30)
        load_text_file_msgbox_choise_file_but = Button(but_project_view_load_text_file_msgbox ,
                                                       text = 'Выбрать файл')
        load_text_file_msgbox_choise_file_but.place(x = 20 , y = 140 , width = 140 , height = 30)
        load_text_file_msgbox_choise_file_but.bind('<Button-1>' , click_load_event)
        load_text_file_msgbox_create_but = Button(but_project_view_load_text_file_msgbox ,
                                                       text = 'Добавить файл')
        load_text_file_msgbox_create_but.place(x = 180 , y = 140 , width = 140 , height = 30)
        load_text_file_msgbox_create_but.bind('<Button-1>' , click_create_event)
        load_text_file_msgbox_cancel_but = Button(but_project_view_load_text_file_msgbox ,
                                                       text = 'Отмена')
        load_text_file_msgbox_cancel_but.place(x = 340 , y = 140 , width = 140 , height = 30)
        load_text_file_msgbox_cancel_but.bind('<Button-1>' , click_cancel_event)
        load_text_file_msgbox_view_combobox_lab = Label(but_project_view_load_text_file_msgbox ,
                                                        text = LOAD_TEXT_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT ,
                                                        font = 'arial 10 bold')
        load_text_file_msgbox_view_combobox_lab.place(x = 20 , y = 80 , width = 460 , height = 20)
        load_text_file_msgbox_view_combobox = Combobox(but_project_view_load_text_file_msgbox , 
                                                       values = project_view_right_panel_listbox_list,
                                                       font = 'arial 10 bold')
        load_text_file_msgbox_view_combobox.place(x = 20 , y = 100 , width = 460 , height = 30)
        
##

## Project View Window Load PDF File Button event
def but_project_view_load_pdf_file_event(event):
    if event.num == 1:
        def click_load_event(event): 
            load_pdf_file_msgbox_choise_file_entry['text'] = askopenfilename(filetypes = pdffiletypes)
            but_project_view_load_pdf_file_msgbox.update_idletasks()
            print(load_pdf_file_msgbox_choise_file_entry['text'])
        def click_create_event(event):
            pass
        def click_cancel_event(event):
            but_project_view_load_pdf_file_msgbox.destroy()
        but_project_view_load_pdf_file_msgbox = Toplevel(welcome_window , width = LOAD_PDF_FILE_MSGBOX_WIDTH ,
                                                        height = LOAD_PDF_FILE_MSGBOX_HEIGHT)
        but_project_view_load_pdf_file_msgbox.title(LOAD_PDF_FILE_MSGBOX_TITLE_TEXT)
        but_project_view_load_pdf_file_msgbox.resizable(False , False)
        but_project_view_load_pdf_file_msgbox.iconbitmap('Data\Icons\load_pdf_file_but.ico')
        load_pdf_file_msgbox_choise_file_lab = Label(but_project_view_load_pdf_file_msgbox ,
                                                      text = LOAD_PDF_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT ,
                                                      font = 'arial 10 bold')
        load_pdf_file_msgbox_choise_file_lab.place(x = 20 , y = 20 , width = 460 , height = 20)
        load_pdf_file_msgbox_choise_file_entry = Label(but_project_view_load_pdf_file_msgbox , 
                                                        font = 'arial 10 bold' ,
                                                        text = '')
        load_pdf_file_msgbox_choise_file_entry.place(x = 20 , y = 40 , width = 460 , height = 30)
        load_pdf_file_msgbox_choise_file_but = Button(but_project_view_load_pdf_file_msgbox ,
                                                       text = 'Выбрать файл')
        load_pdf_file_msgbox_choise_file_but.place(x = 20 , y = 140 , width = 140 , height = 30)
        load_pdf_file_msgbox_choise_file_but.bind('<Button-1>' , click_load_event)
        load_pdf_file_msgbox_create_but = Button(but_project_view_load_pdf_file_msgbox ,
                                                       text = 'Добавить файл')
        load_pdf_file_msgbox_create_but.place(x = 180 , y = 140 , width = 140 , height = 30)
        load_pdf_file_msgbox_create_but.bind('<Button-1>' , click_create_event)
        load_pdf_file_msgbox_cancel_but = Button(but_project_view_load_pdf_file_msgbox ,
                                                       text = 'Отмена')
        load_pdf_file_msgbox_cancel_but.place(x = 340 , y = 140 , width = 140 , height = 30)
        load_pdf_file_msgbox_cancel_but.bind('<Button-1>' , click_cancel_event)
        load_pdf_file_msgbox_view_combobox_lab = Label(but_project_view_load_pdf_file_msgbox ,
                                                        text = LOAD_PDF_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT ,
                                                        font = 'arial 10 bold')
        load_pdf_file_msgbox_view_combobox_lab.place(x = 20 , y = 80 , width = 460 , height = 20)
        load_pdf_file_msgbox_view_combobox = Combobox(but_project_view_load_pdf_file_msgbox , 
                                                       values = project_view_right_panel_listbox_list,
                                                       font = 'arial 10 bold')
        load_pdf_file_msgbox_view_combobox.place(x = 20 , y = 100 , width = 460 , height = 30)
        
##

## Project View Window Load Image File Button event
def but_project_view_load_image_file_event(event):
    if event.num == 1:
        def click_load_event(event): 
            load_image_file_msgbox_choise_file_entry['text'] = askopenfilename(filetypes = imagefiletypes)
            but_project_view_load_image_file_msgbox.update_idletasks()
            print(load_image_file_msgbox_choise_file_entry['text'])
        def click_create_event(event):
            pass
        def click_cancel_event(event):
            but_project_view_load_image_file_msgbox.destroy()
        but_project_view_load_image_file_msgbox = Toplevel(welcome_window , width = LOAD_IMAGE_FILE_MSGBOX_WIDTH ,
                                                           height = LOAD_IMAGE_FILE_MSGBOX_HEIGHT)
        but_project_view_load_image_file_msgbox.title(LOAD_IMAGE_FILE_MSGBOX_TITLE_TEXT)
        but_project_view_load_image_file_msgbox.resizable(False , False)
        but_project_view_load_image_file_msgbox.iconbitmap('Data\Icons\load_image_file_but.ico')
        load_image_file_msgbox_choise_file_lab = Label(but_project_view_load_image_file_msgbox ,
                                                      text = LOAD_IMAGE_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT ,
                                                      font = 'arial 10 bold')
        load_image_file_msgbox_choise_file_lab.place(x = 20 , y = 20 , width = 460 , height = 20)
        load_image_file_msgbox_choise_file_entry = Label(but_project_view_load_image_file_msgbox , 
                                                        font = 'arial 10 bold' ,
                                                        text = '')
        load_image_file_msgbox_choise_file_entry.place(x = 20 , y = 40 , width = 460 , height = 30)
        load_image_file_msgbox_choise_file_but = Button(but_project_view_load_image_file_msgbox ,
                                                       text = 'Выбрать файл')
        load_image_file_msgbox_choise_file_but.place(x = 20 , y = 140 , width = 140 , height = 30)
        load_image_file_msgbox_choise_file_but.bind('<Button-1>' , click_load_event)
        load_image_file_msgbox_create_but = Button(but_project_view_load_image_file_msgbox ,
                                                       text = 'Добавить файл')
        load_image_file_msgbox_create_but.place(x = 180 , y = 140 , width = 140 , height = 30)
        load_image_file_msgbox_create_but.bind('<Button-1>' , click_create_event)
        load_image_file_msgbox_cancel_but = Button(but_project_view_load_image_file_msgbox ,
                                                       text = 'Отмена')
        load_image_file_msgbox_cancel_but.place(x = 340 , y = 140 , width = 140 , height = 30)
        load_image_file_msgbox_cancel_but.bind('<Button-1>' , click_cancel_event)
        load_image_file_msgbox_view_combobox_lab = Label(but_project_view_load_image_file_msgbox ,
                                                        text = LOAD_IMAGE_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT ,
                                                        font = 'arial 10 bold')
        load_image_file_msgbox_view_combobox_lab.place(x = 20 , y = 80 , width = 460 , height = 20)
        load_image_file_msgbox_view_combobox = Combobox(but_project_view_load_image_file_msgbox , 
                                                       values = project_view_right_panel_listbox_list,
                                                       font = 'arial 10 bold')
        load_image_file_msgbox_view_combobox.place(x = 20 , y = 100 , width = 460 , height = 30)
        
##

## Project View Window Load Archive File Button event
def but_project_view_load_archive_file_event(event):
    if event.num == 1:
        def click_load_event(event): 
            load_archive_file_msgbox_choise_file_entry['text'] = askopenfilename(filetypes = archivefiletypes)
            but_project_view_load_archive_file_msgbox.update_idletasks()
            print(load_archive_file_msgbox_choise_file_entry['text'])
        def click_create_event(event):
            pass
        def click_cancel_event(event):
            but_project_view_load_archive_file_msgbox.destroy()
        but_project_view_load_archive_file_msgbox = Toplevel(welcome_window , width = LOAD_ARCHIVE_FILE_MSGBOX_WIDTH ,
                                                             height = LOAD_ARCHIVE_FILE_MSGBOX_HEIGHT)
        but_project_view_load_archive_file_msgbox.title(LOAD_ARCHIVE_FILE_MSGBOX_TITLE_TEXT)
        but_project_view_load_archive_file_msgbox.resizable(False , False)
        but_project_view_load_archive_file_msgbox.iconbitmap('Data\Icons\load_archive_file_but.ico')
        load_archive_file_msgbox_choise_file_lab = Label(but_project_view_load_archive_file_msgbox ,
                                                      text = LOAD_ARCHIVE_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT ,
                                                      font = 'arial 10 bold')
        load_archive_file_msgbox_choise_file_lab.place(x = 20 , y = 20 , width = 460 , height = 20)
        load_archive_file_msgbox_choise_file_entry = Label(but_project_view_load_archive_file_msgbox , 
                                                        font = 'arial 10 bold' ,
                                                        text = '')
        load_archive_file_msgbox_choise_file_entry.place(x = 20 , y = 40 , width = 460 , height = 30)
        load_archive_file_msgbox_choise_file_but = Button(but_project_view_load_archive_file_msgbox ,
                                                       text = 'Выбрать файл')
        load_archive_file_msgbox_choise_file_but.place(x = 20 , y = 140 , width = 140 , height = 30)
        load_archive_file_msgbox_choise_file_but.bind('<Button-1>' , click_load_event)
        load_archive_file_msgbox_create_but = Button(but_project_view_load_archive_file_msgbox ,
                                                       text = 'Добавить файл')
        load_archive_file_msgbox_create_but.place(x = 180 , y = 140 , width = 140 , height = 30)
        load_archive_file_msgbox_create_but.bind('<Button-1>' , click_create_event)
        load_archive_file_msgbox_cancel_but = Button(but_project_view_load_archive_file_msgbox ,
                                                       text = 'Отмена')
        load_archive_file_msgbox_cancel_but.place(x = 340 , y = 140 , width = 140 , height = 30)
        load_archive_file_msgbox_cancel_but.bind('<Button-1>' , click_cancel_event)
        load_archive_file_msgbox_view_combobox_lab = Label(but_project_view_load_archive_file_msgbox ,
                                                        text = LOAD_ARCHIVE_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT ,
                                                        font = 'arial 10 bold')
        load_archive_file_msgbox_view_combobox_lab.place(x = 20 , y = 80 , width = 460 , height = 20)
        load_archive_file_msgbox_view_combobox = Combobox(but_project_view_load_archive_file_msgbox , 
                                                       values = project_view_right_panel_listbox_list,
                                                       font = 'arial 10 bold')
        load_archive_file_msgbox_view_combobox.place(x = 20 , y = 100 , width = 460 , height = 30)
        
##

## Project View Window Load HTML File Button event
def but_project_view_load_html_file_event(event):
    if event.num == 1:
        def click_load_event(event): 
            load_html_file_msgbox_choise_file_entry['text'] = askopenfilename(filetypes = htmlfiletypes)
            but_project_view_load_html_file_msgbox.update_idletasks()
            print(load_html_file_msgbox_choise_file_entry['text'])
        def click_create_event(event):
            pass
        def click_cancel_event(event):
            but_project_view_load_html_file_msgbox.destroy()
        but_project_view_load_html_file_msgbox = Toplevel(welcome_window , width = LOAD_HTML_FILE_MSGBOX_WIDTH ,
                                                          height = LOAD_HTML_FILE_MSGBOX_HEIGHT)
        but_project_view_load_html_file_msgbox.title(LOAD_HTML_FILE_MSGBOX_TITLE_TEXT)
        but_project_view_load_html_file_msgbox.resizable(False , False)
        but_project_view_load_html_file_msgbox.iconbitmap('Data\Icons\load_html_file_but.ico')
        load_html_file_msgbox_choise_file_lab = Label(but_project_view_load_html_file_msgbox ,
                                                      text = LOAD_HTML_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT ,
                                                      font = 'arial 10 bold')
        load_html_file_msgbox_choise_file_lab.place(x = 20 , y = 20 , width = 460 , height = 20)
        load_html_file_msgbox_choise_file_entry = Label(but_project_view_load_html_file_msgbox , 
                                                        font = 'arial 10 bold' ,
                                                        text = '')
        load_html_file_msgbox_choise_file_entry.place(x = 20 , y = 40 , width = 460 , height = 30)
        load_html_file_msgbox_choise_file_but = Button(but_project_view_load_html_file_msgbox ,
                                                       text = 'Выбрать файл')
        load_html_file_msgbox_choise_file_but.place(x = 20 , y = 140 , width = 140 , height = 30)
        load_html_file_msgbox_choise_file_but.bind('<Button-1>' , click_load_event)
        load_html_file_msgbox_create_but = Button(but_project_view_load_html_file_msgbox ,
                                                       text = 'Добавить файл')
        load_html_file_msgbox_create_but.place(x = 180 , y = 140 , width = 140 , height = 30)
        load_html_file_msgbox_create_but.bind('<Button-1>' , click_create_event)
        load_html_file_msgbox_cancel_but = Button(but_project_view_load_html_file_msgbox ,
                                                       text = 'Отмена')
        load_html_file_msgbox_cancel_but.place(x = 340 , y = 140 , width = 140 , height = 30)
        load_html_file_msgbox_cancel_but.bind('<Button-1>' , click_cancel_event)
        load_html_file_msgbox_view_combobox_lab = Label(but_project_view_load_html_file_msgbox ,
                                                        text = LOAD_HTML_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT ,
                                                        font = 'arial 10 bold')
        load_html_file_msgbox_view_combobox_lab.place(x = 20 , y = 80 , width = 460 , height = 20)
        load_html_file_msgbox_view_combobox = Combobox(but_project_view_load_html_file_msgbox , 
                                                       values = project_view_right_panel_listbox_list,
                                                       font = 'arial 10 bold')
        load_html_file_msgbox_view_combobox.place(x = 20 , y = 100 , width = 460 , height = 30)
        
##

## Project View Window Load Audio File Button event
def but_project_view_load_audio_file_event(event):
    if event.num == 1:
        def click_load_event(event): 
            load_audio_file_msgbox_choise_file_entry['text'] = askopenfilename(filetypes = audiofiletypes)
            but_project_view_load_audio_file_msgbox.update_idletasks()
            print(load_audio_file_msgbox_choise_file_entry['text'])
        def click_create_event(event):
            pass
        def click_cancel_event(event):
            but_project_view_load_audio_file_msgbox.destroy()
        but_project_view_load_audio_file_msgbox = Toplevel(welcome_window , width = LOAD_AUDIO_FILE_MSGBOX_WIDTH ,
                                                           height = LOAD_AUDIO_FILE_MSGBOX_HEIGHT)
        but_project_view_load_audio_file_msgbox.title(LOAD_AUDIO_FILE_MSGBOX_TITLE_TEXT)
        but_project_view_load_audio_file_msgbox.resizable(False , False)
        but_project_view_load_audio_file_msgbox.iconbitmap('Data\icons\load_audio_file_but.ico')
        load_audio_file_msgbox_choise_file_lab = Label(but_project_view_load_audio_file_msgbox ,
                                                      text = LOAD_AUDIO_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT ,
                                                      font = 'arial 10 bold')
        load_audio_file_msgbox_choise_file_lab.place(x = 20 , y = 20 , width = 460 , height = 20)
        load_audio_file_msgbox_choise_file_entry = Label(but_project_view_load_audio_file_msgbox , 
                                                        font = 'arial 10 bold' ,
                                                        text = '')
        load_audio_file_msgbox_choise_file_entry.place(x = 20 , y = 40 , width = 460 , height = 30)
        load_audio_file_msgbox_choise_file_but = Button(but_project_view_load_audio_file_msgbox ,
                                                       text = 'Выбрать файл')
        load_audio_file_msgbox_choise_file_but.place(x = 20 , y = 140 , width = 140 , height = 30)
        load_audio_file_msgbox_choise_file_but.bind('<Button-1>' , click_load_event)
        load_audio_file_msgbox_create_but = Button(but_project_view_load_audio_file_msgbox ,
                                                       text = 'Добавить файл')
        load_audio_file_msgbox_create_but.place(x = 180 , y = 140 , width = 140 , height = 30)
        load_audio_file_msgbox_create_but.bind('<Button-1>' , click_create_event)
        load_audio_file_msgbox_cancel_but = Button(but_project_view_load_audio_file_msgbox ,
                                                       text = 'Отмена')
        load_audio_file_msgbox_cancel_but.place(x = 340 , y = 140 , width = 140 , height = 30)
        load_audio_file_msgbox_cancel_but.bind('<Button-1>' , click_cancel_event)
        load_audio_file_msgbox_view_combobox_lab = Label(but_project_view_load_audio_file_msgbox ,
                                                        text = LOAD_AUDIO_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT ,
                                                        font = 'arial 10 bold')
        load_audio_file_msgbox_view_combobox_lab.place(x = 20 , y = 80 , width = 460 , height = 20)
        load_audio_file_msgbox_view_combobox = Combobox(but_project_view_load_audio_file_msgbox , 
                                                       values = project_view_right_panel_listbox_list,
                                                       font = 'arial 10 bold')
        load_audio_file_msgbox_view_combobox.place(x = 20 , y = 100 , width = 460 , height = 30)
        
##

## Project View Window Load Video File Button event
def but_project_view_load_video_file_event(event):
    if event.num == 1:
        def click_load_event(event): 
            load_video_file_msgbox_choise_file_entry['text'] = askopenfilename(filetypes = videofiletypes)
            but_project_view_load_video_file_msgbox.update_idletasks()
            print(load_video_file_msgbox_choise_file_entry['text'])
        def click_create_event(event):
            pass
        def click_cancel_event(event):
            but_project_view_load_video_file_msgbox.destroy()
        but_project_view_load_video_file_msgbox = Toplevel(welcome_window , width = LOAD_VIDEO_FILE_MSGBOX_WIDTH ,
                                                           height = LOAD_VIDEO_FILE_MSGBOX_HEIGHT)
        but_project_view_load_video_file_msgbox.title(LOAD_VIDEO_FILE_MSGBOX_TITLE_TEXT)
        but_project_view_load_video_file_msgbox.resizable(False , False)
        but_project_view_load_video_file_msgbox.iconbitmap('Data\Icons\load_video_file_but.ico')
        load_video_file_msgbox_choise_file_lab = Label(but_project_view_load_video_file_msgbox ,
                                                      text = LOAD_VIDEO_FILE_MSGBOX_CHOISE_FILE_LAB_TEXT ,
                                                      font = 'arial 10 bold')
        load_video_file_msgbox_choise_file_lab.place(x = 20 , y = 20 , width = 460 , height = 20)
        load_video_file_msgbox_choise_file_entry = Label(but_project_view_load_video_file_msgbox , 
                                                        font = 'arial 10 bold' ,
                                                        text = '')
        load_video_file_msgbox_choise_file_entry.place(x = 20 , y = 40 , width = 460 , height = 30)
        load_video_file_msgbox_choise_file_but = Button(but_project_view_load_video_file_msgbox ,
                                                       text = 'Выбрать файл')
        load_video_file_msgbox_choise_file_but.place(x = 20 , y = 140 , width = 140 , height = 30)
        load_video_file_msgbox_choise_file_but.bind('<Button-1>' , click_load_event)
        load_video_file_msgbox_create_but = Button(but_project_view_load_video_file_msgbox ,
                                                       text = 'Добавить файл')
        load_video_file_msgbox_create_but.place(x = 180 , y = 140 , width = 140 , height = 30)
        load_video_file_msgbox_create_but.bind('<Button-1>' , click_create_event)
        load_video_file_msgbox_cancel_but = Button(but_project_view_load_video_file_msgbox ,
                                                       text = 'Отмена')
        load_video_file_msgbox_cancel_but.place(x = 340 , y = 140 , width = 140 , height = 30)
        load_video_file_msgbox_cancel_but.bind('<Button-1>' , click_cancel_event)
        load_video_file_msgbox_view_combobox_lab = Label(but_project_view_load_video_file_msgbox ,
                                                        text = LOAD_VIDEO_FILE_MSGBOX_VIEW_COMBOBOX_LAB_TEXT ,
                                                        font = 'arial 10 bold')
        load_video_file_msgbox_view_combobox_lab.place(x = 20 , y = 80 , width = 460 , height = 20)
        load_video_file_msgbox_view_combobox = Combobox(but_project_view_load_video_file_msgbox , 
                                                       values = project_view_right_panel_listbox_list,
                                                       font = 'arial 10 bold')
        load_video_file_msgbox_view_combobox.place(x = 20 , y = 100 , width = 460 , height = 30)
        
##

## Project View Window Delete Any File Button event
def but_project_view_delete_any_file_event(event):
    if event.num == 1:
        but_project_view_delete_any_file_msgbox = Toplevel(welcome_window , width = DELETE_ANY_FILE_MSGBOX_WIDTH ,
                                                           height = DELETE_ANY_FILE_MSGBOX_HEIGHT)
        but_project_view_delete_any_file_msgbox.title(DELETE_ANY_FILE_MSGBOX_TITLE_TEXT)
        but_project_view_delete_any_file_msgbox.resizable(False , False)
        but_project_view_delete_any_file_msgbox.iconbitmap('Data\Icons\delete_any_file_but.ico')
        
##

## Project View Window Add File Field Button event
def but_project_view_add_file_field_event(event):
    if event.num == 1:
        def click_create(event):
            if event.num == 1:
                project_view_right_panel_listbox_list.append(add_file_field_msgbox_name_field.get())
                project_view_right_panel_listbox.insert(END , add_file_field_msgbox_name_field.get())
                project_view_right_panel_listbox_count_lab['text'] = '[' + str(project_view_right_panel_listbox.size()) + ']'
                projectpathosmkdir = namesarray[loginnumber - 1]
                os.mkdir('Projects/' + projectpathosmkdir[:len(projectpathosmkdir)-1] + '/' + add_file_field_msgbox_name_field.get() + '_section')
                project_view_window.update_idletasks()
                
                print(project_view_right_panel_listbox_list)
                but_project_view_add_file_field_msgbox.destroy()
        def click_cancel(event):
            if event.num == 1:
                but_project_view_add_file_field_msgbox.destroy()
        but_project_view_add_file_field_msgbox = Toplevel(welcome_window , width = ADD_FILE_FIELD_MSGBOX_WIDTH ,
                                                          height = ADD_FILE_FIELD_MSGBOX_HEIGHT)
        but_project_view_add_file_field_msgbox.title(ADD_FILE_FIELD_MSGBOX_TITLE_TEXT)
        but_project_view_add_file_field_msgbox.resizable(False , False)
        but_project_view_add_file_field_msgbox.iconbitmap('Data\Icons\/add_file_field_but.ico')
        
        pil_add_file_field_msgbox_frame = Image.open("Data\Frames\/add_file_field_msgbox_frame.png")
        add_file_field_msgbox_frame = ImageTk.PhotoImage(pil_add_file_field_msgbox_frame)
        add_file_field_msgbox_frame_view_canvas = Canvas(but_project_view_add_file_field_msgbox)
        add_file_field_msgbox_frame_view =       add_file_field_msgbox_frame_view_canvas.create_image(300,200,image=project_view_window_frame)
        add_file_field_msgbox_frame_view_canvas.place(x = 0 , y = 0 , width = 300 , height = 200)
        
        add_file_field_msgbox_name_field_lab = Label(but_project_view_add_file_field_msgbox , 
                                                     text =  ADD_FILE_FIELD_MSGBOX_NAME_LAB_TEXT,
                                                     font = 'arial 10 bold')
        add_file_field_msgbox_name_field_lab.place(x = 20 , y = 20 , width = 260 , height = 20)
        add_file_field_msgbox_name_field = Entry(but_project_view_add_file_field_msgbox,
                                                 font = 'arial 10 bold')
        add_file_field_msgbox_name_field.place(x = 20 , y = 40 , width = 260 , height = 30)
        but_add_file_field_msgbox_create = Button(but_project_view_add_file_field_msgbox,
                                                  text = BUT_ADD_FILE_FIELD_MSGBOX_CREATE_TEXT)
        but_add_file_field_msgbox_create.place(x = 20 , y = 80 , width = 120 , height = 40)
        but_add_file_field_msgbox_create.bind('<Button-1>',click_create)
        but_add_file_field_msgbox_cancel = Button(but_project_view_add_file_field_msgbox,
                                                  text = BUT_ADD_FILE_FIELD_MSGBOX_CANCEL_TEXT)
        but_add_file_field_msgbox_cancel.place(x = 160 , y = 80 , width = 120 , height = 40)
        but_add_file_field_msgbox_cancel.bind('<Button-1>',click_cancel)
        
##

## Project View Window Add Label Field Button event
def but_project_view_add_label_field_event(event):
    if event.num == 1:
        but_project_view_add_label_field_msgbox = Toplevel(welcome_window , width = ADD_LABEL_FIELD_MSGBOX_WIDTH ,
                                                           height = ADD_LABEL_FIELD_MSGBOX_HEIGHT)
        but_project_view_add_label_field_msgbox.title(ADD_LABEL_FIELD_MSGBOX_TITLE_TEXT)
        but_project_view_add_label_field_msgbox.resizable(False , False)
        but_project_view_add_label_field_msgbox.iconbitmap('Data\Icons\/add_label_field_but.ico')
        
##

## Project View Window Add Image Field Button event
def but_project_view_add_image_field_event(event):
    if event.num == 1:
        but_project_view_add_image_field_msgbox = Toplevel(welcome_window , width = ADD_IMAGE_FIELD_MSGBOX_WIDTH ,
                                                           height = ADD_IMAGE_FIELD_MSGBOX_HEIGHT)
        but_project_view_add_image_field_msgbox.title(ADD_IMAGE_FIELD_MSGBOX_TITLE_TEXT)
        but_project_view_add_image_field_msgbox.resizable(False , False)
        but_project_view_add_image_field_msgbox.iconbitmap('Data\Icons\/add_image_field_but.ico')
##

## Project View Window Delete Any Field Button event
def but_project_view_delete_any_field_event(event):
    if event.num == 1:
        def click_delete(event):
            if event.num == 1:
                if delete_any_field_msgbox_object_list.get() in project_view_right_panel_listbox_list:
                    project_view_right_panel_listbox_list.remove(delete_any_field_msgbox_object_list.get())
                    project_view_right_panel_listbox.delete(0 , END)
                delete_any_field_msgbox_object_list['values'] = project_view_right_panel_listbox_list
                for project_view_right_panel_listbox_list_item in project_view_right_panel_listbox_list:
                    project_view_right_panel_listbox.insert(END , project_view_right_panel_listbox_list_item)
                shutil.rmtree('Projects/'+ namesarray[loginnumber - 1][:len(namesarray[loginnumber - 1]) - 1] + '/' + delete_any_field_msgbox_object_list.get() + '_section')
                delete_any_field_msgbox_object_list.set('')
                but_project_view_delete_any_field_msgbox.update_idletasks()
                project_view_window.update_idletasks()
                print(delete_any_field_msgbox_object_list.get())
                print(project_view_right_panel_listbox_list)
        def click_cancel(event):
            if event.num == 1:
                but_project_view_delete_any_field_msgbox.destroy()
        but_project_view_delete_any_field_msgbox = Toplevel(welcome_window , width = DELETE_ANY_FIELD_MSGBOX_WIDTH ,
                                                            height = DELETE_ANY_FIELD_MSGBOX_HEIGHT)
        but_project_view_delete_any_field_msgbox.title(DELETE_ANY_FIELD_MSGBOX_TITLE_TEXT)
        but_project_view_delete_any_field_msgbox.resizable(False , False)
        but_project_view_delete_any_field_msgbox.iconbitmap('Data\Icons\delete_any_field_but.ico')
        delete_any_field_msgbox_object_list_lab = Label(but_project_view_delete_any_field_msgbox ,
                                                        text = DELETE_ANY_FILE_MSGBOX_OBJECT_LIST_LAB_TEXT ,
                                                        font = 'arial 10 bold')
        delete_any_field_msgbox_object_list_lab.place(x = 20 , y = 20 , width = 260 , height = 20)
        delete_any_field_msgbox_object_list = Combobox(but_project_view_delete_any_field_msgbox ,
                                                       values = project_view_right_panel_listbox_list ,
                                                       state = 'readonly',
                                                       font = 'arial 10 bold')
        delete_any_field_msgbox_object_list.place(x = 20 , y = 40 , width = 260 , height = 30)
        but_delete_any_field_msgbox_delete = Button(but_project_view_delete_any_field_msgbox ,
                                                    text = BUT_DELETE_ANY_FIELD_MSGBOX_DELETE_TEXT)
        but_delete_any_field_msgbox_delete.place(x = 20 , y = 80 , width = 120 , height = 40)
        but_delete_any_field_msgbox_delete.bind('<Button-1>' , click_delete)
        but_delete_any_field_msgbox_cancel = Button(but_project_view_delete_any_field_msgbox ,
                                                    text = BUT_DELETE_ANY_FIELD_MSGBOX_CANCELE_TEXT)
        but_delete_any_field_msgbox_cancel.place(x = 160 , y = 80 , width = 120 , height = 40)
        but_delete_any_field_msgbox_cancel.bind('<Button-1>' , click_cancel)
        
##

## Welcome Window Delete Project Button event
def but_welcome_delete_project_event(event):
    pass

##

## Welcome Window Delete Project Button event
def but_welcome_add_project_event(event):
    pass

#-------------------------------------------------------------------------------------------------------
##******************************************************************************************************



##
##
##



##******************************************************************************************************
## PROGRAMM CORE
##******************************************************************************************************
##------------------------------------------------------------------------------------------------------
## MAIN PROGRAMM
##------------------------------------------------------------------------------------------------------
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Main Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
main_window = Tk()
main_window.withdraw()
main_window.iconbitmap('icon.ico')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Directories~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if os.path.exists('Projects') == True:
    pass
else:
    os.mkdir('Projects')
    
loginsfile = 'Data/logins.pmlpnf'
passwordsfile = 'Data/passwords.pmlpnf'
namesfile = 'Data/names.pmlpnf'
arrayfile = 'Data/arrays.pmlpnf'
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
welcome_window = Toplevel(width = WELCOME_WINDOW_WIDTH ,height = WELCOME_WINDOW_HEIGHT)
welcome_window.title(WELCOME_WINDOW_TITLE)
welcome_window.resizable(False , False)
welcome_window.iconbitmap('icon.ico')

pil_welcome_window_frame = Image.open("Data/Frames/welcome_window_frame.png")
welcome_window_frame = ImageTk.PhotoImage(pil_welcome_window_frame)
welcome_window_frame_view_canvas = Canvas(welcome_window)
welcome_window_frame_view = welcome_window_frame_view_canvas.create_image(200,125,image=welcome_window_frame)
welcome_window_frame_view_canvas.place(x = 0 , y = 50 , width = 400 , height = 250)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Label~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pil_title_image = Image.open("Data/title.png")
title_image = ImageTk.PhotoImage(pil_title_image)
title_image_view_canvas = Canvas(welcome_window)
title_image_view = title_image_view_canvas.create_image(200,25,image=title_image)
title_image_view_canvas.place(x = 0 , y = 0 , width = 400 , height = 50)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Combobox~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
welcome_cbox = Combobox(welcome_window, values = [WELCOME_WINDOW_CBOX1_1 , WELCOME_WINDOW_CBOX1_2], state =
                 'readonly' , font = 'arial 10 bold')
welcome_cbox.set(WELCOME_WINDOW_CBOX1_1)
welcome_cbox_ttp = CreateToolTip(welcome_cbox ,'Вебырите режим, в котром откроется портфолио.\n \nВ режиме просмотра вы сможете только просмотреть портфолио, при этом достаточно ввести лишь логин от портфолио.\n \nВ режиме редактирования вы сможете полностью отредактировать портфолио, но при этом всместе логином требуется ввести пароль.')
welcome_cbox.place(x = 10 , y = 60 , width = 180 , height = 30)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Come Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
but_come = Button(welcome_window , text = BUT_COME_TEXT)
but_come.place(x = 10 , y = 220 , width = 180 , height = 30)
but_come.bind('<Button-1>', but_come_event)
but_come_ttp = CreateToolTip(but_come , 'Открыть портфолио в выбранном режиме.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Cancel Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
but_start_cancel = Button(welcome_window , text = BUT_START_CANCEL_TEXT)
but_start_cancel.place(x = 10 , y = 260 , width = 180 , height = 30)
but_start_cancel.bind('<Button-1>', but_start_cancel_event)
but_start_cancel_ttp = CreateToolTip(but_start_cancel , 'Выйти из программы.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Login Label~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
login_label = Label(welcome_window, text = LOGIN_LAB_TEXT , font = 'arial 10 bold')
login_label.place(x = 10 , y = 100 , width = 180 , height = 20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Login Entry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
login_entry = Entry(welcome_window)
login_entry.place(x = 10 , y = 120 , width = 180 , height = 30)
login_entry_ttp = CreateToolTip(login_entry , 'Введите логин, привязанный к портфолио.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Password Label~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
password_label = Label(welcome_window, text = PASSWORD_LAB_TEXT , font = 'arial 10 bold')
password_label.place(x = 10 , y = 160 , width = 180 , height = 20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Password Show~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#but_password_show = Button(welcome_window, text = '~')
#but_password_show.place(x = 170 , y = 160 , width = 20 , height = 20)
#but_password_show_ttp = CreateToolTip(but_password_show , 'Показать\скрыть пароль.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Password Entry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
password_entry = Entry(welcome_window)
password_entry.place(x = 10 , y = 180 , width = 180 , height = 30)
password_entry_ttp = CreateToolTip(password_entry , 'Введите пароль, привязанный к логину. Необходим для режима редактирования.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Image~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
welcome_image_canvas = Canvas(welcome_window, bg = 'white')
welcome_image_canvas.place(x = 210 , y = 60 , width = 180 , height = 110)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Projects Listbox~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
welcome_projects_listbox_lab = Label(welcome_window , text = WELCOME_PROJECTS_LISTBOX_LAB_TEXT ,
                                     font = 'arial 8 bold')
welcome_projects_listbox_lab.place(x = 210 , y = 60 , width = 180 , height = 20)
welcome_projects_listbox = Listbox(welcome_window , selectmode = SINGLE , font = 'arial 8 bold')
welocme_projects_listbox_list = []
for projects_in_directory in glob("Projects\*/"):
    welocme_projects_listbox_list.append(str(projects_in_directory)) 
for project_name_in_welcome_listbox in welocme_projects_listbox_list:
    welcome_projects_listbox.insert(END , project_name_in_welcome_listbox)
welcome_projects_listbox.place(x = 210 , y = 80 , width = 180 , height = 90)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Window Delete Project Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
but_welcome_delete_project = Button(welcome_window , text = BUT_WELCOME_DELETE_PROJECT_TEXT)
but_welcome_delete_project.place(x = 210 , y = 180 , width = 180 , height = 30)
but_welcome_delete_project.bind('<Button-1>' , but_welcome_delete_project_event)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Window Add Project Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
but_welcome_add_project = Button(welcome_window , text = BUT_WELCOME_ADD_PROJECT_TEXT)
but_welcome_add_project.place(x = 210 , y = 220 , width = 180 , height = 30)
but_welcome_add_project.bind('<Button-1>' , but_welcome_add_project_event)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Welcome Create Project Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
but_create_project = Button(welcome_window, text = BUT_CREATE_PROJECT_TEXT)
but_create_project.place(x = 210 , y = 260 , width = 180 , height = 30)
but_create_project.bind('<Button-1>', but_create_project_event)
but_create_project_ttp = CreateToolTip(but_create_project , 'Создать новое портфолио.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project Viev Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_window = Toplevel(welcome_window, width = PROJECT_VIEW_WINDOW_WIDTH , height =
                               PROJECT_VIEW_WINDOW_HEIGHT)
#project_view_window.attributes('-fullscreen', 1)
project_view_window.title('Portfolio Manager \ Менеджер Портфолио')
project_view_window.resizable(False , False)
project_view_window.lower()
project_view_window.withdraw()
project_view_window.iconbitmap('icon.ico')

pil_project_view_window_frame = Image.open("Data/Frames/project_view_frame.png")
project_view_window_frame = ImageTk.PhotoImage(pil_project_view_window_frame)
project_view_window_frame_view_canvas = Canvas(project_view_window)
project_view_window_frame_view = project_view_window_frame_view_canvas.create_image(400,300,image=project_view_window_frame)
project_view_window_frame_view_canvas.place(x = 0 , y = 0 , width = 800 , height = 600)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Create Project Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_create_window = Toplevel(welcome_window, width = PROJECT_CREATE_WINDOW_WIDTH, height =
                                 PROJECT_CREATE_WINDOW_HEIGHT)
project_create_window.title('Создать новое портфолио')
project_create_window.resizable(False , False)
project_create_window.withdraw()
project_create_window.iconbitmap('icon.ico')

pil_project_create_window_frame = Image.open("Data/Frames/project_create_frame.png")
project_create_window_frame = ImageTk.PhotoImage(pil_project_create_window_frame)
project_create_window_frame_view_canvas = Canvas(project_create_window)
project_create_window_frame_view = project_create_window_frame_view_canvas.create_image(300,200,image=project_create_window_frame)
project_create_window_frame_view_canvas.place(x = 0 , y = 0 , width = 600 , height = 400)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~User Login Register Label~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user_login_register_lab = Label(project_create_window, text = USER_LOGIN_REGISTER_LAB_TEXT ,
                                font = 'arial 10 bold')
user_login_register_lab.place(x = 20 , y = 20 , width = 270 , height = 20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~User Login Register Entry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user_login_register_entry = Entry(project_create_window)
user_login_register_entry.place(x = 20 , y = 40 , width = 270 , height = 30)
user_login_register_entry_ttp = CreateToolTip(user_login_register_entry , 'Придумайте пароль, который будет привязан к портфолио.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~User Password Register Label~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user_password_register_lab = Label(project_create_window, text = USER_PASSWORD_REGISTER_LAB_TEXT , 
                                   font = 'arial 10 bold')
user_password_register_lab.place(x = 20 , y = 80 , width = 270 , height = 20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~User Password Register Entry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user_password_register_entry = Entry(project_create_window)
user_password_register_entry.place(x = 20 , y = 100 , width = 270 , height = 30)
user_password_register_entry_ttp = CreateToolTip(user_password_register_entry , 'Придумайте пароль, который будет привязан к логину от портфолио.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project Create Name Label~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_create_name_lab = Label(project_create_window, text = PROJECT_CREATE_NAME_LAB_TEXT , 
                                font = 'arial 10 bold')
project_create_name_lab.place(x = 20 , y = 140 , width = 270 , height = 20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project Create Name Entry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_create_name_entry = Entry(project_create_window)
project_create_name_entry.place(x = 20 , y = 160 , width = 270 , height = 30)
project_create_name_entry_ttp = CreateToolTip(project_create_name_entry , 'Придумайте имя для портфолио. Оно будет использоваться, как название папки в дистрибутиве программы.')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Template Choise List Label~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
template_choise_list_lab = Label(project_create_window, text = TEMPLATE_CHOISE_LIST_LABEL_TEXT , 
                                 font = 'arial 10 bold')
template_choise_list_lab.place(x = 310 , y = 20 , width = 270 , height = 20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Template Choise List~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
template_choise_list = Listbox(project_create_window, selectmode = SINGLE , font = 'arial 16 bold')
t_ch_list = [TEMPLATE_CHOISE_LIST_ITEM1_TEXT , TEMPLATE_CHOISE_LIST_ITEM2_TEXT , TEMPLATE_CHOISE_LIST_ITEM3_TEXT]
for t_ch_list_item in t_ch_list:
    template_choise_list.insert(END , t_ch_list_item)
template_choise_list.selection_set(1)
template_choise_list.place(x = 310 , y = 40 , width = 270 , height = 150)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Template Choise List Attributes~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
template_choise_list_attributes = Text(project_create_window , font = 'arial 12 bold')
template_choise_list_attributes.place(x = 310 , y = 200 , width = 270, height = 180)
template_choise_list_attributes.insert(1.0 , TEMPLATE_CHOISE_LIST_ITEM1_TEXT + '\n')
template_choise_list_attributes.insert(2.0 , '\n')
template_choise_list_attributes.insert(3.0 , TEMPLATE_CHOISE_LIST_ITEM1_TEXT_ATTRIBUTE1)
template_choise_list_attributes.insert(4.0 , TEMPLATE_CHOISE_LIST_ITEM1_TEXT_ATTRIBUTE2)
template_choise_list_attributes.insert(5.0 , '---------------------------------\n')
template_choise_list_attributes.insert(6.0 , TEMPLATE_CHOISE_LIST_ITEM2_TEXT + '\n')
template_choise_list_attributes.insert(7.0 , '\n')
template_choise_list_attributes.insert(8.0 , TEMPLATE_CHOISE_LIST_ITEM2_TEXT_ATTRIBUTE1)
template_choise_list_attributes.insert(9.0 , TEMPLATE_CHOISE_LIST_ITEM2_TEXT_ATTRIBUTE2)
template_choise_list_attributes.insert(10.0 , '---------------------------------\n')
template_choise_list_attributes.insert(11.0 , TEMPLATE_CHOISE_LIST_ITEM3_TEXT + '\n')
template_choise_list_attributes.insert(12.0 , '\n')
template_choise_list_attributes.insert(13.0 , TEMPLATE_CHOISE_LIST_ITEM3_TEXT_ATTRIBUTE1)
template_choise_list_attributes.insert(14.0 , TEMPLATE_CHOISE_LIST_ITEM3_TEXT_ATTRIBUTE2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project Create Create Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
but_project_create_create = Button(project_create_window, text = PROJECT_CREATE_CREATE_BUTTON_TEXT)
but_project_create_create.place(x = 20 , y = 310 , width = 270 , height = 30)
but_project_create_create.bind('<Button-1>', but_project_create_create_event)
but_project_create_create_ttp = CreateToolTip(but_project_create_create , 'Создать новое портфолио.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project Create Cancel Button~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
but_project_create_cancel = Button(project_create_window, text = PROJECT_CREATE_CANCEL_BUTTON_TEXT)
but_project_create_cancel.place(x = 20 , y = 350 , width = 270 , height = 30)
but_project_create_cancel.bind('<Button-1>', but_project_create_cancel_event)
but_project_create_cancel_ttp = CreateToolTip(but_project_create_cancel , 'Отменить создание портфолио.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project Type Combobox~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_create_project_type_cbox = Combobox(project_create_window, values = [PROJECT_CREATE_PROJECT_TYPE_1 ,
                                            PROJECT_CREATE_PROJECT_TYPE_2], state ='readonly' , 
                                            font = 'arial 10 bold')
project_create_project_type_cbox.set(PROJECT_CREATE_PROJECT_TYPE_1)
project_create_project_type_cbox.place(x = 20 , y = 260 , width = 270 , height = 30)
project_create_project_type_cbox_ttp = CreateToolTip(project_create_project_type_cbox , 'Выберите тип для портфолио. От типа портфолио зависит содержимое шаблонов(за исключением пустого шаблона).')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project Type Combobox Label~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_create_project_type_lab = Label(project_create_window , text = PROJECT_CREATE_PROJECT_TYPE_LAB_TEXT , 
                                        font = 'arial 10 bold')
project_create_project_type_lab.place(x = 20 , y = 240 , width = 270 , height = 20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Tools Panel 1 Canvas~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_tools_panel_1_canvas = Canvas(project_view_window , bg = '#4278ff')
project_view_tools_panel_1_canvas.place(x = 5 , y = 5 , width = 40 , height = 577)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Tools Panel 2 Canvas~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_tools_panel_2_canvas = Canvas(project_view_window , bg = '#4278ff')
project_view_tools_panel_2_canvas.place(x = 50 , y = 5 , width = 745 , height = 40)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Main Panel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_main_panel_canvas = Canvas(project_view_window , bg = '#4278ff')
project_view_main_panel_canvas.place(x = 50 , y = 50 , width = 445 , height = 528)
project_view_main_panel_items_canvas = Canvas(project_view_main_panel_canvas , bg = 'white')
project_view_main_panel_items_canvas.place(x = 10 , y = 10 , width = 425 , height = 500)
test_listbox = Listbox(project_view_main_panel_items_canvas , width = 70 , height = 31 , bg = 'light green')
test_listbox.pack()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Right Panel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_right_panel_canvas = Canvas(project_view_window , bg = '#4278ff')
project_view_right_panel_canvas.place(x = 500 , y = 50 , width = 295 , height = 528)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Properties Bar Panel~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_properties_bar_panel_canvas = Canvas(project_view_window , bg = '#4278ff')
project_view_properties_bar_panel_canvas.place(x = 45 , y = 572 , width = 750 , height = 23)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project Viev Lines~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_line5 = Canvas(project_view_window , bg = 'blue')
project_view_line5.place(x = 45 , y = 4 , width = 5 , height = 592)
project_view_line6 = Canvas(project_view_window , bg = 'blue')
project_view_line6.place(x = 48 , y = 45 , width = 748 , height = 5)
project_view_line7 = Canvas(project_view_window , bg = 'blue')
project_view_line7.place(x = 180 , y = 4 , width = 5 , height = 43)
project_view_line8 = Canvas(project_view_window , bg = 'blue')
project_view_line8.place(x = 465 , y = 4 , width = 5 , height = 43)
project_view_line9 = Canvas(project_view_window , bg = 'blue')
project_view_line9.place(x = 635 , y = 4 , width = 5 , height = 43)
project_view_line10 = Canvas(project_view_window , bg = 'blue')
project_view_line10.place(x = 48 , y = 574 , width = 748 , height = 5)
project_view_line11 = Canvas(project_view_window , bg = 'blue')
project_view_line11.place(x = 495 , y = 48 , width = 5 , height = 527)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Tools Panel 2 Objects~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pil_but_project_view_change_user_icon = Image.open("Data/Icons/change_user_but.png")
but_project_view_change_user_icon = ImageTk.PhotoImage(pil_but_project_view_change_user_icon)
but_project_view_change_user = Button(project_view_window , image = but_project_view_change_user_icon)
but_project_view_change_user.place(x = 50 , y = 5 , width = 40 , height = 40)
but_project_view_change_user.bind('<Button-1>', but_project_view_change_user_event)
but_project_view_change_user_ttp = CreateToolTip(but_project_view_change_user , 'Сменить портфолио.')
pil_but_project_view_help_icon = Image.open("Data/Icons/help_but.png")
but_project_view_help_icon = ImageTk.PhotoImage(pil_but_project_view_help_icon)
but_project_view_help = Button(project_view_window , image = but_project_view_help_icon)
but_project_view_help.place(x = 95 , y = 5 , width = 40 , height = 40)
but_project_view_help.bind('<Button-1>', but_project_view_help_event)
but_project_view_help_ttp = CreateToolTip(but_project_view_help , 'Помощь.')
pil_but_project_view_about_icon = Image.open("Data/Icons/about_but.png")
but_project_view_about_icon = ImageTk.PhotoImage(pil_but_project_view_about_icon)
but_project_view_about = Button(project_view_window , image = but_project_view_about_icon)
but_project_view_about.place(x = 140 , y = 5 , width = 40 , height = 40)
but_project_view_about.bind('<Button-1>', but_project_view_about_event)
but_project_view_about_ttp = CreateToolTip(but_project_view_about , 'О программе\разработчике.')
project_view_project_type_viewer = Label(project_view_window , text = PROJECT_VIEW_PROJECT_TYPE_TEXT + ' : ' +
                                         lookprojecttype , font = PROJECT_VIEW_TEXT1_FONT)
project_view_project_type_viewer.place(x = 185 , y = 5 , width = 280 , height = 40)
project_view_project_opening_type = Label(project_view_window , text = lookmode ,
                                          font = PROJECT_VIEW_TEXT1_FONT)
project_view_project_opening_type.place(x = 470 , y = 5 , width = 165 , height = 40)
pil_but_project_view_change_view_type_icon = Image.open("Data/Icons/change_view_but.png")
but_project_view_change_view_type_icon = ImageTk.PhotoImage(pil_but_project_view_change_view_type_icon)
but_project_view_change_view_type = Button(project_view_window , image = but_project_view_change_view_type_icon)
but_project_view_change_view_type.place(x = 640 , y = 5 , width = 40 , height = 40)
but_project_view_change_view_type.bind('<Button-1>', but_project_view_change_view_type_event)
but_project_view_change_view_type_ttp = CreateToolTip(but_project_view_change_view_type , 'Сменить режим(Просмотр \ Редактирование).')
pil_but_project_view_options_icon = Image.open("Data/Icons/options_but.png")
but_project_view_options_icon = ImageTk.PhotoImage(pil_but_project_view_options_icon)
but_project_view_options = Button(project_view_window , image = but_project_view_options_icon)
but_project_view_options.place(x = 685 , y = 5 , width = 40 , height = 40)
but_project_view_options.bind('<Button-1>' , but_project_view_options_event)
but_project_view_options_ttp = CreateToolTip(but_project_view_options , 'Настройки.')
pil_but_project_view_quit_icon = Image.open("Data/Icons/quit_but.png")
but_project_view_quit_icon = ImageTk.PhotoImage(pil_but_project_view_quit_icon)
but_project_view_quit = Button(project_view_window , image = but_project_view_quit_icon)
but_project_view_quit.place(x = 730 , y = 5 , width = 63 , height = 40)
but_project_view_quit.bind('<Button-1>', but_project_view_quit_event)
but_project_view_quit_ttp = CreateToolTip(but_project_view_quit , 'Выход из программы.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Tools Panel 1 Objects~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pil_but_project_view_project_save_icon = Image.open("Data/Icons/project_save_but.png")
but_project_view_project_save_icon = ImageTk.PhotoImage(pil_but_project_view_project_save_icon)
but_project_view_project_save = Button(project_view_window , image = but_project_view_project_save_icon)
but_project_view_project_save.place(x = 5 , y = 5 , width = 40 , height = 40)
but_project_view_project_save.bind('<Button-1>', but_project_view_project_save_event)
but_project_view_project_save_ttp = CreateToolTip(but_project_view_project_save , 'Сохранить портфолио.')
pil_but_project_view_load_text_file_icon = Image.open("Data/Icons/load_text_file_but.png")
but_project_view_load_text_file_icon = ImageTk.PhotoImage(pil_but_project_view_load_text_file_icon)
but_project_view_load_text_file = Button(project_view_window , image = but_project_view_load_text_file_icon)
but_project_view_load_text_file.place(x = 5 , y = 50 , width = 40 , height = 40)
but_project_view_load_text_file.bind('<Button-1>', but_project_view_load_text_file_event)
but_project_view_load_text_file_ttp = CreateToolTip(but_project_view_load_text_file , 'Загрузить Текстовый/Microsoft Office файл.')
pil_but_project_view_load_pdf_file_icon = Image.open("Data/Icons/load_pdf_file_but.png")
but_project_view_load_pdf_file_icon = ImageTk.PhotoImage(pil_but_project_view_load_pdf_file_icon)
but_project_view_load_pdf_file = Button(project_view_window , image = but_project_view_load_pdf_file_icon)
but_project_view_load_pdf_file.place(x = 5 , y = 95 , width = 40 , height = 40)
but_project_view_load_pdf_file.bind('<Button-1>', but_project_view_load_pdf_file_event)
but_project_view_load_pdf_file_ttp = CreateToolTip(but_project_view_load_pdf_file , 'Загрузить pdf файл.')
pil_but_project_view_load_image_file_icon = Image.open("Data/Icons/load_image_file_but.png")
but_project_view_load_image_file_icon = ImageTk.PhotoImage(pil_but_project_view_load_image_file_icon)
but_project_view_load_image_file = Button(project_view_window , image = but_project_view_load_image_file_icon)
but_project_view_load_image_file.place(x = 5 , y = 140 , width = 40 , height = 40)
but_project_view_load_image_file.bind('<Button-1>', but_project_view_load_image_file_event)
but_project_view_load_image_file_ttp = CreateToolTip(but_project_view_load_image_file , 'Загрузить изображение.')
pil_but_project_view_load_archive_file_icon = Image.open("Data/Icons/load_archive_file_but.png")
but_project_view_load_archive_file_icon = ImageTk.PhotoImage(pil_but_project_view_load_archive_file_icon)
but_project_view_load_archive_file = Button(project_view_window , image = but_project_view_load_archive_file_icon)
but_project_view_load_archive_file.place(x = 5 , y = 185 , width = 40 , height = 40)
but_project_view_load_archive_file.bind('<Button-1>', but_project_view_load_archive_file_event)
but_project_view_load_archive_file_ttp = CreateToolTip(but_project_view_load_archive_file , 'Загрузить архив.')
pil_but_project_view_load_html_file_icon = Image.open("Data/Icons/load_html_file_but.png")
but_project_view_load_html_file_icon = ImageTk.PhotoImage(pil_but_project_view_load_html_file_icon)
but_project_view_load_html_file = Button(project_view_window , image = but_project_view_load_html_file_icon)
but_project_view_load_html_file.place(x = 5 , y = 230 , width = 40 , height = 40)
but_project_view_load_html_file.bind('<Button-1>', but_project_view_load_html_file_event)
but_project_view_load_html_file_ttp = CreateToolTip(but_project_view_load_html_file , 'Загрузить веб-страницу.')
pil_but_project_view_load_audio_file_icon = Image.open("Data/Icons/load_audio_file_but.png")
but_project_view_load_audio_file_icon = ImageTk.PhotoImage(pil_but_project_view_load_audio_file_icon)
but_project_view_load_audio_file = Button(project_view_window , image = but_project_view_load_audio_file_icon)
but_project_view_load_audio_file.place(x = 5 , y = 275 , width = 40 , height = 40)
but_project_view_load_audio_file.bind('<Button-1>', but_project_view_load_audio_file_event)
but_project_view_load_audio_file_ttp = CreateToolTip(but_project_view_load_audio_file , 'Загрузить аудио-файл.')
pil_but_project_view_load_video_file_icon = Image.open("Data/Icons/load_video_file_but.png")
but_project_view_load_video_file_icon = ImageTk.PhotoImage(pil_but_project_view_load_video_file_icon)
but_project_view_load_video_file = Button(project_view_window , image = but_project_view_load_video_file_icon)
but_project_view_load_video_file.place(x = 5 , y = 320 , width = 40 , height = 40)
but_project_view_load_video_file.bind('<Button-1>', but_project_view_load_video_file_event)
but_project_view_load_video_file_ttp = CreateToolTip(but_project_view_load_video_file , 'Загрузить видео-файл.')
pil_but_project_view_delete_any_file_icon = Image.open("Data/Icons/delete_any_file_but.png")
but_project_view_delete_any_file_icon = ImageTk.PhotoImage(pil_but_project_view_delete_any_file_icon)
but_project_view_delete_any_file = Button(project_view_window , image = but_project_view_delete_any_file_icon)
but_project_view_delete_any_file.place(x = 5 , y = 365 , width = 40 , height = 40)
but_project_view_delete_any_file.bind('<Button-1>', but_project_view_delete_any_file_event)
but_project_view_delete_any_file_ttp = CreateToolTip(but_project_view_delete_any_file , 'Удалить какой-либо файл.')
pil_but_project_view_add_file_field_icon = Image.open("Data/Icons/add_file_field_but.png")
but_project_view_add_file_field_icon = ImageTk.PhotoImage(pil_but_project_view_add_file_field_icon)
but_project_view_add_file_field = Button(project_view_window , image = but_project_view_add_file_field_icon)
but_project_view_add_file_field.place(x = 5 , y = 410 , width = 40 , height = 40)
but_project_view_add_file_field.bind('<Button-1>', but_project_view_add_file_field_event)
but_project_view_add_file_field_ttp = CreateToolTip(but_project_view_add_file_field , 'Добавить раздел портфолио.')
pil_but_project_view_add_label_field_icon = Image.open("Data/Icons/add_label_field_but.png")
but_project_view_add_label_field_icon = ImageTk.PhotoImage(pil_but_project_view_add_label_field_icon)
but_project_view_add_label_field = Button(project_view_window , image = but_project_view_add_label_field_icon)
but_project_view_add_label_field.place(x = 5 , y = 455 , width = 40 , height = 40)
but_project_view_add_label_field.bind('<Button-1>', but_project_view_add_label_field_event)
but_project_view_add_label_field_ttp = CreateToolTip(but_project_view_add_label_field , 'Добавить поле для текста(резюме).')
pil_but_project_view_add_image_field_icon = Image.open("Data/Icons/add_image_field_but.png")
but_project_view_add_image_field_icon = ImageTk.PhotoImage(pil_but_project_view_add_image_field_icon)
but_project_view_add_image_field = Button(project_view_window , image = but_project_view_add_image_field_icon)
but_project_view_add_image_field.place(x = 5 , y = 500 , width = 40 , height = 40)
but_project_view_add_image_field.bind('<Button-1>', but_project_view_add_image_field_event)
but_project_view_add_image_field_ttp = CreateToolTip(but_project_view_add_image_field , 'Добавить поле для изображения(резюме).')
pil_but_project_view_delete_any_field_icon = Image.open("Data/Icons/delete_any_field_but.png")
but_project_view_delete_any_field_icon = ImageTk.PhotoImage(pil_but_project_view_delete_any_field_icon)
but_project_view_delete_any_field = Button(project_view_window , image = but_project_view_delete_any_field_icon)
but_project_view_delete_any_field.place(x = 5 , y = 545 , width = 40 , height = 50)
but_project_view_delete_any_field.bind('<Button-1>', but_project_view_delete_any_field_event)
but_project_view_delete_any_field_ttp = CreateToolTip(but_project_view_delete_any_field , 'Удалить раздел портфолио или поле из резюме.')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Right Panel Objects~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_right_panel_listbox_lab = Label(project_view_window , text = PROJECT_VIEW_RIGHT_PANEL_LISTBOX_LAB , 
                                             font = 'arial 10 bold')
project_view_right_panel_listbox_lab.place(x = 505 , y = 55 , width = 245 , height = 20)
project_view_right_panel_listbox = Listbox(project_view_window , selectmode = SINGLE , bg = '#e6e6e6' , 
                                           font = 'arial 10 bold')
#project_view_right_panel_listbox_list = ['Данные о пользователе']
#for project_view_right_panel_listbox_list_item in project_view_right_panel_listbox_list:
#    project_view_right_panel_listbox.insert(END , project_view_right_panel_listbox_list_item)
project_view_right_panel_listbox.place(x = 505 , y = 75 , width = 285 , height = 493)
project_view_right_panel_listbox_count_lab = Label(project_view_window , 
                                                   font = 'arial 10 bold')
project_view_right_panel_listbox_count_lab['text'] = '[' + str(project_view_right_panel_listbox.size()) + ']'
project_view_right_panel_listbox_count_lab.place(x = 750 , y = 55 , width = 40 , height = 20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Project View Properties Bar Panel Objects~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
project_view_properties_bar_panel_programm_name_lab = Label(project_view_window , text =
                                                            PROJECT_VIEW_PROPERTIES_BAR_PANEL_PROGRAMM_NAME_TEXT,
                                                            font = 'arial 8 bold')
project_view_properties_bar_panel_programm_name_lab.place(x = 49 , y = 577 , width = 103 , height = 17)
project_view_properties_bar_panel_programm_version_lab = Label(project_view_window , text = 
                                                               PROJECT_VIEW_PROPERTIES_BAR_PANEL_PROGRAMM_VERSION
                                                               , font = 'arial 8 bold')
project_view_properties_bar_panel_programm_version_lab.place(x = 152 , y = 577 , width = 36 , height = 17)
project_view_properties_bar_panel_item_selected_text_lab = Label(project_view_window , text = 
                                                                 PROJECT_VIEW_PROPERTIES_BAR_PANEL_ITEM_SELECTED,
                                                                 font = 'arial 8 bold')
project_view_properties_bar_panel_item_selected_text_lab.place(x = 200 , y = 577 , width = 100 , height = 17)
project_view_properties_bar_panel_item = Label(project_view_window , text = ITEM_SELECTED , font =
                                               'arial 8 bold')
project_view_properties_bar_panel_item.place(x = 300 , y = 577 , width = 200 , height = 17)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##~~~~~~~~~~Launch Programm~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
style = Style()
style.theme_use('vista')
welcome_window.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
##------------------------------------------------------------------------------------------------------
##******************************************************************************************************