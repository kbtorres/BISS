#!/usr/bin/env python3
"""
Demo script showing the capabilities of BISS
This script demonstrates automated usage of the solar system simulator
"""

from solar_system import SolarSystem, show_educational_facts, AU_TO_KM, SPEED_OF_LIGHT_KM_S
import math

def demo():
    """Run a demonstration of BISS features"""
    
    print("\n" + "="*70)
    print("BISS DEMONSTRATION")
    print("Showcasing the astronomy teaching tool capabilities")
    print("="*70)
    
    # Create solar system
    solar_system = SolarSystem()
    
    # Demo 1: Initial state
    print("\n--- DEMO 1: Initial Solar System State ---")
    solar_system.display_info()
    
    # Demo 2: Advance time and show how planets move
    print("\n\n--- DEMO 2: Fast Forward 6 Months ---")
    solar_system.update(182.5)
    solar_system.display_info()
    
    # Demo 3: Show visualization
    print("\n\n--- DEMO 3: Visual Representation ---")
    solar_system.display_simple_visualization()
    
    # Demo 4: Advance a full year from start
    print("\n\n--- DEMO 4: One Earth Year Later ---")
    solar_system.update(182.5)  # Complete the year
    print(f"\nTotal time elapsed: {solar_system.time_elapsed:.1f} days")
    print("\nNotice how:")
    print("- Mercury has completed ~4 orbits")
    print("- Venus has completed ~1.6 orbits")
    print("- Earth has completed exactly 1 orbit")
    print("- Mars has completed ~0.5 orbits")
    print("- Jupiter has moved just ~8% of its orbit")
    
    # Demo 5: Planet distance calculations
    print("\n\n--- DEMO 5: Planetary Distances ---")
    earth = solar_system.bodies[2]
    mars = solar_system.bodies[3]
    
    x1, y1 = earth.get_position()
    x2, y2 = mars.get_position()
    
    distance_au = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    distance_km = distance_au * AU_TO_KM
    
    print(f"\nCurrent distance between Earth and Mars:")
    print(f"  {distance_au:.3f} AU")
    print(f"  {distance_km:.2e} km")
    print(f"  Light takes {distance_km / SPEED_OF_LIGHT_KM_S:.2f} seconds to travel this distance")
    
    # Demo 6: Show educational content
    print("\n\n--- DEMO 6: Educational Content ---")
    show_educational_facts()
    
    # Demo 7: Orbital velocity comparison
    print("\n\n--- DEMO 7: Orbital Velocity Comparison ---")
    print("\nPlanets ordered by orbital velocity (fastest to slowest):")
    sorted_bodies = sorted(solar_system.bodies, key=lambda b: b.get_velocity(), reverse=True)
    for i, body in enumerate(sorted_bodies, 1):
        print(f"{i}. {body.name}: {body.get_velocity():.2f} km/s")
    
    print("\n\nThis demonstrates Kepler's laws: planets closer to the Sun")
    print("move faster in their orbits!")
    
    print("\n" + "="*70)
    print("END OF DEMONSTRATION")
    print("Try running 'python3 solar_system.py' for interactive mode!")
    print("="*70 + "\n")

if __name__ == "__main__":
    demo()
