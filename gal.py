#!/usr/bin/env python3

from os import listdir, getcwd
from os.path import isfile, join, splitext
from random import choice
from webbrowser import open

from bottle import (
        route,
        run,
        template,
        static_file,
        TEMPLATE_PATH
        )

#TODO Adicionar try/except
#TODO auto update da página
#TODO Escala de vídeos verticais está errada
#TODO filtrar por extensão (argumento sys.argv)
#TODO verificar novas extensões


class FileManager:
    def __init__(self, path):
        self.working_dir = path
        self.ALREADY_VIEWED_FILES = []
        self.ACCEPTED_FILE_TYPES = (
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
            ".gif",
            ".mp4"
        )
        self.wrapper_for = {
            ".jpg": "<div id='img'></div>",
            ".jpeg": "<div id='img'></div>",
            ".png": "<div id='img'></div>",
            ".webp": "<div id='img'></div>",
            ".gif": "<div id='img'></div>",
            ".mp4": "<video width='100%' height='100%' autoplay muted controls><source src='/static/{file}' type='video/mp4'>fail</video>"
        }
        self.useful_files = self.get_useful_files()
        self.fail_save = len(self.useful_files)

    def select_random_file(self):
        chosen = None
        while chosen is None:
            if(len(self.ALREADY_VIEWED_FILES) == self.fail_save):
                self.ALREADY_VIEWED_FILES = [self.ALREADY_VIEWED_FILES[-1]]
                continue

            pre = choice(self.useful_files)            
            if(pre in self.ALREADY_VIEWED_FILES):
                continue

            
            self.ALREADY_VIEWED_FILES.append(pre)
            chosen = pre
        return chosen

    def get_useful_files(self):
        all_files = [f for f in listdir(self.working_dir) if isfile(join(self.working_dir, f))]
        filtered_files = [ fi for fi in all_files if fi.endswith(self.ACCEPTED_FILE_TYPES) ]
        return(filtered_files)
    
    def create_wrapper(self,file):
        file_format = splitext(file)[1]
        wrapped = self.wrapper_for[file_format].format(file=file)
        return wrapped        

    def next(self):
        next_file = self.select_random_file()
        object_to_render = self.create_wrapper(next_file)
        return template("/opt/gal/template",content=object_to_render,file=next_file)

TEMPLATE_PATH.append("/opt/gal")
manager = FileManager(getcwd())

@route('/')
def index():
    return manager.next()

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=getcwd())

if __name__ == "__main__":
    print("Starting server at: 'http://localhost:8080'")
    open("http://localhost:8080")
    run(host='localhost', port=8080, reloader=False, quiet=True)
