from config import Config
from logger import Logger

from context import Context
from registry import Registry
from router import Router
from consumer import Consumer
from pika_client import PikaClient

from services.shell import ShellService
from services.compose import ComposeService
from services.nginx import NginxService
from services.php import PHPService
from services.mariadb import MariaDBService
from services.redis import RedisService
from services.memcached import MemcachedService
from services.varnish import VarnishService
from services.scheduler import SchedulerService
from services.resources import ResourcesService
from services.logs import LogsService
from services.filesystem import FilesystemService
from services.backup import BackupService
from services.agent import AgentService

from managers.compose import ComposeManager
from managers.nginx import NginxManager
from managers.php import PHPManager
from managers.mariadb import MariaDBManager
from managers.redis import RedisManager
from managers.memcached import MemcachedManager
from managers.varnish import VarnishManager
from managers.scheduler import SchedulerManager
from managers.resources import ResourcesManager
from managers.logs import LogsManager
from managers.filesystem import FilesystemManager
from managers.backup import BackupManager
from managers.agent import AgentManager


def build():

   
    config  = Config()
    logger  = Logger()
    context = Context(
           logger,
           config
    )
    shell   = ShellService()

    context.services["shell"] = shell

    compose = ComposeService(shell)
    context.services["compose"] = compose
    context.services["nginx"] = NginxService(compose)
    context.services["php"] = PHPService(compose)
    context.services["mariadb"] = MariaDBService(compose)
    context.services["redis"] = RedisService(compose)
    context.services["memcached"] = MemcachedService(compose)
    context.services["varnish"] = VarnishService(compose)

    context.services["scheduler"] = SchedulerService(compose)

    context.services["resources"] = ResourcesService(shell)

    context.services["logs"] = LogsService(
        compose,
        shell
    )

    context.services["filesystem"] = FilesystemService(shell)

    context.services["backup"] = BackupService(
        compose,
        context.services["filesystem"]
    )

    context.services["agent"] = AgentService(shell)

    ####################################################################
    # Registry
    ####################################################################

    registry = Registry()

    registry.register(
        "Compose",
        ComposeManager(context)
    )

    registry.register(
        "Nginx",
        NginxManager(context)
    )

    registry.register(
        "PHP",
        PHPManager(context)
    )

    registry.register(
        "MariaDB",
        MariaDBManager(context)
    )

    registry.register(
        "Redis",
        RedisManager(context)
    )

    registry.register(
        "Memcached",
        MemcachedManager(context)
    )

    registry.register(
        "Varnish",
        VarnishManager(context)
    )

    registry.register(
        "Scheduler",
        SchedulerManager(context)
    )

    registry.register(
        "Resources",
        ResourcesManager(context)
    )

    registry.register(
        "Logs",
        LogsManager(context)
    )

    registry.register(
        "Filesystem",
        FilesystemManager(context)
    )

    registry.register(
        "Backup",
        BackupManager(context)
    )

    registry.register(
        "Agent",
        AgentManager(context)
    )

    ####################################################################
    # Router
    ####################################################################

    router = Router(registry)

    ####################################################################
    # Consumer
    ####################################################################

    consumer = Consumer(
        router,
        logger
    )

    ####################################################################
    # Pika
    ####################################################################

    pika = PikaClient(
        config=config,
        consumer=consumer,
        logger=logger
    )

    return pika


if __name__ == "__main__":

    client = build()

    client.run()