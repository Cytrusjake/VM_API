from managers.base import BaseManager


class FilesystemManager(BaseManager):

    COMMANDS = {

        "CreateDirectory"       : "create_directory",
        "RemoveDirectory"       : "remove_directory",
        "ListDirectory"         : "list_directory",
        "Exists"                : "exists",
        "Size"                  : "size",
        "CreateFile"            : "create_file",
        "DeleteFile"            : "delete_file",
        "Copy"                  : "copy",
        "Move"                  : "move",
        "Rename"                : "rename",
        "Read"                  : "read",
        "Write"                 : "write",
        "Append"                : "append",
        "Chmod"                 : "chmod",
        "Chown"                 : "chown",
        "Symlink"               : "symlink",
        "Zip"                   : "zip",
        "Unzip"                 : "unzip",
        "Tar"                   : "tar",
        "Untar"                 : "untar",
        "Find"                  : "find",
        "SHA256"                : "sha256"
    }

    def __init__(self, context):
        super().__init__(context)

    @property
    def filesystem(self):
        return self.services["filesystem"]

    def create_directory(self, params):
        return self.filesystem.create_directory(params["Path"])

    def remove_directory(self, params):
        return self.filesystem.remove_directory(params["Path"])

    def list_directory(self, params):
        return self.filesystem.list_directory(params["Path"])

    def exists(self, params):
        return self.filesystem.exists(params["Path"])

    def size(self, params):
        return self.filesystem.size(params["Path"])

    def create_file(self, params):
        return self.filesystem.create_file(params["File"])

    def delete_file(self, params):
        return self.filesystem.delete_file(params["File"])

    def copy(self, params):
        return self.filesystem.copy(
            params["Source"],
            params["Destination"]
        )

    def move(self, params):
        return self.filesystem.move(
            params["Source"],
            params["Destination"]
        )

    def rename(self, params):
        return self.filesystem.rename(
            params["Source"],
            params["Destination"]
        )

    def read(self, params):
        return self.filesystem.read(params["File"])

    def write(self, params):
        return self.filesystem.write(
            params["File"],
            params["Contents"]
        )

    def append(self, params):
        return self.filesystem.append(
            params["File"],
            params["Contents"]
        )

    def chmod(self, params):
        return self.filesystem.chmod(
            params["Path"],
            params["Permissions"]
        )

    def chown(self, params):
        return self.filesystem.chown(
            params["Path"],
            params["Owner"]
        )

    def symlink(self, params):
        return self.filesystem.symlink(
            params["Source"],
            params["Destination"]
        )

    def zip(self, params):
        return self.filesystem.zip(
            params["Source"],
            params["Destination"]
        )

    def unzip(self, params):
        return self.filesystem.unzip(
            params["Archive"],
            params["Destination"]
        )

    def tar(self, params):
        return self.filesystem.tar(
            params["Source"],
            params["Destination"]
        )

    def untar(self, params):
        return self.filesystem.untar(
            params["Archive"],
            params["Destination"]
        )

    def find(self, params):
        return self.filesystem.find(
            params["Path"],
            params["Pattern"]
        )

    def sha256(self, params):
        return self.filesystem.sha256(
            params["File"]
        )