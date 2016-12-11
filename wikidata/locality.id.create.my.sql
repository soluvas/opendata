CREATE TABLE `locality` (
  `id` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `geonamesId` VARCHAR(255) NULL,
  `place` VARCHAR(255) NOT NULL,
  `stateId` VARCHAR(255) NOT NULL,
  `stateName` VARCHAR(255) NOT NULL,
  `stateIso` VARCHAR(255) NOT NULL,
  `countryId` VARCHAR(255) NOT NULL,
  `countryIso` VARCHAR(2) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `name` (`name` ASC),
  INDEX `geonamesId` (`geonamesId` ASC),
  INDEX `place` (`place` ASC),
  INDEX `stateId` (`stateId` ASC),
  INDEX `stateIso` (`stateIso` ASC),
  INDEX `countryId` (`countryId` ASC),
  INDEX `countryIso` (`countryIso` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
