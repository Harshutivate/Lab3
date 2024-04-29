import Lab2_submodule_directory.bmi
import pytest

def test_bmi_normal_weight():
    # Test BMI calculation for normal weight (BMI between 18.5 and 24.9)
    assert Lab2_submodule_directory.bmi.calculate_bmi(1.75, 70) == 0

def test_bmi_over_weight():
    # Test BMI calculation for overweight (BMI greater than or equal to 25)
    assert Lab2_submodule_directory.bmi.calculate_bmi(1.75, 85) == 1

def test_bmi_under_weight():
    # Test BMI calculation for underweight (BMI less than 18.5)
    assert Lab2_submodule_directory.bmi.calculate_bmi(1.75, 55) == -1
