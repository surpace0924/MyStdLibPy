import add_path
import MyStdLibPy

if __name__ == '__main__':
    v1 = MyStdLibPy.Vector.Vector2(1, 1)
    v2 = MyStdLibPy.Vector.Vector2(2, 2)
    print((v1+v2+2).x)
