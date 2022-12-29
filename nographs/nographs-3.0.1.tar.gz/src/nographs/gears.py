from __future__ import annotations
import collections
from collections.abc import (
    Iterable,
    MutableSequence,
)
from typing import (
    Protocol,
    Literal,
    Generic,
    Union,
    TypeVar,
    Tuple,
)
from abc import abstractmethod
from array import array
from itertools import repeat
from decimal import Decimal

from nographs import (
    # from types
    T_vertex,
    T_vertex_id,
    T_weight,
    T_labels,
)
from nographs import (
    # from gear_collections
    SequenceForGearProto,
    VertexSet,
    VertexMapping,
    VertexSetWrappingSequenceNoBitPacking,
    VertexSetWrappingSequenceBitPacking,
    VertexMappingWrappingSequenceWithoutNone,
    VertexMappingWrappingSequenceWithNone,
)


# With the following, for this module, tuple is replaced by typing.Tuple.
# (Reason: Error in Sphinx with correctly documenting tuple[T] in HTML.
#  In the meantime, this workaround is used. typing.Tuple is depreciated,
#  but still supported...)
U = TypeVar("U")
V = TypeVar("V")

tuple = Tuple[U, V]


# --- ABCs for the needed collection kinds for NoGraphs ---

# The following type aliases are not documented as part of the API documentation.
# In the API documentation, they are replaced by their respective definition.

"""
ABC for a collection that is intended to be used by NoGraphs for storing sets
of vertices represented by your chosen type of hashable vertex ids.

If a VertexIdSet is implemented by a
VertexSetByWrapper
class based on a wrapped sequence, NoGraphs directly accesses the sequence for
better performance.
If method index_and_bit_method of the VertexSetByWrapper returns a function
(not None), the set elements will be stored as bits in the sequence, see
VertexSetByWrapper.
"""
VertexIdSet = VertexSet[T_vertex_id]

"""
ABC for a collection that is intended to be used by NoGraphs for
storing mappings from your chosen type of hashable vertex ids to vertices
of your chosen data type.

If a VertexIdToVertexMapping is implemented by a
VertexMappingWrappingSequenceWithNone
class based on a wrapped sequence, NoGraphs directly accesses the sequence for
better performance.
(The sequence might need to represent gaps without stored values for some
key by None as artificial value. Thus, NoGraphs must be prepared to retrieve
None from the sequence, even if it cannot store this value in case it is
outside T_vertex. Therefore, here, VertexMappingWrappingSequenceWithNone is used.)
"""
VertexIdToVertexMapping = VertexMapping[T_vertex_id, T_vertex]

"""
ABC for a collection that is intended to be used by NoGraphs for
storing mappings from vertices, represented by your chosen type of hashable
vertex ids, to your chosen type of weights.

If a VertexIdToDistanceMapping is implemented by a
VertexMappingWrappingSequenceWithoutNone
class based on a wrapped sequence, NoGraphs directly accesses the sequence for
better performance.
"""
VertexIdToDistanceMapping = VertexMapping[T_vertex_id, T_weight]

"""ABC for a collection that is intended to be used by NoGraphs for
storing mappings from your chosen type of hashable vertex ids to edge data.

If a VertexIdToPathEdgeDataMapping is implemented by a
VertexMappingWrappingSequenceWithNone
class based on a wrapped sequence, NoGraphs directly accesses the sequence for
better performance.
(The sequence might need to represent gaps without stored values for some
key by None as artificial value. Thus, NoGraphs must be prepared to retrieve
None from the sequence, even if it cannot store this value because it is
outside type T_labels.Therefore, here,
VertexMappingWrappingSequenceWithNone is used.)
"""
VertexIdToPathEdgeDataMapping = VertexMapping[T_vertex_id, T_labels]


""" ABC for a MutableSequence of vertices.
"""
MutableSequenceOfVertices = MutableSequence[T_vertex]


# -- Gear protocols --


