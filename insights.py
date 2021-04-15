import streamlit as st
from pytrends.request import TrendReq
import pandas as pd 
from streamlit_tags import st_tags

# https://towardsdatascience.com/google-trends-api-for-python-a84bc25db88f
def interestbyRegion():
    try: 
        pytrends = TrendReq()
        interestOverTime(pytrends)
 
    except:
        pass

def interestOverTime(pytrends):
    st.info("__Interest over time__")
    keywords = st_tags(
    label='Enter Keywords (Max 5):',
    text='Press enter to add more',
    value=[],
    suggestions=['Singapore', 'USA', 'Malaysia'],
    key='1')
    pytrends.build_payload(keywords, timeframe='today 5-y', geo='') 
    InterestByRegionDF = pd.DataFrame(pytrends.interest_over_time()).drop(columns='isPartial')
    InterestByRegionDF = InterestByRegionDF.sort_index(ascending=False)
    InterestByRegionDF.index = InterestByRegionDF.index.strftime('%d/%m/%Y') # Index to %d/%m/%Y
    st.dataframe(InterestByRegionDF)
    st.info("100: Maximum search interest")

    # Line Chart
    InterestByRegionList = InterestByRegionDF.columns.tolist()
    interest_choices = st.multiselect("Choose to show graph: ", InterestByRegionList, default=None)
    new_df = InterestByRegionDF[interest_choices]
    st.line_chart(new_df)

# Get Google Keyword Suggestions
def googleKeywordSuggestions(pytrends):
    st.info("__Google Keyword Suggestion__")
    keyword = st.text_input("Enter Keyword")
    relatedKeywords = pytrends.suggestions(keyword=keyword)
    relatedKWDF = pd.DataFrame(relatedKeywords)
    relatedKWDF.drop(columns= 'mid', inplace=True)
    st.dataframe(relatedKWDF)

# Get Google Top Charts
def googleTopCharts(pytrends):
    googleTopChartDF = pytrends.top_charts(2019, hl='en-SG', tz=300, geo='GLOBAL')
    st.dataframe(googleTopChartDF)

# Get Google Hot Trends data
def googleHotTrends(pytrends):
    googleHotTrendDF = pytrends.trending_searches(pn='united_states')
    st.dataframe(googleHotTrendDF)

# Get Google Top Charts
def googleHotTrends(pytrends):
    googleHotTrendsDF = pytrends.top_charts(2019, hl='en-US', tz=300, geo='GLOBAL')
    st.dataframe(googleHotTrendsDF)

# Related Queries, returns a dictionary of dataframes
def relatedQueries(pytrends):
    st.info("__Related Keyword__")
    pytrends.build_payload(kw_list=['Coronavirus'])
    related_queries = pytrends.related_queries()
    related_queries.values()

# Related Topics, returns a dictionary of dataframes
def relatedQueries(pytrends):
    pytrends.build_payload(kw_list=['Coronavirus'])
    related_topic = pytrends.related_topics()
    related_topic.values()