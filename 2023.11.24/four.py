from typing import Self
from dataclasses import dataclass
from os import name as os_name

if os_name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str
    
    @property
    def extension(self) -> str:
        return ''.join(self.name.rsplit('.', 1)[1:])
    
    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    def __init__(self, name, objects: [File | Self] = None):
       self.name = name
       self.dir_path = self.name + PATH_SEP
       self.objects = objects if objects else []

    def add(self, file: [File | Self]):
        self.objects.append(file)

    def ls(self):
        result = ''

        for i in self.objects:
            if isinstance(i, Folder):
                result += f'{self.name + PATH_SEP + i.name} \n'
                i.ls()
            else:
                result += f'{self.name + PATH_SEP + i.name} \n'
        return result

