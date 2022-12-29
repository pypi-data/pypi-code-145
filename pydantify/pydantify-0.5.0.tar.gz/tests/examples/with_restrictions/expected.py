from __future__ import annotations

from typing import Annotated, Optional

from pydantic import BaseModel, Field


class NameLeaf(BaseModel):
    __root__: str
    """
    Interface name. Example value: GigabitEthernet 0/0/0
    """


class ComplexAddressLeaf(BaseModel):
    __root__: Annotated[str, Field(regex="^(?=^(\\d{1,3}\\.){3}\\d{1,3}$).*$")]
    """
    Interface IP address. Example value: 10.10.10.1
    """


class ComplexPortLeaf(BaseModel):
    __root__: Annotated[int, Field(ge=1, le=65535)]
    """
    Port number. Example value: 8080
    """


class SimplePortLeaf(BaseModel):
    __root__: Annotated[int, Field(ge=1, le=65535)]
    """
    Port number. Example value: 8080
    """


class InterfacesContainer(BaseModel):
    """
    Just a simple example of a container.
    """

    name: Annotated[NameLeaf, Field(alias="interfaces:name")]
    """
    Interface name. Example value: GigabitEthernet 0/0/0
    """
    complex_address: Annotated[
        ComplexAddressLeaf, Field(alias="interfaces:complex-address")
    ]
    """
    Interface IP address. Example value: 10.10.10.1
    """
    complex_port: Annotated[ComplexPortLeaf, Field(alias="interfaces:complex-port")]
    """
    Port number. Example value: 8080
    """
    simple_port: Annotated[SimplePortLeaf, Field(alias="interfaces:simple-port")]
    """
    Port number. Example value: 8080
    """


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

    interfaces: Annotated[
        Optional[InterfacesContainer], Field(alias="interfaces:interfaces")
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
