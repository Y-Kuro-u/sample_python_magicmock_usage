class ExampleCache:
    def __init__(self):
      self.d = {}

    def set_cache(self, key: str, value: int) -> None:
      self.d[key] = value

    def get_cache(self, key: str) -> int:
      return self.d.get(key)

class Examples:
  def __init__(self):
    self.cache = ExampleCache()

  def add(self, a: int, b: int) -> None:
    """
    この関数をテストしたいが内部でcacheが呼ばれている
    """
    # cacheのkeyを作成する
    _f = f"{a}+{b}"

    result = a + b
    self.cache.set_cache(_f, result)

    return result