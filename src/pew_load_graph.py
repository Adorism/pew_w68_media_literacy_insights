import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyreadstat
import seaborn as sns

from pew_crosstab import Cross_Tab

w68spss, metaspss = pyreadstat.read_sav('../data/W68.sav', apply_value_formats = True, formats_as_category = True )

fields = ['COVIDFOL_W68', 
          'COVIDCOVER1_W68', 
          'COVIDFACTS_b_W68', 
          'COVIDNEWSCHNG_a_W68', 
          'COVIDNEWSCHNG_c_W68', 
          'COVIDNEWSCHNG_d_W68',
          'COVIDNEWSCHNG_e_W68',
          'COVIDINFODIFF_W68', 
          'COVIDLOCINFO_W68',
          'COVIDDEAL_W68', 
          'COVIDPLANHRD_W68', 
          'COVIDPLANTRUE_W68', 
          'COVIDPLANWATCH_W68', 
          'F_METRO', 
          'F_EDUCCAT',
          'F_PARTY_FINAL']

facets = ['F_METRO', 
          'F_EDUCCAT',
          'F_PARTY_FINAL']

answers = ['COVIDFOL_W68', 
          'COVIDCOVER1_W68', 
          'COVIDFACTS_b_W68', 
          'COVIDNEWSCHNG_a_W68', 
          'COVIDNEWSCHNG_c_W68', 
          'COVIDNEWSCHNG_d_W68',
          'COVIDNEWSCHNG_e_W68',
          'COVIDINFODIFF_W68', 
          'COVIDLOCINFO_W68',
          'COVIDDEAL_W68', 
          'COVIDPLANHRD_W68', 
          'COVIDPLANTRUE_W68', 
          'COVIDPLANWATCH_W68']

df68 = pd.DataFrame(w68spss)

graph = Cross_Tab()
graph(df68, answers, facets)

