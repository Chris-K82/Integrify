import builtins as _mod_builtins
import msgpack as _mod_msgpack
import msgpack.exceptions as _mod_msgpack_exceptions

BufferFull = _mod_msgpack_exceptions.BufferFull
ExtType = _mod_msgpack.ExtType
ExtraData = _mod_msgpack_exceptions.ExtraData
FormatError = _mod_msgpack_exceptions.FormatError
OutOfData = _mod_msgpack_exceptions.OutOfData
class Packer(_mod_builtins.object):
    "Packer(default=None, encoding=None, unicode_errors=None, bool use_single_float=False, bool autoreset=True, bool use_bin_type=False, bool strict_types=False)\n\n    MessagePack Packer\n\n    usage::\n\n        packer = Packer()\n        astream.write(packer.pack(a))\n        astream.write(packer.pack(b))\n\n    Packer's constructor has some keyword arguments:\n\n    :param callable default:\n        Convert user type to builtin type that Packer supports.\n        See also simplejson's document.\n\n    :param bool use_single_float:\n        Use single precision float type for float. (default: False)\n\n    :param bool autoreset:\n        Reset buffer after each pack and return its content as `bytes`. (default: True).\n        If set this to false, use `bytes()` to get content and `.reset()` to clear buffer.\n\n    :param bool use_bin_type:\n        Use bin type introduced in msgpack spec 2.0 for bytes.\n        It also enables str8 type for unicode.\n        Current default value is false, but it will be changed to true\n        in future version.  You should specify it explicitly.\n\n    :param bool strict_types:\n        If set to true, types will be checked to be exact. Derived classes\n        from serializeable types will not be serialized and will be\n        treated as unsupported type and forwarded to default.\n        Additionally tuples will not be serialized as lists.\n        This is useful when trying to implement accurate serialization\n        for python types.\n\n    :param str unicode_errors:\n        Error handler for encoding unicode. (default: 'strict')\n\n    :param str encoding:\n        (deprecated) Convert unicode to bytes with this encoding. (default: 'utf-8')\n    "
    __class__ = Packer
    def __init__(self, default=None, encoding=None, unicode_errors=None, booluse_single_float=False, boolautoreset=True, booluse_bin_type=False, boolstrict_types=False):
        "Packer(default=None, encoding=None, unicode_errors=None, bool use_single_float=False, bool autoreset=True, bool use_bin_type=False, bool strict_types=False)\n\n    MessagePack Packer\n\n    usage::\n\n        packer = Packer()\n        astream.write(packer.pack(a))\n        astream.write(packer.pack(b))\n\n    Packer's constructor has some keyword arguments:\n\n    :param callable default:\n        Convert user type to builtin type that Packer supports.\n        See also simplejson's document.\n\n    :param bool use_single_float:\n        Use single precision float type for float. (default: False)\n\n    :param bool autoreset:\n        Reset buffer after each pack and return its content as `bytes`. (default: True).\n        If set this to false, use `bytes()` to get content and `.reset()` to clear buffer.\n\n    :param bool use_bin_type:\n        Use bin type introduced in msgpack spec 2.0 for bytes.\n        It also enables str8 type for unicode.\n        Current default value is false, but it will be changed to true\n        in future version.  You should specify it explicitly.\n\n    :param bool strict_types:\n        If set to true, types will be checked to be exact. Derived classes\n        from serializeable types will not be serialized and will be\n        treated as unsupported type and forwarded to default.\n        Additionally tuples will not be serialized as lists.\n        This is useful when trying to implement accurate serialization\n        for python types.\n\n    :param str unicode_errors:\n        Error handler for encoding unicode. (default: 'strict')\n\n    :param str encoding:\n        (deprecated) Convert unicode to bytes with this encoding. (default: 'utf-8')\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        'Packer.__reduce_cython__(self)'
        return ''; return ()
    
    def __setstate__(self, state):
        'Packer.__setstate_cython__(self, __pyx_state)'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def bytes(self):
        'Packer.bytes(self)\nReturn internal buffer contents as bytes object'
        pass
    
    def getbuffer(self):
        'Packer.getbuffer(self)\nReturn view of internal buffer.'
        pass
    
    def pack(self):
        'Packer.pack(self, obj)'
        pass
    
    def pack_array_header(self):
        'Packer.pack_array_header(self, long long size)'
        pass
    
    def pack_ext_type(self):
        'Packer.pack_ext_type(self, typecode, data)'
        pass
    
    def pack_map_header(self):
        'Packer.pack_map_header(self, long long size)'
        pass
    
    def pack_map_pairs(self):
        'Packer.pack_map_pairs(self, pairs)\n\n        Pack *pairs* as msgpack map type.\n\n        *pairs* should be a sequence of pairs.\n        (`len(pairs)` and `for k, v in pairs:` should be supported.)\n        '
        pass
    
    def reset(self):
        'Packer.reset(self)\nReset internal buffer.\n\n        This method is usaful only when autoreset=False.\n        '
        pass
    

