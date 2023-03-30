class Vehicles:
  def __init__(self, nm, ts):
    self._name = nm
    self._tires = ts

  def getName(self):
    return self._name


class Cars(Vehicles):
  def __init__(self, nm, ts, worth):
    super().__init__(nm, ts)
    self.worth = worth

class Trucks(Vehicles):
  def __init__(self, nm, ts, miles):
    super().__init__(nm, ts)
    self.miles = miles

class Buses(Vehicles):
  def __init__(self, nm, ts, hc):
    super().__init__(nm, ts)
    self.homecity = hc
    