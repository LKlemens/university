#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

class fractional:
    def add_frac(self, frac1, frac2):
        return [frac1[0]*frac2[1] + frac2[0]*frac1[1], frac1[1]*frac2[1]]

    def sub_frac(self, frac1, frac2):
        return [frac1[0]*frac2[1] - frac2[0]*frac1[1], frac1[1]*frac2[1]]

    def mul_frac(self, frac1, frac2):
        return [ frac1[0] * frac2[0], frac1[1] * frac2[1] ]

    def div_frac(self, frac1, frac2):
        return [frac1[0] * frac2[1], frac1[1] * frac2[0]]

    def is_positive(self, frac):
        return frac[0] > 0 and frac[1] > 0

    def is_zero(self, frac):
        return frac[0] == 0

    def cmp_frac(self, frac1, frac2):
        sub = self.sub_frac(frac1, frac2)
        if sub[0] == 0:
            return 0
        return 1 if self.is_positive(sub) else -1


    def frac2float(self, frac):
        return float(frac[0])/float(frac[1])
