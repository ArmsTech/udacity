"""Define Model for tech_quote database."""

from tech_quote.extensions import db

Column = db.Column


class CRUDMixin(object):

    """Add convenience methods for CRUD operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create an instance of class `cls` (a model).

        Args:
            **kwargs: Keyword arguments for creating a model instance.

        Returns:
            object: An instance of class `cls` (a model).
        """
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update an instance of a model.

        Args:
            commit (Optional[bool]): Whether to commit changes.
                Default is True.
            **kwargs: Keyword arguments for updating an instance.

        Returns:
            object: Updated model goes back to caller.
        """
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def delete(self, commit=True):
        """Delete an instance of a model.

        Args:
            commit (Optional[bool]): Whether to commit changes.
                Default is True.

        Returns:
            bool: Whether delete was committed successfully.
        """
        db.session.delete(self)
        return commit and db.session.commit()

    def save(self, commit=True):
        """Save an instance of a model.

        Args:
            commit (Optional[bool]): Whether to commit changes.
                Default is True.

        Returns:
            object: Model goes back to caller after commit.
        """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self


class Model(CRUDMixin, db.Model):

    """Base db.Model class with a CRUD mixin."""

    __abstract__ = True
