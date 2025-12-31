class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def createMat(self):
        data = []
        for i in range(self.row):
            r = []
            for j in range(self.col):
                num = int(input())
                r.append(num)
            data.append(r)
        self.mat = data

    def printMat(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.mat[i][j], end=" ")
            print()

    def addMatrix(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Rows & Cols must be same")
        res = []
        for i in range(self.row):
            r = []
            for j in range(self.col):
                x = self.mat[i][j] + other.mat[i][j]
                r.append(x)
            res.append(r)
        print(" A+B  : ")
        for i in range(self.row):
            for j in range(self.col):
                print(res[i][j], end=" ")
            print("")
        print("\n")

    def subMatrix(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError("Rows & Cols must be same")
        res = []
        for i in range(self.row):
            r = []
            for j in range(self.col):
                x = self.mat[i][j] - other.mat[i][j]
                r.append(x)
            res.append(r)
        print("A-B : ")
        for i in range(self.row):
            for j in range(self.col):
                print(res[i][j], end=" ")
            print()
        print("\n")


if __name__ == "__main__":
    m1, n1 = map(int, input("Enter r*c for mat 1: ").split())
    A = Matrix(m1, n1)
    A.createMat()
    A.printMat()

    m2, n2 = map(int, input("Enter r*c for mat 2: ").split())
    B = Matrix(m2, n2)
    B.createMat()
    B.printMat()
    A.addMatrix(B)
    A.subMatrix(B)
