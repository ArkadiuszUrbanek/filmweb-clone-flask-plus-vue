from urllib.parse import urlparse

def same_origin(current_uri, compare_uri):
    current = urlparse(current_uri)
    compare = urlparse(compare_uri)

    return (
        current.scheme == compare.scheme
        and current.hostname == compare.hostname
        and current.port == compare.port
    )