"""Define Model for tech_quote database."""

from tech_quote.extensions import db

Column = db.Column


class CRUDMixin(object):

    """Add convenience methods for CRUD operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update."""
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def delete(self, commit=True):
        """Delete."""
        db.session.delete(self)
        return commit and db.session.commit()

    def save(self, commit=True):
        """Commit (save) if requested."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self


class Model(CRUDMixin, db.Model):

    """Base db.Model class with a CRUD mixin."""

    __abstract__ = True
