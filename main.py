print('Lesson_2: C2118\n')


class StudySubject:
    name: str
    hours: int
    level: str

    def __init__(self, name: str, hours: int, level: str):
        self.name: name
        self.hours: hours
        self.level: level

    def __str__(self):
        return f'{self.name} {self.level}, кількість годин {self.hours}'


class Group:
    group_name: str
    teacher: str
    date: int

    def __init__(self, group_name: str, teacher: str, date: int):
        self.group_name: group_name
        self.teacher: teacher
        self.date: date

    def __str__(self):
        return f'{self.teacher} {self.group_name}, дата {self.date}'


class Student:
    first_name: str
    last_name: str
    age: int
    is_offline: bool
    study_subject: StudySubject

    def __init__(self, last_name: str, first_name: str, age: int, study_subject: StudySubject, is_offline=True):
        self.first_name: first_name
        self.last_name: last_name
        self.age: age
        self.is_offline: is_offline
        self.study_subject: study_subject

    def __str__(self):

        study_type: str
        if self.is_offline:
            study_type: 'offline'
        else:
            study_type: 'online'

        student_info = f'{self.last_name} {self.first_name}, вік {self.age}, навчається {study_type}'

        return f'{student_info}\n{self.study_subject}\n'


Group = Group('C2118', 'Константин Полишко', 04.11)
py_senior = StudySubject('Python', 18, 'Senior')
Don_Oleg = Student('Дон', 'Олег', 13, py_senior)
# print(Don_Oleg)
print(Group)
