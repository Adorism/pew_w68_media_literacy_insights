import matplotlib.pyplot as plt
import pandas as pd
import pyreadstat


from pew_crosstab import CrossTab
from pew_bars import BarNums
from cramer_chi import ContTabs

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

#un-comment the Class you want to run. Or do them simultaneously to get all of the plots in one run. 
#graph = CrossTab(df = df68, q_list=answers, demo_list=facets)
#graph.cross_tabulation()

#viz_plots = BarNums(df=df68, q_cols=answers, dem_cols=facets)
#viz_plots.horizon_bars()

chis = ContTabs(df=df68, q_cols=answers, dem_cols=facets)
chis.cram_chi()