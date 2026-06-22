class EntityNormalizer:

    """
    Normalizes duplicate entities.

    Example:

    Obama
        ->
    Barack Obama

    the University of Mumbai
        ->
    University of Mumbai
    """

    def normalize(self,entities):
        normalized = {}

        for entity_type, values in (entities.items()):
            normalized[entity_type] = self._normalize_group(values)
        return normalized

    def _normalize_group(self, values):
        result = []

        values = sorted(values, key=len, reverse=True)
        for candidate in values:
            duplicate = False
            for existing in result:
                if (candidate.lower() == existing.lower()):
                    duplicate = True

                    break

            if not duplicate:
                result.append(candidate)

        return sorted(result)