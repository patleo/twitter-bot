from dbwrapper import DBWrapper


twitter_handle = ['walmart','exxonmobil', 'chevron', 'gm', 'Phillips66Co', 'generalelectric', 'ford', 'CVS_Extra', 'McKesson', 'att', 'UnitedHealthGrp', 'verizon', 'Healthcare_ABC', 'FannieMae', 'costco', 'hp', 'kroger', 'jpmorgan', 'ExpressScripts', 'BankofAmerica', 'ibm', 'MarathonPetroCo', 'cardinalhealth', 'Boeing', 'Citi', 'amazon', 'WellsFargo', 'Microsoft', 'ProcterGamble', 'HomeDepot']

stock_ticker = ['WMT', 'XOM', 'CVX', 'GM', 'PSX', 'GE', 'F', 'CVS', 'MCK', 'T', 'UNH', 'VZ', 'ABC', 'FNMA', 'COST', 'HPQ', 'KR', 'JPM', 'ESRX', 'BAC', 'IBM', 'MPC', 'CAH', 'BA', 'C', 'AMZN', 'WFC', 'MSFT', 'PG', 'HD']

forbes_rank = [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] 

db = DBWrapper()
db.seed_companies_table(twitter_handle, stock_ticker, forbes_rank)
db.seed_twitter_table(twitter_handle)