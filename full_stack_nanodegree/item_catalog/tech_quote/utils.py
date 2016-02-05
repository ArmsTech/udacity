"""Utilities for TQ application."""

from functools import wraps

from flask import render_template, request


def with_template(template=None):
    """Decorate function with render_template functionality.

    Args:
        template (Optional[str]): Template name to render if different than
            default. Default is None.

    Returns:
        func: A function for rendering a Flask template.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = request.endpoint \
                    .replace('.', '/') + '.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator
