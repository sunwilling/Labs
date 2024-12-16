class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return self.name, self.id
class Manager(Employee):
    def __init__(self, name, id, departament):
        Employee.__init__(self, name, id)
        self.departament = departament
    def manage_project(self):
        return self.name, self.id, self.departament
class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization
    def perform_maintenance(self):
         return self.name, self.id, self.specialization
class TechManager(Manager, Technician):
    def __init__(self, name, id, departament, specialization):
        Manager.__init__(self, name, id, departament)
        Technician.__init__(self, name, id, specialization)
    def add_employee(self, new_worker):
        self.name = new_worker
    def  get_team_info(self):
        return self.name, self.id, self.departament, self.specialization
Worker1 = Employee('Vlad', 1)
Worker2 = Manager('Anton', 2, 'IT')
Worker3 = Technician('Sergey', 3, 'Tester')
Worker4 = TechManager('Egor', 4, 'IT', 'Tester')
print(Worker1.get_info())
print(Worker2.manage_project())
print(Worker3.perform_maintenance())
print(Worker4.get_team_info())
