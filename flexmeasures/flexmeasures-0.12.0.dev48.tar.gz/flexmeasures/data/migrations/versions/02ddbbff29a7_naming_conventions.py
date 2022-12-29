"""naming_conventions

Revision ID: 02ddbbff29a7
Revises: b797328ac32d
Create Date: 2020-09-17 11:05:37.195404

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "02ddbbff29a7"
down_revision = "b797328ac32d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(
        op.f("weather_sensor_type_name_latitude_longitude_key"),
        "weather_sensor",
        ["weather_sensor_type_name", "latitude", "longitude"],
    )
    op.drop_constraint(op.f("_type_name_location_unique"), table_name="weather_sensor")

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("asset_type_can_curtail_idx"), "asset_type", ["can_curtail"], unique=False
    )
    op.create_index(
        op.f("asset_type_can_shift_idx"), "asset_type", ["can_shift"], unique=False
    )
    op.drop_index("ix_asset_type_can_curtail", table_name="asset_type")
    op.drop_index("ix_asset_type_can_shift", table_name="asset_type")
    # ### end Alembic commands ###


def downgrade():

    op.drop_constraint(
        op.f("weather_sensor_type_name_latitude_longitude_key"),
        table_name="weather_sensor",
    )
    op.create_unique_constraint(
        op.f("_type_name_location_unique"),
        "weather_sensor",
        ["weather_sensor_type_name", "latitude", "longitude"],
    )

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "ix_asset_type_can_shift", "asset_type", ["can_shift"], unique=False
    )
    op.create_index(
        "ix_asset_type_can_curtail", "asset_type", ["can_curtail"], unique=False
    )
    op.drop_index(op.f("asset_type_can_shift_idx"), table_name="asset_type")
    op.drop_index(op.f("asset_type_can_curtail_idx"), table_name="asset_type")
    # ### end Alembic commands ###
