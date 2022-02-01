"""
dcp_test
Created January 28, 2022 by Jennifer Baughman

Description: Test file for daily coding problems
"""

import pytest

# from daily_coding_problem.n_steps import n_steps
from dcp_1 import add_to_k
from dcp_2 import calc_mult_array
from dcp_4 import missing_integer
from dcp_5 import car, cdr, cons
from dcp_test_data import *


# def test_n_steps():
#     result = {(1, 1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2), (2, 2)}
#     assert n_steps(5) == result

@pytest.mark.parametrize("test_input,expected", dcp_1_test_data)
def test_add_to_k(test_input, expected):
    num_list, k = test_input
    assert add_to_k(num_list, k) == expected


@pytest.mark.parametrize("test_input,expected", dcp_2_test_data)
def test_mult_calc_array(test_input, expected):
    assert calc_mult_array(test_input) == expected


@pytest.mark.parametrize("test_input,expected", dcp_4_test_data)
def test_missing_integer(test_input, expected):
    assert missing_integer(test_input) == expected


@pytest.fixture(params=dcp_5_fixture_params)
def pair_gen(request):
    a, b = request.param
    return cons(a, b), (a, b)


def test_car(pair_gen):
    pair, result = pair_gen
    assert car(pair) == result[0]


def test_cdr(pair_gen):
    pair, result = pair_gen
    assert cdr(pair) == result[1]
