/********************************************************************
neuralNOD INC.

METADATA TABLE: Track a List of All Data Source(s) for neuralNOD

Data is tracked, fetched, and loaded from many souces which is either
available as open-source, proprietary or limited availability. The
same information can be viewed and tracked in DB using the
`DataSourceID`, and for more information check respective readme file
for more information.

Author  : Debmalya Pramanik
Version : v0.0.1

Copywright © [2024] neuralNOD INC., Debmalya Pramanik
********************************************************************/

CREATE TABLE [dbo].[METADATA_DATASOURCE] (
	DataSourceID	INTEGER PRIMARY KEY IDENTITY(1, 1), -- PK: Generate a New ID when a Source is Registered
	DataSourceURI	NVARCHAR(256) UNIQUE NOT NULL,		-- UQ: Dataset URL Link for API/Documentation/etc.
	DataSourceType	VARCHAR(32) NOT NULL,				-- Can be used for tracking type like open-source, proprietary, etc.

	-- ? optional, the below information can be used for tracking site information
	DataUpdateFrequency VARCHAR(32) NULL, -- frequency of data update, `monthly on 15`, recommended to use cron styling
	DataAvblGranularity VARCHAR(32) NULL, -- data granularity, eg. `city`, for demographic, or `minute` for time based, etc.

	-- ? optional, the below can be used for tracking payment/free usage information
	APIAvailable	     INTEGER CHECK(APIAvailable IN (0, 1)) NULL,
	FreeAccessQuota	     VARCHAR(128) NULL, -- eg. 1k API calls/month, etc. NULL > not available, undefined
	FreeOSSAvailable     INTEGER CHECK(FreeOSSAvailable IN (0, 1)) NULL, -- free open source software license available
	FreeStudentLicense   INTEGER CHECK(FreeStudentLicense IN (0, 1)) NULL,
	FreeDevelopedLicense INTEGER CHECK(FreeDevelopedLicense IN (0, 1)) NULL,

	-- ? optional, add description for the data source
	DataSourceDescription  VARCHAR(512) NULL,
	DataSourceUsageOptions VARCHAR(512) NULL, -- linked modules/services with the data source

	-- ? auto, track created and updated date for understanding
	CreatedOn DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	UpdatedOn DATETIME NULL DEFAULT NULL
);
