# __init__.py

# All tasks events
START_TASK = b"\x80"
START_AND_STOP_ET = b"\x02"

# QCT events
START_VIS = b"\x04"
START_COG = b"\x08"
START_MOT = b"\x10"
START_BLANK = b"\x20"

# REST events
START_FIXATION = b"\x04"
START_MOVIE = b"\x20"
STOP_FIXATION = b"\x10"
STOP_MOVIE = b"\x40"

# BHT events
START_BREATH_IN = b"\x04"
START_BREATH_OUT = b"\x08"
START_HOLD = b"\x10"


def sum_events(events_list):
    """
    Calculate the sum of events represented as bytes.

    Args:
        events_list (List[bytes]): A list of bytes representing events.

    Returns:
        bytes: The sum of the events as bytes.
    """
    result_int = sum(int.from_bytes(event, byteorder="big") for event in events_list)
    result_bytes = result_int.to_bytes(
        (result_int.bit_length() + 7) // 8, byteorder="big"
    )
    return result_bytes