class GearWithoutDistances(Protocol[T_vertex, T_vertex_id, T_labels]):
    """Protocol for a feature-limited kind of gear that offer collections
    that can store vertices, vertex_ids and edge data, but no edge
    weights / distances.
    """

    @abstractmethod
    def vertex_id_set(
        self, initial_content: Iterable[T_vertex_id]
    ) -> VertexIdSet[T_vertex_id]:
        """Factory for a set of vertices.

        :param initial_content: The collection is created with this initial content.
        """
        raise NotImplementedError

    @abstractmethod
    def vertex_id_to_vertex_mapping(
        self, initial_content: Iterable[tuple[T_vertex_id, T_vertex]]
    ) -> VertexIdToVertexMapping[T_vertex_id, T_vertex]:
        """Factory for a mapping from a vertex id to a vertex.

        :param initial_content: The collection is created with this initial content.
        """
        raise NotImplementedError

    @abstractmethod
    def vertex_id_to_path_attributes_mapping(
        self, initial_content: Iterable[tuple[T_vertex_id, T_labels]]
    ) -> VertexIdToPathEdgeDataMapping[T_vertex_id, T_labels]:
        """Factory for a mapping from a vertex id to edge data.

        :param initial_content: The collection is created with this initial content.
        """
        raise NotImplementedError

    @abstractmethod
    def sequence_of_vertices(
        self, initial_content: Iterable[T_vertex]
    ) -> MutableSequenceOfVertices[T_vertex]:
        """Factory for a sequence of vertices."""
        raise NotImplementedError


class Gear(
    Generic[T_vertex, T_vertex_id, T_weight, T_labels],
    GearWithoutDistances[T_vertex, T_vertex_id, T_labels],
    Protocol,
):
    """Protocol for gears with collections that can store vertices,
    vertex_ids, edge data (like a GearWithoutDistances), and additionally,
    edge weights / distances.
    """

    @abstractmethod
    def zero(self) -> T_weight:
        """Return the zero value of T_weight, e.g., 0.0 for float.

        This needs to be a value of type T_weight, that is neutral element
        of the addition in T_weight, i.e., for any value v in T_weight,
        v + zero == v needs to hold.
        """
        raise NotImplementedError

    @abstractmethod
    def infinity(self) -> T_weight:
        """Return the positive infinity value of T_weight, e.g.,
        float("infinity") for float.

        This needs to be a value of type T_weight, that is larger than all
        values of T_weight, that can occur as weights of edges or as distances
        of vertices (sum of a set of edge weights).
        """
        raise NotImplementedError

    @abstractmethod
    def vertex_id_to_distance_mapping(
        self, initial_content: Iterable[tuple[T_vertex_id, T_weight]]
    ) -> VertexIdToDistanceMapping[T_vertex_id, T_weight]:
        """Factory for a mapping from a vertex id to a distance value.

        If the returned mapping does not contain a value for some key,
        its method __getitem__ needs to return a special default value that is
        guaranteed to be larger (w.r.t. object comparison) than any regular value that
        can be stored in the mapping.

        Example: You use *float* as T_weight, and *float("infinity")* as default value.

        :param initial_content: The collection is created with this initial content.
        """
        raise NotImplementedError


# --- Hashable vertex IDs (hashable vertices or vertex_to_id returns hashable ---


class DefaultdictWithNiceStr(collections.defaultdict[T_vertex_id, T_weight]):
    def __str__(self) -> str:
        return str(dict(self))


