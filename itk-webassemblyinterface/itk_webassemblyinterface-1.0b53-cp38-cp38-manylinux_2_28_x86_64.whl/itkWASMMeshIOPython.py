# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 7, 0):
    raise RuntimeError("Python 3.7 or later required")

from . import _ITKCommonPython


from . import _WebAssemblyInterfacePython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkWASMMeshIOPython
else:
    import _itkWASMMeshIOPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkWASMMeshIOPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkWASMMeshIOPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.vnl_vectorPython
import itk.itkVectorPython
import itk.itkFixedArrayPython
import itk.vnl_vector_refPython
import itk.itkCovariantVectorPython
import itk.vnl_matrix_fixedPython
import itk.itkPointPython
import itk.itkMeshIOBasePython

def itkWASMMeshIO_New():
    return itkWASMMeshIO.New()

class itkWASMMeshIO(itk.itkMeshIOBasePython.itkMeshIOBase):
    r"""Proxy of C++ itkWASMMeshIO class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWASMMeshIOPython.itkWASMMeshIO___New_orig__)
    Clone = _swig_new_instance_method(_itkWASMMeshIOPython.itkWASMMeshIO_Clone)
    SetJSON = _swig_new_instance_method(_itkWASMMeshIOPython.itkWASMMeshIO_SetJSON)
    ITKComponentSize = _swig_new_static_method(_itkWASMMeshIOPython.itkWASMMeshIO_ITKComponentSize)
    __swig_destroy__ = _itkWASMMeshIOPython.delete_itkWASMMeshIO
    cast = _swig_new_static_method(_itkWASMMeshIOPython.itkWASMMeshIO_cast)

    def New(*args, **kargs):
        """New() -> itkWASMMeshIO

        Create a new object of the class itkWASMMeshIO and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWASMMeshIO.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkWASMMeshIO.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkWASMMeshIO.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWASMMeshIO in _itkWASMMeshIOPython:
_itkWASMMeshIOPython.itkWASMMeshIO_swigregister(itkWASMMeshIO)
itkWASMMeshIO___New_orig__ = _itkWASMMeshIOPython.itkWASMMeshIO___New_orig__
itkWASMMeshIO_ITKComponentSize = _itkWASMMeshIOPython.itkWASMMeshIO_ITKComponentSize
itkWASMMeshIO_cast = _itkWASMMeshIOPython.itkWASMMeshIO_cast


def itkWASMMeshIOFactory_New():
    return itkWASMMeshIOFactory.New()

class itkWASMMeshIOFactory(itk.ITKCommonBasePython.itkObjectFactoryBase):
    r"""Proxy of C++ itkWASMMeshIOFactory class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkWASMMeshIOPython.itkWASMMeshIOFactory___New_orig__)
    RegisterOneFactory = _swig_new_static_method(_itkWASMMeshIOPython.itkWASMMeshIOFactory_RegisterOneFactory)
    __swig_destroy__ = _itkWASMMeshIOPython.delete_itkWASMMeshIOFactory
    cast = _swig_new_static_method(_itkWASMMeshIOPython.itkWASMMeshIOFactory_cast)

    def New(*args, **kargs):
        """New() -> itkWASMMeshIOFactory

        Create a new object of the class itkWASMMeshIOFactory and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkWASMMeshIOFactory.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkWASMMeshIOFactory.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkWASMMeshIOFactory.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkWASMMeshIOFactory in _itkWASMMeshIOPython:
_itkWASMMeshIOPython.itkWASMMeshIOFactory_swigregister(itkWASMMeshIOFactory)
itkWASMMeshIOFactory___New_orig__ = _itkWASMMeshIOPython.itkWASMMeshIOFactory___New_orig__
itkWASMMeshIOFactory_RegisterOneFactory = _itkWASMMeshIOPython.itkWASMMeshIOFactory_RegisterOneFactory
itkWASMMeshIOFactory_cast = _itkWASMMeshIOPython.itkWASMMeshIOFactory_cast



