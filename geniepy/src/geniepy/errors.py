"""Geniepy Errors Module."""


class GeniePyError(Exception):
    """General GeniePy error, all other geniepy errors inherits from GeniePyError."""


class SchemaError(GeniePyError):
    """Invalid database schema."""


class ConnectionError(GeniePyError):
    """Unable to connect."""


class DaoError(GeniePyError):
    """Data Access Object Error."""


class ParserError(GeniePyError):
    """Unable to parse data."""


class ClassifierError(GeniePyError):
    """Classifier unable to execute command."""


class ConfigError(GeniePyError):
    """Configuration error."""
