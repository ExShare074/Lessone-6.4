# class Report():
#     def __init__(self, tittle, content):
#         self.tittle = tittle
#         self.content = content
#
#
#     def docPrinter(self):
#         print(f"отчет сформирован - {self.tittle} - {self.content}")

from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class Textformatted(Formatted):
    def format(self, report):
        print(report.tittle)
        print(report.content)

class HTMLformatted(Formatted):
    def format(self, report):
        print(f"<h1>{report.tittle}<h1>")
        print(f"<p>{report.content}<p>")

class Report():
    def __init__(self, tittle, content, formatted):
        self.tittle = tittle
        self.content = content
        self.formatted = formatted
    def docPrinter(self):
        self.formatted.format(self)


report = Report('заголовок отчета', 'текст отчета', HTMLformatted())
report.docPrinter()