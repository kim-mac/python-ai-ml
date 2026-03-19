#Filesystem

class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    def __init__(self):
        self.container = []
        

    def add(self, value: int) -> None:
        self.container.append(value)
        self.container.sort()

    def delete(self, value: int) -> bool:
        if value in self.container:
            self.container.remove(value)
            return True
        return False

    def get_median(self) -> int:
       
        if not self.container:
            raise RuntimeError("Empty")
        return self.container[(len(self.container) - 1) // 2]
    

#Progressive Filesystem
from integer_container import IntegerContainer


class IntegerContainerImpl(IntegerContainer):

    def __init__(self):
        self.container = []

    def add(self, value: int) -> int:
        self.container.append(value)
        return len(self.container)

    def delete(self, value: int) -> bool:
        if value in self.container:
            self.container.remove(value)
            return True
        return False


#Progressive Filesystem part 2
from integer_container import IntegerContainer


class IntegerContainerImpl(IntegerContainer):

    def __init__(self):
        self.container = []

    def add(self, value: int) -> int:
        self.container.append(value)
        self.container.sort()
        return len(self.container)

    def delete(self, value: int) -> bool:
        if value in self.container:
            self.container.remove(value)
            return True
        return False
    
    def get_median(self) -> int | None:
        if not self.container:
            return None
        return self.container[(len(self.container) -1)//2]

    


