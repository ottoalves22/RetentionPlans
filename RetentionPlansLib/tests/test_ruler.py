import pytest
from unittest.mock import Mock, call
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
 
# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)
 
# adding the parent directory to
# the sys.path.
sys.path.append(parent)
from Ruler import Ruler


@pytest.mark.parametrize("test_plan, check_period_return, ret_or_del_return, check_period_calls",
                         [("Standard", True, "The referred snapshot is retained.\n", [call("09/08/2023", 42)]),
                          ("standard", False, "The referred snapshot is deleted.\n", [call("09/08/2023", 42)]),
                          ("Gold", True, "The referred snapshot is retained.\n", [call("09/08/2023", 42), call("09/08/2023", 372)]),
                          ("gold", False, "The referred snapshot is deleted.\n", [call("09/08/2023", 42), call("09/08/2023", 372)]),
                          ("platInUM", True, "The referred snapshot is retained.\n", [call("09/08/2023", 42), call("09/08/2023", 372), call("09/08/2023", 2604)]),
                          ("PlatinuM", False, "The referred snapshot is deleted.\n", [call("09/08/2023", 42), call("09/08/2023", 372), call("09/08/2023", 2604)]),])
def test_ruler_classify(mocker, capfd, test_plan, check_period_return, ret_or_del_return, check_period_calls):
    test_date = "09/08/2023"
    ruler = Ruler()
    mock_datetime = Mock()
    mock_date = Mock()
    mock_datetime.strptime.return_value=mock_date
    mock_date.date.return_value = test_date
    mocker.patch('Ruler.datetime', mock_datetime)
    mock_date = mocker.patch('Ruler.datetime.date', side_effect=test_date)
    check_period_mock = mocker.patch.object(ruler, 'check_period', return_value=check_period_return)

    ruler.classify(test_plan, test_date)

    out, err = capfd.readouterr()
    assert out == ret_or_del_return
    check_period_mock.assert_has_calls(check_period_calls)

def test_check_period():
    ruler = Ruler()

