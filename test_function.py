from functions import hello_who, salary
import pytest
def test_hello_who_max():

        assert hello_who("Max") == "Hello, Max"
        assert hello_who("SMax") == "Hello, SMax"
        assert hello_who("mista") == "Hello, mista"
        assert hello_who("Vovan") == "Hello, Vovan"
        assert hello_who("10") == "Hello, 10"

def test_salary():
        assert(2,2) != 8
        assert(6,1) != 6

