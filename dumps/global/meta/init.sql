INSERT INTO meta.forex_rate_source (source_id, source_name, source_desc, website) VALUES
    (1, 'Exchange Rates API', 'Historical and Real-Time Exchange Rates', 'https://exchangeratesapi.io/'),
    (2, 'XE Currency Converter', 'Live Exchange Rates for Personal & Business', 'https://www.xe.com/currencyconverter/');

INSERT INTO meta.forex_rate_source_plan (source_plan_id, forex_source_id, plan_name, plan_type, data_granularity, plan_limit) VALUES
    (1, 1, 'Free Plan', 'freemium', 'daily', '250 API Calls');
