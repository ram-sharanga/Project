-- Run this file with:
-- sqlcmd -U sa -P examlyMssql@123 -i setup.sql

CREATE DATABASE appdb;
GO

USE appdb;
GO

IF NOT EXISTS (
    SELECT * FROM sysobjects WHERE name='SupportTickets' AND xtype='U'
)
CREATE TABLE SupportTickets (
    ticket_id     INT IDENTITY(1,1) PRIMARY KEY,
    employee_name VARCHAR(50),
    issue_type    VARCHAR(50),
    priority      INT,
    raised_date   VARCHAR(20),
    status        VARCHAR(20)
);
GO
