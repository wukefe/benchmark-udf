# User-defined Functions (UDFs)

List of Functions

- [Black-scholes](#black-scholes)
- [Page-rank](#page-rank)

## Black-scholes

> This application is an Intel RMS benchmark. It calculates the prices for a
> portfolio of European options analytically with the Black-Scholes partial
> differential equation (PDE). There is no closed-form expression for the
> Black-Scholes equation and as such it must be computed numerically.

Source: http://wiki.cs.princeton.edu/index.php/PARSEC


### Table Setup

Schema is defined in [udf.ddl#blackscholes](udf.md#L1) as follows.

```sql
CREATE TABLE BLACKSCHOLES ( SPTPRICE   DECIMAL(15,6) NOT NULL,  -- spot price
                            STRIKE     DECIMAL(15,6) NOT NULL,  -- strike price
                            RATE       DECIMAL(15,6) NOT NULL,  -- risk-free interest rate
                            DIVQ       DECIMAL(15,6) NOT NULL,  -- dividend rate
                            VOLATILITY DECIMAL(15,6) NOT NULL,  -- volatility
                            TIME       DECIMAL(15,6) NOT NULL,  -- time to maturity or option expiration in years
                            OPTIONTYPE CHAR(1)       NOT NULL,  -- option type: "P"=PUT, "C"=CALL
                            DIVS       DECIMAL(15,6) NOT NULL,  -- dividend values
                            DGREFVAL   DECIMAL(15,6) NOT NULL); -- DerivaGem Reference Value
```

External links

- [The black-scholes benchmark used in Intel](https://software.intel.com/en-us/articles/multithreaded-code-optimization-in-parsec-30-blackscholes)
    + You can find the formula for calcucations.


A sample data file can be found in [here](data/in_1M.tar.gz).

```bash
tar -xf in_1M.tar.gz
```

Then, the data can be loaded as shown below.

```bash
COPY INTO blackscholes FROM '<path>/data/in_1M.tbl' using DELIMITERS ' ';
```

### Python UDF

```sql
DROP FUNCTION myudf;
CREATE FUNCTION myudf(sptprice FLOAT, strike FLOAT, rate FLOAT, divq FLOAT, volatility FLOAT, time FLOAT, optiontype CHAR, divs FLOAT, dgrefval FLOAT)
RETURNS TABLE(OptionType CHAR, SptPrice FLOAT, OptionPrice FLOAT)
LANGUAGE PYTHON_MAP {
    import bs
    # computing
    optionPrice = bs.BlkSchls(0, sptprice, strike, rate, volatility, time, optiontype)
    # return result
    result = dict()
    result['optiontype']  = optiontype
    result['sptprice']    = sptprice
    result['optionprice'] = optionPrice
    return result
};
```

***Note:***

- The Python function `BlkSchls` is defined and saved in [bs/bs.py](bs/bs.py)
- This is a table UDF which returns a table with three columns

### SQL Queries

**Query 0**

```sql
SELECT
    *
FROM
    myudf((select * from blackscholes))
;
```

**Query 1**

```sql
SELECT
    *
FROM
    myudf((select * from blackscholes))
WHERE
    sptprice BETWEEN 50 AND 100
;
```

**Query 2**

```sql
SELECT
    optiontype, sptprice
FROM
    myudf((select * from blackscholes))
WHERE
    sptprice BETWEEN 50 AND 100
;
```

**Query 3**

```sql
SELECT
    optiontype, sptprice
FROM
    myudf((select * from blackscholes))
WHERE
    optionprice > 15
;
```

**Query 4**

```sql
SELECT
    *
FROM
    myudf((select * from blackscholes))
WHERE
    sptprice < 50 OR sptprice > 100
;
```

**Query 5**

```sql
SELECT
    optiontype, sptprice
FROM
    myudf((select * from blackscholes))
WHERE
    sptprice < 50 OR sptprice > 100
;
```

**Query 6**

```sql
SELECT
    optiontype, sptprice
FROM
    myudf((select * from blackscholes))
WHERE
    optionprice <= 15
;
```

**Query 7**

```sql
SELECT
    *
FROM
    myudf((select * from blackscholes))
WHERE
    sptprice BETWEEN 51 AND 100
;
```

**Query 8**

```sql
SELECT
    optiontype, sptprice
FROM
    myudf((select * from blackscholes))
WHERE
    sptprice BETWEEN 51 AND 100
;
```

**Query 9**

```sql
SELECT
    optiontype, sptprice
FROM
    myudf((select * from blackscholes))
WHERE
    optionprice > 6
;
```


## Page-rank

***Note:***

- The Python UDF and SQL queries used are very similar to the ones in Black-scholes

### Table Setup

Schema is defined in [udf.ddl#pagerank](udf.md#L10) as follows.

```sql
CREATE TABLE PAGERANK     ( URLID      INT NOT NULL,
                            OUTBOUND   INT NOT NULL,
                            INBOUND    INT NOT NULL);
```

### Python UDF

### SQL Queries



