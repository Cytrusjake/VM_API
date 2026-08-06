# result.py

from dataclasses import dataclass, field
from typing import Any, Dict
from datetime import datetime, timezone
import socket


@dataclass
class Result:
    """
    Standard result returned by every manager.
    """

    # Outcome
    success : bool
    status	: str = "SUCCESS"

    # Human-readable information
    message : str = ""
    error	: str | None = None

    # Optional payload
    data 	: Dict[str, Any] = field(default_factory=dict)

    # Metadata
    timestamp: str = field(
        default_factory = lambda: datetime.now(timezone.utc).isoformat()
    )

    hostname: str = field(
        default_factory = socket.gethostname
    )

    duration: float = 0.0

    ####################################################################
    # Factory Methods
    ####################################################################

    @classmethod
    def success_result(
        cls,
        message 	: str = "",
        data 		: Dict[str, Any] | None = None,
        duration	: float = 0.0,
    ):
        return cls(
            success 	= True,
            status 		= "SUCCESS",
            message 	= message,
            data 		= data or {},
            duration 	= duration,
        )

    @classmethod
    def warning_result(
        cls,
        message 	: str,
        data 		: Dict[str, Any] | None = None,
        duration 	: float = 0.0,
    ):
        return cls(
            success 	= True,
            status		= "WARNING",
            message 	= message,
            data 		= data or {},
            duration	= duration,
        )

    @classmethod
    def partial_result(
        cls,
        message 	: str,
        data 		: Dict[str, Any] | None = None,
        duration 	: float = 0.0,
    ):
        return cls(
            success 	= True,
            status 		= "PARTIAL",
            message 	= message,
            data 		= data or {},
            duration 	= duration,
        )

    @classmethod
    def failed_result(
        cls,
        error 	: Exception | str,
        message : str = "",
        duration: float = 0.0,
    ):
        return cls(
            success 	= False,
            status 		= "FAILED",
            message 	= message,
            error 		= str(error),
            duration 	= duration,
        )

    ####################################################################
    # Serialization
    ####################################################################

    def to_dict(self) -> Dict[str, Any]:
        return {
            "Success"	: self.success,
            "Status"	: self.status,
            "Message"	: self.message,
            "Error"		: self.error,
            "Data"		: self.data,
            "Timestamp"	: self.timestamp,
            "Hostname"	: self.hostname,
            "Duration"	: self.duration,
        }

    ####################################################################
    # Convenience
    ####################################################################

    def __bool__(self):
        return self.success

    def __repr__(self):
        return (
            f"<Result "
            f"success={self.success} "
            f"status='{self.status}' "
            f"message='{self.message}'>"
        )