/* public schema is intentional */
CREATE TABLE public.locality (
  id VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  geonamesId VARCHAR(255) NULL,
  place VARCHAR(255) NOT NULL,
  stateId VARCHAR(255) NOT NULL,
  stateName VARCHAR(255) NOT NULL,
  stateIso VARCHAR(255) NOT NULL,
  countryId VARCHAR(255) NOT NULL,
  countryIso VARCHAR(2) NOT NULL,
  PRIMARY KEY (id)
);
CREATE INDEX ON public.locality (name);
CREATE INDEX ON public.locality (geonamesId);
CREATE INDEX ON public.locality (place);
CREATE INDEX ON public.locality (stateId);
CREATE INDEX ON public.locality (stateIso);
CREATE INDEX ON public.locality (countryId);
CREATE INDEX ON public.locality (countryIso);
