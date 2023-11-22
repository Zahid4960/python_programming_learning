from software_engineer import SoftwareEngineer

engineer1 = SoftwareEngineer("Zahid", "SE", "AI", 4.3)
engineer2 = SoftwareEngineer("Nahid Hasan", "Sr. SE", "Web", 8.0)
engineer3 = SoftwareEngineer("Fazle Rabbi", "Sr. SE", "Web", 10)

print(engineer1.name)
print(engineer1.designation)
print(engineer1.department)
print(engineer1.experience)
print(engineer1.is_selected_for_team_lead_position())

print("\n")

print(engineer2.name)
print(engineer2.designation)
print(engineer2.department)
print(engineer2.experience)
print(engineer2.is_selected_for_team_lead_position())

print("\n")

print(engineer3.name)
print(engineer3.designation)
print(engineer3.department)
print(engineer3.experience)
print(engineer3.is_selected_for_team_lead_position())