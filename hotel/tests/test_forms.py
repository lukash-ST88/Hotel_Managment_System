
from faker import Faker
from datetime import datetime
import pytest
from hotel.forms import AvailabilityForm

fake = Faker()


@pytest.mark.parametrize(
    "check_in, check_out, validity",
    [
        (fake.date_time_this_decade(), fake.date_time_this_decade(), True),
        (datetime(2012, 1, 1), datetime(2012, 1, 2), True),
        ("", "2012-01-02", False)
    ],
)
def test_add_expense_form(check_in, check_out, validity):
    form = AvailabilityForm(data={
        'check_in': check_in,
        'check_out': check_out,
    })
    print(dir(form))
    assert form.is_valid() == validity
