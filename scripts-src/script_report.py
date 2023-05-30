import argparse
import logging
import copy
import re
import sys
import traceback
from typing import TypedDict

import pandas as pd
import numpy as np

from lib.pdb_line_parser import read_file_adn_parse_pdb, Atom
from lib.utils import read_file_and_splitlines, read_file
from lib.emoji_list import EMOJI_LIST


class Result(TypedDict):
    selector: str
    main_protein_tempFactor: str
    main_protein_occupancy: str
    main_protein: str
    main_protein_coords: str
    main_protein_group_id: str
    main_protein_location: str
    ref_pretein_id: str
    ref_pretein: str
    ref_pretein_chain: str
    ref_pretein_location: str


def parseLocation(str):
    return str.split("location: ")[1].replace("'", "").replace("]", "")


def parsePdbName(str):
    return str.split(",")[-1].split("location: ")[0].replace("'", "").strip()


def parseCoords(str):
    res = re.search(r"\[\[(.*)\],", str)
    if res:
        return res.group(1)
    return " - "


def parseRefProteinAndChainName(str):
    ProteinAndChainName = str.split(".0.rota.pdb")[0].split("_")[1]
    chain = ProteinAndChainName[-1]
    protein = ProteinAndChainName[:-1]

    return [protein, chain]


def is_number_tryexcept(s):
    """Returns True if string is a number."""
    try:
        float(s)
        return True
    except ValueError:
        return False


parser = argparse.ArgumentParser(
    prog="make_reports",
)

parser.add_argument("--name", help="output filename")
parser.add_argument("--log_name", help="input logs filename")
parser.add_argument("--family_id")
parser.add_argument("-v", "--verbose", action="store_true")  # on/off flag

args = parser.parse_args()
print(args.family_id, args.verbose)

FLAG_NAME = args.name
FLAG_LOG_FILENAME = args.log_name
FLAG_FAMILY_ID = args.family_id
FLAG_VERBOSE = args.verbose

PLAIN_LOG_NAME = FLAG_LOG_FILENAME.replace("probis_py_", "")

scripts_log_filename = "logs/report_" + FLAG_NAME + ".log"

file_handler = logging.FileHandler(filename=scripts_log_filename)
stdout_handler = logging.StreamHandler(stream=sys.stdout)
logging_handlers = [file_handler, stdout_handler]

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=0,
    handlers=logging_handlers,
)

logger = logging.getLogger("script_log")


def handle_sys_except(type_, value, tb):
    text = "".join(traceback.format_exception(type_, value, tb))
    logger.exception(text)


sys.excepthook = handle_sys_except

list_of_atoms = []

tableOfProtAC = pd.read_csv("../database/ProtAC_PDB.csv").loc[
    lambda x: x["family_id"] == FLAG_FAMILY_ID
]
tableOfProtAC["entry_id"] = tableOfProtAC["entry_id"].map(lambda x: x.lower())

tableOfProtACGroupedByProteinAc = (
    tableOfProtAC.groupby(["protein_ac"])
    .agg(" ".join)
    .sort_values(["entry_id"], key=lambda x: x.str.len())
)
tableOfProtACGroupedByProtein = {}

logging.info("tableOfProtAC %s", tableOfProtAC)


for index, row in tableOfProtAC.iterrows():
    tableOfProtACGroupedByProtein[row["entry_id"]] = row["protein_ac"]

print(tableOfProtACGroupedByProtein)
# for index, row in tableOfProtACGroupedByProteinAc.iterrows():
#     for j in row["entry_id"].split(" "):
#         print(j, row.name)

# for row in range(len(tableOfProtACGroupedByProteinAc)):
#     print(
#         # tableOfProtACGroupedByProteinAc.at[row, "protein_ac"],
#         tableOfProtACGroupedByProteinAc.at[row, "entry_id"],
#     )

# print(pd.merge(on=["protein_ac"]))
# print(np.gro)

pymol_response: list[str] = []

try:
    pymol_resp_list = read_file_and_splitlines(
        "./pymol_resp/" + "pymol_rpc_workaround_report_" + PLAIN_LOG_NAME + ".txt",
    )
    pymol_response = list(map(lambda x: x.replace("///", "/"), pymol_resp_list))
