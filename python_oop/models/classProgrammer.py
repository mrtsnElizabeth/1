from .classEmployee import Employee

class Programmer(Employee):
    def work(self):
        work_str1 = super().work()
        return work_str1[:-1] + 'and start codding.'
        
    def __str__(self):
        return 'Programmer:{}'.format (self.full_name)

class Recruiter(Employee):
    def work(self):
        work_str = super().work()
        return work_str[:-1] + 'and start hiring'
        
    def __str__(self):
        return 'Recruiter: {}'.format (self.full_name)
