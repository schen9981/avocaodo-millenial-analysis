import sqlite3

total_conn = sqlite3.connect("../data/db/avocado_project.db")
total_c = total_conn.cursor()
total_c.execute('PRAGMA foreign_keys = ON')

# combines data from demographic database into project database file

create_tables_command1 = '''
    CREATE TABLE demographic (
        region TEXT,
        age INT,
        sex TEXT,
        pop2016 INT,
        pop2017 INT,
        pop2018 INT
    );
    '''


total_c.execute(create_tables_command1)
total_conn.commit()

attach_command1 = '''
    ATTACH DATABASE '../data/db/demographic.db' AS demographic_db;
'''

total_c.execute(attach_command1)

migrate_command1 = '''
    INSERT INTO demographic(region, age, sex, pop2016, pop2017, pop2018)
    SELECT REGION, AGE, SEX, POPULATION2016, POPULATION2017, POPULATION2018
    FROM demographic_db.accumulated_demographic;
'''

total_c.execute(migrate_command1)
total_conn.commit()

# combine data from hab2016 database into project database file

create_tables_command2 = '''
    CREATE TABLE hab2016 (
        region TEXT,
        units_prior_year DOUBLE,
        units_current_year DOUBLE,
        dollars_prior_year DOUBLE,
        dollars_current_year DOUBLE,
        asp_prior_year DOUBLE,
        asp_current_year DOUBLE
    );
    '''

total_c.execute(create_tables_command2)
total_conn.commit()

attach_command2 = '''
    ATTACH DATABASE '../data/db/hab2016.db' AS hab2016_db;
'''

total_c.execute(attach_command2)

migrate_command2 = '''
    INSERT INTO hab2016(region, units_prior_year, units_current_year, dollars_prior_year, dollars_current_year, asp_prior_year, asp_current_year)
    SELECT Geography, units_prior_year, units_current_year, dollars_prior_year, dollars_current_year, asp_prior_year, asp_current_year
    FROM hab2016_db.hab_regions_stats;
'''

total_c.execute(migrate_command2)
total_conn.commit()

# combine data from hab2017 database into project database file

create_tables_command3 = '''
    CREATE TABLE hab2017 (
        region TEXT,
        units_prior_year DOUBLE,
        units_current_year DOUBLE,
        dollars_prior_year DOUBLE,
        dollars_current_year DOUBLE,
        asp_prior_year DOUBLE,
        asp_current_year DOUBLE
    );
    '''

total_c.execute(create_tables_command3)
total_conn.commit()

attach_command3 = '''
    ATTACH DATABASE '../data/db/hab2017.db' AS hab2017_db;
'''

total_c.execute(attach_command3)

migrate_command3 = '''
    INSERT INTO hab2017(region, units_prior_year, units_current_year, dollars_prior_year, dollars_current_year, asp_prior_year, asp_current_year)
    SELECT Geography, units_prior_year, units_current_year, dollars_prior_year, dollars_current_year, asp_prior_year, asp_current_year
    FROM hab2017_db.hab_regions_stats;
'''

total_c.execute(migrate_command3)
total_conn.commit()

# combine data from hab2018 database into project database file

create_tables_command4 = '''
    CREATE TABLE hab2018 (
        region TEXT,
        units_prior_year DOUBLE,
        units_current_year DOUBLE,
        dollars_prior_year DOUBLE,
        dollars_current_year DOUBLE,
        asp_prior_year DOUBLE,
        asp_current_year DOUBLE
    );
    '''

total_c.execute(create_tables_command4)
total_conn.commit()

attach_command4 = '''
    ATTACH DATABASE '../data/db/hab2018.db' AS hab2018_db;
'''

total_c.execute(attach_command4)

migrate_command4 = '''
    INSERT INTO hab2018(region, units_prior_year, units_current_year, dollars_prior_year, dollars_current_year, asp_prior_year, asp_current_year)
    SELECT Geography, units_prior_year, units_current_year, dollars_prior_year, dollars_current_year, asp_prior_year, asp_current_year
    FROM hab2018_db.hab_regions_stats;
'''

total_c.execute(migrate_command4)
total_conn.commit()
