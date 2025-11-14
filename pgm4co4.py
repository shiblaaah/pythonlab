class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __add__(self, other):
        h = self.h + other.h
        m = self.m + other.m
        s = self.s + other.s

        if s >= 60:
            m += s // 60
            s = s % 60
        if m >= 60:
            h += m // 60
            m = m % 60
        return Time(h, m, s)

    def display(self):
        print(f"{self.h} hr : {self.m} min : {self.s} sec")


print("Enter Time 1:")
t1 = Time(int(input("Hour: ")), int(input("Minute: ")), int(input("Second: ")))

print("Enter Time 2:")
t2 = Time(int(input("Hour: ")), int(input("Minute: ")), int(input("Second: ")))

t3 = t1 + t2
print("Sum of Time:")
t3.display()