except FileNotFoundError as err:
    print("")
    print(f"Не найден ответ от pymol {err=}, {type(err)=}")
    raise

print(pymol_response)

#########################################################
#  START CODE
#########################################################

lisftOfResult: list[Result] = []

listOfList = read_file(f"../probisH2O-logs/{FLAG_LOG_FILENAME}.log").split(
    "IDENTIFIED CLUSTERS"
)

# for item in listOfList:
#     print(item)
#     print("++++++++++++++++++++++++++++++++=")

actualLogs = listOfList[-1].split("report_list_1 -------------------------")
actualLogs = list(filter(lambda v: "location:" in v, actualLogs))
# actualLogs = list(filter(lambda v: {}, actualLogs))

actualLogs = list(
    map(
        lambda v: list(filter(lambda v2: "location" in v2, v.split("\n"))),
        actualLogs,
    )
)

for rawList in actualLogs:
    local_list = [__.split(", ") for __ in rawList]
    df = pd.DataFrame(local_list)
    # print(df)
    groupedByCluster = df.groupby(3).groups
    # print("................")
    for name, group in df.groupby(3):
        # print(name)
        # print(group)
        # print(group.columns)
        # print(list(group.columns))
        countOfExclude_rota_pdb = group[~group[5].str.contains(".rota.pdb")]
        if len(countOfExclude_rota_pdb) == 0:
            continue

        # print("111111")
        first_line_as_string = ", ".join(countOfExclude_rota_pdb.iloc[0].to_list())
        locationOfMainPdp = parseLocation(first_line_as_string)

        only_rota_pdb = group[group[5].str.contains(".rota.pdb")]
        for rota_index, rota_iterator in only_rota_pdb.iterrows():
            # print(rota_iterator.to_list())
            # print(rota_iterator[5])
            # print("*********")
            main_protein = parsePdbName(first_line_as_string)
            _coords = parseCoords(first_line_as_string).replace(" ", "")
            # print(_coords)
            # sys.exit(0)
            # print("")
            # print(first_line_as_string)
            # print(main_protein)
            # print(_coords)
            # print("^^^^^^^^^^^^^^")
            itemOfResult = Result(
                selector="null",
                main_protein_occupancy="null",
                main_protein_tempFactor="null",
                main_protein=main_protein,
                main_protein_coords=_coords,
                main_protein_group_id=locationOfMainPdp
                + "_"
                + parseCoords(first_line_as_string),
                main_protein_location=locationOfMainPdp,
                ref_pretein_id="_".join(parseRefProteinAndChainName(rota_iterator[5])),
                ref_pretein=parseRefProteinAndChainName(rota_iterator[5])[0],
                ref_pretein_chain=parseRefProteinAndChainName(rota_iterator[5])[1],
                ref_pretein_location=parseLocation(rota_iterator[5]),
            )
            # print(itemOfResult)
            lisftOfResult.append(itemOfResult)

        # sys.exit(1)
    # for iteratorIndexGroup, values in groupedByCluster:
    # print(iteratorIndexGroup, values)
    # print(df.groupby(3).groups)
    # pprint.pprint(list)
    # print(len(list))

# pd.DataFrame(lisftOfResult).sort_values(
#     by=["main_protein_location", "ref_pretein_id"]
# ).to_csv("py.csv", index=False)

print(len(actualLogs))
print(len(listOfList))
print(len(lisftOfResult))
print(lisftOfResult[0]["main_protein"])
print(lisftOfResult[0]["main_protein_coords"])

list_of_atoms = read_file_adn_parse_pdb("../pdb/" + lisftOfResult[0]["main_protein"])


def addPymolSelector(res: Result):
    [x, y, z] = res["main_protein_coords"].split(",")

    atom = next(
        (
            sub
            for sub in list_of_atoms
            if x in str(sub.x) and y in str(sub.y) and z in str(sub.z)
        ),
        None,
    )

    if atom:
        selector = f"/{res['main_protein'].replace('.pdb', '')}//{atom.chainID}/{atom.resName}`{atom.resSeq}/{atom.name}"
        # print(selector)
        res["selector"] = selector
        res["main_protein_occupancy"] = str(int(atom.occupancy))
        res["main_protein_tempFactor"] = atom.tempFactor
        # print(atom)
        # print(res)
        # sys.exit(1)
        return res
    res["main_protein"] = "kek"

    return res


