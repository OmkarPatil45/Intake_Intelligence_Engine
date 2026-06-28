"""
Common helper functions used by the
Universal Intelligence Validation Framework.
"""


def safe_get(data: dict, path: str, default=None):

    current = data

    for key in path.split("."):

        if (
            not isinstance(current, dict)
            or key not in current
        ):
            return default

        current = current[key]

    return current


# -----------------------------------------------------


def count_entities(entities: dict) -> int:
    """
    Count total extracted entities.
    """

    if not isinstance(entities,dict):
        return 0

    count = 0

    for values in entities.values():

        if isinstance(values,list):
            count += len(values)

    return count


# -----------------------------------------------------


def is_empty(value) -> bool:
    """
    Generic empty value detector.
    """

    return value in (None,"",[],{})


# -----------------------------------------------------


def has_duplicates(values: list) -> bool:
    """
    Check duplicate values.
    """

    if not isinstance(values,list):
        return False

    return len(values) != len(set(values))