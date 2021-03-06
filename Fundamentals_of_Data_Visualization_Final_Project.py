import pandas as pd
import altair as alt
import numpy as np


nhd0 = alt.Chart(data).mark_bar().encode(alt.X('Sex', title='Gender'), alt.Y('count()', title='Number of Patients'), color=alt.Color('Sex:N',
                                                                                       scale=alt.Scale(range=['orange', 'darkblue'])),
                                        column=alt.Column('ChestPainType:N', title='Chest Pain Types'),
                                        tooltip = [alt.Tooltip('count()', title='Number of Patients'), alt.Tooltip('Sex', title='Gender'),
                                                   alt.Tooltip('ChestPainType', title='Type of Chest Pain')]
                                       ).transform_filter(alt.FieldEqualPredicate(field='HeartDisease', equal=0)
                                                         ).properties(title='Types of Chest Pain in Patients Without Heart Disease')

hd0 = alt.Chart(data).mark_bar().encode(alt.X('Sex', title='Gender'), alt.Y('count()', title='Number of Patients'), color=alt.Color('Sex', title='Gender'),
                                        column=alt.Column('ChestPainType:N', title = 'Chest Pain Types'),
                                       tooltip = [alt.Tooltip('count()', title='Number of Patients'), alt.Tooltip('Sex', title='Gender'),
                                                   alt.Tooltip('ChestPainType', title='Type of Chest Pain')]
                                       ).transform_filter(alt.FieldEqualPredicate(field='HeartDisease', equal=1)
                                                         ).properties(title='Types of Chest Pain in Patients With Heart Disease')

alt.vconcat(nhd0,hd0)



hd1 = alt.Chart(data).mark_rect().encode(
    x=alt.X('Age:N', title="Age (Years)"),
    y=alt.Y('Sex:N', title="Gender"),
    color=alt.Color('MaxHR:Q', title="Maximum Heartrate (in BPMs)"),
    tooltip= [alt.Tooltip('MaxHR', title='Maximum Heartrate'), alt.Tooltip('Age'), alt.Tooltip('Sex')]
).transform_filter(alt.FieldEqualPredicate(field='HeartDisease', equal=1)
                  ).properties(title='Maximum Heartrate Levels in Patients With Heart Disease')

nhd1 = alt.Chart(data).mark_rect().encode(
    x=alt.X('Age:N', title="Age (Years)"),
    y=alt.Y('Sex:N', title="Gender"),
    color=alt.Color('MaxHR:Q', title="Maximum Heartrate (in BPMs)"),
    tooltip= [alt.Tooltip('MaxHR', title='Maximum Heartrate'), alt.Tooltip('Age'), alt.Tooltip('Sex')]
).transform_filter(alt.FieldEqualPredicate(field='HeartDisease', equal=0)
                  ).properties(title='Maximum Heartrate Levels in Patients Without Heart Disease')


alt.vconcat(nhd1, hd1)




nhd2 = alt.Chart(data).mark_circle().encode(x=alt.X('Age', title = 'Age (Years)'), y=alt.Y('RestingBP', title='Resting Blood Pressure (in mmHg)'),
                                           color=alt.Color('Sex', scale=alt.Scale(range=['red', 'blue'])),
                                           tooltip= [alt.Tooltip('Age'), alt.Tooltip('Sex', title='Gender'), alt.Tooltip('RestingBP', title='Resting Blood Pressure')]
                                           ).transform_filter(
    alt.FieldEqualPredicate(field='HeartDisease', equal=0)
).properties(title='Resting Blood Pressure Levels in Patients Without Heart Disease').interactive()

hd2 = alt.Chart(data).mark_circle().encode(x=alt.X('Age', title = 'Age (Years)'), y=alt.Y('RestingBP', title='Resting Blood Pressure (in mmHg)'),
                                          color=alt.Color('Sex', title='Gender', scale=alt.Scale(range=['red', 'blue'])),
                                          tooltip= [alt.Tooltip('Age'), alt.Tooltip('Sex', title='Gender'), alt.Tooltip('RestingBP', title='Resting Blood Pressure')]
                                           ).transform_filter(
    alt.FieldEqualPredicate(field='HeartDisease', equal=1)
).properties(title='Resting Blood Pressure Levels in Patients With Heart Disease').interactive()