StackError = _mod_msgpack_exceptions.StackError
class Unpacker(_mod_builtins.object):
    "Unpacker(file_like=None, Py_ssize_t read_size=0, bool use_list=True, bool raw=True, bool strict_map_key=False, object_hook=None, object_pairs_hook=None, list_hook=None, encoding=None, unicode_errors=None, Py_ssize_t max_buffer_size=0, ext_hook=ExtType, Py_ssize_t max_str_len=-1, Py_ssize_t max_bin_len=-1, Py_ssize_t max_array_len=-1, Py_ssize_t max_map_len=-1, Py_ssize_t max_ext_len=-1)\nStreaming unpacker.\n\n    Arguments:\n\n    :param file_like:\n        File-like object having `.read(n)` method.\n        If specified, unpacker reads serialized data from it and :meth:`feed()` is not usable.\n\n    :param int read_size:\n        Used as `file_like.read(read_size)`. (default: `min(1024**2, max_buffer_size)`)\n\n    :param bool use_list:\n        If true, unpack msgpack array to Python list.\n        Otherwise, unpack to Python tuple. (default: True)\n\n    :param bool raw:\n        If true, unpack msgpack raw to Python bytes (default).\n        Otherwise, unpack to Python str (or unicode on Python 2) by decoding\n        with UTF-8 encoding (recommended).\n        Currently, the default is true, but it will be changed to false in\n        near future.  So you must specify it explicitly for keeping backward\n        compatibility.\n\n        *encoding* option which is deprecated overrides this option.\n\n    :param bool strict_map_key:\n        If true, only str or bytes are accepted for map (dict) keys.\n        It's False by default for backward-compatibility.\n        But it will be True from msgpack 1.0.\n\n    :param callable object_hook:\n        When specified, it should be callable.\n        Unpacker calls it with a dict argument after unpacking msgpack map.\n        (See also simplejson)\n\n    :param callable object_pairs_hook:\n        When specified, it should be callable.\n        Unpacker calls it with a list of key-value pairs after unpacking msgpack map.\n        (See also simplejson)\n\n    :param int max_buffer_size:\n        Limits size of data waiting unpacked.  0 means system's INT_MAX (default).\n        Raises `BufferFull` exception when it is insufficient.\n        You should set this parameter when unpacking data from untrusted source.\n\n    :param int max_str_len:\n        Deprecated, use *max_buffer_size* instead.\n        Limits max length of str. (default: max_buffer_size or 1024*1024)\n\n    :param int max_bin_len:\n        Deprecated, use *max_buffer_size* instead.\n        Limits max length of bin. (default: max_buffer_size or 1024*1024)\n\n    :param int max_array_len:\n        Limits max length of array. (default: max_buffer_size or 128*1024)\n\n    :param int max_map_len:\n        Limits max length of map. (default: max_buffer_size//2 or 32*1024)\n\n    :param int max_ext_len:\n        Deprecated, use *max_buffer_size* instead.\n        Limits max size of ext type. (default: max_buffer_size or 1024*1024)\n\n    :param str encoding:\n        Deprecated, use ``raw=False`` instead.\n        Encoding used for decoding msgpack raw.\n        If it is None (default), msgpack raw is deserialized to Python bytes.\n\n    :param str unicode_errors:\n        Error handler used for decoding str type.  (default: `'strict'`)\n\n\n    Example of streaming deserialize from file-like object::\n\n        unpacker = Unpacker(file_like, raw=False, max_buffer_size=10*1024*1024)\n        for o in unpacker:\n            process(o)\n\n    Example of streaming deserialize from socket::\n\n        unpacker = Unpacker(raw=False, max_buffer_size=10*1024*1024)\n        while True:\n            buf = sock.recv(1024**2)\n            if not buf:\n                break\n            unpacker.feed(buf)\n            for o in unpacker:\n                process(o)\n\n    Raises ``ExtraData`` when *packed* contains extra bytes.\n    Raises ``OutOfData`` when *packed* is incomplete.\n    Raises ``FormatError`` when *packed* is not valid msgpack.\n    Raises ``StackError`` when *packed* contains too nested.\n    Other exceptions can be raised during unpacking.\n    "
    __class__ = Unpacker
    def __init__(self, file_like=None, Py_ssize_tread_size=0, booluse_list=True, boolraw=True, boolstrict_map_key=False, object_hook=None, object_pairs_hook=None, list_hook=None, encoding=None, unicode_errors=None, Py_ssize_tmax_buffer_size=0, ext_hook=ExtType, Py_ssize_tmax_str_len=-1, Py_ssize_tmax_bin_len=-1, Py_ssize_tmax_array_len=-1, Py_ssize_tmax_map_len=-1, Py_ssize_tmax_ext_len=-1):
        "Unpacker(file_like=None, Py_ssize_t read_size=0, bool use_list=True, bool raw=True, bool strict_map_key=False, object_hook=None, object_pairs_hook=None, list_hook=None, encoding=None, unicode_errors=None, Py_ssize_t max_buffer_size=0, ext_hook=ExtType, Py_ssize_t max_str_len=-1, Py_ssize_t max_bin_len=-1, Py_ssize_t max_array_len=-1, Py_ssize_t max_map_len=-1, Py_ssize_t max_ext_len=-1)\nStreaming unpacker.\n\n    Arguments:\n\n    :param file_like:\n        File-like object having `.read(n)` method.\n        If specified, unpacker reads serialized data from it and :meth:`feed()` is not usable.\n\n    :param int read_size:\n        Used as `file_like.read(read_size)`. (default: `min(1024**2, max_buffer_size)`)\n\n    :param bool use_list:\n        If true, unpack msgpack array to Python list.\n        Otherwise, unpack to Python tuple. (default: True)\n\n    :param bool raw:\n        If true, unpack msgpack raw to Python bytes (default).\n        Otherwise, unpack to Python str (or unicode on Python 2) by decoding\n        with UTF-8 encoding (recommended).\n        Currently, the default is true, but it will be changed to false in\n        near future.  So you must specify it explicitly for keeping backward\n        compatibility.\n\n        *encoding* option which is deprecated overrides this option.\n\n    :param bool strict_map_key:\n        If true, only str or bytes are accepted for map (dict) keys.\n        It's False by default for backward-compatibility.\n        But it will be True from msgpack 1.0.\n\n    :param callable object_hook:\n        When specified, it should be callable.\n        Unpacker calls it with a dict argument after unpacking msgpack map.\n        (See also simplejson)\n\n    :param callable object_pairs_hook:\n        When specified, it should be callable.\n        Unpacker calls it with a list of key-value pairs after unpacking msgpack map.\n        (See also simplejson)\n\n    :param int max_buffer_size:\n        Limits size of data waiting unpacked.  0 means system's INT_MAX (default).\n        Raises `BufferFull` exception when it is insufficient.\n        You should set this parameter when unpacking data from untrusted source.\n\n    :param int max_str_len:\n        Deprecated, use *max_buffer_size* instead.\n        Limits max length of str. (default: max_buffer_size or 1024*1024)\n\n    :param int max_bin_len:\n        Deprecated, use *max_buffer_size* instead.\n        Limits max length of bin. (default: max_buffer_size or 1024*1024)\n\n    :param int max_array_len:\n        Limits max length of array. (default: max_buffer_size or 128*1024)\n\n    :param int max_map_len:\n        Limits max length of map. (default: max_buffer_size//2 or 32*1024)\n\n    :param int max_ext_len:\n        Deprecated, use *max_buffer_size* instead.\n        Limits max size of ext type. (default: max_buffer_size or 1024*1024)\n\n    :param str encoding:\n        Deprecated, use ``raw=False`` instead.\n        Encoding used for decoding msgpack raw.\n        If it is None (default), msgpack raw is deserialized to Python bytes.\n\n    :param str unicode_errors:\n        Error handler used for decoding str type.  (default: `'strict'`)\n\n\n    Example of streaming deserialize from file-like object::\n\n        unpacker = Unpacker(file_like, raw=False, max_buffer_size=10*1024*1024)\n        for o in unpacker:\n            process(o)\n\n    Example of streaming deserialize from socket::\n\n        unpacker = Unpacker(raw=False, max_buffer_size=10*1024*1024)\n        while True:\n            buf = sock.recv(1024**2)\n            if not buf:\n                break\n            unpacker.feed(buf)\n            for o in unpacker:\n                process(o)\n\n    Raises ``ExtraData`` when *packed* contains extra bytes.\n    Raises ``OutOfData`` when *packed* is incomplete.\n    Raises ``FormatError`` when *packed* is not valid msgpack.\n    Raises ``StackError`` when *packed* contains too nested.\n    Other exceptions can be raised during unpacking.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __iter__(self):
        'Implement iter(self).'
        return Unpacker()
    
    def __next__(self):
        pass
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        'Unpacker.__reduce_cython__(self)'
        return ''; return ()
    
    def __setstate__(self, state):
        'Unpacker.__setstate_cython__(self, __pyx_state)'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def feed(self):
        'Unpacker.feed(self, next_bytes)\nAppend `next_bytes` to internal buffer.'
        pass
    
    def read_array_header(self):
        'Unpacker.read_array_header(self)\nassuming the next object is an array, return its size n, such that\n        the next n unpack() calls will iterate over its contents.\n\n        Raises `OutOfData` when there are no more bytes to unpack.\n        '
        pass
    
    def read_bytes(self):
        'Unpacker.read_bytes(self, Py_ssize_t nbytes)\nRead a specified number of raw bytes from the stream'
        pass
    
    def read_map_header(self):
        'Unpacker.read_map_header(self)\nassuming the next object is a map, return its size n, such that the\n        next n * 2 unpack() calls will iterate over its key-value pairs.\n\n        Raises `OutOfData` when there are no more bytes to unpack.\n        '
        pass
    
    def skip(self):
        'Unpacker.skip(self)\nRead and ignore one object, returning None\n\n        Raises `OutOfData` when there are no more bytes to unpack.\n        '
        pass
    
    def tell(self):
        'Unpacker.tell(self)'
        pass
    
    def unpack(self):
        'Unpacker.unpack(self)\nUnpack one object\n\n        Raises `OutOfData` when there are no more bytes to unpack.\n        '
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/chris/anaconda3/lib/python3.6/site-packages/msgpack/_cmsgpack.cpython-36m-x86_64-linux-gnu.so'
__name__ = 'msgpack._cmsgpack'
__package__ = 'msgpack'
__test__ = _mod_builtins.dict()
def default_read_extended_type(typecode, data):
    'default_read_extended_type(typecode, data)'
    pass