# f = lambda x:(
#      x + 1
# )

lisftOfResult = list(map(lambda x: addPymolSelector(x), lisftOfResult))

# print(list_of_atoms[-10])
# print(list_of_atoms[-10].x)
# print(str(list_of_atoms[-10].x))
# print("9" in str(list_of_atoms[-10].x))
# print(found_user)

list_of_res_df = pd.DataFrame(lisftOfResult)
# print(
#     list_of_res_df.groupby("main_protein_group_id").agg(
#         ref_pretein_id=("ref_pretein_id", "unique"),
#         ref_pretein_location=("ref_pretein_location", "unique"),
#     )
# )
# list_of_res_df.to_csv("test.csv", index=False)

grouped_by_ref_pretein_id = (
    list_of_res_df.groupby("ref_pretein_id")
    .agg(
        ref_pretein_location=("ref_pretein_location", "unique"),
    )
    .to_dict()["ref_pretein_location"]
)


grouped_by_main_protein_location_and_coords = list_of_res_df.groupby(
    "main_protein_group_id"
).groups


#########################################################
#  NEXT PART
#########################################################

# tableOfProtACGroupedByProteinAc = (
#     tableOfProtAC.groupby(["protein_ac"]).agg(
#     ref_pretein_location=("ref_pretein_location", "unique")
#     )
#     .sort_values(["entry_id"], key=lambda x: x.str.len())
# )

tableOfProtACGroupedByProteinAc = (
    tableOfProtAC.groupby(["protein_ac"])
    .agg(
        protein_ac=("protein_ac", "unique"),
        entry_id=("entry_id", "unique"),
    )
    .sort_values(["entry_id"], key=lambda x: x.str.len())
)
# print(tableOfProtAC)
tableFromSqlGroupedByProtein = {}

for index, row in tableOfProtAC.iterrows():
    tableFromSqlGroupedByProtein[row["entry_id"]] = row["protein_ac"]


subHeaders = []
subHeadersWithoutProtein_ac: list[str] = []
proteinNameFromFamilyCsv = []
proteinAcDict = {}

for index, row in tableOfProtACGroupedByProteinAc.iterrows():
    for entry_id in row["entry_id"]:
        similarPdbs = list(
            filter(lambda v: entry_id + "_" in v, grouped_by_ref_pretein_id.keys())
        )
        proteinNameFromFamilyCsv.append(entry_id)
        for similarPdb in similarPdbs:
            subHeaders.append((row["protein_ac"][0], similarPdb))
            subHeadersWithoutProtein_ac.append(similarPdb)
            proteinAcDict[row["protein_ac"][0]] = True
        if len(similarPdbs) == 0:
            subHeaders.append((row["protein_ac"][0], entry_id))
            subHeadersWithoutProtein_ac.append(entry_id)
            proteinAcDict[row["protein_ac"][0]] = True

# uniqProteinAc = list(np.unique(np.array(list(map(lambda x: x[0], subHeaders))), axis=0))
uniqProteinAc = list(proteinAcDict.keys())

uniqProteinNameFromFamilyCsv = proteinNameFromFamilyCsv

print(proteinNameFromFamilyCsv)
print(uniqProteinNameFromFamilyCsv)


#########################################################
#  NEXT PART
#########################################################

main_protein_name = list_of_res_df["main_protein"][0].replace(".pdb", "")
print(main_protein_name)


final = []

