Saya berharap 512 kotamadya + kabupaten di Wikidata tersebut lengkap dengan ID GeoNames-nya
(dan juga memiliki koordinat point serta kode kemendagri).

Saat ini masih ada 304 yang kosong.

Awalnya aku ingin mencari di GeoNames secara offline. Namun ternyata ada GeoNames web service API yang lebih praktis.

    CREATE TABLE geoname (
        geonameid integer PRIMARY KEY,
        name varchar(200),
        asciiname varchar(200),
        alternatenames text,
        latitude double,
        longitude double,
        featureClass char(1),
        featureCode varchar(10),
        countryCode varchar(2),
        cc2 varchar(200),
        admin1Code varchar(20),
        admin2Code varchar(80),
        admin3Code varchar(20),
        admin4Code varchar(20),
        population bigint,
        elevation integer,
        dem integer,
        timezone varchar(40),
        modificationTime date
    )

Lalu import dari file ID.txt
