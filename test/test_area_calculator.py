import pytest
from src.calculations_functions.area_calculator import AreaCalculator

class TestAreaCalculations:

    def test_rectangle_calculation_positive_values(self):
        ac = AreaCalculator()
        assert ac.rectangle_calculations(5, 10) == 50

    def test_rectangle_calculation_negative_values(self):
        with pytest.raises(ValueError):
            assert AreaCalculator().rectangle_calculations(-5, 10)

    def test_rectangle_calculation_zero_values(self):
        with pytest.raises(ValueError):
            assert AreaCalculator().rectangle_calculations(0, 10)


