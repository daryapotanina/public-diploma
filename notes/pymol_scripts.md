## Load a file with multiple models

```
load /Users/admin/.probisH2O/Probis_H2O/5MCT.pdb, multiplex=1; as sticks
load /Users/admin/.probisH2O/Probis_H2O/1YTB.pdb, multiplex=1; as sticks
```

## Print list of atoms in selection

```
list=[]
iterate (foo),list.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list
```

## Select atoms near to protein and nucleic

```
select boo, cons near_to 3.5 of polymer.protein
select foo, boo near_to 3.5 of polymer.nucleic
select sur, * near_to 3.5 of foo
```

## Pipeline

### LAGLIDADG_1

#### 6BD0

```
load /Users/admin/.probisH2O/Probis_H2O/6BD0.pdb, multiplex=1; as cartoon

bg_color white
color slate, polymer.nucleic
color 0xf5deb3, polymer.protein
color sand, ((resi 168-270 and chain A) or (resi 12-111 and chain A))
select calcium, resn CA
show spheres, calcium
color limon,  calcium


select cons, (///C/HOH`126/ or ///A/HOH`650/ or ///A/HOH`642/ or ///C/HOH`145/ or ///B/HOH`165/ or ///B/HOH`151/ or ///B/HOH`127/ or ///A/HOH`848/ or ///A/HOH`633/ or ///C/HOH`184/ or ///C/HOH`173/ or ///C/HOH`169/ or ///C/HOH`166/ or ///C/HOH`152/ or ///C/HOH`131/ or ///C/HOH`129/ or ///C/HOH`124/ or ///C/HOH`112/ or ///C/HOH`111/ or ///B/HOH`183/ or ///B/HOH`176/ or ///B/HOH`160/ or ///B/HOH`156/ or ///B/HOH`147/ or ///B/HOH`145/ or ///B/HOH`138/ or ///B/HOH`135/ or ///B/HOH`133/ or ///B/HOH`128/ or ///B/HOH`121/ or ///B/HOH`116/ or ///B/HOH`114/ or ///B/HOH`113/ or ///A/HOH`837/ or ///A/HOH`797/ or ///A/HOH`783/ or ///A/HOH`767/ or ///A/HOH`742/ or ///A/HOH`731/ or ///A/HOH`689/ or ///A/HOH`664/ or ///A/HOH`635/ or ///A/HOH`634/ or ///A/HOH`622/ or ///A/HOH`609/ or ///A/HOH`606/ or ///A/HOH`505/ or ///A/HOH`502/ or ///C/HOH`175/ or ///C/HOH`158/ or ///C/HOH`156/ or ///C/HOH`155/ or ///C/HOH`153/ or ///C/HOH`143/ or ///C/HOH`134/ or ///C/HOH`123/ or ///B/HOH`187/ or ///B/HOH`158/ or ///B/HOH`152/ or ///B/HOH`143/ or ///B/HOH`132/ or ///B/HOH`129/ or ///B/HOH`120/ or ///A/HOH`761/ or ///A/HOH`679/ or ///A/HOH`670/ or ///A/HOH`663/ or ///A/HOH`662/ or ///A/HOH`646/ or ///A/HOH`627/ or ///A/HOH`608/ or ///A/HOH`595/ or ///A/HOH`592/ or ///A/HOH`552/ or ///A/HOH`547/ or ///A/HOH`530/)
show spheres, cons

