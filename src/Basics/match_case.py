# Switch

unit = input("Enter target unit... ").lower()
dist = int(input("Enter distance in meters... "))
def from_m_to(dist, unit):
    match unit:
        case "km":
            return dist / 1000
        case "cm":
            return dist /100

print(from_m_to(dist, unit))