from datetime import datetime


class BackupService:

    def __init__(
        self,
        compose,
        filesystem
    ):

        self.compose = compose
        self.filesystem = filesystem

    
    def backup_database(
        self,
        directory,
        database,
        destination
    ):

        filename = (
            f"{database}-"
            f"{datetime.utcnow():%Y%m%d-%H%M%S}.sql"
        )

        file = f"{destination}/{filename}"

        command = (
            "docker compose exec -T mariadb "
            'sh -c '
            f'"mariadb-dump -uroot -p$MYSQL_ROOT_PASSWORD '
            f'{database}" > "{file}"'
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

        command = (
            "docker compose exec -T mariadb "
            'sh -c '
            f'"mariadb -uroot -p$MYSQL_ROOT_PASSWORD '
            f'{database}" < "{backup}"'
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

        