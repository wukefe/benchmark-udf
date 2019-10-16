function runner()

% feature accel off;
[sptprice,strike,rate,divq,volatility,otime,otype,divs,DGrefval] = InputData();
disp('Data loaded');
elapsed = zeros(1,10);
for i = 1:10
    tic;
    prices = BlkSchls(sptprice, strike, rate, volatility, otime, otype);
    elapsed(i) = toc;
end

disp('"The elapsed time (ms)": ');
disp(mean(elapsed)* 1000);
disp(sum(prices));
end
