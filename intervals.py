from datetime import datetime, timedelta
from enum import StrEnum


class IntervalEnum(StrEnum):
    seconds = 'seconds'
    minutes = 'minutes'
    hours = 'hours'
    days = 'days'


def get_intervals(body: str, n: int, from_date: datetime):

    if n < 0:
        raise Exception('Sequence is less than zero', n)

    intervals = [interval for interval in IntervalEnum]
    if body not in intervals:
        raise Exception('Unsupported interval type', body)

    result = [
        [str(from_date), str(from_date + timedelta(**{body: i}))]
        for i in range(1, n+1)
    ]

    return result


print (get_intervals('days', 4, datetime.utcnow()))
