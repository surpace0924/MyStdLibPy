# -*- coding: utf-8 -*-
##
# @file PurePursuitControl.h
# @brief PurePursuit制御（単純追従制御）

from enum import Enum
import MyStdLibPy.Vector.Pose2D as Pose2D
import MyStdLibPy.Control.FBController.PID as PID


##
# @class PurePursuitControl
# @brief PurePursuit制御（単純追従制御）

class PurePursuitControl:
    ##
    # @brief モードリスト
    class Mode:
        def __init__(self):
            self.diff = 0  # < 2DoF（差動二輪型） */
            self.omni = 1  # < 3DoF（全方位移動型） */

    ##
    # @brief パラメータ構造体
    class param_t:
        def __init__(self):
            self.mode = PurePursuitControl.Mode().diff   # < モード */
            self.fbc_linear = PID()   # < 並進用のフィードバックコントローラ */
            self.fbc_angular = PID()  # < 回転用のフィードバックコントローラ */

    ##
    # @brief コンストラクタ パラメータと経路データで初期化
    # @param param: パラメータ構造体
    # @param path: 経路データ（Pose2Dのリスト）
    def __init__(self, param=None, path=None):
        self.__param = param
        self.__path = path
        self.__output = Pose2D()

    ##
    # @brief 経路データの設定
    # @param path: 経路データ
    def setPath(self, path):
        self.__path.clear()
        self.__path = path

    ##
    # @brief パラメータの設定
    # @param param: パラメータ構造体
    def setParam(self, param):
        self.__param = param

    ##
    # @brief モードの設定
    # @param mode: モードリスト
    def setMode(self, mode):
        self.__param.mode = mode

    ##
    # @brief 追従用フィードバックコントローラの設定
    # @param fbc_linear: 並進用のフィードバックコントローラ
    # @param fbc_angular: 回転用のフィードバックコントローラ
    def setController(self, fbc_linear, fbc_angular):
        self.__param.fbc_linear = fbc_linear
        self.__param.fbc_angular = fbc_angular

    ##
    # @brief 経路データを末尾に追加
    # @param path: 経路データ（Pose2Dのリスト）
    def push_back(self, path):
        for i in range(len(path)):
            self.__path.push_back(path[i])

    ##
    # @brief 値の更新
    # @param target: 経路データのインデックス
    # @param now_val: 現在値
    # @param dt: 前回この関数をコールしてからの経過時間
    def update(self, idx, now_pose, dt):
        print(self.__path[idx].toString())
        print(now_pose.toString())
        distance = Pose2D.getDistance(now_pose, self.__path[idx])
        self.__param.fbc_linear.update(0, distance, dt)
        self.__output.x = self.__param.fbc_linear.getControlVal()

        angle = Pose2D.getAngle(now_pose, self.__path[idx]) - now_pose.theta
        self.__param.fbc_angular.update(0, angle, dt)
        self.__output.theta = self.__param.fbc_angular.getControlVal()

    ##
    # @brief 制御量（計算結果）の取得
    # @return 制御量（計算結果）
    # @attention update()を呼び出さないと値は更新されない
    def getControlVal(self):
        return self.__output
