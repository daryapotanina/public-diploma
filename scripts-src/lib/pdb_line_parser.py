from pathlib import Path
import copy
import sys
import warnings

import numpy as np


class Atom:
    def __init__(
        self,
        serial,
        name,
        altLoc,
        resName,
        chainID,
        resSeq,
        iCode,
        x,
        y,
        z,
        occupancy,
        tempFactor,
        element,
        charge,
    ):
        self.serial = serial
        self.name = name
        self.altLoc = altLoc
        self.resName = resName
        self.chainID = chainID
        self.resSeq = resSeq
        self.iCode = iCode
        self.x = x
        self.y = y
        self.z = z
        self.occupancy = occupancy
        self.tempFactor = tempFactor
        self.element = element
        self.charge = charge

    def __getitem__(self, k):
        return k

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return f"<Atom {self.__dict__}>"


def read_file_adn_parse_pdb(path: str) -> list[Atom]:
    print("path", path)
    atoms: list[Atom] = []
    list_of_raw_atoms = Path(path).read_text().splitlines()

    for item in list_of_raw_atoms:
        if "HETATM" in str(item[0:6]) or "ATOM" in str(item[0:6]):
            serial = int(item[6:11])
            name = item[12:16].strip()
            altLoc = item[16:17].strip()
            resName = item[17:20].strip()
            chainID = item[21:22].strip()
            resSeq = item[22:26].strip()
            iCode = item[26:27].strip()
            x = float(item[30:38])
            y = float(item[38:46])
            z = float(item[46:54])
            occupancy = float(item[54:60])
            tempFactor = float(item[60:66])
            element = item[76:78].strip()
            charge = item[78:80].strip()

            atom = Atom(
                serial,
                name,
                altLoc,
                resName,
                chainID,
                resSeq,
                iCode,
                x,
                y,
                z,
                occupancy,
                tempFactor,
                element,
                charge,
            )
            # print(atom)
            atoms.append(atom)

    # print(atoms[0].x)

    return atoms
