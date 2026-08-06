
from result import Result


class MariaDBService:

    def __init__(self, compose):
        self.compose = compose

   
    def restart(self, directory):
        return self.compose._run(
            directory,
            "docker compose restart mariadb"
        )

    def start(self, directory):
        return self.compose._run(
            directory,
            "docker compose start mariadb"
        )

    def stop(self, directory):
        return self.compose._run(
            directory,
            "docker compose stop mariadb"
        )

    def status(self, directory):
        return self.compose._run(
            directory,
            "docker compose ps mariadb"
        )

    
    def version(self, directory):
        return self.compose._run(
            directory,
            "docker compose exec -T mariadb mariadb --version"
        )

    def databases(self, directory):
        return self.compose._run(
            directory,
            'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "SHOW DATABASES;"'
        )

    def users(self, directory):
        return self.compose._run(
            directory,
            'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "SELECT User,Host FROM mysql.user;"'
        )

    def process_list(self, directory):
        return self.compose._run(
            directory,
            'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "SHOW PROCESSLIST;"'
        )

    def create_database(self, directory, database):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "CREATE DATABASE `{database}`;"'
        )

    def delete_database(self, directory, database):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "DROP DATABASE `{database}`;"'
        )

    
    def create_user(self, directory, username, password):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "CREATE USER \'{username}\'@\'%\' IDENTIFIED BY \'{password}\';"'
        )

    def delete_user(self, directory, username):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "DROP USER \'{username}\'@\'%\';"'
        )

    def reset_password(self, directory, username, password):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "ALTER USER \'{username}\'@\'%\' IDENTIFIED BY \'{password}\';"'
        )

    
    def grant_all(self, directory, database, username):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "GRANT ALL PRIVILEGES ON `{database}`.* TO \'{username}\'@\'%\'; FLUSH PRIVILEGES;"'
        )

    def revoke_all(self, directory, database, username):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "REVOKE ALL PRIVILEGES ON `{database}`.* FROM \'{username}\'@\'%\'; FLUSH PRIVILEGES;"'
        )

    
    def optimize(self, directory, database):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mysqlcheck -uroot -p"$MYSQL_ROOT_PASSWORD" --optimize {database}'
        )

    def repair(self, directory, database):
        return self.compose._run(
            directory,
            f'docker compose exec -T mariadb mysqlcheck -uroot -p"$MYSQL_ROOT_PASSWORD" --repair {database}'
        )

    def flush_privileges(self, directory):
        return self.compose._run(
            directory,
            'docker compose exec -T mariadb mariadb -uroot -p"$MYSQL_ROOT_PASSWORD" -e "FLUSH PRIVILEGES;"'
        )

        