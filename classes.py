
class Mario :
    _lives = 3.0
    _speed = 30.0

    def test(self):
        print("test")
        print("Speed is : ", self._speed)

instanceMario = Mario()
print(instanceMario._lives)
instanceMario.test()
Mario._lives = 1000000
print(instanceMario._lives)
