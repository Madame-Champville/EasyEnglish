from django.db import models
from datetime import datetime






class Student(models.Model):
    first_name = models.CharField(max_length=50, default='Имя')
    last_name = models.CharField(max_length=50, default='Фамилия')
    phone = models.CharField(max_length=50, default='Номер')
    email = models.EmailField(max_length=50, default='Почта')
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")))
    course_level = models.CharField(max_length=50, choices=(
        ("A1", "beginner"), ("A2", "Elementary"), ("B1", "Pre-Intermediate"), ("B2", "Intermedia"),
        ('C1', 'Upper-Intermediate')), verbose_name='Выберите уровень курса')
    reg_date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.first_name

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, default='Имя')
    last_name = models.CharField(max_length=50, default='Фамилия')
    phone = models.CharField(max_length=50, default='Номер')
    email = models.EmailField(max_length=50, default='Почта')
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")))

    def __str__(self):
        return self.first_name

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_level = models.CharField(max_length=50, choices=(("A1", "beginner"),("A2", "Elementary"), ("B1", "Pre-Intermediate"), ("B2", "Intermedia"), ('C1', 'Upper-Intermediate')))
    course_duration = models.IntegerField(choices=((2, "2 month"),(4, "4 months"), (6, "6 months"), (6, "6 months")))
    fee = models.FloatField(default=0)

    def __str__(self):
        return self.course_name




class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")))
    course_level = models.CharField(max_length=50, choices=(
        ("A1", "beginner"), ("A2", "Elementary"), ("B1", "Pre-Intermediate"), ("B2", "Intermedia"),
        ('C1', 'Upper-Intermediate')))
    attendance_day = models.DateField()
    attendance_status = models.CharField(max_length=50, choices=(("-", "absence"), ("+", "present")))

    def __str__(self):
        return self.attendance_status

class Assessment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Имя студента')
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")),verbose_name='Выберите курс')
    course_level = models.CharField(max_length=50, choices=(
    ("A1", "beginner"), ("A2", "Elementary"), ("B1", "Pre-Intermediate"), ("B2", "Intermedia"),
    ('C1', 'Upper-Intermediate')), verbose_name='Выберите уровень курса')
    assessment_date = models.DateField(auto_now_add=True)
    file = models.FileField(upload_to='material/', verbose_name='Прикрепите файл')

    def __str__(self):
        return self.course



class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")),
                              verbose_name='Выберите курс')
    course_level = models.CharField(max_length=50, choices=(
        ("A1", "beginner"), ("A2", "Elementary"), ("B1", "Pre-Intermediate"), ("B2", "Intermedia"),
        ('C1', 'Upper-Intermediate')))
    assessment = models.CharField(max_length=50, choices=(("2", "poor"),("3", "Satisfactory"), ("4", "good"), ("5", "excellent")))
    grade_day = models.DateField(auto_now=True)

    def __str__(self):
        return self.assessment

class Material(models.Model):
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")),
                              verbose_name='Выберите курс')
    course_level = models.CharField(max_length=50, default='Выберите уровень курса', choices=(
        ("A1", "beginner"), ("A2", "Elementary"), ("B1", "Pre-Intermediate"), ("B2", "Intermedia"),
        ('C1', 'Upper-Intermediate')))
    material_name = models.CharField(max_length=50)
    material_description = models.TextField()
    material_link = models.FileField(upload_to='material/')

    def __str__(self):
        return self.material_name

class Schedule(models.Model):
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")),
                              verbose_name='Выберите курс')
    course_level = models.CharField(max_length=50, default='Выберите уровень курса', choices=(
        ("A1", "beginner"), ("A2", "Elementary"), ("B1", "Pre-Intermediate"), ("B2", "Intermedia"),
        ('C1', 'Upper-Intermediate')))
    day_per_week = models.CharField(max_length=50)
    start_time = models.DateField()
    end_time = models.DateField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.day_per_week

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, default='Выберите курс', choices=(
        ("General English", "Общий английский"), ("Individual lessons", "Индивидуальные занятия"),
        ("English for kids", "Английский для детей"), ("Online lessons", "Онлайн занятия"),
        ("IELTS and TOEFL", "IELTS и TOEFL"), ("EAP", "Английский для академический целей")),
                              verbose_name='Выберите курс')
    course_level = models.CharField(max_length=50, choices=(
    ("A1", "beginner"), ("A2", "Elementary"), ("B1", "Pre-Intermediate"), ("B2", "Intermedia"),
    ('C1', 'Upper-Intermediate')))
    payment_date = models.DateField()
    payment_amount = models.FloatField(default=0, verbose_name='Сумма платежа')


