## Problem 1: The Date of Easter

Description

- [Function to return date of Easter for the given year](https://stackoverflow.com/questions/2192533/function-to-return-date-of-easter-for-the-given-year)

Solution

- [A simple algorithm](https://aa.usno.navy.mil/faq/docs/easter.php)
    + No branch / no loop

MATLAB code

```matlab
% Input : year (y)
% Return: easter's month and day
function [result] = compute_easter(y)
    c = y / 100
    n = y - 19 * ( y / 19 )
    k = ( c - 17 ) / 25
    i = c - c / 4 - ( c - k ) / 3 + 19 * n + 15
    i = i - 30 * ( i / 30 )
    i = i - ( i / 28 ) * ( 1 - ( i / 28 ) * ( 29 / ( i + 1 ) ) * ( ( 21 - n ) / 11 ) )
    j = y + y / 4 + i + 2 - c + c / 4
    j = j - 7 * ( j / 7 )
    l = i - j
    m = 3 + ( l + 40 ) / 44
    d = l + 28 - 31 * ( m / 4 )
    result = m * 100 + d;
end
```

## Problem 2: Prime Number

Inspired by MemSQL

- [Scalar UDF](https://docs.memsql.com/v6.5/reference/sql-reference/procedural-sql-reference/create-function-udf/)
- [Table UDF](https://docs.memsql.com/v6.5/reference/sql-reference/procedural-sql-reference/create-function-tvf/)

The following code is written in [PL/SQL](https://www.tutorialspoint.com/plsql/plsql_functions.htm).

```
DELIMITER //
CREATE FUNCTION is_prime(n BIGINT NOT NULL) RETURNS BIGINT AS
  BEGIN
    IF n <= 1 THEN
      RETURN FALSE;
    END IF;
    FOR i IN 2 .. (n-1) LOOP
      EXIT WHEN i * i > n;
      IF n % i != 0 THEN
        CONTINUE;
      END IF;
      RETURN FALSE;
    END LOOP;
    RETURN TRUE;
  END //
DELIMITER ;
```

It can be translated to MATLAB code as follows.

```matlab
function [result] = is_prime(n)
    if n <= 1
        return 1;
    end
    for i in 2:(n-1)
        if i * i > n
            break
        end
        if mod(n, i)
            continue
        end
        return 0;
    end
    return 1;
end
```

