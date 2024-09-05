/********************************************************************
A META Table Schema Design for Historic Currency Data

Currency related historic data - like exchange rates, currency codes,
crypto currency details, etc. are available under the global database
under the schema ``currency`` and the meta tables for the same are as
defined below. Backend database is PostgreSQL.

Copywright © [2024] Debmalya Pramanik
********************************************************************/

CREATE TABLE IF NOT EXISTS meta.forex_rate_source (
    source_id
        SMALLSERIAL
        CONSTRAINT pk_forex_rate_source PRIMARY KEY,

    source_name
        VARCHAR(64)
        CONSTRAINT uq_forex_rate_source_name UNIQUE
        NOT NULL,

    source_desc
        VARCHAR(256)
        NOT NULL,

    website
        VARCHAR(128)
        CONSTRAINT uq_forex_rate_source_website UNIQUE
        NOT NULL
);

CREATE TABLE IF NOT EXISTS meta.forex_rate_source_plan (
    source_plan_id
        SMALLSERIAL
        CONSTRAINT pk_forex_rate_source_plan PRIMARY KEY,

    forex_source_id
        SMALLINT
        CONSTRAINT fk_forex_rate_source_id
            REFERENCES meta.forex_rate_source (source_id)
            ON DELETE CASCADE
            ON UPDATE CASCADE,

    plan_name
        VARCHAR(64)
        NOT NULL,

    plan_type
        VARCHAR(32)
        NOT NULL,

    data_granularity
        VARCHAR(32)
        NOT NULL,

    plan_limit
        VARCHAR(32)
        NOT NULL
);
