class Data:
    def __init__(self, df):
        self.df = df

    def null_count(self):
        return self.isnull().sum().sum()

    def list_2_series(self, li):
        return self.append(li)


pass
