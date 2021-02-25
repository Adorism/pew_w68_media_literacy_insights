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
    def ContTables(self):
        tables = []
        facets = []
        answers = []

        for facet in self.dem_cols:
            for answer in self.q_cols:
                table = df.crosstab([facet], [answer], normalize = 'index')
                tables.append(table)
                facets.append(facet)
                answers.append(answer)

        return tables, facets, answers

        
#Then I want to apply Cramer's chi square test to each of the dataframes output and write the results to a text file
    def CramChi(self):
        tables, facets, answers = self.ContTables()    
        chi_results = open('../data/chiresults.txt', 'w')
        for data in tables:
            num = 0 
            X2 = stats.chi2_contingency(data, correction=False)[0]
            n = np.sum(data)
            minDim = min(data.shape)-1
            V = np.sqrt((X2/n) / minDim)
            addition = [f'The chi test result for {facets[num]} and {answers[num]} is {V}']
            if len(chi_results) >0:
                chi_results.write("\n")
            chi_results.write(addition)
            num +=1
        chi_results.close()

                


if __name__ == "__main__":
    ContTabs()
