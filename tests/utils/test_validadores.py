from procergs.sitedemo.utils import validadores

import pytest


@pytest.mark.parametrize(
    "value,expected",
    [
        ["51999528312", True],
        ["(51)999528312", False],
        ["5439528312", True],
        ["5132104100", True],
        [" ", False],
        ["(999)1234566", False],
    ],
)
def test_is_valid_telefone(value, expected):
    """Testa a função is_valid_extension."""
    assert validadores.is_valid_telefone(value) is expected
