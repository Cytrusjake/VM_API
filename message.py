# message.py

import json
import uuid
from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class Message:

    message_id      : str
    request_id      : str
    namespace       : str
    action          : str
    reply_to        : str = ""
    parameters      : Dict[str, Any] = field(default_factory=dict)
    
    @classmethod
    def from_json(cls, body):

        if isinstance(body, bytes):
            body = body.decode("utf-8")

        return cls.from_dict(json.loads(body))

    @classmethod
    def from_dict(cls, data):

        namespace   = data.get("Namespace")
        action      = data.get("Action")

        if not namespace:
            raise ValueError("Missing 'Namespace'.")

        if not action:
            raise ValueError("Missing 'Action'.")

        return cls(

            message_id = data.get(
                "MessageID",
                str(uuid.uuid4())
            ),

            request_id = data.get(
                "RequestID",
                str(uuid.uuid4())
            ),

            namespace   = namespace,
            action      = action,
            reply_to    = data.get(
                "ReplyTo",
                ""
            ),

            parameters  = data.get(
                "Parameters",
                {}
            )
        )

    def to_dict(self):

        return {

            "MessageID" : self.message_id,
            "RequestID" : self.request_id,
            "Namespace" : self.namespace,
            "Action"    : self.action,
            "ReplyTo"   : self.reply_to,
            "Parameters": self.parameters
        }

    def to_json(self):

        return json.dumps(self.to_dict())

    def __repr__(self):

        return (
            f"<Message "
            f"{self.namespace}.{self.action} "
            f"Request={self.request_id} "
            f"ReplyTo={self.reply_to}>"
        )
        