# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TicketStatusEnum(str, enum.Enum):
    """
    * `OPEN` - OPEN
    * `CLOSED` - CLOSED
    * `IN_PROGRESS` - IN_PROGRESS
    * `ON_HOLD` - ON_HOLD
    """

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    IN_PROGRESS = "IN_PROGRESS"
    ON_HOLD = "ON_HOLD"

    def visit(
        self,
        open: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        on_hold: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TicketStatusEnum.OPEN:
            return open()
        if self is TicketStatusEnum.CLOSED:
            return closed()
        if self is TicketStatusEnum.IN_PROGRESS:
            return in_progress()
        if self is TicketStatusEnum.ON_HOLD:
            return on_hold()
