import pandas as pd
import sqlite3


##### Part 1: Basic Filtering #####

# Connect to the planets database.
conn1 = sqlite3.connect("planets.db")


# STEP 1
# Return all columns for planets that have 0 moons.
df_no_moons = pd.read_sql(
    """
    SELECT *
    FROM planets
    WHERE num_of_moons = 0;
    """,
    conn1,
)


# STEP 2
# Return the name and mass of planets whose names contain exactly 7 letters.
df_name_seven = pd.read_sql(
    """
    SELECT name, mass
    FROM planets
    WHERE LENGTH(name) = 7;
    """,
    conn1,
)


##### Part 2: Advanced Filtering #####

# STEP 3
# Return the name and mass of planets with mass less than or equal to 1.00.
df_mass = pd.read_sql(
    """
    SELECT name, mass
    FROM planets
    WHERE mass <= 1.00;
    """,
    conn1,
)


# STEP 4
# Return all columns for planets with at least one moon
# and a mass less than 1.00.
df_mass_moon = pd.read_sql(
    """
    SELECT *
    FROM planets
    WHERE num_of_moons >= 1
      AND mass < 1.00;
    """,
    conn1,
)


# STEP 5
# Return the name and color of planets whose color contains "blue".
df_blue = pd.read_sql(
    """
    SELECT name, color
    FROM planets
    WHERE color LIKE '%blue%';
    """,
    conn1,
)


##### Part 3: Ordering and Limiting #####

# Connect to the dogs database.
conn2 = sqlite3.connect("dogs.db")


# STEP 6
# Return hungry dogs from youngest to oldest.
df_hungry = pd.read_sql(
    """
    SELECT name, age, breed
    FROM dogs
    WHERE hungry = 1
    ORDER BY age ASC;
    """,
    conn2,
)


# STEP 7
# Return hungry dogs between ages 2 and 7,
# sorted alphabetically by name.
df_hungry_ages = pd.read_sql(
    """
    SELECT name, age, hungry
    FROM dogs
    WHERE hungry = 1
      AND age BETWEEN 2 AND 7
    ORDER BY name ASC;
    """,
    conn2,
)


# STEP 8
# Return the four oldest dogs.
# Age determines the primary order, and breed breaks ties alphabetically.
df_4_oldest = pd.read_sql(
    """
    SELECT name, age, breed
    FROM dogs
    ORDER BY age DESC, breed ASC
    LIMIT 4;
    """,
    conn2,
)


##### Part 4: Aggregation #####

# Connect to the Babe Ruth database.
conn3 = sqlite3.connect("babe_ruth.db")


# STEP 9
# Count the total number of professional baseball seasons.
df_ruth_years = pd.read_sql(
    """
    SELECT COUNT(*) AS total_years
    FROM babe_ruth_stats;
    """,
    conn3,
)


# STEP 10
# Calculate Babe Ruth's career home-run total.
df_hr_total = pd.read_sql(
    """
    SELECT SUM(HR) AS total_home_runs
    FROM babe_ruth_stats;
    """,
    conn3,
)


##### Part 5: Grouping and Aggregation #####

# STEP 11
# Count how many years Babe Ruth played for each team.
df_teams_years = pd.read_sql(
    """
    SELECT team, COUNT(*) AS number_years
    FROM babe_ruth_stats
    GROUP BY team
    ORDER BY team ASC;
    """,
    conn3,
)


# STEP 12
# Calculate average at-bats for each team and keep only
# teams whose average is greater than 200.
df_at_bats = pd.read_sql(
    """
    SELECT team, AVG(at_bats) AS average_at_bats
    FROM babe_ruth_stats
    GROUP BY team
    HAVING AVG(at_bats) > 200;
    """,
    conn3,
)


# STEP 13
# Close all database connections.
conn1.close()
conn2.close()
conn3.close()