class alias:

    def __set__(self, instance, value):
        if self._is_writeable:
            setattr(instance, self._private_name, value)
        else:
            raise AttributeError("can't set attribute")

    def __get__(self, obj, objtype=None):
        if not obj and objtype:
            return getattr(objtype, self._private_name)
        return getattr(obj, self._private_name)

    def __init__(self, name: str, *args, write: bool = False, **kwargs):
        self._private_name = name
        self._is_writeable = write


class DataRecord:
    title = alias("serial")

    def __init__(self, serial):
        self.serial = serial
