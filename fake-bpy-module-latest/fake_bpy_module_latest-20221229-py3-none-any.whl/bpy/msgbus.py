import sys
import typing

GenericType = typing.TypeVar("GenericType")


def clear_by_owner(owner):
    ''' Clear all subscribers using this owner.

    '''

    pass


def publish_rna(key: typing.Any):
    ''' Notify subscribers of changes to this property (this typically doesn't need to be called explicitly since changes will automatically publish updates). In some cases it may be useful to publish changes explicitly using more general keys.

    :param key: Represents the type of data being subscribed to Arguments include - `bpy.types.Property` instance. - `bpy.types.Struct` type. - (`bpy.types.Struct`, str) type and property name.
    :type key: typing.Any
    '''

    pass


def subscribe_rna(key: typing.Any,
                  owner: typing.Any,
                  args,
                  notify,
                  options: typing.Set = 'set()'):
    ''' Register a message bus subscription. It will be cleared when another blend file is loaded, or can be cleared explicitly via :func:`bpy.msgbus.clear_by_owner`.

    :param key: Represents the type of data being subscribed to Arguments include - `bpy.types.Property` instance. - `bpy.types.Struct` type. - (`bpy.types.Struct`, str) type and property name.
    :type key: typing.Any
    :param owner: Handle for this subscription (compared by identity).
    :type owner: typing.Any
    :param options: Change the behavior of the subscriber. - ``PERSISTENT`` when set, the subscriber will be kept when remapping ID data.
    :type options: typing.Set
    '''

    pass
