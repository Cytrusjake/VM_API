class ResponseBuilder:

    @staticmethod
    def build(command, result):

        if command is None:

            return {
                "Success"   : False,
                "Status"    : result.status,
                "Error"     : result.error,
                "Message"   : result.message,
                "Data"      : result.data,
                "Duration"  : result.duration,
                "Hostname"  : result.hostname,
                "Timestamp" : result.timestamp,
            }

        return {

            "MessageID"     : command.message_id,
            "RequestID"     : command.request_id,
            "Namespace"     : command.namespace,
            "Action"        : command.action,
            "Result"        : result.to_dict()
        }