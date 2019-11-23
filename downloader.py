def download(type: str, version: str, url: str):
    import Storage
    Storage.logger.debug(f'Downloading {type} version {version} from {url}')
