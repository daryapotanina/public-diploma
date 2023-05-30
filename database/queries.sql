-- количество уникальных белков и структур в выбранных семействах, удовлетворяющие условиям
select boo1.family_id,
       boo1.protein_amount,
       boo2.pdb_amount
from (select foo.family_id,
             count(foo.family_id) protein_amount
      from (select pdbmap.family_id
            from diploma.pdbmap
                     join diploma.dna_proteins on pdbmap.entry_id = dna_proteins.entry_id
            where dna_proteins.number_of_water_molecules_per_deposited_model > 10
            and dna_proteins.resolution <= 2.5
            group by pdbmap.protein_ac, pdbmap.family_id
            ORDER BY family_id ASC, count(distinct pdbmap.protein_ac) DESC) as foo
      group by family_id
      order by count(family_id) DESC) as boo1
         join (select pdbmap.family_id,
                      count(distinct pdbmap.entry_id) pdb_amount
               from diploma.pdbmap
                        join diploma.dna_proteins on pdbmap.entry_id = dna_proteins.entry_id
               where dna_proteins.number_of_water_molecules_per_deposited_model > 10
               and dna_proteins.resolution <= 2.5
               group by pdbmap.family_id) as boo2 on boo1.family_id = boo2.family_id
where boo1.family_id in ('LAGLIDADG_1', 'LAGLIDADG_3', 'TBP', 'P53', 'HTH_3')
order by protein_amount DESC;

-- координаты доменов по цепям в выбранных семействах 
select pdbmap.family_id,
       pdbmap.protein_ac,
       pdbmap.entry_id,
       pdbmap.chain,
       pdbmap.domain_coordinates
from diploma.pdbmap
         join diploma.dna_proteins on pdbmap.entry_id = dna_proteins.entry_id
where dna_proteins.number_of_water_molecules_per_deposited_model > 10
  and resolution <= 2.5
  and pdbmap.family_id in ('LAGLIDADG_1', 'LAGLIDADG_3', 'TBP', 'P53', 'HTH_3')
group by pdbmap.entry_id, pdbmap.family_id, pdbmap.family_ac, pdbmap.protein_ac, dna_proteins.resolution,
         dna_proteins.number_of_water_molecules_per_deposited_model, pdbmap.domain_coordinates, pdbmap.chain
order by pdbmap.family_id;

-- списки структур выбранных семейств с указанием разрешения и количества молекул воды
select pdbmap.family_ac,
       pdbmap.family_id,
       pdbmap.entry_id,
       pdbmap.protein_ac,
       dna_proteins.resolution,
       dna_proteins.number_of_water_molecules_per_deposited_model
from diploma.pdbmap
         join diploma.dna_proteins on pdbmap.entry_id = dna_proteins.entry_id
where dna_proteins.number_of_water_molecules_per_deposited_model > 10
  and resolution <= 2.5
  and pdbmap.family_id in ('LAGLIDADG_1', 'LAGLIDADG_3', 'TBP', 'P53', 'HTH_3')
group by pdbmap.entry_id, pdbmap.family_id, pdbmap.family_ac, pdbmap.protein_ac, dna_proteins.resolution,
         dna_proteins.number_of_water_molecules_per_deposited_model
order by pdbmap.family_id, dna_proteins.resolution, dna_proteins.number_of_water_molecules_per_deposited_model DESC;