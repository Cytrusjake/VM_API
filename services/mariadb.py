# services/mariadb.py

import re
import shlex

from result import Result


class MariaDBService:

    SERVICE = "mariadb"

    def __init__(self, compose):
        self.compose = compose

    # ============================================================
    # Helpers
    # ============================================================

    def _validate_identifier(self, value, name="identifier"):
       

        if not isinstance(value, str):
            raise ValueError(f"{name} must be a string")

        if not re.fullmatch(r"[A-Za-z0-9_$-]+", value):
            raise ValueError(
                f"Invalid {name}: {value!r}. "
                "Only letters, numbers, _, $, and - are allowed."
            )

        return value

    def _sql_string(self, value):
        
        if not isinstance(value, str):
            raise ValueError("SQL string value must be a string")

        return "'" + value.replace("'", "''") + "'"

    def _execute_sql(self, directory, sql):
        

        sql_argument = shlex.quote(sql)

        command = (
            f"printf '%s\\n' {sql_argument} | "
            f"docker compose exec -T {self.SERVICE} "
            f"sh -c 'mariadb -uroot -p\"$MYSQL_ROOT_PASSWORD\"'"
        )

        return self.compose._run(
            directory,
            command
        )

    def _mysqlcheck(self, directory, database, operation):
       

        database = self._validate_identifier(
            database,
            "database"
        )

        allowed_operations = {
            "optimize",
            "repair"
        }

        if operation not in allowed_operations:
            raise ValueError(
                f"Unsupported mysqlcheck operation: {operation}"
            )

        return self.compose._run(
            directory,
            (
                f"docker compose exec -T {self.SERVICE} "
                f"sh -c 'mysqlcheck "
                f'-uroot -p"$MYSQL_ROOT_PASSWORD" '
                f"--{operation} {shlex.quote(database)}'"
            )
        )

   

    def restart(self, directory):

        return self.compose._run(
            directory,
            f"docker compose restart {self.SERVICE}"
        )

    def start(self, directory):

        return self.compose._run(
            directory,
            f"docker compose start {self.SERVICE}"
        )

    def stop(self, directory):

        return self.compose._run(
            directory,
            f"docker compose stop {self.SERVICE}"
        )

    def status(self, directory):

        return self.compose._run(
            directory,
            f"docker compose ps {self.SERVICE}"
        )

    
    def version(self, directory):

        return self.compose._run(
            directory,
            f"docker compose exec -T {self.SERVICE} mariadb --version"
        )

    def databases(self, directory):

        return self._execute_sql(
            directory,
            "SHOW DATABASES;"
        )

    def users(self, directory):

        return self._execute_sql(
            directory,
            "SELECT User, Host FROM mysql.user;"
        )

    def process_list(self, directory):

        return self._execute_sql(
            directory,
            "SHOW PROCESSLIST;"
        )

  
    def create_database(self, directory, database):

        database = self._validate_identifier(
            database,
            "database"
        )

        return self._execute_sql(
            directory,
            f"CREATE DATABASE IF NOT EXISTS `{database}`;"
        )

    def delete_database(self, directory, database):

        database = self._validate_identifier(
            database,
            "database"
        )

        return self._execute_sql(
            directory,
            f"DROP DATABASE IF EXISTS `{database}`;"
        )

   
    def create_user(self, directory, username, password):

        username = self._validate_identifier(
            username,
            "username"
        )

        password = self._sql_string(password)

        return self._execute_sql(
            directory,
            (
                f"CREATE USER IF NOT EXISTS "
                f"'{username}'@'%' "
                f"IDENTIFIED BY {password};"
            )
        )

    def delete_user(self, directory, username):

        username = self._validate_identifier(
            username,
            "username"
        )

        return self._execute_sql(
            directory,
            f"DROP USER IF EXISTS '{username}'@'%';"
        )

    def reset_password(self, directory, username, password):

        username = self._validate_identifier(
            username,
            "username"
        )

        password = self._sql_string(password)

        return self._execute_sql(
            directory,
            (
                f"ALTER USER "
                f"'{username}'@'%' "
                f"IDENTIFIED BY {password};"
            )
        )

   
    def grant_all(self, directory, database, username):

        database = self._validate_identifier(
            database,
            "database"
        )

        username = self._validate_identifier(
            username,
            "username"
        )

        return self._execute_sql(
            directory,
            (
                f"GRANT ALL PRIVILEGES "
                f"ON `{database}`.* "
                f"TO '{username}'@'%';"
            )
        )

    def revoke_all(self, directory, database, username):

        database = self._validate_identifier(
            database,
            "database"
        )

        username = self._validate_identifier(
            username,
            "username"
        )

        return self._execute_sql(
            directory,
            (
                f"REVOKE ALL PRIVILEGES "
                f"ON `{database}`.* "
                f"FROM '{username}'@'%';"
            )
        )

    
    def optimize(self, directory, database):

        return self._mysqlcheck(
            directory,
            database,
            "optimize"
        )

    def repair(self, directory, database):

        return self._mysqlcheck(
            directory,
            database,
            "repair"
        )

    def flush_privileges(self, directory):

        return self._execute_sql(
            directory,
            "FLUSH PRIVILEGES;"
        )