class GearForHashableVertexIDs(Gear[T_vertex, T_vertex_id, T_weight, T_labels]):
    """Factory methods for bookkeeping collections. For graphs with hashable vertices
    (or vertices made hashable by providing a `VertexToID` function to the traversal).

    Uses hash-based collections (e.g., set and dict) for storing data.

    :param zero: Value of type T_weight that is used to represent zero distance.

    :param inf: Value of type T_weight that is used to represent infinite distance
      (larger than any finite distance that might occur)
    """

    def __init__(self, zero: T_weight, inf: T_weight) -> None:
        self._zero_value = zero
        self._infinity_value = inf

    def vertex_id_set(
        self, initial_content: Iterable[T_vertex_id]
    ) -> VertexSet[T_vertex_id]:
        return set[T_vertex_id](initial_content)

    def vertex_id_to_vertex_mapping(
        self, initial_content: Iterable[tuple[T_vertex_id, T_vertex]]
    ) -> VertexMapping[T_vertex_id, T_vertex]:
        return dict[T_vertex_id, T_vertex](initial_content)

    def vertex_id_to_path_attributes_mapping(
        self, initial_content: Iterable[tuple[T_vertex_id, T_labels]]
    ) -> VertexMapping[T_vertex_id, T_labels]:
        return dict[T_vertex_id, T_labels](initial_content)

    def sequence_of_vertices(
        self, initial_content: Iterable[T_vertex]
    ) -> MutableSequenceOfVertices[T_vertex]:
        return list[T_vertex](initial_content)

    def zero(self) -> T_weight:
        return self._zero_value

    def infinity(self) -> T_weight:
        return self._infinity_value

    def vertex_id_to_distance_mapping(
        self, initial_content: Iterable[tuple[T_vertex_id, T_weight]]
    ) -> VertexMapping[T_vertex_id, T_weight]:

        return DefaultdictWithNiceStr[T_vertex_id, T_weight](
            lambda: self._infinity_value, initial_content
        )


# Implementation note:
# In the following, a separate class GearForHashableVertexIDsAndIntsMaybeFloats is used
# instead of an additional (class) factory method, e.g. something like for_float()
# in class GearForHashableVertexIDs, since calling such a method in typed
# code would require to specify the weight type twice, like in:
#   g = GearForHashableVertexIDs[T_vertex, T_vertex_id, float].for_float()
# Also, an additional static factory method does not work. Like any function,
# it can be generic only in its parameters - but it would not have parameters.
# Something like the following is not possible:
#   g = GearForHashableVertexIDs.for_float[int, int]()
# (Error: Value of type "Callable[[], GearForHashableVertexIDs[
#  T_vertex, T_vertex_id, float]]" is not indexable)
# The same holds for the other classes for specific weight type.


class GearDefault(
    Generic[T_vertex, T_vertex_id, T_weight, T_labels],
    GearForHashableVertexIDs[T_vertex, T_vertex_id, Union[T_weight, float], T_labels],
):
    """A `GearForHashableVertexIDs` that uses the integer 0 for zero
    distance, and float("infinity") for infinite distance and thus,
    Union[T_weight, float] as type of distances.

    When using GearDefault, the choice of these two numbers has the following
    consequences:

    - Additional requirement for T_weight: Additionally to the usual requirements
      for edge weights in NoGraphs (see `T_weight`), it needs to be possible to
      add the integer 0 to a weight, and a weight needs to be comparable
      to *float("infinity")*.

    - Distances calculated and returned by NoGraphs can not only be values of the
      chosen type T_weight for edge weights, but also the integer 0 and
      float("infinity").

    - In typed code, a traversal object that uses GearDefault must be declared with
      Union[T_weight, float] for the weight type because it might return a float
      generated by GearDefault as distance (otherwise, your typing is inconsistent,
      and a static type checker will report an error).

    **Examples for typical T_weight number types** that can be used with GearDefault,
    because they fulfil the requirements described above:

       *float*, *int*, *Decimal* and class *mpf* of library *mpmath*.
    """

    def __init__(self) -> None:
        super().__init__(0, float("inf"))


class GearForHashableVertexIDsAndIntsMaybeFloats(
    GearForHashableVertexIDs[T_vertex, T_vertex_id, float, T_labels]
):
    """A `GearForHashableVertexIDs` for weights that are of type float or integer.

    It uses the integer 0 for zero distance. If all occurring edge weights
    are also integers, all reported distances of reached vertices will also be
    integers. So, this gear can also be used for calculations within the integers.

    It uses *float("infinity")* for infinite distance. So, infinite distance will
    always be reported as float.
    """

    def __init__(self) -> None:
        super().__init__(0, float("inf"))


