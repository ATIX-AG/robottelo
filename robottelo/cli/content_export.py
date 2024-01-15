"""
Usage::

    hammer content-export [OPTIONS] SUBCOMMAND [ARG] ...

Parameters::

    SUBCOMMAND                    subcommand
    [ARG] ...                     subcommand arguments

Subcommands::

    complete                      Prepare content for a full export to a disconnected Katello
    generate-metadata             Writes export metadata to disk for use by the importing Katello.
                                  This command only needs to be used if the export was performed
                                  asynchronously or if the metadata was lost
    incremental                   Prepare content for an incremental export to a disconnected
                                  Katello
    list                          View content view export histories

"""
from robottelo.cli.base import Base


class ContentExport(Base):
    """
    Exports content from satellite
    """

    command_base = 'content-export'
    command_requires_org = True

    @classmethod
    def list(cls, options=None, output_format='json'):
        """
        List previous exports
        """
        cls.command_sub = 'list'
        return cls.execute(cls._construct_command(options), output_format=output_format)

    @classmethod
    def completeLibrary(cls, options, output_format='json', timeout=None):
        """
        Make full library export
        """
        cls.command_sub = 'complete library'
        return cls.execute(
            cls._construct_command(options), output_format=output_format, timeout=timeout
        )

    @classmethod
    def completeRepository(cls, options, output_format='json', timeout=None):
        """
        Make full repository export
        """
        cls.command_sub = 'complete repository'
        return cls.execute(
            cls._construct_command(options), output_format=output_format, timeout=timeout
        )

    @classmethod
    def completeVersion(cls, options, output_format='json', timeout=None):
        """
        Make full CV version export
        """
        cls.command_sub = 'complete version'
        return cls.execute(
            cls._construct_command(options), output_format=output_format, timeout=timeout
        )

    @classmethod
    def incrementalLibrary(cls, options, output_format='json', timeout=None):
        """
        Make incremental library export
        """
        cls.command_sub = 'incremental library'
        return cls.execute(
            cls._construct_command(options), output_format=output_format, timeout=timeout
        )

    @classmethod
    def incrementalRepository(cls, options, output_format='json', timeout=None):
        """
        Make incremental repository export
        """
        cls.command_sub = 'incremental repository'
        return cls.execute(
            cls._construct_command(options), output_format=output_format, timeout=timeout
        )

    @classmethod
    def incrementalVersion(cls, options, output_format='json', timeout=None):
        """
        Make incremental CV version export
        """
        cls.command_sub = 'incremental version'
        return cls.execute(
            cls._construct_command(options), output_format=output_format, timeout=timeout
        )

    @classmethod
    def generateMetadata(cls, options, output_format='json'):
        """
        Generates export metadata
        """
        cls.command_sub = 'generate-metadata'
        return cls.execute(cls._construct_command(options), output_format=output_format)
