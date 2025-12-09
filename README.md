# BISS - Basic Interactive Solar System Simulator

An interactive astronomy teaching tool for learning about our solar system and celestial mechanics.

## Overview

BISS is an educational Python tool designed to help students and enthusiasts learn about astronomy through an interactive simulation of our solar system. The simulator demonstrates planetary motion, orbital mechanics, and provides educational information about celestial bodies.

## Features

- **Real-time Solar System Simulation**: Watch planets orbit the Sun with scientifically accurate orbital periods
- **Interactive Controls**: Advance time by days, months, or years to see planetary motion
- **Educational Content**: Learn about Kepler's laws, orbital mechanics, and astronomical concepts
- **Visual Representation**: ASCII-based top-down view of the solar system
- **Distance Calculator**: Calculate distances between planets at any point in time
- **Detailed Information**: View orbital velocities, positions, and periods for each planet

## Installation

### Requirements

- Python 3.6 or higher (no additional dependencies required!)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/kbtorres/BISS.git
cd BISS
```

2. Make the script executable (optional):
```bash
chmod +x solar_system.py
```

## Usage

Run the simulator:

```bash
python3 solar_system.py
```

### Menu Options

Once started, you'll see an interactive menu with these options:

1. **View current solar system status** - See detailed information about all planets
2. **Advance time by 1 day** - Move the simulation forward by one day
3. **Advance time by 30 days** - Move forward by one month
4. **Advance time by 365 days** - Move forward by one year
5. **Show simple visualization** - Display an ASCII representation of the solar system
6. **Show educational facts** - Learn about astronomy concepts
7. **Calculate distance between planets** - Find the distance between any two planets
0. **Exit** - Close the program

### Example Session

```
Welcome to BISS - Basic Interactive Solar System Simulator

1. View current solar system status
> Shows orbital information for Mercury, Venus, Earth, Mars, Jupiter, and Saturn

5. Show simple visualization
> Displays a top-down ASCII view of the planetary positions

6. Show educational facts
> Learn about AU, Kepler's Laws, and orbital velocities

7. Calculate distance between planets
> Find out how far apart Earth and Mars are at the current time
```

## Educational Value

BISS helps teach:

- **Planetary Orbits**: Understanding how planets move around the Sun
- **Kepler's Laws**: The fundamental laws governing planetary motion
- **Astronomical Units**: Using AU as a convenient measurement for solar system distances
- **Orbital Mechanics**: Relationships between distance, period, and velocity
- **Scale of the Solar System**: Appreciating the vast distances in space
- **Time in Astronomy**: How planetary positions change over days, months, and years

## Technical Details

### Planets Included

The simulator includes six planets with accurate data:

- **Mercury**: Closest and fastest planet (88-day orbit)
- **Venus**: Earth's "twin" with a retrograde rotation
- **Earth**: Our home planet (365.25-day orbit, 1 AU from Sun)
- **Mars**: The red planet with the largest volcano in the solar system
- **Jupiter**: Gas giant, more massive than all other planets combined
- **Saturn**: Famous for its spectacular ring system

### Simplified Model

This simulation uses simplified circular orbits for educational purposes. Real planetary orbits are slightly elliptical, but the circular approximation provides an excellent introduction to orbital mechanics while keeping the math accessible.

## Learning Activities

### Activity 1: Observe Planetary Motion
1. Start the simulator
2. Note the initial positions of all planets
3. Advance time by 365 days (1 Earth year)
4. Observe which planets completed their orbits and which are still in progress

### Activity 2: Compare Orbital Speeds
1. View the solar system status
2. Compare the orbital velocities of inner planets (Mercury, Venus, Earth) with outer planets (Jupiter, Saturn)
3. Notice how closer planets move faster - this demonstrates Kepler's laws!

### Activity 3: Planet Alignment
1. Use the visualization to see current planetary positions
2. Advance time and watch how planets align differently
3. Calculate how long it takes for two planets to return to similar positions

### Activity 4: Distance Calculations
1. Use the distance calculator to find how far apart Earth and Mars are
2. Advance time by 30 days and calculate again
3. Observe how planetary distances change over time

## Contributing

Contributions are welcome! Some ideas for enhancements:

- Add more celestial bodies (asteroids, comets, moons)
- Implement elliptical orbits
- Add graphical visualization using matplotlib
- Include more educational content
- Add quiz mode for testing knowledge
- Export orbital data to files

## License

This project is open source and available for educational use.

## About

Created as an educational tool for teaching astronomy and celestial mechanics. Perfect for students, teachers, and space enthusiasts!

## Contact

For questions or suggestions, please open an issue on GitHub. 