class GearForHashableVertexIDsAndDecimals(
    GearForHashableVertexIDs[T_vertex, T_vertex_id, Decimal, T_labels]
):
    """A `GearForHashableVertexIDs` for weights that are of type Decimal."""

    def __init__(self) -> None:
        super().__init__(Decimal(0), Decimal("inf"))


class GearForHashableVertexIDsAndFloats(
    GearForHashableVertexIDs[T_vertex, T_vertex_id, float, T_labels]
):
    """A `GearForHashableVertexIDs` for weights that are of type float."""

    def __init__(self) -> None:
        super().__init__(0.0, float("inf"))


# --- Integers ----------------------------------------------------------

IntVertexID = int

# --- Integer vertex IDs ---


class GearForIntVertexIDs(
    Gear[T_vertex, IntVertexID, T_weight, T_labels],
    Generic[T_vertex, T_weight, T_labels],
):
    """Factory methods for bookkeeping collections. For graphs with
    vertex IDs that are non-negative integers (to be exact: they should be
    a dense subset of the natural numbers starting at 0).
    (Either, your vertices are such numbers, or you assign such numbers as IDs to
    them, see tutorial section about `vertex identity <vertex_identity>`).

    Trades type flexibility and runtime for an (often large) reduction of the memory
    consumption: Uses sequence-based collections (instead of hash-based collections
    like dict and set) for bookkeeping. Arrays are preferred over lists, since there,
    data can be stored as C-native values. Boolean values are packed into integers.

    Notes:

    - If you are on a 32-bit system, lists and arrays can not be larger than
      sys.maxsize/4 = 536,870,912 entries, what limits your vertex ids (and vertices,
      if you do not use a `VertexToID` function).

    - NoGraphs does not access the lists or arrays via an emulation of the
      mappings that are demanded by protocol Gear, but is able to directly
      access them, and the code for this is inlined, for better performance.

    :param zero: Value used to represent zero distance.

    :param inf: Value used to represent infinite distance.

    :param no_arrays: Use only lists, no arrays. (Depending on the used traversal
      and the graph, arrays can reduce the memory consumption by up to 88% in
      comparison to lists, but runtime can increase by up to 10%.)

    :param no_bit_packing: Store boolean values of vertex ID sets as integers instead
      of bits. (Depending on the used traversal and the graph, bit packing can reduce
      the memory consumption by up to 85%, but runtime can increase by up to 30%.
      By default, bit packing is used where possible.)

    :param pre_allocate: Space for this number of vertices is pre-allocated when a
      collection is requested by NoGraphs. Default: 0.
    """

    def __init__(
        self,
        zero: T_weight,
        inf: T_weight,
        no_arrays: bool = False,
        no_bit_packing: bool = False,
        pre_allocate: int = 0,
    ) -> None:
        self._zero_value: T_weight = zero
        self._infinity_value: T_weight = inf
        self._no_bit_packing = no_bit_packing
        self._no_arrays = no_arrays
        self._pre_allocate = pre_allocate

    def vertex_id_set(
        self, initial_content: Iterable[IntVertexID]
    ) -> VertexSet[IntVertexID]:
        pre_allocate = (
            (self._pre_allocate + 7) // 8
            if self._no_bit_packing
            else self._pre_allocate
        )
        extend_size = 1024 if self._no_bit_packing else 1024 // 8
        if self._no_arrays:

            def sequence_factory() -> SequenceForGearProto[int, int, int]:
                return [0] * pre_allocate

        else:

            def sequence_factory() -> SequenceForGearProto[int, int, int]:
                return array("B", repeat(0, pre_allocate))

        collection_class = (
            VertexSetWrappingSequenceNoBitPacking
            if self._no_bit_packing
            else VertexSetWrappingSequenceBitPacking
        )
        return collection_class(sequence_factory, extend_size, initial_content)

    def vertex_id_to_vertex_mapping(
        self, initial_content: Iterable[tuple[IntVertexID, T_vertex]]
    ) -> VertexMapping[IntVertexID, T_vertex]:
        return VertexMappingWrappingSequenceWithNone[T_vertex](
            lambda: [None] * self._pre_allocate, None, 1024, initial_content
        )

    def vertex_id_to_path_attributes_mapping(
        self, initial_content: Iterable[tuple[IntVertexID, T_labels]]
    ) -> VertexMapping[IntVertexID, T_labels]:
        return VertexMappingWrappingSequenceWithNone[T_labels](
            lambda: [None] * self._pre_allocate, None, 1024, initial_content
        )

    def sequence_of_vertices(
        self, initial_content: Iterable[T_vertex]
    ) -> MutableSequenceOfVertices[T_vertex]:
        return list[T_vertex](initial_content)

    def zero(self) -> T_weight:
        return self._zero_value

    def infinity(self) -> T_weight:
        return self._infinity_value

    def vertex_id_to_distance_mapping(
        self, initial_content: Iterable[tuple[IntVertexID, T_weight]]
    ) -> VertexMapping[IntVertexID, T_weight]:
        return VertexMappingWrappingSequenceWithoutNone[T_weight](
            lambda: [self._infinity_value] * self._pre_allocate,
            self._infinity_value,
            1024,
            initial_content,
        )


