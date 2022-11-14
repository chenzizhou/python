def foo(s):
    n = int(s)
    # 程序中如果到处充斥着assert，和print()相比也好不到哪去。
    # 不过，启动Python解释器时可以用-O参数来关闭assert
    # 关闭后，你可以把所有的assert语句当成pass来看。

    assert n != 0,'n is zero!'
    return 10 / n

def main():
    foo('0')
main()