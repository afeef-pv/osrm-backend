# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Example

import flatbuffers

class ArrayStruct(object):
    __slots__ = ['_tab']

    # ArrayStruct
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayStruct
    def A(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # ArrayStruct
    def B(self): return [self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4 + i * 4)) for i in range(15)]
    # ArrayStruct
    def C(self): return self._tab.Get(flatbuffers.number_types.Int8Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(64))
    # ArrayStruct
    def D(self, obj, i):
        obj.Init(self._tab.Bytes, self._tab.Pos + 68 + i * 12)
        return obj


def CreateArrayStruct(builder, a, b, c, d_a, d_b, d_c):
    builder.Prep(4, 92)
    for _idx0 in range(2 , 0, -1):
        builder.Prep(4, 12)
        builder.Pad(1)
        for _idx1 in range(2 , 0, -1):
            builder.PrependInt8(d_c[_idx0-1][_idx1-1])
        builder.PrependInt8(d_b[_idx0-1])
        for _idx1 in range(2 , 0, -1):
            builder.PrependInt32(d_a[_idx0-1][_idx1-1])
    builder.Pad(3)
    builder.PrependInt8(c)
    for _idx0 in range(15 , 0, -1):
        builder.PrependInt32(b[_idx0-1])
    builder.PrependFloat32(a)
    return builder.Offset()
