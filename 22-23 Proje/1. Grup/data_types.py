#!/usr/bin/env python3
#
#         Ferit Yiğit BALABAN <fybalaban@fybx.dev>
#
from ctypes import c_int32


class Word:
    _value = c_int32(0)
    _width = 32
    _maxvl = 2147483647
    _minvl = -2147483648

    def __init__(self, int_value: int):
        """
        Verilen tam sayı değerini içeren bir kelime nesnesi üretir. Kelimeler 32 bit genişliğindedir.

        :param int_value: Kelimenin tutacağı değer
        """
        self._value = c_int32(int_value)

    def set_lrange(self, start: int, end: int, replace_with: str):
        bin_rep = self.as_binary()
        if start < 0 or end >= len(bin_rep) or start > end:
            raise ValueError("Hatalı aralık.")

        self.from_binary(bin_rep[:start] + replace_with + bin_rep[end + 1:])

    def set_rrange(self, start: int, end: int, replace_with: str):
        self.set_lrange(31 - start, 31 - end, replace_with)

    def from_binary(self, binary_value: str):
        """
        Kelimenin değerini verilen ikili değer olacak şekilde günceller.

        :param binary_value: Kelimenin tutacağı değerin ikili gösterimi
        """
        n = int(binary_value, 2)
        self._value = c_int32(n - (1 << 32) if n & (1 << 31) else n)

    def as_binary(self):
        """
        Kelimenin tuttuğu değerin ikinin tümleyeni biçimindeki ikili gösterimini döndürür.

        :return: Kelimenin tuttuğu değerin ikili gösterim string'i.
        :rtype: str
        """
        return format(self._value.value % (1 << self._width), '0{}b'.format(self._width))

    def as_hexadecimal(self):
        return hex(self._value.value)

    @property
    def value(self):
        return self._value.value

    @property
    def width(self):
        return self._width

    @property
    def minvl(self):
        return self._minvl

    @property
    def maxvl(self):
        return self._maxvl
