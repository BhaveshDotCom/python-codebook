import circle_measurement_formulas as circle

radius = float(input("Enter Radius (meters)... "))

print(f"Area: {circle.area_of_circle(radius):.2f}m²")
print(f"Perimeter: {circle.perimeter_of_circle(radius):.2f}m")
print(f"Volume: {circle.volume_of_circle(radius):.2f}m³")