threshold = alt.Chart(pd.DataFrame({'y': [120]})).mark_rule(strokeDash=[10,10]).encode(y='y')

alt.vconcat(nhd + threshold, hd + threshold)



nhd3 = alt.Chart(data).mark_circle().encode(x=alt.X('Age', title='Age (Years)'), y=alt.Y('Cholesterol', title='Cholesterol (in mg/dL)'), color=alt.Color('Sex',
                                                                                     scale=alt.Scale(range=['blue', 'green'])),
                                           tooltip= [alt.Tooltip('Age'), alt.Tooltip('Sex', title='Gender'), alt.Tooltip('Cholesterol')]
                                           ).transform_filter(
    alt.FieldEqualPredicate(field='HeartDisease', equal=0)
).properties(title='Cholesterol Levels in Patients Without Heart Disease').interactive()

hd3 = alt.Chart(data).mark_circle().encode(x=alt.X('Age', title='Age (Years)'), y=alt.Y('Cholesterol', title='Cholesterol (in mg/dL)'), color=alt.Color('Sex',
                                                                                     scale=alt.Scale(range=['blue', 'green'])),
                                          tooltip= [alt.Tooltip('Age'), alt.Tooltip('Sex', title='Gender'), alt.Tooltip('Cholesterol')]
                                           ).transform_filter(
    alt.FieldEqualPredicate(field='HeartDisease', equal=1)
).properties(title='Cholesterol Levels in Patients With Heart Disease').interactive()

threshold = alt.Chart(pd.DataFrame({'y': [200]})).mark_rule(strokeDash=[10,10]).encode(y='y')

res = nhd + threshold | hd + threshold

#avg_age = sum(data['Age'])/len(data['Age'])

#avg_high_cholesterol = sum(data[data['Cholesterol']>160]['Cholesterol']) / len(data[data['Cholesterol']>160]['Cholesterol'])
#avg_high_bp = sum(data[data['RestingBP']>120]['RestingBP']) / len(data[data['RestingBP']>120]['RestingBP'])
#avg_high_bp
#avg_high_cholesterol
alt.vconcat(nhd + threshold, hd + threshold)


high_cholesterol = data[data['Cholesterol']>200]
high_bpandchol = high_cholesterol[high_cholesterol['RestingBP']>120]

nhd4 = alt.Chart(high_bpandchol).mark_rect().encode(
    x=alt.X('Age:N', title="Age"),
    y=alt.Y('RestingBP:N', title="Resting Blood Pressure (in mmHg)"),
    color=alt.Color('Cholesterol:Q', title="Cholesterol Levels"),
    tooltip= [alt.Tooltip('Cholesterol', title='Cholesterol'), alt.Tooltip('Age'), alt.Tooltip('HeartDisease')]
).transform_filter(alt.FieldEqualPredicate(field='HeartDisease', equal=0)
                                          ).properties(title='Cholesterol and Blood Pressure Levels in Patients Without Heart Disease')


nhd4



hd4 = alt.Chart(high_bpandchol).mark_rect().encode(
    x=alt.X('Age:N', title="Age"),
    y=alt.Y('RestingBP:N', title="Resting Blood Pressure (in mmHg)"),
    color=alt.Color('Cholesterol:Q', title="Cholesterol Levels"),
    tooltip= [alt.Tooltip('Cholesterol', title='Cholesterol'), alt.Tooltip('Age'), alt.Tooltip('HeartDisease')]
).transform_filter(alt.FieldEqualPredicate(field='HeartDisease', equal=1
                                          )).properties(title='Cholesterol and Blood Pressure Levels in Patients With Heart Disease')

hd4

