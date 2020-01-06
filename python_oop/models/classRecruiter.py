from .classEmployee import Employee
from .exception import UnableToWorkException

class Candidate(Employee):
    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
#        self.full_name = full_name
#        self.email = email
        super().__init__(full_name, email, 0)
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade
    def work(self):
        raise UnableToWorkException

class Vacancy:
    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level
