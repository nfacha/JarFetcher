import Storage
from link_providers import CraftBukkitProvider

all_links = {
    'craftbukkit': {},
    'nukkit': {},
    'paper': {},
    'spigot': {},
    'vanila': {},
}
Storage.init_logger()
Storage.logger.info('JarFetcher starting')
Storage.logger.info('Getting CraftBukkit links')
all_links['craftbukkit'].update(CraftBukkitProvider.get())

Storage.logger.debug(all_links)
