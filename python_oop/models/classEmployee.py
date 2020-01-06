class Employee:
    def __init__(self, full_name, email, salary_day):
        self.full_name = full_name
        self.email = email
        self.salary_day = salary_day
        self.validate(email)
        self.save_email_to_file()

    def validate(self, mail):
        print(self.get_emails_from_file())
        if mail in self.get_emails_from_file():
            raise ValueError

    def save_email_to_file(self):
        with open('emails', 'a') as f:
            f.write(self.email)
            f.write('\n')

    def get_emails_from_file(self):
        with open('emails', 'a+') as f:
            f.seek(0)
            data = f.read()
        return data.split('\n')

    def work(self):
        return 'I come to the ofice'

    def check_salary (self, day):
        return self.salary_day * day

    def __lt__(self, other):
        return self.salary_day < other.salary_day

    def __gt__(self, other):
        return self.salary_day > other.salary_day
        
    def __eg__(self, other):
        return self.salary_day == other.salary_day
