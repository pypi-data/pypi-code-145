import pytest

import pandas as pd
import timely_beliefs as tb

from flexmeasures.cli.tests.utils import to_flags
from flexmeasures.data.models.time_series import Sensor, TimedBelief
from flexmeasures.cli.tests.utils import get_click_commands


@pytest.mark.skip
def test_add_one_sensor_attribute(app, db, setup_markets):
    from flexmeasures.cli.data_edit import edit_attribute

    # Load sensor from database and count attributes
    sensor = Sensor.query.filter(Sensor.name == "epex_da").one_or_none()
    n_attributes_before = len(sensor.attributes)

    cli_input = {
        "sensor-id": sensor.id,
        "attribute": "some new attribute",
        "float": 3,
    }
    runner = app.test_cli_runner()
    result = runner.invoke(edit_attribute, to_flags(cli_input))
    assert result.exit_code == 0 and "Success" in result.output, result.exception

    # Reload sensor from database and count attributes
    sensor = Sensor.query.filter(Sensor.name == "epex_da").one_or_none()
    n_attributes_after = len(sensor.attributes)

    assert n_attributes_after == n_attributes_before + 1


@pytest.mark.skip_github
@pytest.mark.parametrize(
    "event_starts_after, event_ends_before",
    (
        ["", ""],
        ["2021-03-28 15:00:00+00:00", "2021-03-28 16:00:00+00:00"],
    ),
)
def test_resample_sensor_data(
    app, db, setup_beliefs, event_starts_after: str, event_ends_before: str
):
    """Check resampling market data from hourly to 30 minute resolution and back."""

    from flexmeasures.cli.data_edit import resample_sensor_data

    sensor = Sensor.query.filter(Sensor.name == "epex_da").one_or_none()
    event_starts_after = pd.Timestamp(event_starts_after)
    event_ends_before = pd.Timestamp(event_ends_before)
    beliefs_before = sensor.search_beliefs(
        most_recent_beliefs_only=False,
        event_starts_after=event_starts_after,
        event_ends_before=event_ends_before,
    )

    # Check whether fixtures have flushed
    assert sensor.id is not None

    # Check whether we have all desired beliefs
    query = TimedBelief.query.filter(TimedBelief.sensor_id == sensor.id)
    if not pd.isnull(event_starts_after):
        query = query.filter(TimedBelief.event_start >= event_starts_after)
    if not pd.isnull(event_ends_before):
        query = query.filter(
            TimedBelief.event_start + sensor.event_resolution <= event_ends_before
        )
    all_beliefs_for_given_sensor = query.all()
    pd.testing.assert_frame_equal(
        tb.BeliefsDataFrame(all_beliefs_for_given_sensor), beliefs_before
    )

    cli_input = {
        "sensor-id": sensor.id,
        "event-resolution": sensor.event_resolution.seconds / 60 / 2,
    }
    runner = app.test_cli_runner()
    result = runner.invoke(
        resample_sensor_data, to_flags(cli_input) + ["--skip-integrity-check"]
    )

    # Check result for success
    assert "Successfully resampled" in result.output

    # Check that we now have twice as much data for this sensor
    sensor = Sensor.query.filter(Sensor.name == "epex_da").one_or_none()
    beliefs_after = sensor.search_beliefs(
        most_recent_beliefs_only=False,
        event_starts_after=event_starts_after,
        event_ends_before=event_ends_before,
    )
    assert len(beliefs_after) == 2 * len(beliefs_before)

    # Checksum
    assert beliefs_after["event_value"].sum() == 2 * beliefs_before["event_value"].sum()

    # Resample back to original resolution (on behalf of the next test case)
    cli_input["event-resolution"] = sensor.event_resolution.seconds / 60
    result = runner.invoke(
        resample_sensor_data, to_flags(cli_input) + ["--skip-integrity-check"]
    )
    assert "Successfully resampled" in result.output


def test_cli_help(app):
    """Test that showing help does not throw an error."""
    from flexmeasures.cli import data_edit

    runner = app.test_cli_runner()
    for cmd in get_click_commands(data_edit):
        result = runner.invoke(cmd, ["--help"])
        assert result.exit_code == 0
        assert "Usage" in result.output
