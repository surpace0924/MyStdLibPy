import AddPath

import MyStdLibPy
import MyStdLibPy.Vector.Pose2D as Pose2D
import MyStdLibPy.Control.FBController.PID as PID
import MyStdLibPy.Control.PurePursuitControl as PPC

if __name__ == '__main__':
    v1 = MyStdLibPy.Vector.Vector2(1, 1)
    v2 = MyStdLibPy.Vector.Vector2(2, 2)

    param = PID.param_t()
    param.mode = PID.Mode().pPID
    param.gain = PID.gain_t(2, 0, 0)
    pid = PID(param)
    pid.update(1, 0, 1)

    ppc_param = PPC.param_t()
    ppc_param.mode = PPC.Mode().diff
    ppc_param.fbc_linear = pid
    ppc_param.fbc_angular = pid

    path = [Pose2D(0, 0, 0), Pose2D(0, 1, 0), Pose2D(2, 3, 0)]
    ppc = PPC(ppc_param, path)
    ppc.update(1, Pose2D(0.5, 0.5, 3.14/4), 1)
    print(ppc.getControlVal().toString())
