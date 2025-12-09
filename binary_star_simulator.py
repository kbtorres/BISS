"""
Binary Star System Simulator
Simulates the orbital motion of two stars in a binary system and calculates their radial velocities.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys


class BinaryStarSystem:
    """
    Class to simulate a binary star system using Kepler's laws.
    """
    
    def __init__(self, mass1, mass2, semi_major_axis, period):
        """
        Initialize the binary star system.
        
        Parameters:
        -----------
        mass1 : float
            Mass of star 1 in solar masses
        mass2 : float
            Mass of star 2 in solar masses
        semi_major_axis : float
            Semi-major axis of the orbit in AU
        period : float
            Orbital period in days
        """
        self.mass1 = mass1  # Solar masses
        self.mass2 = mass2  # Solar masses
        self.semi_major_axis = semi_major_axis  # AU
        self.period = period  # days
        
        # Calculate center of mass and individual orbital radii
        self.total_mass = mass1 + mass2
        self.mass_ratio = mass2 / mass1
        
        # Distance of each star from center of mass
        self.r1 = semi_major_axis * mass2 / self.total_mass
        self.r2 = semi_major_axis * mass1 / self.total_mass
        
        # Angular velocity (rad/day)
        self.omega = 2 * np.pi / period
        
        # Orbital velocities (AU/day)
        self.v1 = self.r1 * self.omega
        self.v2 = self.r2 * self.omega
        
        # Convert to km/s for radial velocity (1 AU/day = 1731.5 km/s)
        self.v1_kms = self.v1 * 1731.5
        self.v2_kms = self.v2 * 1731.5
    
    def calculate_positions(self, times):
        """
        Calculate the positions of both stars at given times.
        
        Parameters:
        -----------
        times : array-like
            Array of time values in days
            
        Returns:
        --------
        x1, y1 : arrays
            Position of star 1
        x2, y2 : arrays
            Position of star 2
        """
        theta = self.omega * times
        
        # Star 1 positions (circular orbit approximation)
        x1 = self.r1 * np.cos(theta)
        y1 = self.r1 * np.sin(theta)
        
        # Star 2 positions (opposite side of center of mass)
        x2 = -self.r2 * np.cos(theta)
        y2 = -self.r2 * np.sin(theta)
        
        return x1, y1, x2, y2
    
    def calculate_radial_velocities(self, times, inclination=90):
        """
        Calculate the radial velocities of both stars.
        
        Parameters:
        -----------
        times : array-like
            Array of time values in days
        inclination : float
            Orbital inclination in degrees (90 = edge-on)
            
        Returns:
        --------
        rv1, rv2 : arrays
            Radial velocities in km/s
        """
        theta = self.omega * times
        inc_rad = np.radians(inclination)
        
        # Radial velocity is the velocity component along line of sight
        rv1 = self.v1_kms * np.sin(theta) * np.sin(inc_rad)
        rv2 = self.v2_kms * np.sin(theta + np.pi) * np.sin(inc_rad)
        
        return rv1, rv2
    
    def calculate_doppler_shift(self, rv, wavelength=656.3):
        """
        Calculate the Doppler shift for a given radial velocity.
        
        Parameters:
        -----------
        rv : float or array
            Radial velocity in km/s
        wavelength : float
            Rest wavelength in nm (default: H-alpha line at 656.3 nm)
            
        Returns:
        --------
        shifted_wavelength : float or array
            Doppler-shifted wavelength in nm
        """
        c = 299792.458  # Speed of light in km/s
        return wavelength * (1 + rv / c)


def plot_orbital_motion(system, num_points=200):
    """
    Plot the orbital motion of both stars.
    
    Parameters:
    -----------
    system : BinaryStarSystem
        The binary star system to plot
    num_points : int
        Number of points to plot in the orbit
    """
    times = np.linspace(0, system.period, num_points)
    x1, y1, x2, y2 = system.calculate_positions(times)
    
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Plot orbits
    ax.plot(x1, y1, 'b-', alpha=0.3, label=f'Star 1 orbit ({system.mass1:.1f} M☉)')
    ax.plot(x2, y2, 'r-', alpha=0.3, label=f'Star 2 orbit ({system.mass2:.1f} M☉)')
    
    # Plot starting positions
    ax.plot(x1[0], y1[0], 'bo', markersize=15 * system.mass1, label='Star 1')
    ax.plot(x2[0], y2[0], 'ro', markersize=15 * system.mass2, label='Star 2')
    
    # Plot center of mass
    ax.plot(0, 0, 'k+', markersize=15, mew=2, label='Center of Mass')
    
    # Formatting
    ax.set_xlabel('Distance (AU)', fontsize=12)
    ax.set_ylabel('Distance (AU)', fontsize=12)
    ax.set_title('Binary Star System - Orbital Motion', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.axis('equal')
    
    return fig


def plot_radial_velocities(system, num_points=500, inclination=90):
    """
    Plot the radial velocities of both stars over time.
    
    Parameters:
    -----------
    system : BinaryStarSystem
        The binary star system to plot
    num_points : int
        Number of time points
    inclination : float
        Orbital inclination in degrees
    """
    times = np.linspace(0, 2 * system.period, num_points)
    rv1, rv2 = system.calculate_radial_velocities(times, inclination)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot radial velocities
    ax.plot(times, rv1, 'b-', linewidth=2, label=f'Star 1 ({system.mass1:.1f} M☉)')
    ax.plot(times, rv2, 'r-', linewidth=2, label=f'Star 2 ({system.mass2:.1f} M☉)')
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    
    # Formatting
    ax.set_xlabel('Time (days)', fontsize=12)
    ax.set_ylabel('Radial Velocity (km/s)', fontsize=12)
    ax.set_title('Radial Velocity Variations', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    
    return fig


def plot_doppler_spectrum(system, phase=0.0, inclination=90, wavelength_center=656.3, width=2.0):
    """
    Plot simulated spectrum with Doppler-shifted lines.
    
    Parameters:
    -----------
    system : BinaryStarSystem
        The binary star system
    phase : float
        Orbital phase (0 to 1)
    inclination : float
        Orbital inclination in degrees
    wavelength_center : float
        Center wavelength in nm (default: H-alpha)
    width : float
        Width of spectrum to show in nm
    """
    time = phase * system.period
    rv1, rv2 = system.calculate_radial_velocities(np.array([time]), inclination)
    
    # Calculate Doppler shifts
    wavelength1 = system.calculate_doppler_shift(rv1[0], wavelength_center)
    wavelength2 = system.calculate_doppler_shift(rv2[0], wavelength_center)
    
    # Create wavelength array
    wavelengths = np.linspace(wavelength_center - width, wavelength_center + width, 1000)
    
    # Simulate Gaussian absorption lines
    def gaussian(x, center, amplitude=1.0, sigma=0.05):
        return amplitude * np.exp(-0.5 * ((x - center) / sigma) ** 2)
    
    # Start with flat continuum
    spectrum = np.ones_like(wavelengths)
    
    # Add absorption lines
    spectrum -= gaussian(wavelengths, wavelength1, amplitude=0.6, sigma=0.05)
    spectrum -= gaussian(wavelengths, wavelength2, amplitude=0.4, sigma=0.05)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot spectrum
    ax.plot(wavelengths, spectrum, 'k-', linewidth=2)
    ax.axvline(x=wavelength_center, color='gray', linestyle='--', alpha=0.5, label='Rest wavelength')
    ax.axvline(x=wavelength1, color='b', linestyle='--', alpha=0.7, 
               label=f'Star 1 (RV={rv1[0]:.1f} km/s)')
    ax.axvline(x=wavelength2, color='r', linestyle='--', alpha=0.7,
               label=f'Star 2 (RV={rv2[0]:.1f} km/s)')
    
    # Formatting
    ax.set_xlabel('Wavelength (nm)', fontsize=12)
    ax.set_ylabel('Normalized Flux', fontsize=12)
    ax.set_title(f'Simulated Spectrum at Phase {phase:.2f}', fontsize=14, fontweight='bold')
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.2)
    
    return fig


def get_user_input():
    """
    Get binary star system parameters from user input.
    
    Returns:
    --------
    mass1, mass2, semi_major_axis, period : floats
        System parameters
    """
    print("\n" + "="*60)
    print("Binary Star System Simulator")
    print("="*60)
    print("\nEnter the parameters for the binary star system:")
    print("(Press Enter to use default values)")
    print()
    
    try:
        mass1_input = input("Mass of Star 1 (solar masses) [default: 1.5]: ")
        mass1 = float(mass1_input) if mass1_input.strip() else 1.5
        
        mass2_input = input("Mass of Star 2 (solar masses) [default: 1.0]: ")
        mass2 = float(mass2_input) if mass2_input.strip() else 1.0
        
        sma_input = input("Semi-major axis (AU) [default: 5.0]: ")
        semi_major_axis = float(sma_input) if sma_input.strip() else 5.0
        
        period_input = input("Orbital period (days) [default: 365]: ")
        period = float(period_input) if period_input.strip() else 365.0
        
        inclination_input = input("Orbital inclination (degrees, 90=edge-on) [default: 90]: ")
        inclination = float(inclination_input) if inclination_input.strip() else 90.0
        
    except ValueError:
        print("Invalid input. Using default values.")
        mass1, mass2, semi_major_axis, period, inclination = 1.5, 1.0, 5.0, 365.0, 90.0
    
    return mass1, mass2, semi_major_axis, period, inclination


def save_plots(fig, filename):
    """
    Save a plot to a file.
    
    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to save
    filename : str
        Output filename
    """
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved to: {filename}")


def main():
    """
    Main function to run the binary star system simulator.
    """
    # Get user input or use defaults
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        mass1, mass2, semi_major_axis, period, inclination = get_user_input()
    else:
        # Default parameters
        mass1 = 1.5  # Solar masses
        mass2 = 1.0  # Solar masses
        semi_major_axis = 5.0  # AU
        period = 365.0  # days
        inclination = 90.0  # degrees
        print("Using default parameters (use --interactive flag for custom values)")
    
    # Create binary star system
    system = BinaryStarSystem(mass1, mass2, semi_major_axis, period)
    
    # Display system information
    print("\n" + "="*60)
    print("Binary Star System Parameters:")
    print("="*60)
    print(f"Star 1 mass: {system.mass1:.2f} M☉")
    print(f"Star 2 mass: {system.mass2:.2f} M☉")
    print(f"Semi-major axis: {system.semi_major_axis:.2f} AU")
    print(f"Orbital period: {system.period:.2f} days")
    print(f"Star 1 orbital radius: {system.r1:.3f} AU")
    print(f"Star 2 orbital radius: {system.r2:.3f} AU")
    print(f"Star 1 orbital velocity: {system.v1_kms:.2f} km/s")
    print(f"Star 2 orbital velocity: {system.v2_kms:.2f} km/s")
    print(f"Inclination: {inclination:.1f}°")
    print("="*60)
    
    # Generate plots
    print("\nGenerating visualizations...")
    
    # Plot 1: Orbital motion
    fig1 = plot_orbital_motion(system)
    save_plots(fig1, 'orbital_motion.png')
    
    # Plot 2: Radial velocities
    fig2 = plot_radial_velocities(system, inclination=inclination)
    save_plots(fig2, 'radial_velocities.png')
    
    # Plot 3: Doppler spectrum at different phases
    phases = [0.0, 0.25, 0.5, 0.75]
    for phase in phases:
        fig = plot_doppler_spectrum(system, phase=phase, inclination=inclination)
        save_plots(fig, f'spectrum_phase_{phase:.2f}.png')
    
    print("\nAll visualizations generated successfully!")
    print("\nGenerated files:")
    print("  - orbital_motion.png")
    print("  - radial_velocities.png")
    print("  - spectrum_phase_0.00.png")
    print("  - spectrum_phase_0.25.png")
    print("  - spectrum_phase_0.50.png")
    print("  - spectrum_phase_0.75.png")
    
    # Show plots
    plt.show()


if __name__ == "__main__":
    main()
