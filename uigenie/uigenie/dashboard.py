"""Flask app dashboard page."""
from flask import Blueprint, render_template

BP = Blueprint('blog', __name__)


@BP.route('/')
def index():
    """Show genie dashboard page."""
    return render_template('dashboard.html')
