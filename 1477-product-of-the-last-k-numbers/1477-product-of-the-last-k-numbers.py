class ProductOfNumbers:

    def __init__(self):
        self.prefixProd = [1]
        self.size = 0

    def add(self, num: int) -> None:
        
        if num == 0:
            self.prefixProd = [1]
            self.size = 0
        else:
            self.prefixProd.append(self.prefixProd[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return self.prefixProd[-1]//self.prefixProd[self.size - k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)