#pycityschools

#dependencies

from pathlib import Path
import pandas as pd
import csv

School_Data_Path = Path("/Resources/schools_complete.csv")
Students_Data_Path = Path("/Resources/students_complete.csv")

#Make a DataFrame with those csv files

School_Data_df = pd.read_csv(School_Data_Path)
Students_Data_df = pd.read_csv(Students_Data_Path)

#Merge the two dataframe

School_and_students_df = pd.merge(School_Data_df, Students_Data_df, how="left", on=['school_name'])
School_and_students_df.head()



###DISTRICT SUMMARY###

#TOTAL NUMBER OF UNIQUE SCHOOLS#

Total_Number_of_Unique_Schools = School_and_students_df["school_name"].value_counts()
School_Type_Count = School_and_students_df["type"].unique()


Total_Number_of_Students = len(School_and_students_df[0])


Total_Budget = School_and_students_df["budget"].sum()

#Average Math Score
Average_Math_Score = School_and_students_df["math_score"].mean()

#Average Reading Score
Average_Reading_Score = School_and_students_df["reading_score"].mean()

Count_Passing_Math = School_and_students_df[(School_and_students_df["math_score"] >= 70)].count()["Student_Name"]
passing_math_percentage = Count_Passing_Math / float(Total_Number_of_Students) * 100


Count_Passing_Reading = School_and_students_df[(School_and_students_df["reading_score"] >=70)].count()["Student_Name"]
passing_reading_percentage = Count_Passing_Reading / float(Total_Number_of_Students) * 100








####SCHOOL SUMMARY####

School_Summary_df = pd.DataFrame({"School Name" : Total_Number_of_Unique_Schools,
                                  "School Type" : School_Type_Count,
                                  "Total Students" : Total_Number_of_Students,
                                  "Total School Budget" : Total_Budget,
                                  "Average Math Score" : Average_Math_Score,
                                  "Average Reading Score" : Average_Reading_Score})

                                  ###complete the rest at another time###})