def unpack(stream, **kwargs):
    'unpack(stream, **kwargs)'
    pass

def unpackb(packed, object_hook=None, list_hook=None, booluse_list=True, boolraw=True, boolstrict_map_key=False, encoding=None, unicode_errors=None, object_pairs_hook=None, ext_hook=ExtType, Py_ssize_tmax_str_len=-1, Py_ssize_tmax_bin_len=-1, Py_ssize_tmax_array_len=-1, Py_ssize_tmax_map_len=-1, Py_ssize_tmax_ext_len=-1):
    'unpackb(packed, object_hook=None, list_hook=None, bool use_list=True, bool raw=True, bool strict_map_key=False, encoding=None, unicode_errors=None, object_pairs_hook=None, ext_hook=ExtType, Py_ssize_t max_str_len=-1, Py_ssize_t max_bin_len=-1, Py_ssize_t max_array_len=-1, Py_ssize_t max_map_len=-1, Py_ssize_t max_ext_len=-1)\n\n    Unpack packed_bytes to object. Returns an unpacked object.\n\n    Raises ``ExtraData`` when *packed* contains extra bytes.\n    Raises ``ValueError`` when *packed* is incomplete.\n    Raises ``FormatError`` when *packed* is not valid msgpack.\n    Raises ``StackError`` when *packed* contains too nested.\n    Other exceptions can be raised during unpacking.\n\n    See :class:`Unpacker` for options.\n\n    *max_xxx_len* options are configured automatically from ``len(packed)``.\n    '
    pass

