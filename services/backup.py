from datetime import datetime
import re
import shlex


class BackupService:

    def __init__(
        self,
        compose,
        filesystem
    ):

        self.compose = compose
        self.filesystem = filesystem

   
    def _validate_database(self, database):

        if not isinstance(database, str):
            raise ValueError("Database must be a string")

        if not re.fullmatch(r"[A-Za-z0-9_$-]+", database):
            raise ValueError(
                f"Invalid database name: {database!r}. "
                "Only letters, numbers, _, $, and - are allowed."
            )

        return database

    
    def backup_database(
        self,
        directory,
        database,
        destination
    ):

        database = self._validate_database(database)

        filename = (
            f"{database}-"
            f"{datetime.utcnow():%Y%m%d-%H%M%S}.sql"
        )

        file = f"{destination}/{filename}"

        command = (
            "docker compose exec -T mariadb "
            "sh -c "
            f"'mariadb-dump "
            f'-uroot -p"$MYSQL_ROOT_PASSWORD" '
            f'{shlex.quote(database)}' 
            "' "
            f"> {shlex.quote(file)}"
        )

        return self.compose._run(
            directory,
            command
        )

   
    def backup_files(
        self,
        source,
        destination
    ):

        filename = (
            f"website-"
            f"{datetime.utcnow():%Y%m%d-%H%M%S}.tar.gz"
        )

        archive = (
            f"{destination}/{filename}"
        )

        return self.filesystem.tar(
            source,
            archive
        )

    
    def full_backup(
        self,
        directory,
        website_path,
        database,
        destination
    ):

        db = self.backup_database(
            directory,
            database,
            destination
        )

        if not db.success:
            return db

        return self.backup_files(
            website_path,
            destination
        )

   
    def restore_database(
        self,
        directory,
        database,
        backup
    ):

        database = self._validate_database(database)

        command = (
            "docker compose exec -T mariadb "
            "sh -c "
            f"'mariadb "
            f'-uroot -p"$MYSQL_ROOT_PASSWORD" '
            f'{shlex.quote(database)}'
            "' "
            f"< {shlex.quote(backup)}"
        )

        return self.compose._run(
            directory,
            command
        )

   
    def restore_files(
        self,
        archive,
        destination
    ):

        return self.filesystem.untar(
            archive,
            destination
        )

   
    def list(self, path):

        return self.filesystem.list_directory(
            path
        )

    def delete(self, file):

        return self.filesystem.delete_file(
            file
        )