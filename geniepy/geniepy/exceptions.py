"""Geniepy Exceptions Classes."""


class GeniePyError(Exception):
    """General GeniePy error, all other geniepy errors inherits from GeniePyError."""


class SchemaError(GeniePyError):
    """Invalid database schema."""
