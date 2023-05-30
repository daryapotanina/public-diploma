==== dna_proteins
entry_id
experimental_method
number_of_water_molecules_per_deposited_model
resolution_a

==== pdbmap
entry_id
chain
family_id
family_ac
protein_ac
domain_coordinates

```sql
TRUNCATE diploma.dna_proteins;
with t(a) as
         (
             select string_to_array(full_line, ';')
             from dropme_later_real
         )
insert
into diploma.dna_proteins
select a[1],
       a[2],
       NULLIF(a[3], '')::int,
       case
           when a[4] like '%.%' then NULLIF(replace(split_part(a[4], ',', 1), ',', '.'), '')::numeric
           else NULLIF(replace(replace(a[4], ',', '.'), '. ', '.'), '')::numeric end
from t;

select *
from diploma.dna_proteins;

select *
from diploma.dna_proteins where entry_id = '3JBW';

select *
from dropme_later_real;
select *
from dropme_later_real
where full_line like '%X-RAY DIFFRACTION%';
select count(*)
from dropme_later_real;

TRUNCATE diploma.dropme_later_real;
COPY dropme_later_real
    FROM './database/input/dan_proteins_raw.csv'
    DELIMITER '|'
    CSV HEADER;
```
