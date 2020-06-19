import uuid


def get_file_path(instance, filename: str) -> str:
    """Sets path for all loaded files"""
    return f'{instance.__class__.__name__.lower()}/{uuid.uuid4().hex}_{filename}'
