# Data directory

This project will combine the two data sources to create a new dataset. 
Delphi 
1. data: https://cmu-delphi.github.io/delphi-epidata/api/covidcast_signals.html
2. Exploring: https://delphi.cmu.edu/covidcast/ 
3. Accessing: https://cmu-delphi.github.io/delphi-epidata/api/covidcast.html#accessing-the-data 
This dataset contains information about the popularity/usage of a particular brand for each of the US states over a period of 1 year. For instance, the following table represents data for few brands in the month of June 2021 in the Texas region.

Safegraph:
1. https://docs.safegraph.com/docs/monthly-patterns (US) https://docs.safegraph.com/docs/weekly-patterns (CA) 
2. Summary statistics: https://docs.safegraph.com/docs/patterns-summary-statistics
3. Accessing: https://shop.safegraph.com/account/?poi=ALL&tab=downloads
The second data source will inform the public behavioural information, and the project will be using the following features:
1. COVID Symptom Searches on google: 'sum_anosmia_ageusia_smoothed_search' (source: Google):
This variable aggregates the Google search volume for symptoms related to COVID-19 such as anosmia (lack of smell) and ageusia (lack of taste). This variable is represented in arbitrary units that are normalized for overall search users, and scaled by the maximum value of the normalized popularity within a geographic region across a specific time range. Thus, values are not comparable across geographic regions.
2. Mask wearing habits: 'smoothed_wearing_mask_7d' (source: fb survey):
This variable estimates the percentage of people who wore a mask for most or all of the time while in public in the past 7 days; those not in public in the past 7 days are not counted. It is adjusted using survey weights to be demographically representative.
3. Vaccination: 'smoothed_wcovid_vaccinated_or_accept' (source: fb survey):
This variable estimates the percentage of respondents who either have already received a COVID vaccine or would definitely or probably choose to get vaccinated, if a vaccine were offered to them today. It is adjusted using survey weights to be demographically representative. This variable was discontinued as of Wave 11, May 19, 2021.

Data Licensces: 
Delphi-epidata operates under the MIT License. Copy of license: https://github.com/cmu-delphi/delphi-epidata/blob/dev/LICENSE 
You can learn more about Safegraph freely available datasets: https://docs.safegraph.com/docs/about-safegraph
