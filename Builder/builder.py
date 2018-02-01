#coding=utf-8
class Car(object):
    """产品
    """
    def __init__(self, name):
        self.name = name
        self.body = None
        self.engine = None
        self.tire = None

    def __str__(self):
        info = ("Name: {}".format(self.name),
                "Body: {}".format(self.body),
                "Engine: {}".format(self.engine),
                "Tire: {}".format(self.tire))
        return '\n'.join(info)

class CarBuilder(object):
    """建造者
    """
    def __init__(self):
        self.car = Car("Mercedes")

    def add_body(self, body):
        self.car.body = body

    def add_engine(self, engine):
        """AMG 5.5L V8 biturbo"""
        self.car.engine = engine

    def add_tire(self, tire):
        self.car.tire = tire

    def assemble_car(self):
        return self.car

class Engineer(object):
    """指挥者
    """
    def __init__(self):
        self.builder = None

    def construct_car(self, body, engine, tire):
        self.builder = CarBuilder()
        self.builder.add_body(body)
        self.builder.add_engine(engine)
        self.builder.add_tire(tire)
        return self.builder.assemble_car()

if __name__ == '__main__':
    engineer = Engineer()
    car = engineer.construct_car(body="G63",
                                 engine="AMG 5.5L V8 biturbo", tire="Michelin 18inch")
    print(car)
