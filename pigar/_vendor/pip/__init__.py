from typing import List, Optional

__version__ = "22.3.1"


def main(args: Optional[List[str]] = None) -> int:
    """This is an internal API only meant for use by pip's own console scripts.

    For additional details, see https://github.com/pypa/pip/issues/7498.
    """
    from pigar._vendor.pip._internal.utils.entrypoints import _wrapper

    return _wrapper(args)
