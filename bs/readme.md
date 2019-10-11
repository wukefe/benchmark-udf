## Configurations

Setup databases

    monetdbd-19 create /mnt/local/datafarm/PL20
    monetdbd-19 start /mnt/local/datafarm/PL20
    monetdb-19 create dbbs
    monetdb-19 release dbbs
    mclient-19 -d dbbs
        \<bs.ddl
        COPY INTO blackscholes from '/home/sable/hanfeng.c/github/benchmark-udf/data/in_1M.tbl' USING DELIMITERS ' ','\n';
        select count(*) from blackscholes;

Execute scripts

    mclient-19 -d dbbs -f raw -e exec.mon


## Files

- bs0.sql: a query for blackscholes
- bs0.plan: an execution plan for bs0.sql
- exe.mon: a monetdb script