class GearForIntVertexIDsAndIntsMaybeFloats(
    GearForIntVertexIDs[T_vertex, float, T_labels]
):
    """A `GearForIntVertexIDs` for weights that are of type float or integer.

    It uses the integer 0 for zero distances. If all occurring edge weights are
    also integers, all reported distances of reached vertices will also be integers.
    So, this gear can also be used for calculations within the integers.

    It uses float(“infinity”) for infinite distance. So, infinite distance
    will always be reported as float.

    :param no_arrays: Use only lists, no arrays. See `GearForIntVertexIDs`.

    :param no_bit_packing: Store boolean values in vertex sets as integers instead of
      bits. See `GearForIntVertexIDs`.

    :param pre_allocate: Space for this number of vertices is pre-allocated when a
      collection is requested by NoGraphs. Default: 0.
    """

    def __init__(
        self,
        no_arrays: bool = False,
        no_bit_packing: bool = False,
        pre_allocate: int = 0,
    ) -> None:
        super().__init__(0, float("inf"), no_arrays, no_bit_packing, pre_allocate)


class GearForIntVertexIDsAndDecimals(GearForIntVertexIDs[T_vertex, Decimal, T_labels]):
    """A `GearForIntVertexIDs` for weights that are of type Decimal.

    :param no_arrays: Use lists instead of arrays. See `GearForIntVertexIDs`.

    :param no_bit_packing: Store boolean values in vertex sets as integers instead of
      bits. See `GearForIntVertexIDs`.

    :param pre_allocate: Space for this number of vertices is pre-allocated when a
      collection is requested by NoGraphs. Default: 0.
    """

    def __init__(
        self,
        no_arrays: bool = False,
        no_bit_packing: bool = False,
        pre_allocate: int = 0,
    ) -> None:
        super().__init__(
            Decimal(0), Decimal("inf"), no_arrays, no_bit_packing, pre_allocate
        )


