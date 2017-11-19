#! /usr/bin/python2.7
# -*- coding: utf-8 -*-
import operator as op
import numpy as np

class Polys:
    def makeTablesLenEqual(self, poly1, poly2):
        maxLength = max(len(poly1), len(poly2))
        if(len(poly1) == maxLength):
            poly2 += [0]*(maxLength - len(poly2))
        else:
            poly1 += [0]*(maxLength - len(poly1))

    def add_poly(self, poly1, poly2):
        self.makeTablesLenEqual(poly1, poly2)
        return map(op.add, poly1, poly2)

    def sub_poly(self, poly1, poly2):
        self.makeTablesLenEqual(poly1, poly2)
        return map(op.sub, poly1, poly2)


    def mul_poly(self, poly1, poly2):
        return np.polymul(poly1, poly2)


    def is_zero(self, poly):
        return all(i==0 for i in poly)

    def cmp_poly(self, poly1, poly2):
        self.makeTablesLenEqual(poly1, poly2)
        return poly1 == poly2

    def eval_poly(self, poly, x0):
        return np.polyval(poly, x0)

    def combine_poly(self, poly1, poly2):
        return np.polyval(poly1, poly2)

    def pow_poly(self, poly, n):
        return np.polypow(poly, n)

    def diff_poly(self, poly): pass               # pochodna wielomianu


obj = Polys()
print obj.cmp_poly([0,0], [0, 0, 0])
print obj.eval_poly([1, 0, 0], 2)
print obj.combine_poly([0,0,1], [0,1,2])
print obj.pow_poly([0, 1, 1], 2)
