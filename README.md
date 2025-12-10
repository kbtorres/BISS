# BISS - Binary Star System Simulator

A Python-based simulator for visualizing and analyzing binary star systems. This tool calculates orbital mechanics, radial velocities, and generates visualizations including Doppler-shifted spectra.

## Features

- **Orbital Mechanics**: Simulates the orbital motion of two stars around their common center of mass using Kepler's laws
- **Radial Velocity Calculation**: Computes radial velocities as a function of time for both stars
- **Visualizations**:
  - Orbital position plots showing the motion of both stars
  - Radial velocity curves over multiple orbital periods
  - Simulated spectra with Doppler-shifted absorption lines at different orbital phases
- **Interactive Mode**: Allows users to input custom star masses, orbital parameters, and inclination
- **Export Functionality**: Automatically saves all plots as high-resolution PNG images

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kbtorres/BISS.git
cd BISS
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage (Default Parameters)

Run the simulator with default parameters:
```bash
python binary_star_simulator.py
```

This will use default values:
- Star 1 mass: 1.5 solar masses
- Star 2 mass: 1.0 solar masses
- Semi-major axis: 5.0 AU
- Orbital period: 365 days
- Inclination: 90° (edge-on)

### Interactive Mode

To input your own parameters:
```bash
python binary_star_simulator.py --interactive
```

You will be prompted to enter:
- Mass of each star (in solar masses)
- Semi-major axis of the orbit (in AU)
- Orbital period (in days)
- Orbital inclination (in degrees, where 90° is edge-on)

## Output

The simulator generates the following output files:

1. **orbital_motion.png**: Shows the orbital paths of both stars around the center of mass
2. **radial_velocities.png**: Displays radial velocity variations over two complete orbits
3. **spectrum_phase_X.XX.png**: Simulated spectra at different orbital phases (0.00, 0.25, 0.50, 0.75)

## Physics Background

### Orbital Mechanics
The simulator uses Kepler's third law and Newton's laws of motion to calculate:
- Individual orbital radii based on the mass ratio
- Orbital velocities of each star
- Positions as a function of time

### Radial Velocity
The radial velocity (RV) is the component of velocity along the line of sight:
- RV varies sinusoidally with orbital phase
- Amplitude depends on orbital velocity and inclination
- The two stars show opposite velocity variations

### Doppler Effect
The simulator demonstrates how spectral lines shift due to the Doppler effect:
- Lines shift to the blue when a star moves toward us
- Lines shift to the red when a star moves away
- The shift magnitude is proportional to radial velocity

## Examples

### Example 1: Equal Mass System
```bash
python binary_star_simulator.py --interactive
# Enter: 1.0, 1.0, 10.0, 500, 90
```

### Example 2: High Mass Ratio
```bash
python binary_star_simulator.py --interactive
# Enter: 3.0, 0.5, 8.0, 600, 75
```

### Running Pre-built Examples

The repository includes an `examples.py` script that demonstrates various binary star configurations:

```bash
python examples.py
```

This will generate five example scenarios:
1. Equal mass binary system
2. High mass ratio system (star-planet like)
3. Effect of orbital inclination on radial velocities
4. Doppler shift visualization through the orbit
5. Short period binary system

## Requirements

- Python 3.7 or higher
- NumPy >= 1.21.0
- Matplotlib >= 3.4.0

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Created for astronomical visualization and education.
