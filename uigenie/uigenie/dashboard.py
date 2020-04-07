"""Flask app dashboard page."""
from flask import Blueprint

BLUEPRINT = Blueprint('blog', __name__)


@bp.route('/')
def index():
    """Show genie dashboard page."""
    return 'New Dashboard'