for main_protein_group_id in grouped_by_main_protein_location_and_coords.keys():
    port_list = list_of_res_df.loc[
        lambda x: x["main_protein_group_id"] == main_protein_group_id
    ]
    prot = port_list.loc[port_list.index[0]]

    interface_field = next(
        (sub for sub in pymol_response if sub in prot.selector),
        None,
    )

    item = {
        "selector": prot.selector,
        "interface": bool(interface_field) and ("//" + str(interface_field)) or "",
        "coords": prot.main_protein_coords,
        "main_protein_location": prot.main_protein_location,
        "occupancy": prot.main_protein_occupancy,
        "tempFactor": prot.main_protein_tempFactor,
    }

    for index, value in enumerate(subHeaders):
        item[subHeaders[index][1]] = "‎ "
        # print("index", index, "for value", value)

    for indx in grouped_by_main_protein_location_and_coords[main_protein_group_id]:
        find_res = list_of_res_df.loc[int(str(indx))]
        # item[find_res.ref_pretein_id] =  find_res.ref_pretein_location + "";
        # print(indx)
        # print(find_res["ref_pretein_id"])
        # print(find_res["ref_pretein_location"])
        item[find_res["ref_pretein_id"]] = str(find_res["ref_pretein_location"]) + ""

    item[main_protein_name] = item["main_protein_location"]

    filtededHeaders = list(
        filter(lambda x: is_number_tryexcept(item[x]), subHeadersWithoutProtein_ac)
    )
    print("subHeadersWithoutProtein_ac", subHeadersWithoutProtein_ac)

    print(
        "item[x]",
        item[subHeadersWithoutProtein_ac[0]],
        is_number_tryexcept(item[subHeadersWithoutProtein_ac[0]]),
    )
    filtededHeadersUniqWithoutChain = set(
        list(map(lambda x: x.split("_")[0], filtededHeaders))
    )

    uniqGroup = set(
        list(
            map(
                lambda x: tableFromSqlGroupedByProtein[x],
                filtededHeadersUniqWithoutChain,
            )
        )
    )

    item["sum_with_chain"] = len(filtededHeaders)
    item["sum"] = len(filtededHeadersUniqWithoutChain)
    item["cons"] = len(filtededHeadersUniqWithoutChain) / len(
        uniqProteinNameFromFamilyCsv
    )
    item[
        "cons_exp"
    ] = f"{len(filtededHeadersUniqWithoutChain)} / {len(uniqProteinNameFromFamilyCsv)}"
    item["sum_prot_ac"] = len(uniqGroup)

    # print(item)
    # print("-----------------")
    final.append(item)
    # print(main_protein_group_id)


def lineWithProteinAcIndexOnlyFunc(key, val):
    if key == "selector":
        return "Protein_AC"
    if key in subHeadersWithoutProtein_ac:
        protein_ac = next(el[0] for el in subHeaders if el[1] == key)
        indexOfPAC = uniqProteinAc.index(protein_ac)
        return indexOfPAC

    return " "


lineWithProteinAcIndexOnly = dict(
    map(
        lambda item: (item[0], lineWithProteinAcIndexOnlyFunc(item[0], item[1])),
        copy.deepcopy(final[0]).items(),
    )
)


def lineWithProteinAcEmojOnlyFunc(key, val):
    if key == "selector":
        return "Protein_AC"
    if key in subHeadersWithoutProtein_ac:
        protein_ac = next(el[0] for el in subHeaders if el[1] == key)
        indexOfPAC = uniqProteinAc.index(protein_ac)
        if key == main_protein_name:
            return EMOJI_LIST[indexOfPAC] + " ↑↑↑ "
        return EMOJI_LIST[indexOfPAC]

    return " "


lineWithProteinAcEmojOnly = dict(
    map(
        lambda item: (item[0], lineWithProteinAcEmojOnlyFunc(item[0], item[1])),
        copy.deepcopy(final[0]).items(),
    )
)


def lineWithProteinAcFunc(key, val):
    if key == "selector":
        return "Protein_AC"
    if key in subHeadersWithoutProtein_ac:
        protein_ac = next(el[0] for el in subHeaders if el[1] == key)
        return protein_ac

    return " "


lineWithProteinAc = dict(
    map(
        lambda item: (item[0], lineWithProteinAcFunc(item[0], item[1])),
        copy.deepcopy(final[0]).items(),
    )
)

final_df = pd.DataFrame(final)
final_df = final_df.sort_values(["interface", "main_protein_location"], ascending=False)

pd.concat(
    [
        pd.DataFrame(
            [
                lineWithProteinAcIndexOnly,
                lineWithProteinAcEmojOnly,
                lineWithProteinAc,
            ]
        ),
        final_df,
    ],
    ignore_index=True,
).to_csv("../reports/report_" + FLAG_NAME + ".csv", index=False)

print(subHeadersWithoutProtein_ac)
print(uniqProteinAc)
