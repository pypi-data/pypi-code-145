"""add event_resolution field to Asset, Market & WeatherSennsor

Revision ID: bddc5e9f72a3
Revises: 02ddbbff29a7
Create Date: 2020-10-07 14:12:45.761789

"""
from alembic import op
import sqlalchemy as sa

from datetime import timedelta


# revision identifiers, used by Alembic.
revision = "bddc5e9f72a3"
down_revision = "02ddbbff29a7"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "asset",
        sa.Column(
            "event_resolution",
            sa.Interval(),
            nullable=False,
            server_default=str(timedelta(minutes=0)),
        ),
    )
    op.add_column(
        "market",
        sa.Column(
            "event_resolution",
            sa.Interval(),
            nullable=False,
            server_default=str(timedelta(minutes=0)),
        ),
    )
    op.add_column(
        "weather_sensor",
        sa.Column(
            "event_resolution",
            sa.Interval(),
            nullable=False,
            server_default=str(timedelta(minutes=0)),
        ),
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("weather_sensor", "event_resolution")
    op.drop_column("market", "event_resolution")
    op.drop_column("asset", "event_resolution")
    # ### end Alembic commands ###
