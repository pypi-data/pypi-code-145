from __future__ import annotations

from typing import Annotated, Optional, Union

from pydantic import BaseModel, Field


class IntervalLeaf(BaseModel):
    __root__: Annotated[int, Field(ge=0, le=65535)]


class IntervalCase(BaseModel):
    interval: Annotated[IntervalLeaf, Field(alias="interfaces:interval")] = 30


class DailyLeaf(BaseModel):
    __root__: str = ""


class TimeOfDayLeaf(BaseModel):
    __root__: str


class DailyCase(BaseModel):
    daily: Annotated[Optional[DailyLeaf], Field(alias="interfaces:daily")] = None
    time_of_day: Annotated[TimeOfDayLeaf, Field(alias="interfaces:time-of-day")] = "1am"


class ManualLeaf(BaseModel):
    __root__: str = ""


class ManualCase(BaseModel):
    manual: Annotated[Optional[ManualLeaf], Field(alias="interfaces:manual")] = None


class Model(BaseModel):
    """
    Initialize an instance of this class and serialize it to JSON; this results in a RESTCONF payload.

    ## Tips
    Initialization:
    - all values have to be set via keyword arguments
    - if a class contains only a `__root__` field, it can be initialized as follows:
        - `member=MyNode(__root__=<value>)`
        - `member=<value>`

    Serialziation:
    - use `exclude_defaults=True` to
    - use `by_alias=True` to ensure qualified names are used ()
    """

    how: Annotated[
        Optional[Union[IntervalCase, DailyCase, ManualCase]],
        Field(alias="interfaces:how"),
    ] = None


from pydantic import BaseConfig, Extra

BaseConfig.allow_population_by_field_name = True
BaseConfig.smart_union = True  # See Pydantic issue#2135 / pull#2092
BaseConfig.extra = Extra.forbid


if __name__ == "__main__":
    model = Model(
        # <Initialize model here>
    )

    restconf_payload = model.json(exclude_defaults=True, by_alias=True)

    print(f"Generated output: {restconf_payload}")

    # Send config to network device:
    # from pydantify.utility import restconf_patch_request
    # restconf_patch_request(url='...', user_pw_auth=('usr', 'pw'), data=restconf_payload)
