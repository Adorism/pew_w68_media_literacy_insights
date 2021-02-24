class CrossTab():


    def __init__ (self, df, q_list, demo_list):
        self.df = df
        self.q_list = q_list
        self.demo_list = demo_list

    def cross_tabulation(self):
        for facet in self.demo_list:
            for answer in self.q_list:
                crosstab = pd.crosstab(df[facet], df[answer], normalize='index')
                crosstab_normalized = crosstab.div(crosstab.sum(1).astype(float), axis=0)
                crosstab_normalized.plot(kind='bar', stacked=True, title='Default by ' + str(attribute) + ' class')

                plt.savefig(f'./images/{facet}-{answer}") #outputs blank file

if name == __main___: 
    CrossTab()
