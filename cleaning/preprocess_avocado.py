import sqlite3

conn2016 = sqlite3.connect("../data/db/hab2016.db")
conn2017 = sqlite3.connect("../data/db/hab2017.db")
conn2018 = sqlite3.connect("../data/db/hab2018.db")

c1 = conn2016.cursor()
c2 = conn2017.cursor()
c3 = conn2018.cursor()

c1.execute('PRAGMA foreign_keys = ON')
c2.execute('PRAGMA foreign_keys = ON')
c3.execute('PRAGMA foreign_keys = ON')

# extract only the accumulated statistics for the regions

new_avocado_table = '''
    CREATE TABLE hab_regions_stats AS
        SELECT Geography, units_prior_year, units_current_year, dollars_prior_year, dollars_current_year, asp_prior_year, asp_current_year
        FROM hab_cleaned
        WHERE Geography IN ('California', 'West', 'Plains', 'South Central', 'Midsouth', 'Southeast', 'Great Lakes', 'Northeast');
    '''

c1.execute(new_avocado_table)
conn2016.commit()

c2.execute(new_avocado_table)
conn2017.commit()

c3.execute(new_avocado_table)
conn2018.commit()
