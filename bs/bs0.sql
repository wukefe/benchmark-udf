WITH optionpricing(sptprice, strike, rate, volatility, time, optiontype, optionprice, numoptions)
	AS
	(
	 SELECT sptprice, strike, rate, volatility, time, optiontype, optionprice, COUNT(*) numoptions
	 FROM myudf ((SELECT * FROM blackscholes))
	 GROUP BY sptprice, strike, rate, volatility, time, optiontype, optionprice
	)
	SELECT b.sptprice, b.strike, b.rate, b.divq, b.volatility, b.time,
		   b.optiontype, b.divs, b.dgrefval, op.optionprice, op.numoptions,
		   mx_s_o.max_spt_optionprice
	FROM blackscholes  AS b, optionpricing op,
	(
		 SELECT sptprice, MAX(optionprice) max_spt_optionprice
		 FROM optionpricing
		 GROUP BY sptprice
	) mx_s_o
	WHERE b.sptprice     = op.sptprice
		AND b.strike     = op.strike
		AND b.rate       = op.rate
		AND b.volatility = op.volatility
		AND b.time       = op.time
		AND b.optiontype = op.optiontype
		AND b.sptprice   = op.sptprice
		AND b.sptprice   = mx_s_o.sptprice
		AND op.optionprice   >= 0.90 * max_spt_optionprice
	LIMIT 10
	;

