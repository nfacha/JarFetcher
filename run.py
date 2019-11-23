import concurrent.futures
import os

import Storage
import conf_generator
import downloader

all_links = {
    'craftbukkit': {},
    'nukkit': {},
    'paper': {},
    'spigot': {},
    'vanila': {},
}
all_links = {'craftbukkit': {
    'craftbukkit-1.14.4.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.4-R0.1-SNAPSHOT.jar',
    'craftbukkit-1.14.3.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.3-R0.1-SNAPSHOT.jar',
    'craftbukkit-1.14.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.2-R0.1-SNAPSHOT.jar',
    'craftbukkit-1.14.1.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.1-R0.1-SNAPSHOT.jar',
    'craftbukkit-1.14.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14-R0.1-SNAPSHOT.jar',
    'craftbukkit-1.13.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.13.2.jar',
    'craftbukkit-1.13.1.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.13.1.jar',
    'craftbukkit-1.13.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.13.jar',
    'craftbukkit-1.12.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.12.2.jar',
    'craftbukkit-1.12.1.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.12.1.jar',
    'craftbukkit-1.12.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.12.jar',
    'craftbukkit-1.11.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.11.2.jar',
    'craftbukkit-1.11.1.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.11.1.jar',
    'craftbukkit-1.11.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.11.jar',
    'craftbukkit-1.10.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.10.2-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.10.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.10-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.9.4.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.9.4-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.9.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.9.2-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.9.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.9-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.8.8.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.8-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.8.7.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.7-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.8.6.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.6-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.8.5.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.5-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.8.4.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.4-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.8.3.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.3-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.8.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8-R0.1-SNAPSHOT-latest.jar',
    'craftbukkit-1.7.10.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.10-R0.1-20140808.005431-8.jar',
    'craftbukkit-1.7.9.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.9-R0.2-SNAPSHOT.jar',
    'craftbukkit-1.7.8.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.8-R0.1-SNAPSHOT.jar',
    'craftbukkit-1.7.5.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.5-R0.1-20140402.020013-12.jar',
    'craftbukkit-1.7.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.2-R0.4-20140216.012104-3.jar',
    'craftbukkit-1.6.4.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.6.4-R2.0.jar',
    'craftbukkit-1.6.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.6.2-R0.1-SNAPSHOT.jar',
    'craftbukkit-1.6.1.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.6.1-R0.1-SNAPSHOT.jar',
    'craftbukkit-1.5.2.jar': 'https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.5.2-R1.0.jar'}, 'nukkit': {},
    'paper': {}, 'spigot': {'spigot-1.14.4.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.14.4.jar',
                            'spigot-1.14.3.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.14.3.jar',
                            'spigot-1.14.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.14.2.jar',
                            'spigot-1.14.1.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.14.1.jar',
                            'spigot-1.14.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.14.jar',
                            'spigot-1.13.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.13.2.jar',
                            'spigot-1.13.1.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.13.1.jar',
                            'spigot-1.13.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.13.jar',
                            'spigot-1.12.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar',
                            'spigot-1.12.1.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.12.1.jar',
                            'spigot-1.12.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.12.jar',
                            'spigot-1.11.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.11.2.jar',
                            'spigot-1.11.1.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.11.1.jar',
                            'spigot-1.11.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.11.jar',
                            'spigot-1.10.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.10.2-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.10.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.10-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.9.4.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.9.4-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.9.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.9.2-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.9.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.9-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.8.8.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.8.7.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.8.7-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.8.6.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.8.6-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.8.5.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.8.5-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.8.4.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.8.4-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.8.3.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.8.3-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.8.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.8-R0.1-SNAPSHOT-latest.jar',
                            'spigot-1.7.10.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.7.10-SNAPSHOT-b1657.jar',
                            'spigot-1.7.9.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.7.9-R0.2-SNAPSHOT.jar',
                            'spigot-1.7.8.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.7.8-R0.1-SNAPSHOT.jar',
                            'spigot-1.7.5.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.7.5-R0.1-SNAPSHOT-1387.jar',
                            'spigot-1.7.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.7.2-R0.4-SNAPSHOT-1339.jar',
                            'spigot-1.6.4.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.6.4-R2.1-SNAPSHOT.jar',
                            'spigot-1.6.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.6.2-R1.1-SNAPSHOT.jar',
                            'spigot-1.5.2.jar': 'https://cdn.getbukkit.org/spigot/spigot-1.5.2-R1.1-SNAPSHOT.jar'},
    'vanila': {}}
Storage.init_logger()
Storage.logger.info('JarFetcher starting')
Storage.logger.info('Getting CraftBukkit links')
# Using hardcoded values for easier dev
# all_links['craftbukkit'].update(CraftBukkitProvider.get())
# all_links['spigot'].update(SpigotProvider.get())
# all_links['vanila'].update(VanillaProvider.get())

Storage.logger.debug(all_links)
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = []
    for jar_type in all_links:
        Storage.logger.info(f'Downloading {jar_type} jars')
        for jar_name in all_links[jar_type]:
            jar_link = all_links[jar_type][jar_name]
            jar_version = jar_name.split('-')[1].replace('.jar', '')
            Storage.logger.debug(f'{jar_name} ({jar_version}): {jar_link}')
            results.append(executor.submit(downloader.download, jar_type, jar_version, jar_link))
Storage.logger.info('Generating configs')
for stage in os.listdir('jar'):
    for jar_type in os.listdir(f'jar/{stage}'):
        Storage.logger.info(f'Generating configs for {stage} -> {jar_type}')
        for jar_name in os.listdir(f'jar/{stage}/{jar_type}'):
            if jar_name.startswith('.') or os.path.isdir(f'jar/{stage}/{jar_type}/{jar_name}'):
                continue
            Storage.logger.info(f'Generating configs for {jar_name}')
            jar_version = jar_name.split('-')[1].replace('.jar', '')
            conf_generator.generate(jar_type, jar_version, stage)
