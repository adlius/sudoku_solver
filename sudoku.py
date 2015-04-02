__author__ = 'yl3ak'

class sudoku:
    rows = []
    columns = []
    def __init__(self):
        for i in range(9):
            self.rows.append([])
            self.columns.append([])

    def __str__(self):
        string = self.get_row(0).__str__() + "\n"
        for i in range(1,9):
            string = string + self.get_row(i).__str__() +"\n"

        return string

    def initialize(self,file_name):
        file = open(file_name,"r")
        row_num = 0
        for r in range(9):
            for lines in file:
                for symbols in lines:
                    if symbols is not "\n":
                        self.rows[row_num].append(int(symbols))
                row_num = row_num + 1

        for r in self.rows:
            column_num = 0
            for item in r:
                self.columns[column_num].append(item)
                column_num = column_num + 1

    def get_row(self,row_num):
        return self.rows[row_num]


    def get_column(self,column_num):
        return self.columns[column_num]

    def get_region(self,row_num,column_num):
        region_dict = {0:0,1:0,2:0,3:3,4:3,5:3,6:6,7:6,8:6}
        region = []
        r = region_dict[row_num]
        c = region_dict[column_num]
        rlimit = r+3
        climit = c+3
        for i in range(r,rlimit):
            for j in range(c,climit):
                region.append(self.get_row(i)[j])
        return region

    def is_row_conflict(self,value,row_num):
        if value in self.get_row(row_num):
            return True
        else:
            return False

    def is_column_conflict(self,value,column_num):
        if value in self.get_column(column_num):
            return True
        else:
            return False

    def is_region_conflict(self,value,row_num,column_num):
        if value in self.get_region(row_num,column_num):
            return True
        else:
            return False

    def fill_in_blank(self,value,row_num,column_num):
        self.rows[row_num][column_num] = value
        self.columns[column_num][row_num] = value

    def is_empty(self,row_num,column_num):
        if self.get_row(row_num)[column_num] == 0:
            return True
        else:
            return False

    def is_conflict(self,value,row,column):
        if not self.is_column_conflict(value,column) and not self.is_row_conflict(value,row) and not self.is_region_conflict(value,row,column):
            return False
        else:
            return True

    def is_solved(self):

        for i in range(9):
            for j in range(9):
                if self.rows[i][j] == 0:
                    return False

        return True

def find_empty_location(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku.is_empty(row,col):
                return [row,col]
    return False

def solve(sudoku):


    if not find_empty_location(sudoku):
        return True
    else:
        coor = find_empty_location(sudoku)
        row = coor[0]
        col = coor[1]

    for num in range(1,10):
        if not sudoku.is_conflict(num,row,col):
            sudoku.fill_in_blank(num,row,col)
            if solve(sudoku) == True:
                print(sudoku)
                return True
            sudoku.fill_in_blank(0,row,col)

    return False



def run():
    su = sudoku()
    su.initialize("sudoku_file.txt")
    solve(su)
    print(su)

run()