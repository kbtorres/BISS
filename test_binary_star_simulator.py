"""
Test script for binary star system simulator.

This module contains unit tests to validate the core functionality and calculations
of the binary star system simulator, including orbital mechanics, radial velocities,
and Doppler shift calculations.

Run with: python test_binary_star_simulator.py
"""

import numpy as np
from binary_star_simulator import BinaryStarSystem


def test_binary_star_system_creation():
    """Test creating a binary star system with default parameters"""
    print("Testing Binary Star System creation...")
    system = BinaryStarSystem(1.5, 1.0, 5.0, 365.0)
    
    assert system.mass1 == 1.5, "Star 1 mass incorrect"
    assert system.mass2 == 1.0, "Star 2 mass incorrect"
    assert system.semi_major_axis == 5.0, "Semi-major axis incorrect"
    assert system.period == 365.0, "Period incorrect"
    
    print("✓ Binary star system creation test passed")


def test_orbital_radii():
    """Test that orbital radii sum to semi-major axis"""
    print("Testing orbital radii calculation...")
    system = BinaryStarSystem(1.5, 1.0, 5.0, 365.0)
    
    # r1 + r2 should equal semi-major axis
    total_radius = system.r1 + system.r2
    assert abs(total_radius - system.semi_major_axis) < 1e-10, \
        f"Orbital radii sum {total_radius} != semi-major axis {system.semi_major_axis}"
    
    print(f"✓ Orbital radii test passed: r1={system.r1:.3f} AU, r2={system.r2:.3f} AU")


def test_center_of_mass():
    """Test that center of mass is at origin"""
    print("Testing center of mass...")
    system = BinaryStarSystem(2.0, 1.0, 6.0, 500.0)
    
    # At any time, m1*r1 should equal m2*r2 (balance around center of mass)
    moment1 = system.mass1 * system.r1
    moment2 = system.mass2 * system.r2
    
    assert abs(moment1 - moment2) < 1e-10, \
        f"Center of mass not balanced: m1*r1={moment1} != m2*r2={moment2}"
    
    print(f"✓ Center of mass test passed: m1*r1={moment1:.3f}, m2*r2={moment2:.3f}")


def test_position_calculation():
    """Test position calculations at different times"""
    print("Testing position calculations...")
    system = BinaryStarSystem(1.0, 1.0, 4.0, 365.0)
    
    # Test at time = 0
    times = np.array([0.0, system.period/4, system.period/2])
    x1, y1, x2, y2 = system.calculate_positions(times)
    
    # At t=0, star 1 should be at (r1, 0)
    assert abs(x1[0] - system.r1) < 1e-10, f"x1 at t=0 incorrect: {x1[0]}"
    assert abs(y1[0]) < 1e-10, f"y1 at t=0 incorrect: {y1[0]}"
    
    # At t=0, star 2 should be at (-r2, 0)
    assert abs(x2[0] + system.r2) < 1e-10, f"x2 at t=0 incorrect: {x2[0]}"
    assert abs(y2[0]) < 1e-10, f"y2 at t=0 incorrect: {y2[0]}"
    
    print("✓ Position calculation test passed")


def test_radial_velocity_symmetry():
    """Test that radial velocities are antisymmetric"""
    print("Testing radial velocity symmetry...")
    system = BinaryStarSystem(1.5, 1.0, 5.0, 365.0)
    
    times = np.linspace(0, system.period, 100)
    rv1, rv2 = system.calculate_radial_velocities(times, inclination=90)
    
    # At edge-on viewing (i=90°), RV curves should have opposite signs
    # Check at quarter period
    idx_quarter = len(times) // 4
    
    # The stars should have opposite radial velocities
    assert rv1[idx_quarter] * rv2[idx_quarter] < 0, \
        f"Radial velocities should have opposite signs at quarter period"
    
    print("✓ Radial velocity symmetry test passed")


def test_doppler_shift():
    """Test Doppler shift calculation"""
    print("Testing Doppler shift calculation...")
    system = BinaryStarSystem(1.0, 1.0, 5.0, 365.0)
    
    # Test with zero velocity
    shifted = system.calculate_doppler_shift(0.0, wavelength=656.3)
    assert abs(shifted - 656.3) < 1e-10, "Zero velocity should give no shift"
    
    # Test with positive velocity (redshift)
    shifted_red = system.calculate_doppler_shift(100.0, wavelength=656.3)
    assert shifted_red > 656.3, "Positive velocity should give redshift"
    
    # Test with negative velocity (blueshift)
    shifted_blue = system.calculate_doppler_shift(-100.0, wavelength=656.3)
    assert shifted_blue < 656.3, "Negative velocity should give blueshift"
    
    print("✓ Doppler shift calculation test passed")


def test_equal_mass_system():
    """Test special case of equal masses"""
    print("Testing equal mass system...")
    system = BinaryStarSystem(1.0, 1.0, 10.0, 500.0)
    
    # For equal masses, both stars should have equal orbital radii
    assert abs(system.r1 - system.r2) < 1e-10, \
        f"Equal masses should have equal radii: r1={system.r1}, r2={system.r2}"
    
    # And equal velocities
    assert abs(system.v1_kms - system.v2_kms) < 1e-10, \
        f"Equal masses should have equal velocities: v1={system.v1_kms}, v2={system.v2_kms}"
    
    print(f"✓ Equal mass system test passed: r1=r2={system.r1:.3f} AU")


def run_all_tests():
    """Run all test functions"""
    print("\n" + "="*60)
    print("Running Binary Star System Tests")
    print("="*60 + "\n")
    
    tests = [
        test_binary_star_system_creation,
        test_orbital_radii,
        test_center_of_mass,
        test_position_calculation,
        test_radial_velocity_symmetry,
        test_doppler_shift,
        test_equal_mass_system,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ Test failed: {test.__name__}")
            print(f"  Error: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ Test error: {test.__name__}")
            print(f"  Exception: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
