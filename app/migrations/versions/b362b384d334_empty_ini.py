"""Empty ini

Revision ID: b362b384d334
Revises: 27f388307cb0
Create Date: 2025-05-26 15:26:42.068033

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b362b384d334'
down_revision: Union[str, None] = '27f388307cb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
