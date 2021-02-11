""" Route docstrings go here. """


class Default:
    """
    This setting maps database aliases, which are a way to refer to a specific database throughout Django,
    to a dictionary of settings for that specific connection. The settings in the inner dictionaries are
    described fully in the DATABASES documentation.
    """

    def db_for_read(self, model, **hints):
        """Suggest the database that should be used for read operations for objects of type model."""
        if model._meta.app_label in ["osm"]:
            return "osm"
        return None

    def db_for_write(self, model, **hints):
        """Suggest the database that should be used for writes of objects of type Model."""
        if model._meta.app_label in ["osm"]:
            return "osm"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Return True if a relation between obj1 and obj2 should be allowed, False if the relation should be prevented,
        or None if the router has no opinion. This is purely a validation operation, used by foreign key and
        many to many operations to determine if a relation should be allowed between two objects.
        """
        if obj1._meta.app_label in ["osm"] or obj2._meta.app_label == ["osm"]:
            return False
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Determine if the migration operation is allowed to run on the database with alias db. Return True
        if the operation should run, False if it shouldn’t run, or None if the router has no opinion.
        """
        if app_label in ["osm"]:
            return db == "osm"
        return None
