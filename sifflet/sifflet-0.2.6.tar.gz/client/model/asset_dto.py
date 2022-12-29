"""
    Sifflet Backend API

    Requirements: <br>    - [Create your access token through the UI](https://docs.siffletdata.com/docs/generate-an-api-token#create-an-api-token) <br>    - Get your tenant name: if you access to Sifflet with `https://abcdef.siffletdata.com`, then your tenant would be `abcdef`  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from client.exceptions import ApiAttributeError


def lazy_import():
    from client.model.asset_usage_dto import AssetUsageDto
    from client.model.tag_dto import TagDto
    globals()['AssetUsageDto'] = AssetUsageDto
    globals()['TagDto'] = TagDto


class AssetDto(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('entity_type',): {
            'DATASOURCE': "DATASOURCE",
            'DATASOURCE_INGESTION_RUN': "DATASOURCE_INGESTION_RUN",
            'DATASET': "DATASET",
            'DASHBOARD': "DASHBOARD",
            'CHART': "CHART",
            'COLLECTION': "COLLECTION",
            'DATASET_FIELD': "DATASET_FIELD",
            'DAG': "DAG",
            'RULE_RUN': "RULE_RUN",
            'INCIDENT': "INCIDENT",
            'USER': "USER",
            'ACCESS_TOKEN': "ACCESS_TOKEN",
            'SIFFLET_RULE': "SIFFLET_RULE",
            'CONFIG': "CONFIG",
            'TAG': "TAG",
        },
        ('displayed_type_enum',): {
            'TABLE': "TABLE",
            'EXTERNAL_TABLE': "EXTERNAL_TABLE",
            'VIEW': "VIEW",
            'MATERIALIZED_VIEW': "MATERIALIZED_VIEW",
            'DASHBOARD': "DASHBOARD",
            'MODEL': "MODEL",
            'DAG': "DAG",
            'NONE': "NONE",
        },
        ('quality_status',): {
            'CRITICAL': "CRITICAL",
            'AT_RISK': "AT_RISK",
            'HEALTHY': "HEALTHY",
            'UNMONITORED': "UNMONITORED",
            'NOT_SUPPORTED': "NOT_SUPPORTED",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'urn': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'created_date': (int,),  # noqa: E501
            'last_modified_date': (int,),  # noqa: E501
            'created_by': (str,),  # noqa: E501
            'modified_by': (str,),  # noqa: E501
            'entity_type': (str,),  # noqa: E501
            'displayed_type': (str,),  # noqa: E501
            'displayed_type_enum': (str,),  # noqa: E501
            'quality_status': (str,),  # noqa: E501
            'usage': (AssetUsageDto,),  # noqa: E501
            'source_id': (str,),  # noqa: E501
            'external_link': (str,),  # noqa: E501
            'datasource_id': (str,),  # noqa: E501
            'datasource_name': (str,),  # noqa: E501
            'datasource_type': (str,),  # noqa: E501
            'tags': ([TagDto],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'urn': 'urn',  # noqa: E501
        'name': 'name',  # noqa: E501
        'created_date': 'createdDate',  # noqa: E501
        'last_modified_date': 'lastModifiedDate',  # noqa: E501
        'created_by': 'createdBy',  # noqa: E501
        'modified_by': 'modifiedBy',  # noqa: E501
        'entity_type': 'entityType',  # noqa: E501
        'displayed_type': 'displayedType',  # noqa: E501
        'displayed_type_enum': 'displayedTypeEnum',  # noqa: E501
        'quality_status': 'qualityStatus',  # noqa: E501
        'usage': 'usage',  # noqa: E501
        'source_id': 'sourceId',  # noqa: E501
        'external_link': 'externalLink',  # noqa: E501
        'datasource_id': 'datasourceId',  # noqa: E501
        'datasource_name': 'datasourceName',  # noqa: E501
        'datasource_type': 'datasourceType',  # noqa: E501
        'tags': 'tags',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, id, urn, name, *args, **kwargs):  # noqa: E501
        """AssetDto - a model defined in OpenAPI

        Args:
            id (str):
            urn (str):
            name (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created_date (int): [optional]  # noqa: E501
            last_modified_date (int): [optional]  # noqa: E501
            created_by (str): [optional]  # noqa: E501
            modified_by (str): [optional]  # noqa: E501
            entity_type (str): [optional]  # noqa: E501
            displayed_type (str): [optional]  # noqa: E501
            displayed_type_enum (str): [optional]  # noqa: E501
            quality_status (str): [optional]  # noqa: E501
            usage (AssetUsageDto): [optional]  # noqa: E501
            source_id (str): [optional]  # noqa: E501
            external_link (str): [optional]  # noqa: E501
            datasource_id (str): [optional]  # noqa: E501
            datasource_name (str): [optional]  # noqa: E501
            datasource_type (str): [optional]  # noqa: E501
            tags ([TagDto]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.urn = urn
        self.name = name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, id, urn, name, *args, **kwargs):  # noqa: E501
        """AssetDto - a model defined in OpenAPI

        Args:
            id (str):
            urn (str):
            name (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            created_date (int): [optional]  # noqa: E501
            last_modified_date (int): [optional]  # noqa: E501
            created_by (str): [optional]  # noqa: E501
            modified_by (str): [optional]  # noqa: E501
            entity_type (str): [optional]  # noqa: E501
            displayed_type (str): [optional]  # noqa: E501
            displayed_type_enum (str): [optional]  # noqa: E501
            quality_status (str): [optional]  # noqa: E501
            usage (AssetUsageDto): [optional]  # noqa: E501
            source_id (str): [optional]  # noqa: E501
            external_link (str): [optional]  # noqa: E501
            datasource_id (str): [optional]  # noqa: E501
            datasource_name (str): [optional]  # noqa: E501
            datasource_type (str): [optional]  # noqa: E501
            tags ([TagDto]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.id = id
        self.urn = urn
        self.name = name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
