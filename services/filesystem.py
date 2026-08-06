from result import Result


class FilesystemService:

    def __init__(self, shell):

        self.shell = shell

   def create_directory(self, path):

        return self.shell.run_result(
            f'mkdir -p "{path}"'
        )

    def remove_directory(self, path):

        return self.shell.run_result(
            f'rm -rf "{path}"'
        )

    def list_directory(self, path):

        return self.shell.run_result(
            f'ls -lah "{path}"'
        )

    def exists(self, path):

        return self.shell.run_result(
            f'test -e "{path}" && echo true || echo false'
        )

    def size(self, path):

        return self.shell.run_result(
            f'du -sh "{path}"'
        )

    
    def create_file(self, file):

        return self.shell.run_result(
            f'touch "{file}"'
        )

    def delete_file(self, file):

        return self.shell.run_result(
            f'rm -f "{file}"'
        )

    def copy(self, source, destination):

        return self.shell.run_result(
            f'cp -R "{source}" "{destination}"'
        )

    def move(self, source, destination):

        return self.shell.run_result(
            f'mv "{source}" "{destination}"'
        )

    def rename(self, source, destination):

        return self.move(source, destination)

    
    def read(self, file):

        return self.shell.run_result(
            f'cat "{file}"'
        )

    def write(self, file, contents):

        command = (
            f'cat > "{file}" << \'EOF\'\n'
            f'{contents}\n'
            f'EOF'
        )

        return self.shell.run_result(command)

    def append(self, file, contents):

        command = (
            f'cat >> "{file}" << \'EOF\'\n'
            f'{contents}\n'
            f'EOF'
        )

        return self.shell.run_result(command)

    
    def chmod(self, path, permissions):

        return self.shell.run_result(
            f'chmod {permissions} "{path}"'
        )

    def chown(self, path, owner):

        return self.shell.run_result(
            f'chown -R {owner} "{path}"'
        )

    
    def symlink(self, source, destination):

        return self.shell.run_result(
            f'ln -s "{source}" "{destination}"'
        )

    
    def zip(self, source, destination):

        return self.shell.run_result(
            f'zip -r "{destination}" "{source}"'
        )

    def unzip(self, archive, destination):

        return self.shell.run_result(
            f'unzip "{archive}" -d "{destination}"'
        )

    def tar(self, source, destination):

        return self.shell.run_result(
            f'tar czf "{destination}" "{source}"'
        )

    def untar(self, archive, destination):

        return self.shell.run_result(
            f'tar xzf "{archive}" -C "{destination}"'
        )

   
    def find(self, path, pattern):

        return self.shell.run_result(
            f'find "{path}" -name "{pattern}"'
        )

   
    def sha256(self, file):

        return self.shell.run_result(
            f'sha256sum "{file}"'
        )

        