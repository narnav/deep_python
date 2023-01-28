class Rectangel:
    def __init__(self):
        pass

    def __privateData(self):
        print("not allowed")

    def pubData(self):
        print("allowed")


r1 = Rectangel()
# r1.__privateData()  # raise error
r1.pubData()
r1.waga = "baga"  # new property - not all languages allow
