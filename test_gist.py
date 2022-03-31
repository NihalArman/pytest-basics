import pytest

def test_our_first_test() -> None:
    assert 1 == 1

## to run: pytest test_gist.py -v

@pytest.mark.skip
def test_should_be_skipped() -> None:
    pass

def test_should_not_be_skipped() -> None:
    assert 1 == 1

@pytest.mark.skipif(2 > 1, reason="Skipped because 4 > 1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2

@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 2 == 3

@pytest.mark.slow
def test_slow_test() -> None:
    pass
###to hide the warning: pytest test_gist.py -v -p no:warnings
###to only run the slow test: pytest test_gist.py -v -p no:warnings -m slow

##----------------------FIXTURE--------------------------------------------###
class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name
        self.stock_symbol = stock_symbol

    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"

@pytest.fixture
def company() -> Company:
    return Company(name="Blancco", stock_symbol="Blc")

def test_test_with_fixture(company: Company) -> None:
    print(f"Printing {company} with fixture")

##to print: pytest test_gist.py -v -s
## -s will print what the fixture

##----------------------FIXTURE ENDS--------------------------------------------###

##----------------------PARMETERIZED TEST--------------------------------------------###
@pytest.mark.parametrize(
    "company_name",
    ["microsoft", "google", "apple"],
    ids=["MICROSFT TEST", "GOOGLE TEST", "APPLE TEST"]
)
def test_does_parametr_work(company_name: str) -> None:
    print(f"Test with {company_name} \n")
##----------------------PARMETERIZED TESTENDS--------------------------------------------###

##----------------------Exception--------------------------------------------###
def raise_covid19_exception() -> None:
    raise ValueError("CoronaVirus Exception")

def test_expection_should_pass() -> None:
    with pytest.raises(ValueError) as e:
        raise_covid19_exception()
    assert "CoronaVirus Exception" == str(e.value)
##----------------------Exception--------------------------------------------###