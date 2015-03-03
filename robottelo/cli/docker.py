# -*- encoding: utf-8 -*-

"""Docker related hammer commands"""

from robottelo.cli.base import Base


class DockerContainer(Base):
    """Manipulates Docker containers

    Usage::

        hammer docker container [OPTIONS] SUBCOMMAND [ARG] ...

    Parameters::

        SUBCOMMAND                    subcommand
        [ARG] ...                     subcommand arguments

    Subcommands::

        create                        Create a container
        delete                        Delete a container
        info                          Show a container
        list                          List all containers
        logs                          Show container logs
        start                         Power a container on
        status                        Run power operation on a container
        stop                          Power a container off

    """
    command_base = 'docker image'

    @classmethod
    def create(cls, options=None):
        """Creates a docker container

        Usage::

            hammer docker container create [OPTIONS]

        Options::

            --attach-stderr ATTACH_STDERR             One of true/false,
                                                      yes/no, 1/0.
            --attach-stdin ATTACH_STDIN               One of true/false,
                                                      yes/no, 1/0.
            --attach-stdout ATTACH_STDOUT             One of true/false,
                                                      yes/no, 1/0.
            --cmd CMD
            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --cpu-sets CPU_SETS
            --cpu-shares CPU_SHARES
            --entrypoint ENTRYPOINT
            --image IMAGE                             Image to use to create
                                                      the container. Format
                                                      should be repository:tag,
                                                      e.g: centos:7
            --katello KATELLO                         One of true/false,
                                                      yes/no, 1/0.
            --location-ids LOCATION_IDS               REPLACE locations with
                                                      given ids. Comma
                                                      separated list of values.
            --locations LOCATION_NAMES                Comma separated list of
                                                      values.
            --memory MEMORY
            --name NAME
            --organization-ids ORGANIZATION_IDS       REPLACE organizations
                                                      with given ids. Comma
                                                      separated list of values.
            --organizations ORGANIZATION_NAMES        Comma separated list of
                                                      values.
            --registry-id REGISTRY_ID                 Registry this container
                                                      will have to use to get
                                                      the image
            --tty TTY                                 One of true/false,
                                                      yes/no, 1/0.

        """
        return super(DockerContainer, cls).create(options)

    @classmethod
    def delete(cls, options=None):
        """Deletes a docker container

        Usage::

            hammer docker container delete [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        return super(DockerContainer, cls).delete(options)

    @classmethod
    def info(cls, options=None):
        """Gets information about a docker container

        Usage::

            hammer docker container info [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        return super(DockerContainer, cls).info(options)

    @classmethod
    def list(cls, options=None):
        """Lists docker containers

        Usage::

            hammer docker container list [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --page PAGE                               paginate results
            --per-page PER_PAGE                       number of entries per
                                                      request

        """
        return super(DockerContainer, cls).list(options)

    @classmethod
    def logs(cls, options=None):
        """Reads container logs

        Usage::

            hammer docker container logs [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by
            --stderr STDERR                           One of true/false,
                                                      yes/no, 1/0.
            --stdout STDOUT                           One of true/false,
                                                      yes/no, 1/0.
            --tail TAIL                               Number of lines to tail.
                                                      Default: 100

        """
        cls.command_sub = 'logs'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def start(cls, options=None):
        """Starts a docker container

        Usage::

            hammer docker container start [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        cls.command_sub = 'start'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def status(cls, options=None):
        """Gets the running status of a docker container

        Usage::

            hammer docker container status [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        cls.command_sub = 'status'
        return cls.execute(cls._construct_command(options))

    @classmethod
    def stop(cls, options=None):
        """Stops a docker container

        Usage::

            hammer docker container stop [OPTIONS]

        Options::

            --compute-resource COMPUTE_RESOURCE_NAME  Compute resource name
            --compute-resource-id COMPUTE_RESOURCE_ID
            --id ID
            --name NAME                               Name to search by

        """
        cls.command_sub = 'stop'
        return cls.execute(cls._construct_command(options))


class DockerImage(Base):
    """Manipulates Docker images

    Usage::

        hammer docker image [OPTIONS] SUBCOMMAND [ARG] ...

    Parameters::

        SUBCOMMAND                    subcommand
        [ARG] ...                     subcommand arguments

    Subcommands::

        info                          Show a docker image
        list                          List docker_images

    """
    command_base = 'docker image'

    @classmethod
    def info(cls, options=None):
        """Gets information about docker images

        Usage::

            hammer docker image info [OPTIONS]

        Options::

            --id ID                       a docker image identifier
            --name NAME                   Name to search by
            --repository REPOSITORY_NAME  Repository name to search by
            --repository-id REPOSITORY_ID repository ID

        """
        return super(DockerImage, cls).info(options)

    @classmethod
    def list(cls, options=None, per_page=True):
        """List docker images

        Usage::

            hammer docker image list [OPTIONS]

        Options::

            --content-view CONTENT_VIEW_NAME                    Content view
                                                                name
            --content-view-filter CONTENT_VIEW_FILTER_NAME      Name to search
                                                                by
            --content-view-filter-id CONTENT_VIEW_FILTER_ID     filter
                                                                identifier
            --content-view-id CONTENT_VIEW_ID                   content view
                                                                numeric
                                                                identifier
            --content-view-version CONTENT_VIEW_VERSION_VERSION Content view
                                                                version number
            --content-view-version-id CONTENT_VIEW_VERSION_ID   Content view
                                                                version
                                                                identifier
            --environment ENVIRONMENT_NAME                      Name to search
                                                                by
            --environment-id ENVIRONMENT_ID
            --organization ORGANIZATION_NAME                    Organization
                                                                name to search
                                                                by
            --organization-id ORGANIZATION_ID                   organization ID
            --organization-label ORGANIZATION_LABEL             Organization
                                                                label to search
                                                                by
            --product PRODUCT_NAME                              Product name to
                                                                search by
            --product-id PRODUCT_ID                             product numeric
                                                                identifier
            --repository REPOSITORY_NAME                        Repository name
                                                                to search by
            --repository-id REPOSITORY_ID                       repository ID

        """
        return super(DockerImage, cls).list(options, per_page)


class DockerTag(Base):
    """Manipulates Docker tags

    Usage::

        hammer docker tag [OPTIONS] SUBCOMMAND [ARG] ...

    Parameters::

        SUBCOMMAND                    subcommand
        [ARG] ...                     subcommand arguments

    Subcommands::

        info                          Show a docker tag
        list                          List docker_tags

    """
    command_base = 'docker tag'

    @classmethod
    def info(cls, options=None):
        """Gets information about docker tags

        Usage::

            hammer docker tag info [OPTIONS]

        Options::

            --id ID                       a docker tag identifier
            --name NAME                   Name to search by
            --repository REPOSITORY_NAME  Repository name to search by
            --repository-id REPOSITORY_ID repository ID

        """
        return super(DockerTag, cls).info(options)

    @classmethod
    def list(cls, options=None, per_page=True):
        """List docker tags

        Usage::

            hammer docker tag list [OPTIONS]

        Options::

            --content-view CONTENT_VIEW_NAME                    Content view
                                                                name
            --content-view-filter CONTENT_VIEW_FILTER_NAME      Name to search
                                                                by
            --content-view-filter-id CONTENT_VIEW_FILTER_ID     filter
                                                                identifier
            --content-view-id CONTENT_VIEW_ID                   content view
                                                                numeric
                                                                identifier
            --content-view-version CONTENT_VIEW_VERSION_VERSION Content view
                                                                version number
            --content-view-version-id CONTENT_VIEW_VERSION_ID   Content view
                                                                version
                                                                identifier
            --environment ENVIRONMENT_NAME                      Name to search
                                                                by
            --environment-id ENVIRONMENT_ID
            --organization ORGANIZATION_NAME                    Organization
                                                                name to search
                                                                by
            --organization-id ORGANIZATION_ID                   organization ID
            --organization-label ORGANIZATION_LABEL             Organization
                                                                label to search
                                                                by
            --product PRODUCT_NAME                              Product name to
                                                                search by
            --product-id PRODUCT_ID                             product numeric
                                                                identifier
            --repository REPOSITORY_NAME                        Repository name
                                                                to search by
            --repository-id REPOSITORY_ID                       repository ID

        """
        return super(DockerTag, cls).list(options, per_page)


class Docker(Base):
    """Manipulates Docker images and tags

    Usage::

        hammer docker [OPTIONS] SUBCOMMAND [ARG] ...

    Parameters::

        SUBCOMMAND                    subcommand
        [ARG] ...                     subcommand arguments

    Subcommands::

        container                     Manage docker containers
        image                         Manage docker images
        tag                           Manage docker tags

    """
    command_base = 'docker'

    # Shortcuts to docker subcommands. Instead of importing each subcommand
    # class, import the Docker class and use it like this: Docker.image.list()
    container = DockerContainer
    image = DockerImage
    tag = DockerTag
