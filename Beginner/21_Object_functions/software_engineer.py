class SoftwareEngineer:
    def __init__(self, name, designation, department, experience):
        self.name = name
        self.designation = designation
        self.department = department
        self.experience = experience

    def is_selected_for_team_lead_position(self):
        if self.experience >= 10:
            return True
        else:
            return False