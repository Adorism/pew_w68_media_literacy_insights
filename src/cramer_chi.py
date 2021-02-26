#loads
import scipy.stats as stats
import numpy as np
import pandas as pd
import csv

class ContTabs():

    def __init__(self, df, q_cols, dem_cols):
        self.df = df
        self.q_cols = q_cols
        self.dem_cols = dem_cols
        
        

#First I want to create a contingency table for each pairing of demographic facet and question/answer
    def cont_tables(self):
        tables = []
        facets = []
        answers = []

        for facet in self.dem_cols:
            for answer in self.q_cols:
                table = pd.crosstab(self.df[facet], [answer], normalize = 'index')
                tables.append(table)
                facets.append(facet)
                answers.append(answer)

        return tables, facets, answers

        
#Then I want to apply Cramer's chi square test to each of the dataframes output and write the results to a text file
    def cram_chi(self):
        tables, facets, answers = self.cont_tables()    
        chi_results = open('../data/chiresults.txt', 'w')
        for data in tables:
            #data = pandas.DataFrame(data).tonumpy()
            num = 0 

            '''
            chi2 = stats.chi2_contingency(data)[0]
            n = data.sum().sum()
            phi2 = chi2/n
            r,k = data.shape
            phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))    
            rcorr = r - ((r-1)**2)/(n-1)
            kcorr = k - ((k-1)**2)/(n-1)
            newline =  np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))
            '''

            chi2, p, dof, _ = stats.chi2_contingency([data.iloc[0].values,data.iloc[1].values])
           
            addition = f"The Pearson's Chi-Squared test result for {facets[num]} and {answers[num]}:  \n chi2 : {chi2} \n p-value: {p} \n Degrees of Freedom: {dof}"
            chi_results.write("\n")
            chi_results.write(addition)
            num +=1

        print("Your results are ready")
        chi_results.close()

                


if __name__ == "__main__":
    ContTabs()
