from models.classProgrammer import Programmer, Recruiter
from models.classRecruiter import Candidate, Vacancy
import datetime
import traceback

def validate(emp_list):
    emails = []
    for i in emp_list:
        emails.append(i.email)
    em_set = set(emails)
    if len(emails) != len(em_set):
        raise ValueError

if __name__ == '__main__':
    try:
        bob = Recruiter('Bob Smith', 'b@outlook.com', 300)
        sue = Programmer('Sue Jones', 's@outlook.com', 200)
        dave = Programmer('Dave Li', 'd@outlook.com', 100)
        mary = Candidate('Mary Jons', 'm@gmail.com', 'None', 'None', 'None')
        sam = Candidate('Sam Jons', 'a@gmail.com', 'None', 'None', 'None')
        john = Candidate('John Li', 'a@gmail.com', 'None', 'None', 'None')
        mark = Vacancy('None', 'None', 'None')
        kate = Vacancy('None', 'None', 'None')
        validate([bob, sue, dave, mary, sam, john])

    except Exception as err:
        with open('logs.txt', 'a') as f:
            message = '{}    {}:\n {} \n\n'.format(
            	datetime.datetime.now(),
            	err.__class__.__name__,
            	traceback.format_exc()
            )
            f.write(message)
    finally:
    	print('Exception was handled. Check the logs for additional info.')



    # print(bob.full_name, sam.email)