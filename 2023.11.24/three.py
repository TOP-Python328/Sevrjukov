from pathlib import Path
from sys import path
from two import HTMLTag, HTMLBuilder


class CVProfiler:
    def __init__(self, full_name, age, job, email):
        self.name = full_name
        self.age = age
        self.job = job
        self.email = email
        self.html = HTMLTag
        self.result = f'''
{self.html.create('div')
.sibling('h1', f'фио:{self.name}')
.sibling('p', f'{self.age} лет')
.sibling('p', f'должность: {self.job}')
.sibling('p', f'связь: {self.email}')
.build()}'''

    def add_education(self, place, degree, year):
        self.result += f"""\n{self.html.create('div')
            .sibling('h1', f'место обучения: {place}')
            .sibling('p', f'специальность: {degree}')
            .sibling('p', f'{year} год')
            .build()}"""

        return self 
    
    def add_project(self, name, url):
        self.result += f"""\n{self.html.create('div')
            .sibling('h1', f'проект: {name}')
            .sibling('img', src=url, alt='неверная_ссылка')
            .build()}"""
        
        return self
    
    def add_contact(self, **kwargs):
        for key, value in kwargs.items():
            self.result += f"""
  {self.html.create('p', f'{key}: {value}').build()}"""

        return self 
    
    def build(self):
        return f'''
<html>
{self.html.create('head')
.sibling('title', f'{self.name}: портфолио')
.build()} \n<body>''' + self.result + """
</body>
</html>
"""
 
cv1 = CVProfiler('Иванов Иван Иванович', 26, 'художник-фрилансер', 'ivv@abc.de')\
        .add_education('Архитектурная Академия', 'Компьютерный дизайн', 2019)\
        .add_project('Разработка логотипа для компании по производству снеков', 'sq')\
        .add_project('UI разработка для интернет-магазина для восковых дел мастеров', 'sqs')\
        .add_contact(devianart='ivovuvan_in_art')\
        .add_contact(telegram='@ivovuvan')\
        .build()
print(cv1)

