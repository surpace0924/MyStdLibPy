# -*- coding: utf-8 -*-
##
# @file PID.py
# @brief PIDの計算

##
# @class PID
# @brief PIDの計算


class PID:
    ##
    # @brief モードリスト
    class Mode:
        def __init__(self):
            self.pPID = 0  # < 位置型PID
            self.sPID = 1  # < 速度型PID
            self.PI_D = 2  # < 微分先行型PID
            self.I_PD = 3  # < 比例微分先行型PID

    ##
    # @brief ゲイン構造体
    class gain_t:
        def __init__(self, Kp=0, Ki=0, Kd=0):
            self.Kp = Kp  # < 比例ゲイン
            self.Ki = Ki  # < 積分ゲイン
            self.Kd = Kd  # < 微分ゲイン

    ##
    # @brief パラメータ構造体
    class param_t:
        def __init__(self):
            self.mode = PID.Mode().pPID   # < PIDモード
            self.gain = PID.gain_t()      # < PIDゲイン
            self.need_saturation = False  # < 出力制限を行うか
            self.output_min = 0           # < 出力制限時の最小値
            self.output_max = 0           # < 出力制限時の最大値

    ##
    # @brief コンストラクタ
    def __init__(self, param=None):
        self.__param = param
        self.__diff = [0] * 3  # 0: 現在, 1: 過去, 2: 大過去
        self.__prev_val = 0
        self.__prev_target = 0
        self.__integral = 0
        self.__output = 0

    ##
    # @brief リセット
    def reset(self):
        for i in range(len(self.__diff[i])):
            self.__diff[i] = 0
        prev_val = prev_target = 0
        integral = 0
        output = 0

    ##
    # @brief パラメータの設定
    # @param param: パラメータ構造体
    def setParam(self, param):
        self.__param = param

    ##
    # @brief ゲインの設定
    # @param gain: ゲイン構造体
    def setGain(self, gain):
        self.__param.gain = gain

    ##
    # @brief PIDモードの設定
    # @param mode: PIDモードenum
    def setMode(self, mode):
        self.__param.mode = mode

    ##
    # @brief 出力の最小，最大値の設定
    # @param min_v: 最小値
    # @param min_v: 最大値
    def setSaturation(self, min_v, max_v):
        self.__param.need_saturation = True
        self.__param.output_min = min_v
        self.__param.output_max = max_v

    ##
    # @brief 値の更新
    # @param target: 目標値
    # @param now_val: 現在値
    # @param dt: 前回この関数をコールしてからの経過時間
    def update(self, target, now_val, dt):
        self.__diff[0] = target - now_val  # 最新の偏差
        self.__integral += (self.__diff[0] + self.__diff[1]) * (dt / 2.0)  # 積分

        if (self.__param.mode == PID.Mode().pPID):
            self.__output = self.__calculate_pPID(target, now_val, dt)
        elif (self.__param.mode == PID.Mode().pPID):
            self.__output = self.__calculate_sPID(target, now_val, dt)
        elif (self.__param.mode == PID.Mode().pPID):
            self.__output = self.__calculate_PI_D(target, now_val, dt)
        elif (self.__param.mode == PID.Mode().pPID):
            self.__output = self.__calculate_I_PD(target, now_val, dt)

        # 次回ループのために今回の値を前回の値にする
        self.__diff[2] = self.__diff[1]
        self.__diff[1] = self.__diff[0]
        self.__prev_target = target
        self.__prev_val = now_val

        # ガード処理
        if (self.__param.need_saturation):
            if (self.__output > self.__param.output_max):
                self.__output = self.__param.output_max
            if (self.__output < self.__param.output_min):
                self.__output = self.__param.output_min

    ##
    # @brief 制御量（PIDの計算結果）の取得
    # @return 制御量（PIDの計算結果）
    # @attention update()を呼び出さないと値は更新されない
    def getControlVal(self):
        return self.__output

    # 位置型PID
    def __calculate_pPID(self, target, now_val, dt):
        p = self.__param.gain.Kp * self.__diff[0]
        i = self.__param.gain.Ki * self.__integral
        d = self.__param.gain.Kd * ((self.__diff[0] - self.__diff[1]) / dt)
        return p + i + d

    # 速度型PID
    def __calculate_sPID(self, target, now_val, dt):
        p = self.__param.gain.Kp * self.__diff[0] - self.__diff[1]
        i = self.__param.gain.Ki * self.__diff[0] * dt
        d = self.__param.gain.Kd * \
            (self.__diff[0] - 2 * self.__diff[1] + self.__diff[2]) / dt
        return self.__prev_val + p + i + d

    # 微分先行型PID
    def __calculate_PI_D(self, target, now_val, dt):
        p = self.__param.gain.Kp * self.__diff[0]
        i = self.__param.gain.Ki * self.__integral
        d = -self.__param.gain.Kd * ((now_val - self.__prev_val) / dt)
        return p + i + d

    # 比例微分先行型PID
    def __calculate_I_PD(self, target, now_val, dt):
        p = -self.__param.gain.Kp * now_val
        i = self.__param.gain.Ki * self.__integral
        d = -self.__param.gain.Kd * ((now_val - self.__prev_val) / dt)
        return p + i + d
