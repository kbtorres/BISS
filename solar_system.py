#!/usr/bin/env python3
"""
BISS - Basic Interactive Solar System Simulator
A tool for teaching astronomy and celestial mechanics
"""

import math
import time
import sys

class CelestialBody:
    """Represents a celestial body in the solar system"""
    
    def __init__(self, name, mass, distance, orbital_period, radius, color="white"):
        """
        Initialize a celestial body
        
        Args:
            name: Name of the body
            mass: Mass in kg
            distance: Average distance from sun in AU (Astronomical Units)
            orbital_period: Orbital period in Earth days
            radius: Radius in km
            color: Display color
        """
        self.name = name
        self.mass = mass
        self.distance = distance  # AU
        self.orbital_period = orbital_period  # days
        self.radius = radius  # km
        self.color = color
        self.angle = 0  # Current position in orbit (radians)
        
    def update_position(self, time_step):
        """Update the position of the body based on time step"""
        # Angular velocity (radians per day)
        angular_velocity = (2 * math.pi) / self.orbital_period
        self.angle += angular_velocity * time_step
        self.angle = self.angle % (2 * math.pi)
        
    def get_position(self):
        """Get current x, y position"""
        x = self.distance * math.cos(self.angle)
        y = self.distance * math.sin(self.angle)
        return x, y
    
    def get_velocity(self):
        """Calculate orbital velocity in km/s"""
        # Simplified calculation using circular orbit approximation
        # v = 2πr / T
        distance_km = self.distance * 149597870.7  # Convert AU to km
        period_seconds = self.orbital_period * 24 * 3600
        velocity = (2 * math.pi * distance_km) / period_seconds
        return velocity

class SolarSystem:
    """Solar system simulator"""
    
    def __init__(self):
        self.bodies = []
        self.time_elapsed = 0  # days
        self.setup_solar_system()
        
    def setup_solar_system(self):
        """Initialize the solar system with planets"""
        # Sun (not moving in this simulation)
        self.sun = CelestialBody("Sun", 1.989e30, 0, 0, 696340, "yellow")
        
        # Inner planets
        self.bodies.append(CelestialBody("Mercury", 3.285e23, 0.39, 88, 2439.7, "gray"))
        self.bodies.append(CelestialBody("Venus", 4.867e24, 0.72, 225, 6051.8, "orange"))
        self.bodies.append(CelestialBody("Earth", 5.972e24, 1.0, 365.25, 6371, "blue"))
        self.bodies.append(CelestialBody("Mars", 6.39e23, 1.52, 687, 3389.5, "red"))
        
        # Outer planets (simplified distances for visualization)
        self.bodies.append(CelestialBody("Jupiter", 1.898e27, 5.2, 4333, 69911, "orange"))
        self.bodies.append(CelestialBody("Saturn", 5.683e26, 9.54, 10759, 58232, "yellow"))
        
    def update(self, time_step):
        """Update all bodies for given time step (in days)"""
        for body in self.bodies:
            body.update_position(time_step)
        self.time_elapsed += time_step
        
    def display_info(self):
        """Display information about the solar system"""
        print("\n" + "="*70)
        print(f"BISS - Solar System Simulation")
        print(f"Time elapsed: {self.time_elapsed:.1f} days ({self.time_elapsed/365.25:.2f} years)")
        print("="*70)
        
        for body in self.bodies:
            x, y = body.get_position()
            velocity = body.get_velocity()
            print(f"\n{body.name}:")
            print(f"  Distance from Sun: {body.distance:.2f} AU")
            print(f"  Orbital Period: {body.orbital_period:.1f} days ({body.orbital_period/365.25:.2f} years)")
            print(f"  Current Position: ({x:.2f}, {y:.2f}) AU")
            print(f"  Orbital Velocity: {velocity:.2f} km/s")
            print(f"  Angle in Orbit: {math.degrees(body.angle):.1f}°")
            
    def display_simple_visualization(self):
        """Display a simple ASCII visualization"""
        print("\n" + "="*70)
        print("Solar System View (Top-Down)")
        print("="*70)
        
        # Create a simple grid
        size = 40
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        center = size // 2
        
        # Place sun at center
        grid[center][center] = '*'
        
        # Place planets
        scale = 3  # Scale factor for visualization
        for body in self.bodies:
            x, y = body.get_position()
            grid_x = int(center + x * scale)
            grid_y = int(center + y * scale)
            
            # Check bounds
            if 0 <= grid_x < size and 0 <= grid_y < size:
                # Use first letter of planet name
                grid[grid_y][grid_x] = body.name[0]
        
        # Print grid
        for row in grid:
            print(''.join(row))
        
        print("\nLegend: * = Sun, M = Mercury, V = Venus, E = Earth")
        print("        m = Mars, J = Jupiter, S = Saturn")

