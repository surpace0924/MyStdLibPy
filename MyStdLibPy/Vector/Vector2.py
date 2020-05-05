##
# @file Vector2.py
# @brief 2要素のベクトル


# -*- coding: utf-8 -*-
import numpy as np

##
# @class Pose2D
# @brief 2要素のベクトル


class Vector2:
    ##
    # @brief コンストラクタ 直交座標(_x, _y)で初期化
    def __init__(self, _x, _y):
        self.x = _x  # < 2次元直交座標におけるx成分
        self.y = _y  # < 2次元直交座標におけるy成分

    ##
    # @brief 指定されたベクトルがこのベクトルと等しい場合にtrueを返す
    # @param v: 指定するベクトル
    def equals(self, v):
        return self == v

    ##
    # @brief このベクトルの大きさを1にする
    def normalize(self):
        self /= self.length()

    ##
    # @brief 直交座標形式でこのベクトルを設定
    # @param _x: 指定するベクトル
    def set(self, _x,  _y):
        self.x = _x
        self.y = _y

    ##
    # @brief 極座標形式でこのベクトルを設定
    # @param r: 原点からの距離
    # @param angle: 原点との角度
    def setByPolar(self, r,  angle):
        self.x = r * np.cos(angle)
        self.y = r * np.sin(angle)

    ##
    # @brief このベクトルを原点中心にangle[rad]回転
    # @param angle: 回転させる角度[rad]
    def rotate(self, angle):
        p = Vector2.Vector2(0, 0)
        rotate(p, angle)

    ##
    # @brief 指定座標中心(rot_x, rot_y)に回転
    # @param rot_x: 回転中心のx座標
    # @param rot_y: 回転中心のy座標
    # @param angle: 回転させる角度[rad]
    def rotate(self, rot_x,  rot_y,  angle):
        p = Vector2.Vector2(rot_x, rot_x)
        rotate(p, angle)

    ##
    # @brief 座標oを中心にangleだけ回転
    # @param o: 回転中心の座標
    # @param angle: 回転させる角度[rad]
    def rotate(self, o, angle):
        p = Vector2.Vector2(self.x - o.x, self.y - o.y)
        p.rotate(angle)
        p.x += o.x
        p.y += o.y
        x = p.x
        y = p.y

    ##
    # @brief このベクターをフォーマットした文字列を返す
    # @return フォーマットした文字列
    def toString(self):
        return '(' + self.x + ", " + self.y + ')'

    ##
    # @brief このベクトルの長さを返す
    # @return このベクトルの長さ
    def length(self):
        return self.magnitude()

    ##
    # @brief このベクトルの長さを返す
    # @return このベクトルの長さ
    def magnitude(self):
        return np.sqrt(self.sqrMagnitude())

    ##
    # @brief 大きさが1のこのベクトルを返す
    # @return 大きさが1のこのベクトル

    def normalized(self):
        return self / self.length(self)

    ##
    # @brief このベクトルの長さの2乘を返す
    # @return このベクトルの長さ2乘
    def sqrLength(self):
        return self.sqrMagnitude()

    ##
    # @brief このベクトルの長さの2乘を返す
    # @return このベクトルの長さ2乘
    def sqrMagnitude(self):
        return self.x ** 2 + self.y ** 2

    ##
    # @brief 2つのベクトルの内積を返す
    # @param a: 1つ目のベクトル
    # @param b: 2つ目のベクトル
    # @return 2つのベクトルの内積
    def getDot(self, a,  b):
        return (a.x * b.x + a.y * b.y)

    ##
    # @brief 2つのベクトルのなす角を弧度法で返す
    # @param a: 1つ目のベクトル
    # @param b: 2つ目のベクトル
    # @return 2つのベクトルのなす角[rad]
    def getAngle(self, a,  b):
        return np.tan2(b.y - a.y, b.x - a.x)

    ##
    # @brief 2つのベクトルの距離を返す
    # @param a: 1つ目のベクトル
    # @param b: 2つ目のベクトル
    # @return 2つのベクトルの距離を返す
    def getDistance(self, a,  b):
        p = Vector2.Vector2(b - a)
        return v.magnitude()

    ##
    # @brief ベクトルaとbの間をtで線形補間
    # @param a: 1つ目のベクトル
    # @param b: 2つ目のベクトル
    # @param t: 媒介変数
    # @return 補間点
    def leap(self, a, b, t):
        t = guard(t, 0.0, 1.0)
        v = a
        v.x += (b.x - a.x) * t
        v.y += (b.y - a.y) * t
        return v

    ##
    # @brief ベクトルの要素同士の和（スカラとの和の場合は全ての要素に対して加算）
    def __add__(self, other):
        if type(other) is Vector2:
            return self.__class__(self.x + other.x, self.y + other.y)
        else:
            return self.__class__(self.x + other, self.y + other)

    ##
    # @brief ベクトルの要素同士の和（スカラとの和の場合は全ての要素に対して加算）
    def __radd__(self, other):
        if type(other) is Vector2:
            return self.__class__(other.x + self.x, other.y + self.y)
        else:
            return self.__class__(other + self.x, other + self.y)

    ##
    # @brief ベクトルの要素同士の差（スカラとの差の場合は全ての要素に対して減算）
    def __sub__(self,  other):
        if type(other) is Vector2:
            return self.__class__(self.x - other.x, self.y - other.y)
        else:
            return self.__class__(self.x - other, self.y - other)

    ##
    # @brief ベクトルの要素同士の差（スカラとの差の場合は全ての要素に対して減算）
    def __rsub__(self, other):
        if type(other) is Vector2:
            return self.__class__(other.x - self.x, other.y - self.y)
        else:
            return self.__class__(other - self.x, other - self.y)

    ##
    # @brief 全ての要素にスカラ乗算
    # @attention ベクトル同士の乗算は未定義，内積の計算はgetDot()を使用
    def __mul__(self, other):
        return self.__class__(self.x * other, self.y * other)

    ##
    # @brief 全ての要素にスカラ乗算
    # @attention ベクトル同士の乗算は未定義，内積の計算はgetDot()を使用
    def __rmul__(self, other):
        return self.__class__(other * self.x, other * self.y)

    ##
    # @brief 全ての要素にスカラ除算
    # @attention ベクトル同士の除算は未定義
    def __truediv__(self, other):
        return self.__class__(self.x / other, self.y / other)

    ##
    # @brief 全ての要素にスカラ除算
    # @attention ベクトル同士の除算は未定義
    def __rtruediv__(self, other):
        return self.__class__(other / self.x, other / self.y)

    ##
    # @brief ベクトルの要素同士の和を代入（スカラとの和の場合は全ての要素に対して加算）
    def __iadd__(self, other):
        if type(other) is Vector2:
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other

    ##
    # @brief ベクトルの要素同士の差を代入（スカラとの差の場合は全ての要素に対して減算）
    def __isub__(self, other):
        if type(other) is Vector2:
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other

    ##
    # @brief 全ての要素に対してスカラ乗算して代入（ベクトル同士の乗算は未定義）
    def __imul__(self, other):
        self.x *= other
        self.y *= other

    ##
    # @brief 全ての要素に対してスカラ除算して代入（ベクトル同士の除算は未定義）
    def __itruediv__(self, other):
        self.x /= other
        self.y /= other

    ##
    # @brief 2つのベクトルが等しい場合にtrueを返す
    def __eq__(self, v):
        return self.x == Vector2.x and self.y == Vector2.y

    ##
    # @brief 2つのベクトルが等しい場合にfalseを返す
    def __ne__(self, other):
        return not(self == other)
