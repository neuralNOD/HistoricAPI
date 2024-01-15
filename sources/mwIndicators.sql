/********************************************************************
Master Table Definations, and Table Initialization Statements

Global indicators like WDI, GDP, PPP are sourced from World Bank and
International Monetary Fund (IMF). This data is stored into database
and the same is tracked and categorized using the following master
tables. The category information is modified/changed as required.

Author  : Debmalya Pramanik
Version : v0.0.1

Copywright © [2024] neuralNOD INC., Debmalya Pramanik
********************************************************************/

CREATE TABLE [dbo].[mwCategoryIndicator] (
    CategoryID      VARCHAR(3) PRIMARY KEY,
    CategoryName    VARCHAR(64) UNIQUE NOT NULL,
    CategoryDesc    VARCHAR(4096) NOT NULL
);


INSERT INTO [dbo].[mwCategoryIndicator] (CategoryID, CategoryName, CategoryDesc) VALUES
    ('WDI', 'World Development Indicators', 'WDI is the primary collection of development indicators, which includes national, regional and global data available. Important indicators like GDP, Mortality Rate, etc. are tracked under this category. The information is sourced from World Bank and IMF, who in-turn source the data from recogniged sources. The data from IMF has a greater precision, however NUMERIC(*, 2) is best for tracking of global indicators. In addition, IMF has a good API facility which provides forecasted result, extrapolated from the current/last available data point. This information is available on a "YEARLY" granularity.'),
    ('FSI', 'Financial Sector Indicators', 'FSI is the primary collection of financial indicators, like GDF, GFI, debts, budget allocations, etc. on a national level. This information is available on a "YEARLY" granularity.'),
    ('HNP', 'Health, Nutrition & Population Statistics', 'HNP tracks informations on a national level, about the health, quality of life, population information etc. This information is available on a "YEARLY" granularity.'),
    ('WGI', 'Worldwide Governance Indicators', 'Aggregate and individual governance indicators for six dimensions of governance: Voice and Accountability; Political Stability and Absence of Violence/Terrorism; Government Effectiveness; Regulatory Quality; Rule of Law; Control of Corruption.');


CREATE TABLE [dbo].[mwSubCategoryIndicator] (
    SubCategoryID      VARCHAR(3) PRIMARY KEY,
    CategoryID         VARCHAR(3) NOT NULL,
    SubCategoryName    VARCHAR(64) UNIQUE NOT NULL,
    SubCategoryDesc    VARCHAR(4096) NOT NULL,

    CONSTRAINT category_id_fk FOREIGN KEY(CategoryID) REFERENCES mwCategoryIndicator(CategoryID)
);


INSERT INTO [dbo].[mwSubCategoryIndicator] (SubCategoryID, CategoryID, SubCategoryName, SubCategoryDesc) VALUES
    ('GDF', 'FSI', 'International Debt Statistics', 'International Debt Statistics (IDS), formerly known as Global Development Finance (GDF) - provides external debt and financial flows statistics for countries that report public and publicly-guaranteed debt under the World Banks Debtor Reporting System (DRS).'),
    ('GFI', 'FSI', 'Global Financial Inclusions', 'Indicators of financial inclusions, summarized for all adults and disaggregated by key demographic chareteristics like gender, age, education.'),
    ('ICP', 'WDI', 'International Comparison Program', 'A collection of comparative price data and detailed expenditure values of countries gross domestic products (GDP), and purchasing power parities (PPPs) estimates of the worlds economies.'),
    ('GEM', 'FSI', 'Global Economic Monitor', 'Updates of global economic developments for high income and developing countries - covers exchange rates, equity markets, interest rates, stripped bond spreads, and emerging market bond indices'),
    ('FPN', 'HNP', 'Food Prices for Nutrition', 'Food Prices for Nutrition provides indicators on the cost and affordability of healthy diets in each country, showing the populations physical and economic access to sufficient quantities of locally available items for an active and healthy life. It also provides indicators on the cost and affordability of an energy-sufficient diet and a nutrient-adequate diet.'),
    ('SEA', 'WDI', 'Sustainable Energy for All', 'The “Sustainable Energy for All (SE4ALL)” initiative, launched in 2010 by the UN Secretary General, established three global objectives to be accomplished by 2030: to ensure universal access to modern energy services, to double the global rate of improvement in global energy efficiency, and to double the share of renewable energy in the global energy mix. SE4ALL database supports this initiative and provides country level historical data for access to electricity and non-solid fuel; share of renewable energy in total final energy consumption by technology; and energy intensity rate of improvement.');


CREATE TABLE [dbo].[mwGlobalIndicators] (
    IndicatorID     VARCHAR(32) PRIMARY KEY,
    CategoryID      VARCHAR(3) NOT NULL,
    SubCategoryID   VARCHAR(3) NULL,
    IndicatorName   VARCHAR(64) UNIQUE NOT NULL,
    IndicatorDesc   VARCHAR(4096) NOT NULL,

    -- ? Information for Sourcing Data from IMF, using API
    IMF_INDICATOR_CODE    VARCHAR(64) NULL,
    IMF_INDICATOR_UNIT    VARCHAR(32) NULL,
    IMF_INDICATOR_LABEL   VARCHAR(64) NULL,
    IMF_INDICATOR_SOURCE  VARCHAR(256) NULL,
    IMF_INDICATOR_DATASET VARCHAR(128) NULL,

    -- ?  Information for Sourcing Data from World Bank, using Manual Download
    WB_INDICATOR_CODE   VARCHAR(64) NULL,
    WB_INDICATOR_NAME   VARCHAR(256) NULL,
    WB_INDICATOR_SOURCE VARCHAR(4096) NULL,

    CONSTRAINT category_id_fk_1 FOREIGN KEY(CategoryID) REFERENCES mwCategoryIndicator(CategoryID),
    CONSTRAINT sub_category_id_fk FOREIGN KEY(SubCategoryID) REFERENCES mwSubCategoryIndicator(SubCategoryID)
);
