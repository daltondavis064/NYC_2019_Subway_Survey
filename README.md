## 1-6-2025
Found the [2019 New York Subway Rider Survey](https://catalog.data.gov/dataset/2019-subway-rider-survey) on data.gov link

Had some simple questions and wanted to clean up the data to make sure it was more useful.

For the repository there are a few files, the original csv uploaded the the link above, the cleaned csv and the python file used to clean the data set along with reasoning for the cleans in this readme file and in the Python code itself.

Approaching this data with a few questions in mind of what the data could be used for
- What the top three complaints are.
- How often riders who were surveyed use the system.
- How frequent the delays have been for those who completed the survey.

With this in mind I wanted to make sure the data was cleaned and had answers for at least one of the three columns when looking at the data. Since the dataset is large enough I thought it would be okay to include some null values for some rows of data as there should be enough data to get the answers we required.

First the information that I think would be irrelevant to the data set with the questions in mind: the first three columns that come to mind would be how the riders get to the subway station (get_to_subway_via), their primary use (primary_use_of_subway) and the location information (survey_stop_borough, survey_stop_location, and zip_code) as this was not gathered in full on the online form - if my questions had been about where in the boroughs did riders think an increase in fares was most well received this information would be included and would include in any writeup on analysis of the data that these fields should be made mandatory for online submission of the form if this was to be done again to gauge feedback after possible changes.

Next I went through and deleted rows that did not have enough data of the columns that we were looking at.

Lastly the top_three_complaints needed to be split up into the columns complaint_1, complaint_2,and complaint_3

## 1-7-2025
Ran into an issue where some online responders filled out more than 3 responses to the top three complaints questions which caused an issue when splitting the column. To avoid this in the future if this survey were to be done again, I would recommend the team in charge make the form only allow up to three options.

I ended up having to split the columns into a new dataframe and drop the extra columns.

With that done there were extra characters that were not needed in the cells - primarily the ']', '[', and "'" characters.

I cleaned those up and then used the concat function in pandas to add the columns back into the newData dataframe that we were using to drop the NULL values from our riderSurvey dataframe.

I dropped the top_three_complaints column as we had those seperated out into individual columns.

Finally it output the data in our newData dataframe into a brand new csv file titled Edited_2019_Subway_Rider_Survey.csv finishing the cleaning and transformation of the data we downloaded into a usable csv for our data analysis.

