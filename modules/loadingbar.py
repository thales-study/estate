import time
class LoadingBar():
  def __init__(self, total, size = 50):
    """
    初始化
    """
    self._size = size
    self._total = total
  def start(self):
    """
    loading开始
    """
    self._start = time.perf_counter()
    print(r"{:-^{}}".format("开始执行", self._size))
  def process(self, step):
    """
    loading进行
    @param  step  步骤
    """
    now = time.perf_counter() - self._start
    rate = step / self._total
    star = "=" * int(rate * self._size)
    print("\r{:.2%}[{:-<{}}]{:.2f}s".format(rate, star, self._size, now), end='')
  def end(self):
    """
    loading结束
    """
    print("\n{:-^{}}".format("执行结束", self._size))