select cons2, (///A/HOH`726/ or ///A/HOH`648/ or ///C/HOH`177/ or ///C/HOH`176/ or ///A/HOH`887/ or ///A/HOH`886/ or ///A/HOH`809/ or ///A/HOH`707/ or ///A/HOH`559/ or ///C/HOH`228/ or ///C/HOH`197/ or ///B/HOH`102/ or ///A/HOH`991/ or ///A/HOH`982/ or ///A/HOH`979/ or ///A/HOH`973/ or ///A/HOH`965/ or ///A/HOH`963/ or ///A/HOH`962/ or ///A/HOH`950/ or ///A/HOH`933/ or ///A/HOH`923/ or ///A/HOH`919/ or ///A/HOH`918/ or ///A/HOH`915/ or ///A/HOH`913/ or ///A/HOH`911/ or ///A/HOH`903/ or ///A/HOH`900/ or ///A/HOH`898/ or ///A/HOH`896/ or ///A/HOH`884/ or ///A/HOH`880/ or ///A/HOH`873/ or ///A/HOH`868/ or ///A/HOH`867/ or ///A/HOH`865/ or ///A/HOH`864/ or ///A/HOH`859/ or ///A/HOH`857/ or ///A/HOH`855/ or ///A/HOH`853/ or ///A/HOH`849/ or ///A/HOH`844/ or ///A/HOH`842/ or ///A/HOH`824/ or ///A/HOH`823/ or ///A/HOH`821/ or ///A/HOH`817/ or ///A/HOH`813/ or ///A/HOH`810/ or ///A/HOH`804/ or ///A/HOH`802/ or ///A/HOH`794/ or ///A/HOH`790/ or ///A/HOH`789/ or ///A/HOH`782/ or ///A/HOH`778/ or ///A/HOH`770/ or ///A/HOH`768/ or ///A/HOH`766/ or ///A/HOH`757/ or ///A/HOH`753/ or ///A/HOH`748/ or ///A/HOH`740/ or ///A/HOH`728/ or ///A/HOH`724/ or ///A/HOH`723/ or ///A/HOH`720/ or ///A/HOH`718/ or ///A/HOH`708/ or ///A/HOH`705/ or ///A/HOH`699/ or ///A/HOH`693/ or ///A/HOH`692/ or ///A/HOH`688/ or ///A/HOH`686/ or ///A/HOH`680/ or ///A/HOH`669/ or ///A/HOH`667/ or ///A/HOH`661/ or ///A/HOH`654/ or ///A/HOH`639/ or ///A/HOH`638/ or ///A/HOH`637/ or ///A/HOH`632/ or ///A/HOH`628/ or ///A/HOH`620/ or ///A/HOH`615/ or ///A/HOH`597/ or ///A/HOH`571/ or ///A/HOH`568/ or ///A/HOH`562/ or ///A/HOH`560/ or ///A/HOH`558/ or ///A/HOH`549/ or ///A/HOH`545/ or ///A/HOH`539/ or ///A/HOH`535/ or ///A/HOH`523/ or ///A/HOH`518/ or ///A/HOH`511/ or ///A/HOH`508/ or ///C/HOH`226/ or ///C/HOH`217/ or ///C/HOH`211/ or ///C/HOH`210/ or ///C/HOH`208/ or ///C/HOH`206/ or ///B/HOH`204/ or ///C/HOH`203/ or ///C/HOH`201/ or ///C/HOH`198/ or ///B/HOH`198/ or ///B/HOH`197/ or ///C/HOH`195/ or ///B/HOH`194/ or ///C/HOH`193/ or ///B/HOH`193/ or ///B/HOH`192/ or ///C/HOH`191/ or ///B/HOH`191/ or ///B/HOH`190/ or ///C/HOH`187/ or ///C/HOH`186/ or ///B/HOH`186/ or ///B/HOH`185/ or ///C/HOH`185/ or ///C/HOH`181/ or ///B/HOH`180/ or ///C/HOH`178/ or ///B/HOH`173/ or ///B/HOH`172/ or ///B/HOH`171/ or ///C/HOH`171/ or ///C/HOH`168/ or ///C/HOH`167/ or ///B/HOH`163/ or ///B/HOH`162/ or ///C/HOH`162/ or ///B/HOH`161/ or ///B/HOH`157/ or ///C/HOH`157/ or ///B/HOH`155/ or ///B/HOH`154/ or ///C/HOH`151/ or ///B/HOH`150/ or ///C/HOH`150/ or ///B/HOH`149/ or ///C/HOH`146/ or ///B/HOH`141/ or ///B/HOH`140/ or ///C/HOH`138/ or ///B/HOH`136/ or ///C/HOH`136/ or ///B/HOH`131/ or ///B/HOH`130/ or ///C/HOH`128/ or ///C/HOH`127/ or ///C/HOH`125/ or ///C/HOH`122/ or ///B/HOH`122/ or ///B/HOH`117/ or ///B/HOH`105/ or ///C/HOH`105/ or ///C/HOH`104/ or ///B/HOH`104/ or ///C/HOH`101/ or ///A/HOH`992/ or ///A/HOH`990/ or ///A/HOH`971/ or ///A/HOH`970/ or ///A/HOH`968/ or ///A/HOH`956/ or ///A/HOH`954/ or ///A/HOH`952/ or ///A/HOH`948/ or ///A/HOH`947/ or ///A/HOH`939/ or ///A/HOH`934/ or ///A/HOH`924/ or ///A/HOH`922/ or ///A/HOH`914/ or ///A/HOH`905/ or ///A/HOH`904/ or ///A/HOH`899/ or ///A/HOH`897/ or ///A/HOH`893/ or ///A/HOH`891/ or ///A/HOH`890/ or ///A/HOH`885/ or ///A/HOH`877/ or ///A/HOH`874/ or ///A/HOH`872/ or ///A/HOH`869/ or ///A/HOH`856/ or ///A/HOH`854/ or ///A/HOH`850/ or ///A/HOH`841/ or ///A/HOH`839/ or ///A/HOH`832/ or ///A/HOH`830/ or ///A/HOH`827/ or ///A/HOH`826/ or ///A/HOH`819/ or ///A/HOH`816/ or ///A/HOH`812/ or ///A/HOH`811/ or ///A/HOH`808/ or ///A/HOH`807/ or ///A/HOH`806/ or ///A/HOH`798/ or ///A/HOH`796/ or ///A/HOH`793/ or ///A/HOH`777/ or ///A/HOH`773/ or ///A/HOH`771/ or ///A/HOH`769/ or ///A/HOH`763/ or ///A/HOH`762/ or ///A/HOH`760/ or ///A/HOH`759/ or ///A/HOH`754/ or ///A/HOH`747/ or ///A/HOH`744/ or ///A/HOH`743/ or ///A/HOH`741/ or ///A/HOH`739/ or ///A/HOH`738/ or ///A/HOH`737/ or ///A/HOH`736/ or ///A/HOH`735/ or ///A/HOH`733/ or ///A/HOH`729/ or ///A/HOH`727/ or ///A/HOH`725/ or ///A/HOH`722/ or ///A/HOH`719/ or ///A/HOH`716/ or ///A/HOH`711/ or ///A/HOH`710/ or ///A/HOH`709/ or ///A/HOH`706/ or ///A/HOH`704/ or ///A/HOH`700/ or ///A/HOH`698/ or ///A/HOH`695/ or ///A/HOH`683/ or ///A/HOH`682/ or ///A/HOH`677/ or ///A/HOH`676/ or ///A/HOH`675/ or ///A/HOH`674/ or ///A/HOH`673/ or ///A/HOH`658/ or ///A/HOH`657/ or ///A/HOH`652/ or ///A/HOH`649/ or ///A/HOH`645/ or ///A/HOH`641/ or ///A/HOH`640/ or ///A/HOH`636/ or ///A/HOH`631/ or ///A/HOH`626/ or ///A/HOH`625/ or ///A/HOH`621/ or ///A/HOH`619/ or ///A/HOH`612/ or ///A/HOH`610/ or ///A/HOH`607/ or ///A/HOH`603/ or ///A/HOH`602/ or ///A/HOH`601/ or ///A/HOH`599/ or ///A/HOH`598/ or ///A/HOH`596/ or ///A/HOH`593/ or ///A/HOH`591/ or ///A/HOH`590/ or ///A/HOH`589/ or ///A/HOH`588/ or ///A/HOH`585/ or ///A/HOH`584/ or ///A/HOH`582/ or ///A/HOH`580/ or ///A/HOH`579/ or ///A/HOH`578/ or ///A/HOH`576/ or ///A/HOH`575/ or ///A/HOH`574/ or ///A/HOH`565/ or ///A/HOH`563/ or ///A/HOH`561/ or ///A/HOH`551/ or ///A/HOH`544/ or ///A/HOH`542/ or ///A/HOH`540/ or ///A/HOH`532/ or ///A/HOH`531/ or ///A/HOH`529/ or ///A/HOH`528/ or ///A/HOH`517/ or ///A/HOH`516/ or ///A/HOH`510/ or ///A/HOH`504/ or ///A/HOH`501/ or ///C/HOH`220/ or ///C/HOH`219/ or ///C/HOH`216/ or ///B/HOH`209/ or ///C/HOH`207/ or ///B/HOH`207/ or ///C/HOH`204/ or ///B/HOH`200/ or ///C/HOH`190/ or ///C/HOH`188/ or ///B/HOH`184/ or ///B/HOH`182/ or ///C/HOH`179/ or ///B/HOH`177/ or ///B/HOH`175/ or ///B/HOH`174/ or ///C/HOH`170/ or ///B/HOH`169/ or ///B/HOH`166/ or ///C/HOH`165/ or ///B/HOH`164/ or ///C/HOH`163/ or ///C/HOH`160/ or ///B/HOH`159/ or ///C/HOH`159/ or ///C/HOH`154/ or ///C/HOH`144/ or ///B/HOH`144/ or ///C/HOH`142/ or ///C/HOH`139/ or ///C/HOH`137/ or ///C/HOH`130/ or ///B/HOH`123/ or ///C/HOH`121/ or ///C/HOH`119/ or ///C/HOH`118/ or ///B/HOH`111/ or ///C/HOH`110/ or ///C/HOH`109/)
show spheres, cons2

select cons_i, (///C/HOH`126/ or ///A/HOH`650/ or ///A/HOH`642/ or ///B/HOH`127/ or ///A/HOH`848/ or ///A/HOH`633/)
show spheres, cons_i
color red, cons_i

select sur_sol_i, solvent near_to 3.5 of cons_i
show nb_spheres, sur_sol_i

select sur_i, * near_to 3.5 of cons_i

list1=[]
iterate (sur_i),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur_i, (///A/ASP`20/ or ///A/ALA`21/ or ///A/SER`24/ or ///A/PHE`25/ or ///A/ASN`139/ or ///A/GLU`178/ or ///A/PHE`181/ or ///A/GLN`195/ or ///A/VAL`196/ or ///A/GLN`204/ or ///A/THR`240/ or ///A/LYS`241/ or ///A/ASN`298/ or ///A/CA`402/ or ///A/HOH`632/ or ///A/HOH`638/ or ///A/HOH`664/ or ///B/DC`14/ or ///B/DA`16/ or ///C/DA`4/ or ///C/DA`6/ or ///C/DA`16/ or ///C/DA`17/ or ///C/HOH`148/ or ///C/HOH`176/)
show sticks, sur_i
hide cartoon, sur_i and polymer.nucleic
show cartoon, (sur_i and backbone)
show nb_spheres, (sur_i and solvent)


select cons_n_i, (///A/HOH`726/ or ///A/HOH`648/ or ///C/HOH`177/)
show spheres, cons_n_i
color salmon, cons_n_i

select sur_sol_n_i, solvent near_to 3.5 of cons_n_i
show nb_spheres, sur_sol_i

select sur_n_i, * near_to 3.5 of cons_n_i

list1=[]
iterate (sur_n_i),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur_n_i, (///A/GLU`178/ or ///A/SER`201/ or ///A/SER`201/ or ///A/THR`203/ or ///A/GLY`222/ or ///A/HOH`809/ or ///B/DA`15/ or ///B/HOH`102/ or ///B/HOH`157/ or ///C/DA`14/ or ///C/HOH`127/ or ///A/HOH`605/)
show sticks, sur_n_i
hide cartoon, sur_n_i and polymer.nucleic
show cartoon, (sur_n_i and backbone)
show nb_spheres, (///A/HOH`809/ or ///B/HOH`102/ or ///B/HOH`157/ or ///C/HOH`127/ or ///A/HOH`605/)

select cons_ni, (///A/HOH`726/ or ///A/HOH`648/ or ///C/HOH`177/ or ///C/HOH`176/ or ///A/HOH`887/ or ///A/HOH`886/ or ///A/HOH`809/ or ///A/HOH`707/ or ///A/HOH`559/ or ///C/HOH`228/ or ///C/HOH`197/ or ///B/HOH`102/ or ///A/HOH`991/ or ///A/HOH`982/ or ///A/HOH`979/ or ///A/HOH`973/ or ///A/HOH`965/ or ///A/HOH`963/ or ///A/HOH`962/ or ///A/HOH`950/ or ///A/HOH`933/ or ///A/HOH`923/ or ///A/HOH`919/ or ///A/HOH`918/ or ///A/HOH`915/ or ///A/HOH`913/ or ///A/HOH`911/ or ///A/HOH`903/ or ///A/HOH`900/ or ///A/HOH`898/ or ///A/HOH`896/ or ///A/HOH`884/ or ///A/HOH`880/ or ///A/HOH`873/ or ///A/HOH`868/ or ///A/HOH`867/ or ///A/HOH`865/ or ///A/HOH`864/ or ///A/HOH`859/ or ///A/HOH`857/ or ///A/HOH`855/ or ///A/HOH`853/ or ///A/HOH`849/ or ///A/HOH`844/ or ///A/HOH`842/ or ///A/HOH`824/ or ///A/HOH`823/ or ///A/HOH`821/ or ///A/HOH`817/ or ///A/HOH`813/ or ///A/HOH`810/ or ///A/HOH`804/ or ///A/HOH`802/ or ///A/HOH`794/ or ///A/HOH`790/ or ///A/HOH`789/ or ///A/HOH`782/ or ///A/HOH`778/ or ///A/HOH`770/ or ///A/HOH`768/ or ///A/HOH`766/ or ///A/HOH`757/ or ///A/HOH`753/ or ///A/HOH`748/ or ///A/HOH`740/ or ///A/HOH`728/ or ///A/HOH`724/ or ///A/HOH`723/ or ///A/HOH`720/ or ///A/HOH`718/ or ///A/HOH`708/ or ///A/HOH`705/ or ///A/HOH`699/ or ///A/HOH`693/ or ///A/HOH`692/ or ///A/HOH`688/ or ///A/HOH`686/ or ///A/HOH`680/ or ///A/HOH`669/ or ///A/HOH`667/ or ///A/HOH`661/ or ///A/HOH`654/ or ///A/HOH`639/ or ///A/HOH`638/ or ///A/HOH`637/ or ///A/HOH`632/ or ///A/HOH`628/ or ///A/HOH`620/ or ///A/HOH`615/ or ///A/HOH`597/ or ///A/HOH`571/ or ///A/HOH`568/ or ///A/HOH`562/ or ///A/HOH`560/ or ///A/HOH`558/ or ///A/HOH`549/ or ///A/HOH`545/ or ///A/HOH`539/ or ///A/HOH`535/ or ///A/HOH`523/ or ///A/HOH`518/ or ///A/HOH`511/ or ///A/HOH`508/ or ///C/HOH`226/ or ///C/HOH`217/ or ///C/HOH`211/ or ///C/HOH`210/ or ///C/HOH`208/ or ///C/HOH`206/ or ///B/HOH`204/ or ///C/HOH`203/ or ///C/HOH`201/ or ///C/HOH`198/ or ///B/HOH`198/ or ///B/HOH`197/ or ///C/HOH`195/ or ///B/HOH`194/ or ///C/HOH`193/ or ///B/HOH`193/ or ///B/HOH`192/ or ///C/HOH`191/ or ///B/HOH`191/ or ///B/HOH`190/ or ///C/HOH`187/ or ///C/HOH`186/ or ///B/HOH`186/ or ///B/HOH`185/ or ///C/HOH`185/ or ///C/HOH`181/ or ///B/HOH`180/ or ///C/HOH`178/ or ///B/HOH`173/ or ///B/HOH`172/ or ///B/HOH`171/ or ///C/HOH`171/ or ///C/HOH`168/ or ///C/HOH`167/ or ///B/HOH`163/ or ///B/HOH`162/ or ///C/HOH`162/ or ///B/HOH`161/ or ///B/HOH`157/ or ///C/HOH`157/ or ///B/HOH`155/ or ///B/HOH`154/ or ///C/HOH`151/ or ///B/HOH`150/ or ///C/HOH`150/ or ///B/HOH`149/ or ///C/HOH`146/ or ///B/HOH`141/ or ///B/HOH`140/ or ///C/HOH`138/ or ///B/HOH`136/ or ///C/HOH`136/ or ///B/HOH`131/ or ///B/HOH`130/ or ///C/HOH`128/ or ///C/HOH`127/ or ///C/HOH`125/ or ///C/HOH`122/ or ///B/HOH`122/ or ///B/HOH`117/ or ///B/HOH`105/ or ///C/HOH`105/ or ///C/HOH`104/ or ///B/HOH`104/ or ///C/HOH`101/ or ///A/HOH`992/ or ///A/HOH`990/ or ///A/HOH`971/ or ///A/HOH`970/ or ///A/HOH`968/ or ///A/HOH`956/ or ///A/HOH`954/ or ///A/HOH`952/ or ///A/HOH`948/ or ///A/HOH`947/ or ///A/HOH`939/ or ///A/HOH`934/ or ///A/HOH`924/ or ///A/HOH`922/ or ///A/HOH`914/ or ///A/HOH`905/ or ///A/HOH`904/ or ///A/HOH`899/ or ///A/HOH`897/ or ///A/HOH`893/ or ///A/HOH`891/ or ///A/HOH`890/ or ///A/HOH`885/ or ///A/HOH`877/ or ///A/HOH`874/ or ///A/HOH`872/ or ///A/HOH`869/ or ///A/HOH`856/ or ///A/HOH`854/ or ///A/HOH`850/ or ///A/HOH`841/ or ///A/HOH`839/ or ///A/HOH`832/ or ///A/HOH`830/ or ///A/HOH`827/ or ///A/HOH`826/ or ///A/HOH`819/ or ///A/HOH`816/ or ///A/HOH`812/ or ///A/HOH`811/ or ///A/HOH`808/ or ///A/HOH`807/ or ///A/HOH`806/ or ///A/HOH`798/ or ///A/HOH`796/ or ///A/HOH`793/ or ///A/HOH`777/ or ///A/HOH`773/ or ///A/HOH`771/ or ///A/HOH`769/ or ///A/HOH`763/ or ///A/HOH`762/ or ///A/HOH`760/ or ///A/HOH`759/ or ///A/HOH`754/ or ///A/HOH`747/ or ///A/HOH`744/ or ///A/HOH`743/ or ///A/HOH`741/ or ///A/HOH`739/ or ///A/HOH`738/ or ///A/HOH`737/ or ///A/HOH`736/ or ///A/HOH`735/ or ///A/HOH`733/ or ///A/HOH`729/ or ///A/HOH`727/ or ///A/HOH`725/ or ///A/HOH`722/ or ///A/HOH`719/ or ///A/HOH`716/ or ///A/HOH`711/ or ///A/HOH`710/ or ///A/HOH`709/ or ///A/HOH`706/ or ///A/HOH`704/ or ///A/HOH`700/ or ///A/HOH`698/ or ///A/HOH`695/ or ///A/HOH`683/ or ///A/HOH`682/ or ///A/HOH`677/ or ///A/HOH`676/ or ///A/HOH`675/ or ///A/HOH`674/ or ///A/HOH`673/ or ///A/HOH`658/ or ///A/HOH`657/ or ///A/HOH`652/ or ///A/HOH`649/ or ///A/HOH`645/ or ///A/HOH`641/ or ///A/HOH`640/ or ///A/HOH`636/ or ///A/HOH`631/ or ///A/HOH`626/ or ///A/HOH`625/ or ///A/HOH`621/ or ///A/HOH`619/ or ///A/HOH`612/ or ///A/HOH`610/ or ///A/HOH`607/ or ///A/HOH`603/ or ///A/HOH`602/ or ///A/HOH`601/ or ///A/HOH`599/ or ///A/HOH`598/ or ///A/HOH`596/ or ///A/HOH`593/ or ///A/HOH`591/ or ///A/HOH`590/ or ///A/HOH`589/ or ///A/HOH`588/ or ///A/HOH`585/ or ///A/HOH`584/ or ///A/HOH`582/ or ///A/HOH`580/ or ///A/HOH`579/ or ///A/HOH`578/ or ///A/HOH`576/ or ///A/HOH`575/ or ///A/HOH`574/ or ///A/HOH`565/ or ///A/HOH`563/ or ///A/HOH`561/ or ///A/HOH`551/ or ///A/HOH`544/ or ///A/HOH`542/ or ///A/HOH`540/ or ///A/HOH`532/ or ///A/HOH`531/ or ///A/HOH`529/ or ///A/HOH`528/ or ///A/HOH`517/ or ///A/HOH`516/ or ///A/HOH`510/ or ///A/HOH`504/ or ///A/HOH`501/ or ///C/HOH`220/ or ///C/HOH`219/ or ///C/HOH`216/ or ///B/HOH`209/ or ///C/HOH`207/ or ///B/HOH`207/ or ///C/HOH`204/ or ///B/HOH`200/ or ///C/HOH`190/ or ///C/HOH`188/ or ///B/HOH`184/ or ///B/HOH`182/ or ///C/HOH`179/ or ///B/HOH`177/ or ///B/HOH`175/ or ///B/HOH`174/ or ///C/HOH`170/ or ///B/HOH`169/ or ///B/HOH`166/ or ///C/HOH`165/ or ///B/HOH`164/ or ///C/HOH`163/ or ///C/HOH`160/ or ///B/HOH`159/ or ///C/HOH`159/ or ///C/HOH`154/ or ///C/HOH`144/ or ///B/HOH`144/ or ///C/HOH`142/ or ///C/HOH`139/ or ///C/HOH`137/ or ///C/HOH`130/ or ///B/HOH`123/ or ///C/HOH`121/ or ///C/HOH`119/ or ///C/HOH`118/ or ///B/HOH`111/ or ///C/HOH`110/ or ///C/HOH`109/)
<!-- 345 -->
select sur_dna_nt, cons_ni near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 56 -->
select sur_dna_bb, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
<!-- 70 -->
select sur_dna_bb_nt_0, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt, sur_dna_bb_nt_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 34 -->


select cons_all_i, (///C/HOH`126/ or ///A/HOH`650/ or ///A/HOH`642/ or ///C/HOH`145/ or ///B/HOH`165/ or ///B/HOH`151/ or ///B/HOH`127/ or ///A/HOH`848/ or ///A/HOH`633/ or ///C/HOH`184/ or ///C/HOH`173/ or ///C/HOH`169/ or ///C/HOH`166/ or ///C/HOH`152/ or ///C/HOH`131/ or ///C/HOH`129/ or ///C/HOH`124/ or ///C/HOH`112/ or ///C/HOH`111/ or ///B/HOH`183/ or ///B/HOH`176/ or ///B/HOH`160/ or ///B/HOH`156/ or ///B/HOH`147/ or ///B/HOH`145/ or ///B/HOH`138/ or ///B/HOH`135/ or ///B/HOH`133/ or ///B/HOH`128/ or ///B/HOH`121/ or ///B/HOH`116/ or ///B/HOH`114/ or ///B/HOH`113/ or ///A/HOH`837/ or ///A/HOH`797/ or ///A/HOH`783/ or ///A/HOH`767/ or ///A/HOH`742/ or ///A/HOH`731/ or ///A/HOH`689/ or ///A/HOH`664/ or ///A/HOH`635/ or ///A/HOH`634/ or ///A/HOH`622/ or ///A/HOH`609/ or ///A/HOH`606/ or ///A/HOH`505/ or ///A/HOH`502/ or ///C/HOH`175/ or ///C/HOH`158/ or ///C/HOH`156/ or ///C/HOH`155/ or ///C/HOH`153/ or ///C/HOH`143/ or ///C/HOH`134/ or ///C/HOH`123/ or ///B/HOH`187/ or ///B/HOH`158/ or ///B/HOH`152/ or ///B/HOH`143/ or ///B/HOH`132/ or ///B/HOH`129/ or ///B/HOH`120/ or ///A/HOH`761/ or ///A/HOH`679/ or ///A/HOH`670/ or ///A/HOH`663/ or ///A/HOH`662/ or ///A/HOH`646/ or ///A/HOH`627/ or ///A/HOH`608/ or ///A/HOH`595/ or ///A/HOH`592/ or ///A/HOH`552/ or ///A/HOH`547/ or ///A/HOH`530/)
<!-- 76 -->
select sur_dna_nt_i, cons_all_i near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 30 -->
select sur_dna_bb_i, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
<!-- 59 -->
select sur_dna_bb_nt_i_0, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt_i, sur_dna_bb_nt_i_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 13 -->


```

#### 1T9I

```
load /Users/admin/.probisH2O/Probis_H2O/1T9I.pdb, multiplex=1; as cartoon

bg_color white
color slate, polymer.nucleic
color 0xf5deb3, polymer.protein
color sand, ((resi 13-108 and chain A) or (resi 13-108 and chain B))
select calcium, resn CA
show spheres, calcium
color limon,  calcium

select cons_i, (///C/HOH`1001 or ///C/HOH`1078 or ///C/HOH`1027 or ///C/HOH`1023 or ///A/HOH`1026)
show spheres, cons_i
color red, cons_i

select cons_n_i, (///D/HOH`1086 or ///A/HOH`1241 or ///A/HOH`1169 or ///A/HOH`1069 or ///C/HOH`1043 or ///A/HOH`1002)
show spheres, cons_n_i
color salmon, cons_n_i

select cons, (///A/HOH`1026/ or ///C/HOH`1027/ or ///C/HOH`1043/ or ///C/HOH`1078/ or ///D/HOH`1086/)

select sur, * near_to 3.5 of cons

list1=[]
iterate (sur),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur, (///A/SER`72/ or ///A/THR`140/ or ///A/HOH`1020/ or ///C/DG`513/ or ///C/DA`516/ or ///C/DC`517/ or ///C/HOH`1004/ or ///C/HOH`1009/ or ///C/HOH`1014/ or ///D/DA`563/ or ///D/HOH`1003/ or ///D/HOH`1013/ or ///D/HOH`1076/ or ///C/DG`515/)
show sticks, sur
hide cartoon, sur and polymer.nucleic
show cartoon, (sur and backbone)
show nb_spheres, (sur and solvent)

select a, (///C/DG`515/)
show sticks, a
hide cartoon, a and polymer.nucleic
show cartoon, (a and backbone)

select cons_ni, (///A/HOH`1656/ or ///A/HOH`1655/ or ///A/HOH`1654/ or ///A/HOH`1650/ or ///C/HOH`1648/ or ///A/HOH`1645/ or ///D/HOH`1644/ or ///C/HOH`1643/ or ///D/HOH`1642/ or ///A/HOH`1640/ or ///A/HOH`1638/ or ///A/HOH`1637/ or ///A/HOH`1635/ or ///B/HOH`1633/ or ///B/HOH`1632/ or ///B/HOH`1631/ or ///D/HOH`1630/ or ///D/HOH`1629/ or ///A/HOH`1625/ or ///B/HOH`1624/ or ///B/HOH`1623/ or ///C/HOH`1622/ or ///D/HOH`1620/ or ///A/HOH`1619/ or ///A/HOH`1618/ or ///B/HOH`1614/ or ///A/HOH`1609/ or ///A/HOH`1608/ or ///A/HOH`1596/ or ///A/HOH`1595/ or ///C/HOH`1590/ or ///D/HOH`1588/ or ///A/HOH`1587/ or ///A/HOH`1584/ or ///C/HOH`1583/ or ///A/HOH`1579/ or ///A/HOH`1576/ or ///A/HOH`1574/ or ///B/HOH`1573/ or ///A/HOH`1571/ or ///A/HOH`1569/ or ///A/HOH`1565/ or ///D/HOH`1563/ or ///B/HOH`1562/ or ///D/HOH`1561/ or ///A/HOH`1553/ or ///A/HOH`1551/ or ///A/HOH`1545/ or ///D/HOH`1543/ or ///A/HOH`1535/ or ///D/HOH`1533/ or ///A/HOH`1520/ or ///A/HOH`1515/ or ///A/HOH`1514/ or ///A/HOH`1512/ or ///A/HOH`1511/ or ///A/HOH`1509/ or ///A/HOH`1506/ or ///C/HOH`1504/ or ///A/HOH`1502/ or ///B/HOH`1501/ or ///A/HOH`1500/ or ///A/HOH`1499/ or ///A/HOH`1498/ or ///A/HOH`1497/ or ///A/HOH`1496/ or ///D/HOH`1495/ or ///D/HOH`1494/ or ///A/HOH`1493/ or ///A/HOH`1491/ or ///C/HOH`1489/ or ///A/HOH`1488/ or ///A/HOH`1486/ or ///C/HOH`1484/ or ///A/HOH`1482/ or ///A/HOH`1480/ or ///A/HOH`1479/ or ///A/HOH`1478/ or ///A/HOH`1477/ or ///A/HOH`1474/ or ///A/HOH`1472/ or ///A/HOH`1471/ or ///A/HOH`1469/ or ///A/HOH`1468/ or ///C/HOH`1464/ or ///A/HOH`1462/ or ///C/HOH`1461/ or ///A/HOH`1457/ or ///A/HOH`1454/ or ///D/HOH`1453/ or ///A/HOH`1450/ or ///A/HOH`1448/ or ///A/HOH`1443/ or ///A/HOH`1442/ or ///B/HOH`1438/ or ///A/HOH`1433/ or ///C/HOH`1432/ or ///C/HOH`1431/ or ///D/HOH`1429/ or ///B/HOH`1427/ or ///A/HOH`1425/ or ///A/HOH`1421/ or ///D/HOH`1419/ or ///A/HOH`1417/ or ///A/HOH`1404/ or ///A/HOH`1402/ or ///C/HOH`1399/ or ///B/HOH`1396/ or ///A/HOH`1394/ or ///C/HOH`1388/ or ///A/HOH`1385/ or ///A/HOH`1379/ or ///C/HOH`1378/ or ///A/HOH`1374/ or ///D/HOH`1371/ or ///A/HOH`1369/ or ///D/HOH`1368/ or ///B/HOH`1365/ or ///A/HOH`1363/ or ///B/HOH`1362/ or ///A/HOH`1361/ or ///A/HOH`1360/ or ///B/HOH`1358/ or ///A/HOH`1357/ or ///B/HOH`1355/ or ///D/HOH`1354/ or ///A/HOH`1346/ or ///A/HOH`1345/ or ///D/HOH`1343/ or ///D/HOH`1341/ or ///A/HOH`1340/ or ///A/HOH`1338/ or ///D/HOH`1334/ or ///A/HOH`1331/ or ///D/HOH`1330/ or ///A/HOH`1326/ or ///D/HOH`1321/ or ///A/HOH`1318/ or ///A/HOH`1317/ or ///B/HOH`1315/ or ///B/HOH`1314/ or ///C/HOH`1313/ or ///C/HOH`1312/ or ///A/HOH`1311/ or ///D/HOH`1307/ or ///B/HOH`1302/ or ///B/HOH`1301/ or ///A/HOH`1298/ or ///C/HOH`1296/ or ///B/HOH`1294/ or ///A/HOH`1290/ or ///B/HOH`1289/ or ///A/HOH`1280/ or ///A/HOH`1278/ or ///B/HOH`1277/ or ///A/HOH`1274/ or ///A/HOH`1273/ or ///B/HOH`1272/ or ///C/HOH`1271/ or ///A/HOH`1268/ or ///A/HOH`1267/ or ///A/HOH`1265/ or ///A/HOH`1263/ or ///D/HOH`1261/ or ///D/HOH`1256/ or ///D/HOH`1253/ or ///C/HOH`1249/ or ///C/HOH`1248/ or ///A/HOH`1247/ or ///A/HOH`1245/ or ///A/HOH`1242/ or ///A/HOH`1241/ or ///A/HOH`1240/ or ///B/HOH`1239/ or ///A/HOH`1236/ or ///A/HOH`1235/ or ///C/HOH`1233/ or ///A/HOH`1231/ or ///C/HOH`1230/ or ///A/HOH`1229/ or ///A/HOH`1228/ or ///B/HOH`1227/ or ///A/HOH`1223/ or ///C/HOH`1221/ or ///A/HOH`1220/ or ///A/HOH`1219/ or ///B/HOH`1218/ or ///A/HOH`1212/ or ///A/HOH`1211/ or ///A/HOH`1207/ or ///B/HOH`1204/ or ///D/HOH`1203/ or ///A/HOH`1202/ or ///A/HOH`1201/ or ///D/HOH`1200/ or ///A/HOH`1198/ or ///A/HOH`1196/ or ///D/HOH`1195/ or ///D/HOH`1194/ or ///C/HOH`1193/ or ///A/HOH`1192/ or ///A/HOH`1191/ or ///C/HOH`1190/ or ///D/HOH`1189/ or ///A/HOH`1188/ or ///B/HOH`1187/ or ///A/HOH`1183/ or ///A/HOH`1180/ or ///A/HOH`1179/ or ///A/HOH`1175/ or ///A/HOH`1174/ or ///A/HOH`1173/ or ///D/HOH`1171/ or ///A/HOH`1169/ or ///A/HOH`1168/ or ///A/HOH`1166/ or ///C/HOH`1165/ or ///B/HOH`1163/ or ///B/HOH`1162/ or ///C/HOH`1161/ or ///A/HOH`1158/ or ///B/HOH`1157/ or ///A/HOH`1156/ or ///B/HOH`1154/ or ///B/HOH`1153/ or ///A/HOH`1152/ or ///A/HOH`1151/ or ///A/HOH`1148/ or ///A/HOH`1145/ or ///A/HOH`1142/ or ///A/HOH`1141/ or ///A/HOH`1139/ or ///A/HOH`1136/ or ///B/HOH`1134/ or ///A/HOH`1133/ or ///A/HOH`1131/ or ///D/HOH`1130/ or ///B/HOH`1129/ or ///A/HOH`1128/ or ///B/HOH`1126/ or ///C/HOH`1125/ or ///A/HOH`1123/ or ///B/HOH`1119/ or ///A/HOH`1117/ or ///B/HOH`1115/ or ///C/HOH`1113/ or ///A/HOH`1112/ or ///D/HOH`1111/ or ///A/HOH`1109/ or ///A/HOH`1108/ or ///A/HOH`1106/ or ///A/HOH`1104/ or ///A/HOH`1103/ or ///C/HOH`1102/ or ///A/HOH`1100/ or ///A/HOH`1095/ or ///A/HOH`1094/ or ///A/HOH`1093/ or ///D/HOH`1092/ or ///B/HOH`1090/ or ///A/HOH`1088/ or ///A/HOH`1087/ or ///D/HOH`1086/ or ///B/HOH`1085/ or ///A/HOH`1084/ or ///A/HOH`1082/ or ///A/HOH`1081/ or ///D/HOH`1076/ or ///A/HOH`1074/ or ///A/HOH`1073/ or ///C/HOH`1071/ or ///A/HOH`1069/ or ///A/HOH`1068/ or ///A/HOH`1066/ or ///A/HOH`1064/ or ///B/HOH`1052/ or ///A/HOH`1047/ or ///B/HOH`1046/ or ///A/HOH`1045/ or ///A/HOH`1044/ or ///C/HOH`1043/ or ///D/HOH`1039/ or ///A/HOH`1038/ or ///A/HOH`1031/ or ///B/HOH`1025/ or ///A/HOH`1024/ or ///A/HOH`1022/ or ///A/HOH`1019/ or ///C/HOH`1009/ or ///B/HOH`1006/ or ///D/HOH`1003/ or ///A/HOH`1002/)
<!-- 292 -->
select sur_dna_nt, cons_ni near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 40 -->
select sur_dna_bb, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
<!-- 45 -->
select sur_dna_bb_nt_0, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt, sur_dna_bb_nt_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 21 -->


select cons_all_i, (///D/HOH`1651/ or ///D/HOH`1627/ or ///D/HOH`1568/ or ///D/HOH`1356/ or ///D/HOH`1215/ or ///D/HOH`1147/ or ///D/HOH`1122/ or ///D/HOH`1105/ or ///D/HOH`1058/ or ///D/HOH`1054/ or ///D/HOH`1036/ or ///D/HOH`1035/ or ///D/HOH`1028/ or ///C/HOH`1615/ or ///C/HOH`1613/ or ///C/HOH`1293/ or ///C/HOH`1160/ or ///C/HOH`1078/ or ///C/HOH`1027/ or ///C/HOH`1023/ or ///C/HOH`1014/ or ///C/HOH`1008/ or ///C/HOH`1007/ or ///C/HOH`1001/ or ///B/HOH`1621/ or ///B/HOH`1607/ or ///B/HOH`1079/ or ///B/HOH`1077/ or ///B/HOH`1072/ or ///B/HOH`1057/ or ///B/HOH`1049/ or ///B/HOH`1048/ or ///B/HOH`1032/ or ///B/HOH`1012/ or ///B/HOH`1011/ or ///A/HOH`1572/ or ///A/HOH`1518/ or ///A/HOH`1264/ or ///A/HOH`1096/ or ///A/HOH`1080/ or ///A/HOH`1062/ or ///A/HOH`1059/ or ///A/HOH`1051/ or ///A/HOH`1042/ or ///A/HOH`1041/ or ///A/HOH`1040/ or ///A/HOH`1030/ or ///A/HOH`1026/ or ///A/HOH`1020/ or ///A/HOH`1018/ or ///A/HOH`1005/)
<!-- 51 -->
select sur_dna_nt_i, cons_all_i near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 27 -->
select sur_dna_bb_i, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
<!-- 33 -->
select sur_dna_bb_nt_i_0, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt_i, sur_dna_bb_nt_i_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 9 -->

```

#### 6BCE

```
load /Users/admin/.probisH2O/Probis_H2O/6BCE.pdb, multiplex=1; as cartoon

bg_color white
color slate, polymer.nucleic
color 0xf5deb3, polymer.protein
color sand, ((resi 22-119 and chain A) or (resi 177-285 and chain A))
select calcium, resn CA
show spheres, calcium
color limon,  calcium

select cons_i, (///C/HOH`120/ or ///A/HOH`573/ or ///A/HOH`658/ or ///A/HOH`553/ or ///B/HOH`117/ or ///A/HOH`541/ or ///B/HOH`108/ or ///A/HOH`536/ or ///B/HOH`137/ or ///B/HOH`107/)
show spheres, cons_i
color red, cons_i

select cons_n_i, (///A/HOH`531/ or ///B/HOH`144/ or ///C/HOH`107/ or ///A/HOH`636/ or ///A/HOH`543/)
show spheres, cons_n_i
color salmon, cons_n_i

select sur, * near_to 3.5 of (cons_n_i or cons_i)

list1=[]
iterate (sur),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur, (///A/ASP`27/ or ///A/ALA`28/ or ///A/GLU`29/ or ///A/ALA`182/ or ///A/GLU`184/ or ///A/PHE`187/ or ///A/ARG`190/ or ///A/LYS`198/ or ///A/THR`199/ or ///A/GLN`202/ or ///A/VAL`203/ or ///A/GLN`204/ or ///A/GLN`208/ or ///A/THR`210/ or ///A/GLN`211/ or ///A/ILE`231/ or ///A/ARG`232/ or ///A/ARG`234/ or ///A/ASP`248/ or ///A/THR`252/ or ///A/ASN`253/ or ///A/LYS`274/ or ///A/ASP`277/ or ///A/ASN`310/ or ///A/CA`401/ or ///A/CA`402/ or ///A/HOH`507/ or ///A/HOH`517/ or ///A/HOH`565/ or ///A/HOH`577/ or ///A/HOH`670/ or ///A/HOH`681/ or ///B/DC`4/ or ///B/DT`5/ or ///B/DA`6/ or ///B/DA`7/ or ///B/DA`8/ or ///B/DG`13/ or ///B/DA`15/ or ///B/DT`16/ or ///B/HOH`105/ or ///B/HOH`109/ or ///B/HOH`123/ or ///B/HOH`149/ or ///C/DC`15/ or ///C/DG`16/ or ///C/DA`17/ or ///C/HOH`102/ or ///C/HOH`117/ or ///C/HOH`118/ or ///C/HOH`133/)
show sticks, sur
hide cartoon, sur and polymer.nucleic
show cartoon, (sur and backbone)
show nb_spheres, (sur and solvent)

select cons_cal, (///A/HOH`573/ or ///A/HOH`658/ or ///A/HOH`531/)
show spheres, cons_cal


select cons, (///B/HOH`108/ or ///A/HOH`541/ or ///C/HOH`107/ or ///B/HOH`144/)
show spheres, cons
select sur, * near_to 3.5 of cons

list1=[]
iterate (sur),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur,  (///A/ARG`190/ or ///A/GLN`208/ or ///A/ARG`232/ or ///A/ARG`234/ or ///A/ASP`248/ or ///B/DA`8/ or ///B/DG`13/ or ///B/DA`15/ or ///B/HOH`105/ or ///B/HOH`123/ or ///B/HOH`149/ or ///C/DC`15/ or ///C/DG`16/ or ///C/DA`17/ or ///C/HOH`117/ or ///B/DT`16/ or ///C/HOH`118/)
show sticks, sur
hide cartoon, sur and polymer.nucleic
show cartoon, (sur and backbone)
show nb_spheres, (sur and solvent)

select cons_ni, (///A/HOH`531/ or ///B/HOH`144/ or ///C/HOH`107/ or ///A/HOH`636/ or ///A/HOH`612/ or ///A/HOH`610/ or ///A/HOH`546/ or ///B/HOH`105/ or ///A/HOH`540/ or ///A/HOH`583/ or ///A/HOH`578/ or ///C/HOH`133/ or ///B/HOH`109/ or ///A/HOH`543/ or ///A/HOH`507/ or ///B/HOH`139/ or ///A/HOH`570/ or ///A/HOH`592/ or ///A/HOH`589/ or ///A/HOH`586/ or ///A/HOH`558/ or ///A/HOH`533/ or ///A/HOH`505/ or ///B/HOH`149/ or ///C/HOH`117/ or ///A/HOH`645/ or ///A/HOH`633/ or ///A/HOH`628/ or ///A/HOH`617/ or ///A/HOH`568/ or ///A/HOH`549/ or ///A/HOH`528/ or ///B/HOH`143/ or ///B/HOH`119/ or ///B/HOH`112/ or ///C/HOH`106/ or ///A/HOH`642/ or ///C/HOH`139/ or ///C/HOH`102/ or ///A/HOH`634/ or ///A/HOH`566/ or ///A/HOH`560/ or ///A/HOH`554/ or ///B/HOH`130/ or ///A/HOH`684/ or ///A/HOH`668/ or ///A/HOH`663/ or ///A/HOH`565/ or ///A/HOH`547/ or ///A/HOH`514/ or ///B/HOH`145/ or ///C/HOH`126/ or ///A/HOH`685/ or ///A/HOH`681/ or ///A/HOH`678/ or ///A/HOH`677/ or ///A/HOH`674/ or ///A/HOH`670/ or ///A/HOH`667/ or ///A/HOH`657/ or ///A/HOH`656/ or ///A/HOH`640/ or ///A/HOH`638/ or ///A/HOH`637/ or ///A/HOH`630/ or ///A/HOH`614/ or ///A/HOH`613/ or ///A/HOH`608/ or ///A/HOH`606/ or ///A/HOH`604/ or ///A/HOH`600/ or ///A/HOH`599/ or ///A/HOH`597/ or ///A/HOH`588/ or ///A/HOH`587/ or ///A/HOH`582/ or ///A/HOH`577/ or ///A/HOH`575/ or ///A/HOH`561/ or ///A/HOH`557/ or ///A/HOH`550/ or ///A/HOH`534/ or ///A/HOH`529/ or ///A/HOH`520/ or ///A/HOH`515/ or ///A/HOH`511/ or ///A/HOH`506/ or ///A/HOH`504/ or ///A/HOH`502/ or ///B/HOH`147/ or ///B/HOH`146/ or ///B/HOH`142/ or ///C/HOH`140/ or ///C/HOH`136/ or ///B/HOH`134/ or ///B/HOH`125/ or ///C/HOH`118/ or ///C/HOH`113/ or ///B/HOH`111/ or ///C/HOH`109/ or ///C/HOH`105/ or ///B/HOH`102/ or ///B/HOH`101/ or ///A/HOH`571/ or ///A/HOH`519/ or ///A/HOH`513/ or ///C/HOH`111/)
<!-- 107 -->
select sur_dna_nt, cons_ni near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 17 -->
select sur_dna_bb, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
<!-- 21 -->
select sur_dna_bb_nt_0, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt, sur_dna_bb_nt_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 9 -->

??????
select cons_all_i, (///C/HOH`120/ or ///A/HOH`573/ or ///A/HOH`658/ or ///A/HOH`553/ or ///B/HOH`117/ or ///A/HOH`541/ or ///B/HOH`108/ or ///A/HOH`536/ or ///B/HOH`137/ or ///B/HOH`107/ or ///A/HOH`584/ or ///C/HOH`129/ or ///C/HOH`123/ or ///B/HOH`135/ or ///B/HOH`128/ or ///B/HOH`114/ or ///A/HOH`563/ or ///A/HOH`542/ or ///A/HOH`518/ or ///B/HOH`122/ or ///B/HOH`133/ or ///A/HOH`525/ or ///A/HOH`581/ or ///A/HOH`564/ or ///C/HOH`131/ or ///C/HOH`130/ or ///B/HOH`131/ or ///B/HOH`126/ or ///B/HOH`123/ or ///B/HOH`118/ or ///B/HOH`115/ or ///A/HOH`639/ or ///A/HOH`631/ or ///A/HOH`593/ or ///A/HOH`555/ or ///A/HOH`527/ or ///A/HOH`526/ or ///A/HOH`517/ or ///C/HOH`110/ or ///C/HOH`104/ or ///B/HOH`116/)
<!-- 41 -->
select sur_dna_nt_i, cons_all_i near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 11 -->
select sur_dna_bb_i, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
<!-- 31 -->
select sur_dna_bb_nt_i_0, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt_i, sur_dna_bb_nt_i_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 1 -->


```

### LAGLIDADG_3

#### 2VS7

```
load /Users/admin/.probisH2O/Probis_H2O/2VS7.pdb, multiplex=1; as cartoon

bg_color white
color slate, polymer.nucleic
color 0xf5deb3, polymer.protein
color sand, ((resi 8-96 and chain A) or (resi 104-178 and chain A) or (resi 8-96 and chain D) or (resi 104-178 and chain F) or (resi 8-96 and chain G) or (resi 104-178 and chain G))
select calcium, resn CA
show spheres, calcium
color limon,  calcium

select cons_i, (///A/HOH`2002/ or ///A/HOH`2022/ or ///A/HOH`2013/ or ///A/HOH`2006/)
show spheres, cons_i
color red, cons_i

select cons_n_i, (///A/HOH`2008/ or ///A/HOH`2019/ or ///A/HOH`2020/ or ///A/HOH`2018/ or ///A/HOH`2010/ or ///A/HOH`2003/ or ///A/HOH`2015/ or ///A/HOH`2023/ or ///A/HOH`2014/ or ///A/HOH`2007/ or ///A/HOH`2021/ or ///A/HOH`2017/ or ///A/HOH`2011/ or ///A/HOH`2005/ or ///A/HOH`2004/)
show spheres, cons_n_i
color salmon, cons_n_i

select cons_all, (///A/HOH`2008/ or ///A/HOH`2019/ or ///A/HOH`2020/ or ///A/HOH`2018/ or ///A/HOH`2010/ or ///A/HOH`2003/ or ///A/HOH`2015/ or ///A/HOH`2023/ or ///A/HOH`2014/ or ///A/HOH`2007/ or ///A/HOH`2021/ or ///A/HOH`2017/ or ///A/HOH`2011/ or ///A/HOH`2005/ or ///A/HOH`2004/)
<!-- 15 -->
select sur_dna_nt_i, cons_all near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 0 -->
select sur_dna_bb_i, cons_all near_to 3.5 of (polymer.nucleic and backbone)
<!-- 0 -->
select sur_dna_bb_nt_i_0, cons_all near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt_i, sur_dna_bb_nt_i_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 0 -->

select cons_all_i, (///A/HOH`2002/ or ///A/HOH`2022/ or ///A/HOH`2013/ or ///A/HOH`2006/)
<!-- 4 -->
select sur_dna_nt_i, cons_all_i near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 2 -->
select sur_dna_bb_i, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
<!-- 3 -->
select sur_dna_bb_nt_i_0, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt_i, sur_dna_bb_nt_i_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 1 -->

select sur, * near_to 3.5 of (sur_dna_nt_i or sur_dna_bb_i or sur_dna_bb_nt_i)

list1=[]
iterate (sur),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur,  (///A/ILE`19/ or ///A/ASP`21/ or ///A/LYS`26/ or ///A/GLY`31/ or ///A/GLN`42/ or ///A/TYR`89/ or ///A/VAL`115/ or ///A/ALA`116/ or ///A/GLU`117/ or ///A/ASN`129/ or ///A/CA`1183/ or ///A/HOH`2059/ or ///A/HOH`2082/ or ///B/DA`14/ or ///B/HOH`2029/ or ///C/DC`3/ or ///C/DC`15/ or ///C/HOH`2030/ or ///C/HOH`2031/ or ///F/DC`1/)
show sticks, sur
hide cartoon, sur and polymer.nucleic
show cartoon, (sur and backbone)
show nb_spheres, (sur and solvent)
```

### HTH_3

#### 2R1J

```
load /Users/admin/.probisH2O/Probis_H2O/2R1J.pdb, multiplex=1; as cartoon

bg_color white
color slate, polymer.nucleic
color 0xf5deb3, polymer.protein
color sand, ((resi 10-64 and chain L) or (resi 10-64 and chain R))

select cons_ni, (///L/HOH`141/ or ///L/HOH`88/ or ///L/HOH`81/ or ///B/HOH`38/ or ///L/HOH`111/ or ///A/HOH`97/ or ///L/HOH`94/ or ///L/HOH`87/ or ///B/HOH`86/ or ///L/HOH`84/ or ///A/HOH`84/ or ///B/HOH`81/ or ///B/HOH`77/ or ///A/HOH`76/ or ///B/HOH`75/ or ///A/HOH`73/ or ///L/HOH`69/ or ///A/HOH`65/ or ///A/HOH`64/ or ///A/HOH`43/ or ///A/HOH`42/ or ///L/HOH`145/ or ///L/HOH`142/ or ///L/HOH`121/ or ///L/HOH`120/ or ///L/HOH`110/ or ///A/HOH`109/ or ///L/HOH`107/ or ///L/HOH`102/ or ///L/HOH`99/ or ///B/HOH`99/ or ///L/HOH`98/ or ///B/HOH`97/ or ///L/HOH`97/ or ///L/HOH`96/ or ///A/HOH`96/ or ///L/HOH`95/ or ///A/HOH`94/ or ///L/HOH`93/ or ///L/HOH`92/ or ///L/HOH`91/ or ///A/HOH`90/ or ///R/HOH`90/ or ///L/HOH`90/ or ///A/HOH`89/ or ///L/HOH`89/ or ///A/HOH`86/ or ///L/HOH`85/ or ///L/HOH`83/ or ///A/HOH`83/ or ///L/HOH`82/ or ///L/HOH`80/ or ///R/HOH`79/ or ///L/HOH`78/ or ///L/HOH`77/ or ///L/HOH`76/ or ///L/HOH`75/ or ///B/HOH`74/ or ///B/HOH`73/ or ///L/HOH`73/ or ///R/HOH`72/ or ///A/HOH`71/ or ///L/HOH`70/ or ///B/HOH`68/ or ///A/HOH`68/ or ///A/HOH`66/ or ///B/HOH`66/ or ///A/HOH`60/ or ///B/HOH`60/ or ///B/HOH`54/ or ///B/HOH`53/ or ///A/HOH`52/ or ///B/HOH`52/ or ///B/HOH`49/ or ///B/HOH`47/ or ///A/HOH`46/ or ///A/HOH`45/ or ///B/HOH`35/ or ///B/HOH`26/ or ///R/HOH`162/ or ///R/HOH`160/ or ///R/HOH`156/ or ///L/HOH`144/ or ///L/HOH`143/ or ///L/HOH`139/ or ///L/HOH`138/ or ///L/HOH`136/ or ///R/HOH`135/ or ///R/HOH`134/ or ///L/HOH`132/ or ///L/HOH`130/ or ///L/HOH`129/ or ///L/HOH`127/ or ///L/HOH`126/ or ///L/HOH`124/ or ///L/HOH`123/ or ///L/HOH`122/ or ///L/HOH`119/ or ///L/HOH`118/ or ///L/HOH`117/ or ///L/HOH`115/ or ///L/HOH`114/ or ///L/HOH`113/ or ///L/HOH`112/ or ///A/HOH`111/ or ///L/HOH`109/ or ///R/HOH`108/ or ///L/HOH`106/ or ///A/HOH`106/ or ///L/HOH`105/ or ///L/HOH`104/ or ///L/HOH`103/ or ///A/HOH`103/ or ///A/HOH`102/ or ///L/HOH`101/ or ///L/HOH`100/)
<!-- 116 -->
select sur_dna_nt, cons_ni near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 20 -->
select sur_dna_bb, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
<!-- 28 -->
select sur_dna_bb_nt_0, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt, sur_dna_bb_nt_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 11 -->

select cons_all_i, (///A/HOH`53/ or ///L/HOH`108/ or ///L/HOH`71/ or ///R/HOH`93/ or ///R/HOH`103/ or ///L/HOH`86/ or ///L/HOH`79/ or ///L/HOH`74/ or ///L/HOH`72/ or ///L/HOH`128/ or ///B/HOH`59/ or ///B/HOH`57/ or ///B/HOH`21/ or ///A/HOH`59/ or ///A/HOH`56/ or ///A/HOH`48/ or ///A/HOH`41/ or ///A/HOH`112/)
<!-- 18 -->
select sur_dna_nt_i, cons_all_i near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 6 -->
select sur_dna_bb_i, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
<!-- 13 -->
select sur_dna_bb_nt_i_0, cons_all_i near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt_i, sur_dna_bb_nt_i_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 1 -->

select cons_i, (///A/HOH`53/ or ///L/HOH`108/ or ///L/HOH`71/ or ///R/HOH`103/)
show spheres, cons_i
color red, cons_i

select cons_n_i, (///L/HOH`141/ or ///L/HOH`88/ or ///L/HOH`81/ or ///L/HOH`94/)
show spheres, cons_n_i
color salmon, cons_n_i

select sur, * near_to 3.5 of (cons_i or cons_n_i)

list1=[]
iterate (sur),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur, (///A/DT`23/ or ///A/HOH`90/ or ///B/DA`11/ or ///B/DT`12/ or ///B/HOH`26/ or ///L/GLU`8/ or ///L/ARG`14/ or ///L/LYS`15/ or ///L/GLN`21/ or ///L/ALA`22/ or ///L/ASN`32/ or ///L/GLU`39/ or ///L/SER`41/ or ///L/LYS`66/ or ///L/HOH`91/ or ///L/HOH`105/ or ///L/HOH`107/ or ///L/HOH`109/ or ///L/HOH`124/ or ///R/ASN`46/ or ///R/GLU`48/)
show sticks, sur
hide cartoon, sur and polymer.nucleic
show cartoon, (sur and backbone)
show nb_spheres, (sur and solvent)

select cons, (///L/HOH`141/ or ///L/HOH`88/ or ///L/HOH`81/ or ///B/HOH`38/ or ///L/HOH`111/ or ///A/HOH`97/ or ///L/HOH`94/ or ///L/HOH`87/ or ///B/HOH`86/ or ///L/HOH`84/ or ///A/HOH`84/ or ///B/HOH`81/ or ///B/HOH`77/ or ///A/HOH`76/ or ///B/HOH`75/ or ///A/HOH`73/ or ///L/HOH`69/ or ///A/HOH`65/ or ///A/HOH`64/ or ///A/HOH`43/ or ///A/HOH`42/ or ///L/HOH`145/ or ///L/HOH`142/ or ///L/HOH`121/ or ///L/HOH`120/ or ///L/HOH`110/ or ///A/HOH`109/ or ///L/HOH`107/ or ///L/HOH`102/ or ///L/HOH`99/ or ///B/HOH`99/ or ///L/HOH`98/ or ///B/HOH`97/ or ///L/HOH`97/ or ///L/HOH`96/ or ///A/HOH`96/ or ///L/HOH`95/ or ///A/HOH`94/ or ///L/HOH`93/ or ///L/HOH`92/ or ///L/HOH`91/ or ///A/HOH`90/ or ///R/HOH`90/ or ///L/HOH`90/ or ///A/HOH`89/ or ///L/HOH`89/ or ///A/HOH`86/ or ///L/HOH`85/ or ///L/HOH`83/ or ///A/HOH`83/ or ///L/HOH`82/ or ///L/HOH`80/ or ///R/HOH`79/ or ///L/HOH`78/ or ///L/HOH`77/ or ///L/HOH`76/ or ///L/HOH`75/ or ///B/HOH`74/ or ///B/HOH`73/ or ///L/HOH`73/ or ///R/HOH`72/ or ///A/HOH`71/ or ///L/HOH`70/ or ///B/HOH`68/ or ///A/HOH`68/ or ///A/HOH`66/ or ///B/HOH`66/ or ///A/HOH`60/ or ///B/HOH`60/ or ///B/HOH`54/ or ///B/HOH`53/ or ///A/HOH`52/ or ///B/HOH`52/ or ///B/HOH`49/ or ///B/HOH`47/ or ///A/HOH`46/ or ///A/HOH`45/ or ///B/HOH`35/ or ///B/HOH`26/ or ///R/HOH`162/ or ///R/HOH`160/ or ///R/HOH`156/ or ///L/HOH`144/ or ///L/HOH`143/ or ///L/HOH`139/ or ///L/HOH`138/ or ///L/HOH`136/ or ///R/HOH`135/ or ///R/HOH`134/ or ///L/HOH`132/ or ///L/HOH`130/ or ///L/HOH`129/ or ///L/HOH`127/ or ///L/HOH`126/ or ///L/HOH`124/ or ///L/HOH`123/ or ///L/HOH`122/ or ///L/HOH`119/ or ///L/HOH`118/ or ///L/HOH`117/ or ///L/HOH`115/ or ///L/HOH`114/ or ///L/HOH`113/ or ///L/HOH`112/ or ///A/HOH`111/ or ///L/HOH`109/ or ///R/HOH`108/ or ///L/HOH`106/ or ///A/HOH`106/ or ///L/HOH`105/ or ///L/HOH`104/ or ///L/HOH`103/ or ///A/HOH`103/ or ///A/HOH`102/ or ///L/HOH`101/ or ///L/HOH`100/ or ///A/HOH`53/ or ///L/HOH`108/ or ///L/HOH`71/ or ///R/HOH`93/ or ///R/HOH`103/ or ///L/HOH`86/ or ///L/HOH`79/ or ///L/HOH`74/ or ///L/HOH`72/ or ///L/HOH`128/ or ///B/HOH`59/ or ///B/HOH`57/ or ///B/HOH`21/ or ///A/HOH`59/ or ///A/HOH`56/ or ///A/HOH`48/ or ///A/HOH`41/ or ///A/HOH`112/)
<!-- 116 -->
select sur_dna_nt, cons near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 20 -->
select sur_dna_bb, cons near_to 3.5 of (polymer.nucleic and backbone)
<!-- 28 -->
select sur_dna_bb_nt_0, cons near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt, sur_dna_bb_nt_0 near_to 3.5 of (polymer.nucleic and not backbone)

select alfa, (chain L and resi 31-40)
show sticks, alfa
select sur, cons near_to 3.5 of alfa
select sur_i, sur near_to 3.5 of polymer.nucleic
select sur_dna, polymer.nucleic near_to 3.5 of sur_i
show spheres, sur_i

list1=[]
iterate (sur_dna),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur_dna, (///A/DT`24/ or ///A/DA`26/ or ///B/DC`13/ or ///B/DA`17/)

show sticks, sur_dna
hide cartoon, sur_dna and polymer.nucleic
show cartoon, (sur_dna and backbone)

select sur_alfa, alfa near_to 3.5 of sur_i

list1=[]
iterate (sur_alfa),list1.append(("///" + chain + "/" + resn + "`" + resi + "/"))
print list1

select sur_alfa, (///L/SER`31/ or ///L/ASN`32/ or ///L/GLN`37/ or ///L/ARG`40/ or ///L/THR`43/ or ///L/GLU`42/ or ///L/GLN`21/)
show sticks, sur_alfa

select sur_sol, solvent near_to 3.5 of sur_i
show nb_spheres, sur_sol

<!-- /2R1J//A/HOH`59/O
/2R1J//A/HOH`56/O
/2R1J//A/HOH`48/O
/2R1J//L/HOH`72/O -->

select a, ((name o1p or name o2p or name o3p or name p) and ///A/DT`25/)
hide sticks, (name c1*+c2*+c3*+c4*+o2*+o4* and ///A/DT`25/)

```

### TBP

#### 1YTB

```
load /Users/admin/.probisH2O/Probis_H2O/1YTB.pdb, multiplex=1; as cartoon

bg_color white
color slate, polymer.nucleic
color 0xf5deb3, polymer.protein
color sand, ((resi 4-86 and chain A) or (resi 94-177 and chain A) or (resi 4-86 and chain B) or (resi 94-177 and chain B))

select cons_ni, (///A/HOH`305/ or ///A/HOH`322/ or ///A/HOH`330/ or ///A/HOH`325/ or ///C/HOH`387/ or ///C/HOH`374/ or ///A/HOH`514/ or ///C/HOH`406/ or ///C/HOH`382/ or ///A/HOH`434/ or ///C/HOH`375/ or ///A/HOH`331/ or ///C/HOH`380/ or ///A/HOH`302/ or ///A/HOH`352/ or ///A/HOH`362/ or ///A/HOH`349/ or ///A/HOH`328/ or ///A/HOH`342/ or ///A/HOH`467/ or ///C/HOH`371/ or ///A/HOH`361/ or ///A/HOH`545/ or ///A/HOH`720/ or ///A/HOH`554/ or ///A/HOH`327/ or ///A/HOH`473/ or ///A/HOH`315/ or ///C/HOH`393/ or ///C/HOH`381/ or ///A/HOH`351/ or ///C/HOH`404/ or ///C/HOH`369/ or ///A/HOH`548/ or ///A/HOH`471/ or ///A/HOH`397/ or ///C/HOH`367/ or ///A/HOH`457/ or ///A/HOH`454/ or ///C/HOH`341/ or ///A/HOH`301/ or ///A/HOH`350/ or ///A/HOH`354/ or ///C/HOH`386/ or ///A/HOH`329/ or ///A/HOH`353/ or ///A/HOH`506/ or ///A/HOH`469/ or ///C/HOH`478/ or ///A/HOH`543/ or ///A/HOH`448/ or ///C/HOH`377/ or ///C/HOH`357/ or ///A/HOH`765/ or ///A/HOH`523/ or ///C/HOH`356/ or ///A/HOH`542/ or ///A/HOH`505/ or ///A/HOH`364/ or ///C/HOH`476/ or ///A/HOH`405/ or ///C/HOH`396/ or ///C/HOH`384/ or ///C/HOH`439/ or ///A/HOH`475/ or ///A/HOH`304/ or ///C/HOH`522/ or ///A/HOH`336/ or ///A/HOH`316/ or ///A/HOH`309/ or ///C/HOH`326/ or ///A/HOH`318/ or ///A/HOH`310/ or ///C/HOH`535/ or ///A/HOH`511/ or ///A/HOH`461/ or ///C/HOH`427/ or ///A/HOH`333/ or ///A/HOH`312/ or ///C/HOH`462/ or ///A/HOH`481/ or ///A/HOH`694/ or ///A/HOH`339/ or ///A/HOH`557/ or ///C/HOH`501/ or ///A/HOH`495/ or ///C/HOH`389/ or ///C/HOH`376/ or ///A/HOH`303/ or ///A/HOH`504/ or ///A/HOH`547/ or ///A/HOH`422/ or ///A/HOH`360/ or ///C/HOH`441/ or ///C/HOH`394/ or ///A/HOH`446/ or ///C/HOH`443/ or ///C/HOH`410/ or ///A/HOH`513/ or ///A/HOH`390/ or ///A/HOH`319/ or ///C/HOH`531/ or ///C/HOH`491/ or ///A/HOH`464/ or ///A/HOH`456/ or ///C/HOH`530/ or ///C/HOH`445/ or ///A/HOH`546/ or ///A/HOH`527/ or ///A/HOH`519/ or ///A/HOH`415/ or ///A/HOH`402/ or ///A/HOH`487/ or ///A/HOH`449/ or ///A/HOH`559/ or ///A/HOH`528/ or ///A/HOH`500/ or ///A/HOH`459/ or ///A/HOH`447/ or ///C/HOH`442/ or ///A/HOH`421/ or ///A/HOH`416/ or ///C/HOH`388/ or ///C/HOH`370/ or ///A/HOH`526/ or ///C/HOH`411/ or ///A/HOH`777/ or ///C/HOH`773/ or ///A/HOH`741/ or ///A/HOH`681/ or ///A/HOH`672/ or ///A/HOH`560/ or ///A/HOH`552/ or ///C/HOH`534/ or ///A/HOH`521/ or ///A/HOH`499/ or ///A/HOH`496/ or ///C/HOH`485/ or ///A/HOH`466/ or ///A/HOH`463/ or ///A/HOH`450/ or ///C/HOH`444/ or ///C/HOH`425/ or ///A/HOH`423/ or ///C/HOH`403/ or ///C/HOH`400/ or ///C/HOH`368/ or ///A/HOH`344/ or ///A/HOH`340/ or ///A/HOH`338/ or ///A/HOH`320/ or ///A/HOH`313/ or ///A/HOH`525/ or ///B/HOH`770/ or ///B/HOH`693/ or ///C/HOH`533/ or ///B/HOH`493/ or ///C/HOH`424/ or ///A/HOH`420/ or ///A/HOH`413/ or ///C/HOH`401/ or ///A/HOH`392/ or ///A/HOH`355/ or ///A/HOH`308/ or ///B/HOH`307/)
<!-- 165 -->
select sur_dna_nt, cons_ni near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 25 -->
select sur_dna_bb, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
<!-- 27 -->
select sur_dna_bb_nt_0, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt, sur_dna_bb_nt_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 7 -->

select cons_i, (///A/HOH`317/ or ///A/HOH`359/ or ///C/HOH`366/ or ///A/HOH`363/ or ///C/HOH`541/ or ///C/HOH`538/ or ///A/HOH`358/ or ///A/HOH`509/ or ///C/HOH`432/ or ///C/HOH`337/ or ///A/HOH`334/ or ///C/HOH`398/ or ///A/HOH`324/ or ///A/HOH`414/ or ///C/HOH`332/ or ///A/HOH`474/ or ///A/HOH`306/ or ///A/HOH`391/)
<!-- 18 -->
select sur_dna_nt_i, cons_i near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 1 -->
select sur_dna_bb_i, cons_i near_to 3.5 of (polymer.nucleic and backbone)
<!-- 17 -->
select sur_dna_bb_nt_i_0, cons_i near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt_i, sur_dna_bb_nt_i_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 0 -->

select cons_i, (///A/HOH`317/ or ///A/HOH`359/ or ///C/HOH`366/ or ///A/HOH`363/)
show spheres, cons_i
color red, cons_i

select cons_n_i, (///A/HOH`305/ or ///A/HOH`322/ or ///A/HOH`330/ or ///A/HOH`325/)
show spheres, cons_n_i
color salmon, cons_n_i


```

### P53

#### 5MCT

```
load /Users/admin/.probisH2O/Probis_H2O/5MCT.pdb, multiplex=1; as cartoon

bg_color white
color slate, polymer.nucleic
color 0xf5deb3, polymer.protein
color sand, ((resi 6-196 and chain A) (resi 6-196 and chain B))
select zinc, resn ZN
show spheres, zinc
color palecyan,  zinc

select cons_ni, (///A/HOH`418/ or ///A/HOH`450/ or ///A/HOH`501/ or ///A/HOH`499/ or ///A/HOH`447/ or ///A/HOH`431/ or ///A/HOH`583/ or ///A/HOH`536/ or ///A/HOH`457/ or ///A/HOH`443/ or ///A/HOH`464/ or ///A/HOH`504/ or ///A/HOH`452/ or ///A/HOH`584/ or ///A/HOH`453/ or ///A/HOH`484/ or ///A/HOH`485/ or ///A/HOH`550/ or ///A/HOH`434/ or ///A/HOH`414/ or ///A/HOH`541/ or ///A/HOH`529/ or ///A/HOH`440/ or ///A/HOH`467/ or ///A/HOH`599/ or ///A/HOH`577/ or ///A/HOH`439/ or ///A/HOH`422/ or ///A/HOH`512/ or ///A/HOH`564/ or ///A/HOH`552/ or ///A/HOH`582/ or ///C/HOH`170/ or ///A/HOH`571/ or ///A/HOH`424/ or ///C/HOH`146/ or ///A/HOH`442/ or ///A/HOH`648/ or ///A/HOH`528/ or ///A/HOH`427/ or ///A/HOH`423/ or ///A/HOH`537/ or ///A/HOH`525/ or ///A/HOH`480/ or ///A/HOH`498/ or ///A/HOH`560/ or ///A/HOH`569/ or ///A/HOH`558/ or ///A/HOH`543/ or ///A/HOH`465/ or ///A/HOH`473/ or ///A/HOH`428/ or ///A/HOH`523/ or ///A/HOH`441/ or ///A/HOH`472/ or ///A/HOH`449/ or ///A/HOH`578/ or ///A/HOH`459/ or ///A/HOH`405/ or ///A/HOH`566/ or ///A/HOH`471/ or ///A/HOH`530/ or ///C/HOH`151/ or ///A/HOH`600/ or ///A/HOH`425/ or ///A/HOH`527/ or ///A/HOH`589/ or ///A/HOH`585/ or ///A/HOH`538/ or ///A/HOH`646/ or ///A/HOH`568/ or ///A/HOH`649/ or ///A/HOH`576/ or ///A/HOH`456/ or ///A/HOH`573/ or ///A/HOH`497/ or ///A/HOH`426/ or ///A/HOH`535/ or ///A/HOH`634/ or ///A/HOH`475/ or ///C/HOH`177/ or ///A/HOH`574/ or ///A/HOH`642/ or ///A/HOH`598/ or ///C/HOH`118/ or ///A/HOH`579/ or ///A/HOH`411/ or ///A/HOH`409/ or ///C/HOH`196/ or ///A/HOH`565/ or ///A/HOH`605/ or ///A/HOH`433/ or ///B/HOH`455/ or ///B/HOH`438/ or ///C/HOH`145/ or ///A/HOH`489/ or ///A/HOH`420/ or ///A/HOH`513/ or ///A/HOH`437/ or ///B/HOH`479/ or ///A/HOH`608/ or ///A/HOH`478/ or ///C/HOH`111/ or ///A/HOH`595/ or ///A/HOH`591/ or ///B/HOH`531/ or ///B/HOH`452/ or ///A/HOH`641/ or ///A/HOH`435/ or ///A/HOH`416/ or ///A/HOH`410/ or ///A/HOH`547/ or ///A/HOH`500/ or ///A/HOH`597/ or ///A/HOH`502/ or ///A/HOH`637/ or ///A/HOH`483/ or ///A/HOH`487/ or ///A/HOH`461/ or ///A/HOH`549/ or ///A/HOH`419/ or ///A/HOH`548/ or ///A/HOH`596/ or ///A/HOH`532/ or ///A/HOH`635/ or ///A/HOH`609/ or ///A/HOH`545/ or ///A/HOH`514/ or ///A/HOH`458/ or ///A/HOH`556/ or ///A/HOH`643/ or ///A/HOH`516/ or ///A/HOH`522/ or ///A/HOH`518/ or ///A/HOH`491/ or ///A/HOH`448/ or ///A/HOH`477/ or ///A/HOH`468/ or ///A/HOH`454/ or ///A/HOH`544/ or ///A/HOH`652/ or ///A/HOH`505/ or ///A/HOH`488/ or ///B/HOH`475/ or ///A/HOH`492/ or ///A/HOH`592/ or ///A/HOH`570/ or ///A/HOH`563/ or ///C/HOH`150/ or ///A/HOH`519/ or ///A/HOH`612/ or ///A/HOH`506/ or ///A/HOH`482/ or ///A/HOH`474/ or ///A/HOH`520/ or ///A/HOH`436/ or ///A/HOH`555/ or ///A/HOH`432/ or ///A/HOH`479/ or ///A/HOH`615/ or ///A/HOH`524/ or ///A/HOH`494/ or ///A/HOH`614/ or ///A/HOH`429/ or ///A/HOH`517/ or ///A/HOH`533/ or ///A/HOH`470/ or ///A/HOH`588/ or ///A/HOH`542/ or ///A/HOH`559/ or ///A/HOH`546/ or ///A/HOH`509/ or ///A/HOH`413/ or ///A/HOH`402/ or ///A/HOH`651/ or ///B/HOH`498/ or ///C/HOH`198/ or ///A/HOH`486/ or ///A/HOH`490/ or ///C/HOH`171/ or ///A/HOH`633/ or ///A/HOH`617/ or ///A/HOH`602/ or ///A/HOH`521/ or ///A/HOH`496/ or ///A/HOH`438/ or ///A/HOH`587/ or ///A/HOH`557/ or ///A/HOH`445/ or ///C/HOH`115/ or ///B/HOH`540/ or ///B/HOH`534/ or ///B/HOH`490/ or ///B/HOH`482/ or ///B/HOH`440/ or ///A/HOH`503/ or ///A/HOH`481/ or ///A/HOH`417/ or ///A/HOH`551/ or ///A/HOH`540/ or ///A/HOH`476/ or ///A/HOH`466/ or ///B/HOH`647/ or ///B/HOH`597/ or ///B/HOH`588/ or ///B/HOH`581/ or ///B/HOH`579/ or ///B/HOH`575/ or ///B/HOH`563/ or ///B/HOH`562/ or ///B/HOH`557/ or ///B/HOH`547/ or ///B/HOH`546/ or ///B/HOH`539/ or ///B/HOH`538/ or ///B/HOH`528/ or ///B/HOH`526/ or ///B/HOH`525/ or ///B/HOH`520/ or ///B/HOH`511/ or ///B/HOH`508/ or ///B/HOH`497/ or ///B/HOH`494/ or ///B/HOH`493/ or ///B/HOH`485/ or ///B/HOH`484/ or ///B/HOH`478/ or ///B/HOH`471/ or ///B/HOH`458/ or ///B/HOH`457/ or ///B/HOH`453/ or ///B/HOH`447/ or ///B/HOH`446/ or ///B/HOH`443/ or ///B/HOH`442/ or ///B/HOH`435/ or ///B/HOH`429/ or ///B/HOH`426/ or ///B/HOH`425/ or ///B/HOH`420/ or ///B/HOH`414/ or ///B/HOH`409/ or ///C/HOH`205/ or ///A/HOH`626/ or ///A/HOH`624/ or ///A/HOH`508/ or ///A/HOH`412/ or ///A/HOH`630/ or ///A/HOH`621/ or ///A/HOH`601/ or ///A/HOH`562/ or ///B/HOH`642/ or ///B/HOH`611/ or ///B/HOH`594/ or ///B/HOH`593/ or ///B/HOH`573/ or ///B/HOH`571/ or ///B/HOH`570/ or ///B/HOH`548/ or ///B/HOH`544/ or ///B/HOH`542/ or ///B/HOH`535/ or ///B/HOH`533/ or ///B/HOH`532/ or ///B/HOH`521/ or ///B/HOH`513/ or ///B/HOH`509/ or ///B/HOH`506/ or ///B/HOH`495/ or ///B/HOH`474/ or ///B/HOH`472/ or ///B/HOH`470/ or ///B/HOH`468/ or ///B/HOH`466/ or ///B/HOH`462/ or ///B/HOH`450/ or ///B/HOH`437/ or ///B/HOH`433/ or ///B/HOH`415/ or ///A/HOH`455/ or ///A/HOH`618/ or ///A/HOH`493/ or ///A/HOH`451/ or ///C/HOH`181/ or ///C/HOH`142/ or ///A/HOH`593/ or ///A/HOH`586/ or ///A/HOH`463/ or ///A/HOH`415/ or ///A/HOH`404/ or ///C/HOH`190/ or ///C/HOH`157/ or ///C/HOH`140/ or ///C/HOH`136/ or ///B/HOH`651/ or ///B/HOH`649/ or ///B/HOH`636/ or ///B/HOH`633/ or ///B/HOH`625/ or ///B/HOH`614/ or ///B/HOH`612/ or ///B/HOH`609/ or ///B/HOH`601/ or ///B/HOH`595/ or ///A/HOH`590/ or ///B/HOH`587/ or ///B/HOH`585/ or ///B/HOH`568/ or ///B/HOH`564/ or ///B/HOH`561/ or ///B/HOH`559/ or ///B/HOH`552/ or ///B/HOH`551/ or ///B/HOH`541/ or ///B/HOH`537/ or ///B/HOH`523/ or ///B/HOH`519/ or ///B/HOH`518/ or ///A/HOH`515/ or ///B/HOH`515/ or ///B/HOH`503/ or ///B/HOH`499/ or ///B/HOH`487/ or ///B/HOH`486/ or ///B/HOH`483/ or ///B/HOH`477/ or ///B/HOH`463/ or ///B/HOH`461/ or ///B/HOH`460/ or ///B/HOH`456/ or ///B/HOH`444/ or ///B/HOH`441/ or ///A/HOH`430/ or ///B/HOH`427/ or ///B/HOH`419/ or ///B/HOH`416/ or ///B/HOH`405/ or ///A/HOH`408/ or ///A/HOH`620/ or ///A/HOH`403/ or ///A/HOH`625/ or ///B/HOH`598/ or ///A/HOH`575/ or ///A/HOH`469/ or ///A/HOH`462/ or ///C/HOH`184/ or ///C/HOH`128/ or ///C/HOH`125/ or ///B/HOH`650/ or ///A/HOH`650/ or ///B/HOH`648/ or ///A/HOH`647/ or ///B/HOH`638/ or ///B/HOH`634/ or ///A/HOH`632/ or ///A/HOH`622/ or ///B/HOH`621/ or ///A/HOH`619/ or ///B/HOH`616/ or ///B/HOH`613/ or ///A/HOH`611/ or ///B/HOH`607/ or ///B/HOH`583/ or ///B/HOH`574/ or ///B/HOH`565/ or ///B/HOH`555/ or ///B/HOH`550/ or ///B/HOH`536/ or ///B/HOH`517/ or ///B/HOH`510/ or ///B/HOH`501/ or ///B/HOH`465/ or ///B/HOH`464/ or ///B/HOH`454/ or ///B/HOH`436/ or ///B/HOH`430/ or ///B/HOH`423/ or ///B/HOH`418/ or ///B/HOH`412/ or ///B/HOH`411/ or ///A/HOH`406/ or ///B/HOH`406/ or ///B/HOH`403/ or ///A/HOH`401/ or ///C/HOH`173/ or ///C/HOH`172/ or ///C/HOH`155/ or ///C/HOH`152/ or ///C/HOH`143/ or ///A/HOH`644/ or ///A/HOH`631/ or ///A/HOH`629/ or ///A/HOH`606/ or ///A/HOH`526/ or ///A/HOH`421/ or ///C/HOH`175/ or ///C/HOH`123/ or ///B/HOH`646/ or ///B/HOH`643/ or ///B/HOH`640/ or ///B/HOH`631/ or ///B/HOH`629/ or ///B/HOH`623/ or ///B/HOH`619/ or ///B/HOH`600/ or ///B/HOH`599/ or ///B/HOH`596/ or ///B/HOH`591/ or ///B/HOH`586/ or ///B/HOH`578/ or ///B/HOH`569/ or ///B/HOH`567/ or ///A/HOH`567/ or ///B/HOH`566/ or ///A/HOH`553/ or ///B/HOH`553/ or ///B/HOH`545/ or ///B/HOH`543/ or ///A/HOH`531/ or ///B/HOH`530/ or ///B/HOH`527/ or ///B/HOH`516/ or ///B/HOH`504/ or ///B/HOH`496/ or ///B/HOH`492/ or ///B/HOH`489/ or ///B/HOH`488/ or ///B/HOH`481/ or ///B/HOH`473/ or ///B/HOH`469/ or ///B/HOH`467/ or ///B/HOH`451/ or ///B/HOH`445/ or ///A/HOH`444/ or ///B/HOH`439/ or ///B/HOH`434/ or ///B/HOH`421/ or ///B/HOH`410/ or ///B/HOH`402/ or ///B/HOH`401/ or ///C/HOH`191/ or ///C/HOH`186/ or ///C/HOH`179/ or ///C/HOH`163/ or ///C/HOH`113/ or ///A/HOH`603/ or ///A/HOH`640/ or ///A/HOH`604/ or ///A/HOH`511/ or ///C/HOH`176/ or ///B/HOH`653/ or ///A/HOH`639/ or ///B/HOH`628/ or ///B/HOH`626/ or ///B/HOH`624/ or ///B/HOH`618/ or ///B/HOH`617/ or ///A/HOH`616/ or ///B/HOH`606/ or ///B/HOH`604/ or ///B/HOH`603/ or ///B/HOH`580/ or ///B/HOH`576/ or ///B/HOH`556/ or ///B/HOH`524/ or ///B/HOH`512/ or ///B/HOH`505/ or ///B/HOH`500/ or ///B/HOH`491/ or ///B/HOH`459/ or ///B/HOH`449/ or ///B/HOH`431/ or ///B/HOH`428/ or ///B/HOH`424/ or ///B/HOH`422/ or ///B/HOH`417/ or ///B/HOH`413/ or ///A/HOH`407/ or ///B/HOH`404/ or ///C/HOH`197/ or ///C/HOH`194/ or ///C/HOH`178/ or ///C/HOH`174/ or ///C/HOH`169/ or ///C/HOH`164/ or ///C/HOH`160/ or ///C/HOH`148/ or ///C/HOH`141/ or ///C/HOH`137/ or ///C/HOH`134/ or ///C/HOH`132/ or ///C/HOH`131/ or ///C/HOH`130/ or ///C/HOH`124/ or ///C/HOH`121/ or ///C/HOH`117/ or ///C/HOH`110/ or ///C/HOH`108/ or ///C/HOH`106/)
<!-- 998 -->
select sur_dna_nt, cons_ni near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 82 -->
select sur_dna_bb, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
<!-- 84 -->
select sur_dna_bb_nt_0, cons_ni near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt, sur_dna_bb_nt_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 58 -->

select cons_i, (///A/HOH`446/ or ///C/HOH`180/ or ///C/HOH`119/ or ///A/HOH`561/ or ///C/HOH`202/ or ///A/HOH`507/ or ///A/HOH`539/ or ///A/HOH`510/ or ///A/HOH`610/ or ///A/HOH`572/ or ///C/HOH`200/ or ///C/HOH`187/ or ///B/HOH`448/ or ///C/HOH`162/ or ///A/HOH`495/ or ///C/HOH`203/ or ///C/HOH`182/ or ///C/HOH`114/ or ///B/HOH`558/ or ///B/HOH`507/ or ///B/HOH`502/ or ///C/HOH`103/ or ///C/HOH`159/ or ///A/HOH`594/ or ///C/HOH`120/ or ///B/HOH`572/ or ///C/HOH`204/ or ///C/HOH`201/ or ///C/HOH`188/ or ///C/HOH`167/ or ///C/HOH`199/ or ///C/HOH`139/ or ///C/HOH`116/ or ///B/HOH`608/ or ///B/HOH`480/ or ///C/HOH`153/ or ///A/HOH`580/ or ///C/HOH`165/ or ///C/HOH`156/ or ///C/HOH`133/ or ///C/HOH`105/ or ///B/HOH`584/ or ///A/HOH`607/)
<!-- 86 -->
select sur_dna_nt_i, cons_i near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 32 -->
select sur_dna_bb_i, cons_i near_to 3.5 of (polymer.nucleic and backbone)
<!-- 64 -->
select sur_dna_bb_nt_i_0, cons_i near_to 3.5 of (polymer.nucleic and backbone)
select sur_dna_bb_nt_i, sur_dna_bb_nt_i_0 near_to 3.5 of (polymer.nucleic and not backbone)
<!-- 10 -->

```
