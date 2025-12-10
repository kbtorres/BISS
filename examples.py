#!/usr/bin/env python3
"""
Example usage scenarios for the Binary Star System Simulator
"""

from binary_star_simulator import BinaryStarSystem, plot_orbital_motion, plot_radial_velocities, plot_doppler_spectrum
import matplotlib.pyplot as plt
import numpy as np


def example_1_equal_masses():
    """Example 1: Equal mass binary system"""
    print("\n=== Example 1: Equal Mass Binary System ===")
    print("Two stars of equal mass (1.0 M☉ each)")
    
    system = BinaryStarSystem(mass1=1.0, mass2=1.0, semi_major_axis=4.0, period=365.0)
    
    print(f"Star 1 orbital radius: {system.r1:.3f} AU")
    print(f"Star 2 orbital radius: {system.r2:.3f} AU")
    print(f"Both stars orbit at equal distances from center of mass")
    
    fig = plot_orbital_motion(system)
    fig.savefig('example1_equal_mass.png', dpi=150)
    print("Saved: example1_equal_mass.png")
    plt.close(fig)


def example_2_high_mass_ratio():
    """Example 2: High mass ratio system (like a star and a planet)"""
    print("\n=== Example 2: High Mass Ratio System ===")
    print("Massive star (10.0 M☉) with smaller companion (0.5 M☉)")
    
    system = BinaryStarSystem(mass1=10.0, mass2=0.5, semi_major_axis=15.0, period=1000.0)
    
    print(f"Star 1 orbital radius: {system.r1:.3f} AU (massive star)")
    print(f"Star 2 orbital radius: {system.r2:.3f} AU (companion)")
    print(f"The massive star barely moves!")
    
    fig = plot_orbital_motion(system)
    fig.savefig('example2_high_mass_ratio.png', dpi=150)
    print("Saved: example2_high_mass_ratio.png")
    plt.close(fig)


def example_3_radial_velocities_different_inclinations():
    """Example 3: Effect of orbital inclination on radial velocities"""
    print("\n=== Example 3: Effect of Orbital Inclination ===")
    
    system = BinaryStarSystem(mass1=1.5, mass2=1.0, semi_major_axis=5.0, period=365.0)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Radial Velocities at Different Inclinations', fontsize=16, fontweight='bold')
    
    inclinations = [90, 60, 30, 0]
    titles = ['Edge-on (90°)', 'Inclined (60°)', 'More inclined (30°)', 'Face-on (0°)']
    
    times = np.linspace(0, system.period, 500)
    
    for ax, inc, title in zip(axes.flat, inclinations, titles):
        rv1, rv2 = system.calculate_radial_velocities(times, inclination=inc)
        
        ax.plot(times, rv1, 'b-', linewidth=2, label=f'Star 1')
        ax.plot(times, rv2, 'r-', linewidth=2, label=f'Star 2')
        ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
        ax.set_xlabel('Time (days)')
        ax.set_ylabel('Radial Velocity (km/s)')
        ax.set_title(title)
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fig.savefig('example3_inclination_effect.png', dpi=150)
    print("Saved: example3_inclination_effect.png")
    print("Notice: Radial velocity amplitude decreases with decreasing inclination")
    plt.close(fig)


def example_4_doppler_animation():
    """Example 4: Doppler shift at multiple orbital phases"""
    print("\n=== Example 4: Doppler Shift Through Orbit ===")
    
    system = BinaryStarSystem(mass1=2.0, mass2=1.5, semi_major_axis=8.0, period=500.0)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Spectral Line Shifts at Different Orbital Phases', fontsize=16, fontweight='bold')
    
    phases = [0.0, 0.25, 0.5, 0.75]
    
    for ax, phase in zip(axes.flat, phases):
        time = phase * system.period
        rv1, rv2 = system.calculate_radial_velocities(np.array([time]), inclination=90)
        
        wavelength_center = 656.3
        wavelength1 = system.calculate_doppler_shift(rv1[0], wavelength_center)
        wavelength2 = system.calculate_doppler_shift(rv2[0], wavelength_center)
        
        wavelengths = np.linspace(wavelength_center - 2, wavelength_center + 2, 1000)
        
        # Gaussian absorption lines
        def gaussian(x, center, amplitude=1.0, sigma=0.05):
            return amplitude * np.exp(-0.5 * ((x - center) / sigma) ** 2)
        
        spectrum = np.ones_like(wavelengths)
        spectrum -= gaussian(wavelengths, wavelength1, amplitude=0.6, sigma=0.05)
        spectrum -= gaussian(wavelengths, wavelength2, amplitude=0.5, sigma=0.05)
        
        ax.plot(wavelengths, spectrum, 'k-', linewidth=2)
        ax.axvline(x=wavelength_center, color='gray', linestyle='--', alpha=0.5)
        ax.axvline(x=wavelength1, color='b', linestyle='--', alpha=0.7)
        ax.axvline(x=wavelength2, color='r', linestyle='--', alpha=0.7)
        
        ax.set_xlabel('Wavelength (nm)')
        ax.set_ylabel('Normalized Flux')
        ax.set_title(f'Phase {phase:.2f} | Star 1: {rv1[0]:.1f} km/s, Star 2: {rv2[0]:.1f} km/s')
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.2)
    
    plt.tight_layout()
    fig.savefig('example4_doppler_phases.png', dpi=150)
    print("Saved: example4_doppler_phases.png")
    print("Notice: Lines shift blue and red as stars move toward and away from us")
    plt.close(fig)


def example_5_short_period_system():
    """Example 5: Short period binary (like hot Jupiters or close binaries)"""
    print("\n=== Example 5: Short Period Binary System ===")
    print("Close binary with 10-day period")
    
    system = BinaryStarSystem(mass1=1.2, mass2=0.8, semi_major_axis=0.2, period=10.0)
    
    print(f"Orbital period: {system.period} days")
    print(f"Star 1 velocity: {system.v1_kms:.1f} km/s")
    print(f"Star 2 velocity: {system.v2_kms:.1f} km/s")
    print("Very high velocities due to short period!")
    
    fig = plot_radial_velocities(system, num_points=1000)
    fig.savefig('example5_short_period.png', dpi=150)
    print("Saved: example5_short_period.png")
    plt.close(fig)


def main():
    """Run all examples"""
    print("="*60)
    print("Binary Star System Simulator - Examples")
    print("="*60)
    
    example_1_equal_masses()
    example_2_high_mass_ratio()
    example_3_radial_velocities_different_inclinations()
    example_4_doppler_animation()
    example_5_short_period_system()
    
    print("\n" + "="*60)
    print("All examples completed!")
    print("Generated files:")
    print("  - example1_equal_mass.png")
    print("  - example2_high_mass_ratio.png")
    print("  - example3_inclination_effect.png")
    print("  - example4_doppler_phases.png")
    print("  - example5_short_period.png")
    print("="*60)


if __name__ == "__main__":
    main()
