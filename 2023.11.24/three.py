from pathlib import Path
from sys import path
from two import HTMLTag, HTMLBuilder


class CVProfiler:
    def __init__(self, full_name, age, job, email):
        self.name = full_name
        self.age = age
        self.job = job
        self.email = email
        self.result = f'''{HTMLTag.create('html')\
            .sibling('head')\
            .sibling('title', f'{self.name}: портфолио')\
            .build()}'''

    def add_education(self, place, degree, year):
        self.result += f'''{HTMLTag.create('div')\
                            .sibling('h1', 'образование:')\
                            .sibling('p', f'')}'''