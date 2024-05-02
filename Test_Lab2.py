import Lab2_submodule_directory.Exercise6

def test_calc_average_temp():
    input = [2,3,4,5]
    test_arr = 3.5

    result = Lab2_submodule_directory.Exercise6.calc_average_temperature(input)
    assert (result == test_arr)

def test_min_max():
    input = [2,3,4,5]
    test_min_arr = 2
    test_max_arr = 5

    min_result = Lab2_submodule_directory.Exercise6.find_min_max(input)
    max_result = Lab2_submodule_directory.Exercise6.find_min_max(input)
    assert (min_result == test_min_arr)
    assert (max_result == test_max_arr)

def test_median():
    input = [2,3,4,5]
    test_arr = 3.5

    result = min_result = Lab2_submodule_directory.Exercise6.calc_median(input)
    assert (result == test_arr)