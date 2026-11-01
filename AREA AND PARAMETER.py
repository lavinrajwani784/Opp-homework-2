import math

class Circle:
    """Circle class to calculate area and perimeter (circumference)."""

    def __init__(self, radius):
        # Validate radius input
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


# Main program
if __name__ == "__main__":
    try:
        # Ask user for radius
        radius_input = float(input("Enter the radius of the circle: "))
        
        # Create Circle object
        circle = Circle(radius_input)
        
        # Display results
        print(f"Area of the circle: {circle.area():.2f}")
        print(f"Perimeter of the circle: {circle.perimeter():.2f}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except TypeError as te:
        print(f"Type Error: {te}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
