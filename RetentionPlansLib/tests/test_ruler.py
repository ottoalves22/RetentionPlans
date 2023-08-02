import pytest
from unittest.mock import Mock, call
from datetime import datetime
import os
import sys

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
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
    mocker.patch('Ruler.datetime.date', side_effect=test_date)
    check_period_mock = mocker.patch.object(ruler, 'check_period', return_value=check_period_return)

    ruler.classify(test_plan, test_date)

    out, err = capfd.readouterr()
    assert out == ret_or_del_return
    check_period_mock.assert_has_calls(check_period_calls)


@pytest.mark.parametrize('tgt_dt, rtt_days, return_bool',
                         [("30/08/2023", 42, True),
                          ("05/12/2023", 42, False)])
def test_check_period(mocker, tgt_dt, rtt_days, return_bool):
    ruler = Ruler()
    # Setting the date.now() as 02/08/2023 (right now)
    date_now_mock = Mock()
    date_mock = Mock()
    date_now_mock.date = date_mock
    date_mock.today.return_value = datetime.strptime("02/08/2023", '%d/%m/%Y').date()
    datetime_mock = mocker.patch('Ruler.datetime', side_effect=date_now_mock)
    target_date = datetime.strptime(tgt_dt, '%d/%m/%Y').date()
    retention_days = 42 
    checked = ruler.check_period(target_date, rtt_days)
    assert checked == return_bool




