#importing packages
import pandas as pd

#reading the original csv file
riderSurvey = pd.read_csv("2019_Subway_Rider_Survey.csv")

#dropping the columns that we mentioned in the README
riderSurvey.drop(["get_to_subway_via", "primary_use_of_subway", "survey_stop_borough", "survey_stop_location", "zip_code"], axis = 1, inplace=True)

#removing lines with less than 2 of the three columns we want data on
newData = riderSurvey.dropna(axis=0, thresh=1, subset=["use_of_subway_frequency", "frequency_of_delays", "top_three_complaints"])

#printing the difference in lines
print("Original frame length: ", len(riderSurvey))
print("New data frame length: ", len(newData))
print("Number of rows with 3 NA values for the columns requested: ",len(riderSurvey) - len(newData))

#separating the "top_three_complaints" column
getComplaints = newData['top_three_complaints'].str.split(pat=', ', expand=True)

#found that some of the online responses had up to 8 complaints instead of 3, naming and dropping the extra columns
getComplaints = getComplaints.rename(columns= {0: 'complaint_1', 1: 'complaint_2', 2: 'complaint_3', 3: 'complaint_4', 4: 'complaint_5', 5:'complaint_6', 6:'complaint_7',7:'complaint_8'})
getComplaints.drop(["complaint_4", "complaint_5", "complaint_6", "complaint_7", "complaint_8"], axis = 1, inplace=True)

#cleaning the columns of data of unnecessary characters
getComplaints['complaint_1'] = getComplaints['complaint_1'].str.replace('[','',regex=True)
getComplaints['complaint_1'] = getComplaints['complaint_1'].str.replace("'",'',regex=True)
getComplaints['complaint_1'] = getComplaints['complaint_1'].str.replace(']','',regex=True)
getComplaints['complaint_2'] = getComplaints['complaint_2'].str.replace('[','',regex=True)
getComplaints['complaint_2'] = getComplaints['complaint_2'].str.replace("'",'',regex=True)
getComplaints['complaint_2'] = getComplaints['complaint_2'].str.replace(']','',regex=True)
getComplaints['complaint_3'] = getComplaints['complaint_3'].str.replace('[','',regex=True)
getComplaints['complaint_3'] = getComplaints['complaint_3'].str.replace("'",'',regex=True)
getComplaints['complaint_3'] = getComplaints['complaint_3'].str.replace(']','',regex=True)

#adding the columns back to our original data
newData = pd.concat([newData,getComplaints], axis=1)

#removing the top three complaints column now that we have them seperated
newData.drop(['top_three_complaints'], axis=1, inplace=True)

#output the new file
newData.to_csv("Edited_2019_Subway_Rider_Survey.csv", index=False)