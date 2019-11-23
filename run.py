import Storage
from link_providers import CraftBukkitProvider, SpigotProvider

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
all_links['spigot'].update(SpigotProvider.get())

Storage.logger.debug(all_links)
