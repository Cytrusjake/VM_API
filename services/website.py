from managers.base import BaseManager
from result import Result


class WebsiteManager(BaseManager):

    def __init__(self, context):
        super().__init__(context)

        self.COMMANDS = {

            "Create"    : self.create,
            "Delete"    : self.delete,
            "Suspend"   : self.suspend
        }

    def create(self, params):

        return Result.success_result(
            "Website created."
        )

    def delete(self, params):

        return Result.success_result(
            "Website deleted."
        )

    def suspend(self, params):

        return Result.success_result(
            "Website suspended."
        )