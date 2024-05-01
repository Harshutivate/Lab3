import Lab2_submodule_directory.bmi
import pytest

def test_bmi_normal_weight():
    bmi_result = Lab2_submodule_directory.bmi.calculate_bmi(1.75, 70)
    if 18.5 <= bmi_result <= 25:
        print("Normal Weight")
    assert bmi_result == 0

def test_bmi_over_weight():
    bmi_result = Lab2_submodule_directory.bmi.calculate_bmi(1.75, 85)
    if bmi_result > 25:
        print("Over Weight")
    assert bmi_result == 1

def test_bmi_under_weight():
    bmi_result = Lab2_submodule_directory.bmi.calculate_bmi(1.75, 55)
    if bmi_result < 18.5:
        print("Under Weight")
    assert bmi_result == -1

