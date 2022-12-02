class Elf: 
    def __init__(self, calArr) -> None:
        self.calArr = calArr
        self.totalCal = sum(map(int, calArr))


