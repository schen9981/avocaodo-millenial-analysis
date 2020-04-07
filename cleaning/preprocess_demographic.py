import sqlite3


conn = sqlite3.connect('../data/db/demographic.db')
c = conn.cursor()
c.execute('PRAGMA foreign_keys = ON')

# remove hawaii, alaska, united states from demographic
remove_states = '''
    DELETE FROM cleaned_demographic
    WHERE NAME = 'Hawaii' OR NAME = 'Alaska' OR NAME = 'United States';
    '''

c.execute(remove_states)
conn.commit()


# adds column that specifies the corresponding region that each state belongs to
add_region_column = '''
    ALTER TABLE cleaned_demographic
    ADD REGION TEXT;
    '''
c.execute(add_region_column)
conn.commit()

region_command = '''
    UPDATE cleaned_demographic
    SET REGION = (CASE  WHEN NAME IN ('California') THEN 'California'
                        WHEN NAME IN ('Washington', 'Oregon', 'Idaho', 'Montana', 'Wyoming', 'Nevada', 'Utah', 'Colorado', 'Arizona', 'New Mexico') THEN 'West'
                        WHEN NAME IN ('North Dakota', 'South Dakota', 'Nebraska', 'Kansas', 'Missouri', 'Iowa', 'Minnesota') THEN 'Plains'
                        WHEN NAME IN ('Texas', 'Oklahoma', 'Arkansas', 'Louisiana') THEN 'South Central'
                        WHEN NAME IN ('Tennessee', 'Kentucky', 'North Carolina', 'Virginia', 'West Virginia', 'Maryland', 'Delaware') THEN 'Midsouth'
                        WHEN NAME IN ('Florida', 'Mississippi', 'Alabama', 'Georgia', 'South Carolina') THEN 'Southeast'
                        WHEN NAME IN ('Illinois', 'Wisconsin', 'Michigan', 'Indiana', 'Ohio') THEN 'Great Lakes'
                        WHEN NAME IN ('Rhode Island', 'New York', 'New Jersey', 'Pennsylvania', 'Connecticut', 'Maine', 'New Hampshire', 'Vermont', 'Massachusetts', 'District of Columbia') THEN 'Northeast'
                        ELSE 'NA' END);
    '''

c.execute(region_command)
conn.commit()

# take region X. for each state in region X, add corresponding population for each age
accumulate_population_command = '''
    CREATE TABLE accumulated_demographic AS
        SELECT REGION, CAST(AGE AS INT) AS AGE, SEX, SUM(POPEST2016_CIV) AS POPULATION2016, SUM(POPEST2017_CIV) AS POPULATION2017, SUM(POPEST2018_CIV) AS POPULATION2018
        FROM cleaned_demographic
        GROUP BY REGION, AGE, SEX
        ORDER BY REGION, AGE;
    '''

c.execute(accumulate_population_command)
conn.commit()
