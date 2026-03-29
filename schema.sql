CREATE TABLE Users (
    Id INT PRIMARY KEY,
    Name NVARCHAR(100),
    Email NVARCHAR(100)
);

INSERT INTO Users (Id, Name, Email)
VALUES (1, 'Test User', 'test@email.com');
