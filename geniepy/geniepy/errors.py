"""Geniepy Errors Module."""


class GeniePyError(Exception):
    """General GeniePy error, all other geniepy errors inherits from GeniePyError."""


class SchemaError(GeniePyError):
    """Invalid database schema."""


class DaoError(GeniePyError):
    """Data Access Object Error."""


class ParserError(GeniePyError):
    """Unable to parse data."""
