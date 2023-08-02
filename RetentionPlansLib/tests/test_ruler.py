import pytest
from unittest.mock import Mock
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


def test_ruler_classify(mocker, capfd):
    test_plan = "standard"
    test_date = "09/08/2023"
    days = 42
    months = 372
    years = 2604
    ruler = Ruler()
    mock_datetime = Mock()
    mock_date = Mock()
    mock_datetime.strptime.return_value=mock_date
    mock_date.date.return_value = test_date
    mocker.patch('Ruler.datetime', mock_datetime)
    mock_date = mocker.patch('Ruler.datetime.date', side_effect=test_date)
    check_period_mock = mocker.patch.object(ruler, 'check_period', return_value=True)

    ruler.classify(test_plan, test_date)

    out, err = capfd.readouterr()
    assert out == "The referred snapshot is retained.\n"
    check_period_mock.assert_called_with(test_date, days)

def test_check_period():
    pass