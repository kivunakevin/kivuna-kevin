class Laptop:
#Constructor to intialize the laptop object
    def _init_(self, brand, model, ram, storage):
        self.brand = Dell                  # Brand of the laptop 
        self.model = XPS 13                  # Model of the laptop 
        self.ram = 8 GB                    # RAM in GB 
        self.storage = 512 GB             # Storage capacity in GB 

#methods to display the laptop details
    def display(self):
        print("brand:", self.brand)
        print("model:", self.model)
        print("ram:", self.ram)
        print("storage:", self.storage)
        #method to boot laptop
        def boot_up(self):
        return f"{self.brand} {self.model} is booting up."