class GearForIntVertexIDsAndCFloats(GearForIntVertexIDs[T_vertex, float, T_labels]):
    """A `GearForIntVertexIDs` for weights that are floats in the limits
    of some C-native float type.

    Here, arrays and C-native storage of data are also used for distances.

    :param no_bit_packing: Store boolean values in vertex sets as integers instead of
      bits. See `GearForIntVertexIDs`.

    :param distance_type_code: Number of bytes used to store distances float values,
      as type_code (see class array.array of the Python standard library):

      - "f" (default): 4 bytes float.
      - "d": 8 bytes float.

    :param pre_allocate: Space for this number of vertices is pre-allocated when a
      collection is requested by NoGraphs. Default: 0.
    """

    def __init__(
        self,
        no_bit_packing: bool = False,
        distance_type_code: Literal["f", "d"] = "f",
        pre_allocate: int = 0,
    ) -> None:
        self.distance_type_code = distance_type_code
        super().__init__(0.0, float("inf"), False, no_bit_packing, pre_allocate)

    def vertex_id_to_distance_mapping(
        self, initial_content: Iterable[tuple[IntVertexID, float]]
    ) -> VertexMapping[IntVertexID, float]:

        return VertexMappingWrappingSequenceWithoutNone[float](
            lambda: array(
                self.distance_type_code,
                repeat(self._infinity_value, self._pre_allocate),
            ),
            self._infinity_value,
            1024,
            initial_content,
        )


class GearForIntVertexIDsAndCInts(GearForIntVertexIDs[T_vertex, int, T_labels]):
    """A `GearForIntVertexIDs` for weights that are integers in the limits
    of some C-native integer type.

    Here, arrays and C-native storage of data are also used for distances.

    :param no_bit_packing: Store boolean values in vertex sets as integers instead of
      bits. See `GearForIntVertexIDs`.

    :param distance_type_code: Number of bytes used to store distances integer values,
      as type_code (see class array.array of the Python standard library):

      - "l" (default): 4 bytes signed long.
      - "b", "B", "h", "H", "i", "I", "L", "q", "Q": See class array.array

    :param pre_allocate: Space for this number of vertices is pre-allocated when a
      collection is requested by NoGraphs. Default: 0.
    """

    def __init__(
        self,
        no_bit_packing: bool = False,
        distance_type_code: Literal[
            "b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"
        ] = "l",
        pre_allocate: int = 0,
    ) -> None:
        self.distance_type_code = distance_type_code
        bytes_of_type_code = {"b": 1, "h": 2, "i": 2, "l": 4, "q": 8}[
            self.distance_type_code.lower()
        ]
        # Highest possible vertex value will be used as NaN value.
        # If this value is stored for some vertex as index, this means that
        # the collection stores no value for the index vertex so far.
        self.max_type_value = 256 ^ bytes_of_type_code - 1

        super().__init__(0, self.max_type_value, False, no_bit_packing, pre_allocate)

    def vertex_id_to_distance_mapping(
        self, initial_content: Iterable[tuple[IntVertexID, int]]
    ) -> VertexMapping[IntVertexID, int]:

        return VertexMappingWrappingSequenceWithoutNone[int](
            lambda: array(
                self.distance_type_code,
                repeat(self._infinity_value, self._pre_allocate),
            ),
            self._infinity_value,
            1024,
            initial_content,
        )


# --- Integer vertices ---


