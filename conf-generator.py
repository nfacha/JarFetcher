def generate(type: str, version: str, stage: str):
    import Storage
    import os
    Storage.logger.debug(f'Generating config for {stage} {type} version {version}')
    if not os.path.isfile(f'conf/{stage}/{type}/{type}-{version}.jar.conf'):
        Storage.logger.info(f'{stage} - Generating {type} ({version})')
    else:
        Storage.logger.info(f'{stage} - {type}-{version}.jar.conf already exists on disk, skipping')
