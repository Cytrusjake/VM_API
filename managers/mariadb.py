
from managers.base import BaseManager


class MariaDBManager(BaseManager):

    COMMANDS = {
        "Restart"			: "restart",
        "Start"				: "start",
        "Stop"				: "stop",
        "Status"			: "status",
        "Version"			: "version",
        "Databases"			: "databases",
        "Users"				: "users",
        "ProcessList"		: "process_list",
        "CreateDatabase"	: "create_database",
        "DeleteDatabase"	: "delete_database",
        "CreateUser"		: "create_user",
        "DeleteUser"		: "delete_user",
        "ResetPassword"		: "reset_password",
        "GrantAll"			: "grant_all",
        "RevokeAll"			: "revoke_all",
        "Optimize"			: "optimize",
        "Repair"			: "repair",
        "FlushPrivileges"	: "flush_privileges"
    }

    def __init__(self, context):
        super().__init__(context)

    @property
    def mariadb(self):
        return self.services["mariadb"]

   
    def restart(self, params):
        return self.mariadb.restart(params["Directory"])

    def start(self, params):
        return self.mariadb.start(params["Directory"])

    def stop(self, params):
        return self.mariadb.stop(params["Directory"])

    def status(self, params):
        return self.mariadb.status(params["Directory"])

    
    def version(self, params):
        return self.mariadb.version(params["Directory"])

    def databases(self, params):
        return self.mariadb.databases(params["Directory"])

    def users(self, params):
        return self.mariadb.users(params["Directory"])

    def process_list(self, params):
        return self.mariadb.process_list(params["Directory"])

    
    def create_database(self, params):
        return self.mariadb.create_database(
            params["Directory"],
            params["Database"]
        )

    def delete_database(self, params):
        return self.mariadb.delete_database(
            params["Directory"],
            params["Database"]
        )

   
    def create_user(self, params):
        return self.mariadb.create_user(
            params["Directory"],
            params["Username"],
            params["Password"]
        )

    def delete_user(self, params):
        return self.mariadb.delete_user(
            params["Directory"],
            params["Username"]
        )

    def reset_password(self, params):
        return self.mariadb.reset_password(
            params["Directory"],
            params["Username"],
            params["Password"]
        )

   
    def grant_all(self, params):
        return self.mariadb.grant_all(
            params["Directory"],
            params["Database"],
            params["Username"]
        )

    def revoke_all(self, params):
        return self.mariadb.revoke_all(
            params["Directory"],
            params["Database"],
            params["Username"]
        )

   
    def optimize(self, params):
        return self.mariadb.optimize(
            params["Directory"],
            params["Database"]
        )

    def repair(self, params):
        return self.mariadb.repair(
            params["Directory"],
            params["Database"]
        )

    def flush_privileges(self, params):
        return self.mariadb.flush_privileges(
            params["Directory"]
        )

        