class GearForIntVerticesAndIDs(GearForIntVertexIDs[IntVertexID, T_weight, T_labels]):
    """A `GearForIntVertexIDs` (see there for constraints on vertex ids)
    for graphs with vertices, that are non-negative
    integers and fulfil one of the offered size constraints.

    Here, arrays and C-native storage of data are also used for vertices.

    :param zero: Value used to represent zero distance.

    :param inf: Value used to represent infinite distance.

    :param no_bit_packing: Store boolean values of vertex ID sets as integers instead
      of bits. (Depending on the used traversal and the graph, bit packing can reduce
      the memory consumption by up to 85%, but runtime can increase by up to 30%.
      By default, bit packing is used where possible.)

    :param vertex_type_code: Number of bytes used to store one of your integer
      vertices, as type_code.

      - "L" (default): 4 bytes. Allows for integers in range(4.294.967.296).

      - "Q": 8 bytes. In case you really need more than "L"...

      - "I": 2 bytes. If range(65536) is enough.

      Note: The highest respective value cannot be used as vertex, since it is
      used for internal purposes (flag for keys without values).

    :param pre_allocate: If you provide a value for parameter pre_allocate, space for
      this number of vertices is pre-allocated when a collection is requested by
      NoGraphs.
    """

    def __init__(
        self,
        zero: T_weight,
        inf: T_weight,
        no_bit_packing: bool = False,
        vertex_type_code: Literal["L", "Q", "I"] = "L",
        pre_allocate: int = 0,
    ) -> None:
        self.vertex_type_code = vertex_type_code
        super().__init__(zero, inf, False, no_bit_packing, pre_allocate)

    def vertex_id_to_vertex_mapping(
        self, initial_content: Iterable[tuple[IntVertexID, IntVertexID]]
    ) -> VertexMapping[IntVertexID, IntVertexID]:
        bytes_of_vertex_type_code = {"L": 4, "Q": 8, "I": 2}[self.vertex_type_code]
        # Highest possible vertex value will be used as NaN value.
        # If this value is stored for some vertex as index, this means that
        # the collection stores no value for the index vertex so far.
        max_vertex_type_value = 256 ^ bytes_of_vertex_type_code - 1

        return VertexMappingWrappingSequenceWithoutNone[IntVertexID](
            lambda: array(
                self.vertex_type_code, repeat(max_vertex_type_value, self._pre_allocate)
            ),
            max_vertex_type_value,
            1024,
            initial_content,
        )

    def sequence_of_vertices(
        self, initial_content: Iterable[IntVertexID]
    ) -> MutableSequenceOfVertices[IntVertexID]:
        return array(self.vertex_type_code, initial_content)


class GearForIntVerticesAndIDsAndIntsMaybeFloats(
    GearForIntVerticesAndIDs[float, T_labels]
):
    """A `GearForIntVerticesAndIDs` for weights that are of type float or integer.

    It uses the integer 0 for zero distances. If all occurring edge weights are
    also integers, all reported distances of reached vertices will also be integers.
    So, this gear can also be used for calculations within the integers.

    It uses float(“infinity”) for infinite distance. So, infinite distance
    will always be reported as float.

    :param no_bit_packing: Store boolean values in vertex sets as integers instead of
      bits. See `GearForIntVerticesAndIDs`.

    :param vertex_type_code: Number of bytes used to store one of your integer
      vertices, as type_code. See `GearForIntVerticesAndIDs`.

    :param pre_allocate: Space for this number of vertices is pre-allocated when a
      collection is requested by NoGraphs. Default: 0.
    """

    def __init__(
        self,
        no_bit_packing: bool = False,
        vertex_type_code: Literal["L", "Q", "I"] = "L",
        pre_allocate: int = 0,
    ) -> None:
        super().__init__(
            0, float("inf"), no_bit_packing, vertex_type_code, pre_allocate
        )


class GearForIntVerticesAndIDsAndDecimals(GearForIntVerticesAndIDs[Decimal, T_labels]):
    """A `GearForIntVerticesAndIDs` for weights that are of type Decimal.

    :param no_bit_packing: Store boolean values of vertex id sets as integers instead
      of bits. See `GearForIntVerticesAndIDs`.

    :param vertex_type_code: Number of bytes used to store one of your integer
      vertices, as type_code. See `GearForIntVerticesAndIDs`.

    :param pre_allocate: Space for this number of vertices is pre-allocated when a
      collection is requested by NoGraphs. Default: 0.
    """

    def __init__(
        self,
        no_bit_packing: bool = False,
        vertex_type_code: Literal["L", "Q", "I"] = "L",
        pre_allocate: int = 0,
    ) -> None:
        super().__init__(
            Decimal(0), Decimal("inf"), no_bit_packing, vertex_type_code, pre_allocate
        )