def print_menu():
    """Print the interactive menu"""
    print("\n" + "="*70)
    print("BISS - Interactive Astronomy Teaching Tool")
    print("="*70)
    print("1. View current solar system status")
    print("2. Advance time by 1 day")
    print("3. Advance time by 30 days")
    print("4. Advance time by 365 days (1 year)")
    print("5. Show simple visualization")
    print("6. Show educational facts")
    print("7. Calculate distance between planets")
    print("0. Exit")
    print("="*70)

def show_educational_facts():
    """Display educational astronomy facts"""
    facts = [
        "\nAstronomical Unit (AU):",
        "  - 1 AU = 149,597,870.7 km (distance from Earth to Sun)",
        "  - Used as a convenient unit for measuring distances in the solar system",
        
        "\nKepler's Laws of Planetary Motion:",
        "  1. Planets move in elliptical orbits with the Sun at one focus",
        "  2. A line joining a planet and the Sun sweeps equal areas in equal times",
        "  3. The square of orbital period is proportional to the cube of semi-major axis",
        
        "\nOrbital Velocity:",
        "  - Earth orbits the Sun at approximately 30 km/s",
        "  - Closer planets move faster (Mercury ~48 km/s)",
        "  - Farther planets move slower (Neptune ~5.4 km/s)",
        
        "\nFun Facts:",
        "  - Jupiter is more massive than all other planets combined",
        "  - Venus rotates backwards compared to most planets",
        "  - Mars has the largest volcano in the solar system (Olympus Mons)",
        "  - Saturn's rings are made of ice and rock particles",
    ]
    
    print("\n" + "="*70)
    print("Educational Astronomy Facts")
    print("="*70)
    for fact in facts:
        print(fact)

def calculate_distance(solar_system):
    """Calculate distance between two planets"""
    print("\nAvailable planets:")
    for i, body in enumerate(solar_system.bodies, 1):
        print(f"{i}. {body.name}")
    
    try:
        planet1_idx = int(input("Select first planet (number): ")) - 1
        planet2_idx = int(input("Select second planet (number): ")) - 1
        
        if 0 <= planet1_idx < len(solar_system.bodies) and 0 <= planet2_idx < len(solar_system.bodies):
            body1 = solar_system.bodies[planet1_idx]
            body2 = solar_system.bodies[planet2_idx]
            
            x1, y1 = body1.get_position()
            x2, y2 = body2.get_position()
            
            distance_au = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            distance_km = distance_au * 149597870.7
            
            print(f"\nDistance between {body1.name} and {body2.name}:")
            print(f"  {distance_au:.3f} AU")
            print(f"  {distance_km:.2e} km")
            print(f"  {distance_km / 299792:.2f} light-seconds")
        else:
            print("Invalid planet selection!")
    except (ValueError, IndexError):
        print("Invalid input!")

def main():
    """Main program loop"""
    print("\n" + "="*70)
    print("Welcome to BISS - Basic Interactive Solar System Simulator")
    print("A tool for teaching astronomy and celestial mechanics")
    print("="*70)
    
    solar_system = SolarSystem()
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == '0':
                print("\nThank you for using BISS! Keep exploring the cosmos!")
                break
            elif choice == '1':
                solar_system.display_info()
            elif choice == '2':
                solar_system.update(1)
                print("\nAdvanced 1 day")
            elif choice == '3':
                solar_system.update(30)
                print("\nAdvanced 30 days")
            elif choice == '4':
                solar_system.update(365)
                print("\nAdvanced 1 year")
            elif choice == '5':
                solar_system.display_simple_visualization()
            elif choice == '6':
                show_educational_facts()
            elif choice == '7':
                calculate_distance(solar_system)
            else:
                print("\nInvalid choice! Please enter a number between 0 and 7.")
                
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nExiting BISS. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
