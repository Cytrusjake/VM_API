from managers.base import BaseManager


class BackupManager(BaseManager):

    COMMANDS = {

        "BackupDatabase"    : "backup_database",
        "BackupFiles"       : "backup_files",
        "FullBackup"        : "full_backup",
        "RestoreDatabase"   : "restore_database",
        "RestoreFiles"      : "restore_files",
        "List"              : "list",
        "Delete"            : "delete"

    }

    def __init__(self, context):

        super().__init__(context)

    @property
    def backup(self):

        return self.services["backup"]

    
    def backup_database(self, params):

        return self.backup.backup_database(

            params["Directory"],
            params["Database"],
            params["Destination"]

        )

    def backup_files(self, params):

        return self.backup.backup_files(

            params["Source"],
            params["Destination"]

        )

    def full_backup(self, params):

        return self.backup.full_backup(

            params["Directory"],
            params["Website"],
            params["Database"],
            params["Destination"]

        )

   
    def restore_database(self, params):

        return self.backup.restore_database(

            params["Directory"],
            params["Database"],
            params["Backup"]

        )

    def restore_files(self, params):

        return self.backup.restore_files(

            params["Archive"],
            params["Destination"]

        )

   
    def list(self, params):

        return self.backup.list(

            params["Path"]

        )

    def delete(self, params):

        return self.backup.delete(

            params["File"]

        )

        