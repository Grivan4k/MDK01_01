from datetime import datetime
class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author=author
        self.year=year
    def get_info(self):
        return f"{self.title} {self.author} {self.year}"
    def isclassic(self):
        cur_year = datetime.now().year
        if (cur_year - self.year) > 50:
            return True
        return False 