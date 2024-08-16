DROP DATABASE IF EXISTS ramanan_db;
--CREATE DATABASE airflow;
CREATE DATABASE ramanan_db;
\c ramanan_db;

CREATE TABLE DimDate (
    DateKey INT PRIMARY KEY,
    Date DATE,
    Year INT,
    Month VARCHAR(3),
    Day INT,
    Quarter INT,
    Weekday VARCHAR(10),
    IsHoliday INT
);

CREATE TABLE FactStockPrices (
    DateKey INT,
    Open DECIMAL(10, 2),
    High DECIMAL(10, 2),
    Low DECIMAL(10, 2),
    Close DECIMAL(10, 2),
    Volume INT,
    FOREIGN KEY (DateKey) REFERENCES DimDate(DateKey)
);