class GearForIntVerticesAndIDsAndCFloats(GearForIntVerticesAndIDs[float, T_labels]):
    """A `GearForIntVerticesAndIDs` for graphs with dense non-negative integers of
    constrained size in bytes as vertex ids AND as vertices, and edge weights
    that are floats in the limits of some C-native float type.

    for edge weight and distance values.

    Here, arrays and C-native storage of data are also used for vertices.

    :param no_bit_packing: Store boolean values of vertex id sets as integers instead
      of bits. See `GearForIntVerticesAndIDs`.

    :param vertex_type_code: Number of bytes used to store one of your integer
      vertices, as type_code. See `GearForIntVerticesAndIDs`.

    :param distance_type_code: Number of bytes used to store distances float values,
      as type_code (see class array.array of the Python standard library):

      - "f" (default): 4 bytes float.
      - "d": 8 bytes float.

    :param pre_allocate: If you provide a value for parameter pre_allocate, space for
      this number of vertices is pre-allocated when a collection is requested by
      NoGraphs.
    """

    def __init__(
        self,
        no_bit_packing: bool = False,
        vertex_type_code: Literal["L", "Q", "I"] = "L",
        distance_type_code: Literal["f", "d"] = "f",
        pre_allocate: int = 0,
    ) -> None:
        self.distance_type_code = distance_type_code
        super().__init__(
            0.0, float("inf"), no_bit_packing, vertex_type_code, pre_allocate
        )

    def vertex_id_to_distance_mapping(
        self, initial_content: Iterable[tuple[IntVertexID, float]]
    ) -> VertexMapping[IntVertexID, float]:

        return VertexMappingWrappingSequenceWithoutNone[float](
            lambda: array(
                self.distance_type_code,
                repeat(self._infinity_value, self._pre_allocate),
            ),
            self._infinity_value,
            1024,
            initial_content,
        )


class GearForIntVerticesAndIDsAndCInts(GearForIntVerticesAndIDs[int, T_labels]):
    """A `GearForIntVerticesAndIDs` for graphs with dense non-negative integers of
    constrained size in bytes as vertex ids AND as vertices, and integers in the limits
    of some C-native integer type.

    Here, arrays and C-native storage of data are also used for vertices.

    :param no_bit_packing: Store boolean values of vertex id sets as integers instead
      of bits. See `GearForIntVerticesAndIDs`.

    :param vertex_type_code: Number of bytes used to store one of your integer
      vertices, as type_code. See `GearForIntVerticesAndIDs`.

    :param distance_type_code: Number of bytes used to store distances integer values,
      as type_code (see class array.array of the Python standard library):

      - "l" (default): 4 bytes signed long.
      - "b", "B", "h", "H", "i", "I", "L", "q", "Q": See class array.array

    :param pre_allocate: If you provide a value for parameter pre_allocate, space for
      this number of vertices is pre-allocated when a collection is requested by
      NoGraphs.
    """

    def __init__(
        self,
        no_bit_packing: bool = False,
        vertex_type_code: Literal["L", "Q", "I"] = "L",
        distance_type_code: Literal[
            "b", "B", "h", "H", "i", "I", "l", "L", "q", "Q"
        ] = "l",
        pre_allocate: int = 0,
    ) -> None:
        self.distance_type_code = distance_type_code
        bytes_of_type_code = {"b": 1, "h": 2, "i": 2, "l": 4, "q": 8}[
            self.distance_type_code.lower()
        ]
        # Highest possible vertex value will be used as NaN value.
        # If this value is stored for some vertex as index, this means that
        # the collection stores no value for the index vertex so far.
        self.max_type_value = 256 ^ bytes_of_type_code - 1

        super().__init__(
            0, self.max_type_value, no_bit_packing, vertex_type_code, pre_allocate
        )

    def vertex_id_to_distance_mapping(
        self, initial_content: Iterable[tuple[IntVertexID, int]]
    ) -> VertexMapping[IntVertexID, int]:
        return VertexMappingWrappingSequenceWithoutNone[int](
            lambda: array(
                self.distance_type_code,
                repeat(self._infinity_value, self._pre_allocate),
            ),
            self._infinity_value,
            1024,
            initial_content,
        )
