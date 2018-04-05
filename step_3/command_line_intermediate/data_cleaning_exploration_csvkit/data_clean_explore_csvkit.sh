# Combining data from all three files using csvstack and adding column
# year with values for each year in data sets.

/home/dq$ csvstack -n year -g 2005,2007,2013 Hud_2005.csv Hud_2007.cs
v Hud_2013.csv > Combined_hud.csv
/home/dq$ head -5 Combined_hud.csv
year,AGE1,BURDEN,FMR,FMTBEDRMS,FMTBUILT,TOTSAL
2005,43,0.513,680,'3 3BR','1980-1989',20000
2005,44,0.223,760,'4 4BR+','1980-1989',71000
2005,58,0.218,680,'3 3BR','1980-1989',63000
2005,22,0.217,519,'1 1BR','1980-1989',27040
/home/dq$ wc -l Combined_hud.csv
154118 Combined_hud.csv

# Using csvlook to display tabular data in a table format.

/home/dq$ head -10 Combined_hud.csv | csvlook
|-------+------+--------+-----+-----------+-------------+---------|
|  year | AGE1 | BURDEN | FMR | FMTBEDRMS | FMTBUILT    | TOTSAL  |
|-------+------+--------+-----+-----------+-------------+---------|
|  2005 | 43   | 0.513  | 680 | '3 3BR'   | '1980-1989' | 20000   |
|  2005 | 44   | 0.223  | 760 | '4 4BR+'  | '1980-1989' | 71000   |
|  2005 | 58   | 0.218  | 680 | '3 3BR'   | '1980-1989' | 63000   |
|  2005 | 22   | 0.217  | 519 | '1 1BR'   | '1980-1989' | 27040   |
|  2005 | 48   | 0.283  | 600 | '1 1BR'   | '1980-1989' | 14000   |
|  2005 | 42   | 0.292  | 788 | '3 3BR'   | '1980-1989' | 42000   |
|  2005 | -9   | -9.000 | 702 | '2 2BR'   | '1980-1989' | -9      |
|  2005 | 23   | 0.145  | 546 | '2 2BR'   | '1980-1989' | 48000   |
|  2005 | 51   | 0.296  | 680 | '3 3BR'   | '1980-1989' | 58000   |
|-------+------+--------+-----+-----------+-------------+---------|

# Using csvcut to display all columns and the first 10 rows in
# column AGE1.

/home/dq$ csvcut -n Combined_hud.csv
  1: year
  2: AGE1
  3: BURDEN
  4: FMR
  5: FMTBEDRMS
  6: FMTBUILT
  7: TOTSAL

/home/dq$ csvcut -c 2 Combined_hud.csv | head -10
AGE1
43
44
58
22
48
42
-9
23
51

# Using csvstat to calculate the means for each row in Combined_hud.csv.

/home/dq$ csvstat --mean Combined_hud.csv
  1. year: 2008.9044232628457
  2. AGE1: 46.511215505103266
  3. BURDEN: 5.303764743668771
  4. FMR: 1037.1186695822005
  5. FMTBEDRMS: None
  6. FMTBUILT: None
  7. TOTSAL: 44041.841931779105

# Using csvstat to dislay full summary statistics on the AGE1 column.

/home/dq$ csvcut -c 2 Combined_hud.csv | csvstat
  1. AGE1
        <class 'int'>
        Nulls: False
        Min: -9
        Max: 93
        Sum: 7168169
        Mean: 46.511215505103266
        Median: 48
        Standard Deviation: 23.04901451351246
        Unique values: 80
        5 most frequent values:
                -9:     11553
                50:     3208
                45:     3056
                40:     3040
                48:     3006

Row count: 154117

# Noticing that nearly half of the ages are -9, we use csvgrep to display
# the first 10 rows of the AGE1 column where the value is -9.
# Dislpay tabular data in table format using csvlook.

/home/dq$ csvgrep -c 2 -m -9 Combined_hud.csv | head -10  | csvlook
|-------+------+--------+------+-----------+-------------+---------|
|  year | AGE1 | BURDEN | FMR  | FMTBEDRMS | FMTBUILT    | TOTSAL  |
|-------+------+--------+------+-----------+-------------+---------|
|  2005 | -9   | -9.000 | 702  | '2 2BR'   | '1980-1989' | -9      |
|  2005 | -9   | -9.000 | 531  | '1 1BR'   | '1980-1989' | -9      |
|  2005 | -9   | -9.000 | 1034 | '3 3BR'   | '2000-2009' | -9      |
|  2005 | -9   | -9.000 | 631  | '1 1BR'   | '1980-1989' | -9      |
|  2005 | -9   | -9.000 | 712  | '4 4BR+'  | '1990-1999' | -9      |
|  2005 | -9   | -9.000 | 1006 | '3 3BR'   | '2000-2009' | -9      |
|  2005 | -9   | -9.000 | 631  | '1 1BR'   | '1980-1989' | -9      |
|  2005 | -9   | -9.000 | 712  | '3 3BR'   | '2000-2009' | -9      |
|  2005 | -9   | -9.000 | 1087 | '3 3BR'   | '2000-2009' | -9      |
|-------+------+--------+------+-----------+-------------+---------|

# Adding data where the age does not equal -9 from Combined_hud.csv to
# positive_ages_only.csv.

/home/dq$ csvgrep -c 2 -m -9 -i Combined_hud.csv > positive_ages_only
.csv
