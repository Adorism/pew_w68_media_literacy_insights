import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns

class BarNums():

    def __init__(self, df, q_cols, dem_cols):
        self.df = df
        self.q_cols = q_cols
        self.dem_cols = dem_cols

    def horizon_bars(self):
        for facet in self.dem_cols:
            for answer in self.q_cols:
                sns.set(style="darkgrid")
                sns.set_palette("hls", 3)
                fig, ax = plt.subplots(figsize=(20, 5))
                ax = sns.countplot(x = facet, hue = answer, data= self.df)

                for p in ax.patches:
                    height = p.get_height()
                    ax.text(p.get_x()+p.get_width()/2, 
                    height + 3, 
                    '{:1.2f}'.format(height/self.df.shape[0]),
                    ha = "center")
                    
                    plt.savefig(f'../images/chi-{facet}-{answer}.png')


if __name__ == "__main__":
    BarNums()