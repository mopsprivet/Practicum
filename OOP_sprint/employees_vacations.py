class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, days):
        self.remaining_vacation_days -= days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

# Расширьте класс Employee, создав классы FullTimeEmployee и PartTimeEmployee. 

class FullTimeEmployee(Employee): 

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender)

    def get_unpaid_vacation(self, vacation_start_date, vacation_days): 
        self.vacation_start_date = vacation_start_date 
        self.vacation_days = vacation_days 

        message = f'Начало неоплачиваемого отпуска: {self.vacation_start_date}, продолжительность: {self.vacation_days} дней.' 

        return message

class PartTimeEmployee(Employee): 
    vacation_days = 14 

    def __init__(self, first_name, second_name, gender):
        super().__init__(first_name, second_name, gender) 

# Пример использования:
full_time_employee = FullTimeEmployee('Роберт', 'Крузо', 'м')
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Алёна', 'Пятницкая', 'ж')
print(part_time_employee.get_vacation_details())