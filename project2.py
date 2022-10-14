import pandas as pd
csv_path='data.csv'
df=pd.read_csv(csv_path)
df.head()
#print(df)
#expenditure = df.iloc[0,0]
#print(expenditure)
i=0
while i<50:
	a1=df.iloc[i,0]
	a2=df.iloc[i,1]
	a3=df.iloc[i,2]
	a4=df.iloc[i,4]
	b=a1+a3+a2
	
	
	if b<a4:
		print(df.iloc[i,3]+" is in profit");
	if b>a4:
		print(df.iloc[i,3]+" is in loss");
	
		
	i=i+1