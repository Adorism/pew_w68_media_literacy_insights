# Media Literacy Insights from PEW Research Center's American Trends Panel: Wave 68 

![Intro image with a cellphone opened to headlines and the guiding question for this dataset exploration](./images/News%20Media%20Literacy.png)

## Background
For the past five years, I have worked as a school librarian teaching information literacy skills to students in grades PK-12. Often, my instruction focuses on media literacy. Because of my job, I have been keenly aware of the challenges involved in discerning factual information from information that is sensational, misleading, faulty, or propagandistic. I often find myself wondering what the factors are that make us more or less prone to accepting faulty information? What are the factors that play into making it more difficult ot find good information? The pandemic has served to highight the importance 

What factors are the most significant indicators that a population will have a difficult time finding their way through today's information landscape in search of vital information? Addtionally, I wonder, if there are demographic factors playing an important role in fact fining and media use, is there anything we can do to improve the outcomes for those demographics?

<br>
I am using survey information made available by the PEW research center's American Trends Panel: Wave 68 to seek insights on demographic factors as they relate to media literacy issues. I was excited to see that this dataset contains survey questions relating to media consumption as it related to coverage of the COVID-19 pandemic. 

## Data
My dataset consists of 146 columns and 9654 rows. Each row represents a survey respondent. For the purposes of my analysis, I have pulled out 26 rows to examine the data more closely. 15 of those rows are categorized answers to survey questions relating to media coverage of the pandemic. The other ten rows list demographic qualities of respondents. The survey questions I chose to focus on are specifically related to the consumption of news and media literacy. 

More information about the columns I chose to investigate can be found in a seperate .md file in the data directory. 

## Process and Methodology
The survey results are encoded and answers are categorical, rather than truly numeric. Therefore, I used Spearman's Rank Order Correlation to examine relationships between pairs of variables. 
<br><br>
Graphing<br>
Explanation of contingency tables<br>
Explanation of chi-sq testing<br>
Cramer's V Chi-square statistic: measures the strength of association between two nominal variables. 
0 = no association between the two variables 
1 = a string association between two variables<br>
![Formula for Cramer's V](https://www.empirical-methods.hslu.ch/files/2017/02/calculating-the-cramers-v-coefficient-chi-square-contingency.png)<br>

## Key Insights

## Future Considerations
<br>
From a technical perspective: 

I know that there is a sizeable industry focused solely on administering and interpreting surveys. 

There are incredibly useful data vizualization tools on the market that can enhance the readability of the charts I created, making the message more clear. One of those, which I tested out, is called "Flourish" (hyperlink it) and I was curious to try it out because I saw some interesting vizualizations on the web that had been created using this tool. I was looking, specifically, for a tool that could approximate the approach of many vizualizations that PEW Research creates using their own datasets, where a horizontal stacked barchart has a mid-point signifying a shift from positive to negative values. And example of such a chrt can be found here. https://www.pewresearch.org/politics/?attachment_id=20077157 When I used normalized values from contingency tables as the input for a graph on Flourish, I was able to create a rough, albeit imperfect approximation of the way that data is displayed in the PEW chart I linked. I want to know more about chart building tools in Python to see if similar graphing capabilities exist using Python. 

From the perspective of subject-area interest:
I want to know more about practical ways to make news media more useful to people in politically charged times and also, to investigate teachable strategies for news and online media consumers to improve meta-cognition in determining the trustworthines of an information source. 

## Code

## Notes

## References
“An Introduction to the Chi-Square Test & When to Use It | SurveyGizmo.” 2018. Alchemer. https://www.surveygizmo.com/resources/blog/introduction-to-chi-square-test-and-when-to-use-it/ (February 23, 2021).<br>
“Catplot Python Seaborn: One Function to Rule All Plots With Categorical Variables.” 2019. Python and R Tips. https://cmdlinetips.com/2019/03/catplot-in-seaborn-python/ (February 23, 2021).<br>
Chambliss, Charlene. 2019. “Cleaning, Analyzing, and Visualizing Survey Data in Python.” Medium. https://towardsdatascience.com/cleaning-analyzing-and-visualizing-survey-data-in-python-42747a13c713 (February 23, 2021).<br>
Custer, Charlie. 2019. “How to Analyze Survey Data with Python for Beginners.” Dataquest. https://www.dataquest.io/blog/how-to-analyze-survey-data-python-beginner/ (February 22, 2021).<br>
“Kendall Tau Metric - Encyclopedia of Mathematics.” https://encyclopediaofmath.org/index.php?title=Kendall_tau_metric (February 22, 2021).<br>
Mitchell, Amy, Mark Jurkowitz, J. Baxter Oliphant, and Elisa Shearer. 2021. “Methodology.” Pew Research Center’s Journalism Project. https://www.journalism.org/2021/02/22/how-americans-navigated-the-news-in-2020-methodology/ (February 22, 2021).<br>
NW, 1615 L. St, Suite 800Washington, and DC 20036USA202-419-4300 | Main202-857-8562 | Fax202-419-4372 | Media Inquiries. “American News Pathways.” Pew Research Center. https://www.pewresearch.org/topics/american-news-pathways/ (February 22, 2021).<br>
“Ordinal Association.” Statistics Solutions. https://www.statisticssolutions.com/ordinal-association/ (February 22, 2021).<br>
“Plotting with Categorical Data — Seaborn 0.11.1 Documentation.” http://seaborn.pydata.org/tutorial/categorical.html?highlight=bar%20plot (February 23, 2021).<br>
“Scipy.Stats.Chisquare — SciPy v1.6.1 Reference Guide.” https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html (February 23, 2021).<br>
“Spearman’s Rank-Order Correlation - A Guide to When to Use It, What It Does and What the Assumptions Are.” https://statistics.laerd.com/statistical-guides/spearmans-rank-order-correlation-statistical-guide.php (February 22, 2021).<br>
“(Tutorial) Handling Categorical Data in Python.” 2020. DataCamp Community. https://www.datacamp.com/community/tutorials/categorical-data (February 22, 2021).<br>
“Understanding Chi Square | Practical Surveys.” https://practicalsurveys.com/reporting/chisquare.php (February 23, 2021).<br>

Image source for Intro : <span>Photo by <a href="https://unsplash.com/@thenewmalcolm?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Obi Onyeador</a> on <a href="https://unsplash.com/s/photos/news?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
