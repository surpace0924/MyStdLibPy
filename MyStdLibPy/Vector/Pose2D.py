##
# @file Pose2D.py
# @brief 2次元の座標を扱う

# -*- coding: utf-8 -*-
import numpy as np

##
# @class Pose2D
# @brief 2次元の座標を扱う


class Pose2D():
    ##
    # @brief コンストラクタ
    # @param _x: 2次元直交座標におけるx成分
    # @param _y: 2次元直交座標におけるy成分
    # @param _theta: 2次元直交座標における角度（向き）成分 [rad]
    def __init__(self, _x, _y, _theta):
        self.x = _x  # < 2次元直交座標におけるx成分
        self.y = _y  # < 2次元直交座標におけるy成分
        self.theta = _theta  # < 2次元直交座標における角度（向き）成分 [rad]

    ##
    # @brief 指定されたベクトルがこのベクトルと等しい場合にtrueを返す
    # @param v: 指定するベクトル
    def equals(self, v):
        return self == v

    ##
    # @brief 直交座標形式でこのベクトルを設定
    # @param _x: 指定するベクトル
    # @param _y: 指定するベクトル
    # @param _theta: 指定するベクトル
    def set(self, _x, _y, _theta):
        self.x = _x
        self.y = _y
        self.theta = _theta

    ##
    # @brief 極座標形式でこのベクトルを設定
    # @param r: 原点からの距離
    # @param angle: 原点との角度
    # @param robot_theta: ロボットの座標
    def setByPolar(self, r, angle, robot_theta):
        self.x = r * np.cos(angle)
        self.y = r * np.sin(angle)
        self.theta = robot_theta

    ##
    # @brief このベクトルを原点中心にangle[rad]回転
    # @param angle: 回転させる角度[rad]
    def rotate(self, angle):
        Vector2 p(0, 0)
        rotate(p, angle)

    ##
    # @brief 指定座標中心(rot_x, rot_y)に回転
    # @param rot_x: 回転中心のx座標
    # @param rot_y: 回転中心のy座標
    # @param angle: 回転させる角度[rad]
    def rotate(self, rot_x, rot_y, angle):
        Vector2 p(rot_x, rot_y)
        rotate(p, angle)

    ##
    # @brief 座標oを中心にangleだけ回転
    # @param o: 回転中心の座標
    # @param angle: 回転させる角度[rad]
    def rotate(self, Vector2 o, angle):
        Vector2 p(self.x - o.x, self.y - o.y)
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
        return magnitude()

    ##
    # @brief このベクトルの長さを返す
    # @return このベクトルの長さ
    def: magnitude(self):
        return np.sqrt(sqrMagnitude())

    ##
    # @brief このベクトルの長さの2乘を返す
    # @return このベクトルの長さ2乘
    def sqrLength():
        return sqrMagnitude()

    ##
    # @brief このベクトルの長さの2乘を返す
    # @return このベクトルの長さ2乘
    def sqrMagnitude(self):
        return x * x + y * y

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
        return std: : atan2(b.y - a.y, b.x - a.x)

    ##
    # @brief 2つのベクトルの距離を返す
    # @param a: 1つ目のベクトル
    # @param b: 2つ目のベクトル
    # @return 2つのベクトルの距離を返す
    def getDistance(self, a,  b):
        Pose2D v = (b - a)
        return v.magnitude()

    ##
    # @brief ベクトルaとbの間をtで線形補間
    # @param a: 1つ目のベクトル
    # @param b: 2つ目のベクトル
    # @param t: 媒介変数
    # @return 補間点
    def Pose2D leap(self, a, b, t):
        t = guard(t, 0.0, 1.0)
        Pose2D v = a
        v.x += (b.x - a.x) * t
        v.y += (b.y - a.y) * t
        v.theta += (b.theta - a.theta) * t
        return v

    # ##
    # # @brief 全ての要素にスカラ加算
    # constexpr Pose2D operator+() const
    # return *this

    # ##
    # # @brief 全ての要素にスカラ減算

    # constexpr Pose2D operator-() const

    # return -x, -y, -theta

    # ##
    # # @brief ベクトルの要素同士の和

    # constexpr Pose2D operator+(consPose2D & v) const

    # return x + v.x, y + v.y, theta + v.theta

    # ##
    # # @brief ベクトルの要素同士の差

    # constexpr Pose2D operator-(consPose2D & v) const

    # return x - v.x, y - v.y, theta - v.theta

    # ##
    # # @brief 全ての要素にスカラ乗算
    # # @attention ベクトル同士の乗算は未定義，内積の計算はgetDot()を使用

    # constexpr Pose2D operator*(s) const

    # return x * s, y * s, theta * s

    # ##
    # # @brief 全ての要素にスカラ除算
    # # @attention ベクトル同士の除算は未定義

    # constexpr Pose2D operator/(s) const

    # return x / s, y / s, theta / s

    # ##
    # # @brief ベクトルの要素同士の和を代入（スカラとの和の場合は全ての要素に対して加算）

    # Pose2D & operator += (consPose2D & v)

    # x += v.x
    # y += v.y
    # theta += v.theta
    # return *this

    # ##
    # # @brief ベクトルの要素同士の差を代入（スカラとの和の場合は全ての要素に対して減算）

    # Pose2D & operator -= (consPose2D & v)

    # x -= v.x
    # y -= v.y
    # theta -= v.theta
    # return *this

    # ##
    # # @brief 全ての要素に対してスカラ乗算して代入（ベクトル同士の乗算は未定義）

    # Pose2D & operator *= (s)

    # x *= s
    # y *= s
    # theta *= s
    # return *this

    # ##
    # # @brief 全ての要素に対してスカラ除算して代入（ベクトル同士の除算は未定義）

    # Pose2D & operator /= (s)

    # x /= s
    # y /= s
    # theta /= s
    # return *this

    # ##
    # # @brief 2つのベクトルが等しい場合にtrueを返す

    # bool operator == (consPose2D & v) const

    # return ((x == v.x) & & (y == v.y) & & (theta == v.y))

    # ##
    # # @brief 2つのベクトルが等しい場合にfalseを返す

    # bool operator != (consPose2D & v) const

    # return !((x == v.x) & & (y == v.y) & & (theta == v.y))
