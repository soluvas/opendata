LOAD DATA LOCAL INFILE 'locality.id.csv'
    INTO TABLE locality
    CHARACTER SET 'UTF8'
    FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
    IGNORE 1 LINES;
