# Copyright Notice
# ================
#
# The PyMOL Plugin source code in this file is copyrighted, but you can
# freely use and copy it as long as you don't change or remove any of
# the copyright notices.
#
# ----------------------------------------------------------------------
# This PyMOL Plugin is Copyright (C) 2017 by Marko Jukic <marko.jukic@ffa.uni-lj.si>
#
#                        All Rights Reserved
#
# Permission to use, copy and distribute
# versions of this software and its documentation for any purpose and
# without fee is hereby granted, provided that the above copyright
# notice appear in all copies and that both the copyright notice and
# this permission notice appear in supporting documentation, and that
# the name(s) of the author(s) not be used in advertising or publicity
# pertaining to distribution of the software without specific, written
# prior permission.
#
# THE AUTHOR(S) DISCLAIM ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.  IN
# NO EVENT SHALL THE AUTHOR(S) BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
# USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
# OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
# PERFORMANCE OF THIS SOFTWARE.
# ----------------------------------------------------------------------


# -*- coding: utf-8 -*-
# ProBis_H2O
# written for python 2.7.x
# Not Yet Described at PyMOL wiki: /
# Author : Marko Jukic
# Date: October 2017
# License: chech http://insilab.org
# Version: 0.93
#__author__ = "Marko Jukic"
#__licence__ = "http://insilab.org"
#__version__ = "0.93"


# Comments: Script is commented in Slovene language
#

from __future__ import absolute_import
from __future__ import print_function
import sys, re, gzip, os, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse
import stat
import pymol, json, math, multiprocessing
import subprocess
from pymol.cgo import *
from pymol import cmd
import time
from glob import glob
from ftplib import FTP
from itertools import groupby
from pathlib import Path

from pymol.Qt import QtWidgets, QtGui, QtCore
from pymol.Qt.utils import loadUi

# ADDITIONAL MODULES----------------------------------------------------------------------=
try:
    import numpy as np
    print("Numpy module is installed")
except:
    from pip._internal import main as pip
    print("Numpy module has not been installed yet. \nProgram will now install Numpy module")
    time.sleep(1)
    pip(['install', 'numpy'])
    import numpy as np

try:
    from sklearn.cluster import DBSCAN
    print("Sklearn module is installed")
except:
    from pip._internal import main as pip
    print("Sklearn module has not been installed yet. \nProgram will now install Scikit-learn module")
    time.sleep(1)
    pip(['install', 'scikit-learn'])
    from sklearn.cluster import DBSCAN

# ---------------------------------------INITIALIZE-----------------------------

install_dir=os.path.join(Path.home(), ".probish2o_installdir.txt")

install_datoteka = open(install_dir, "r")
H2O_DIRECTORY=install_datoteka.readline()
install_datoteka.close()
MODULE_DIRECTORY=os.path.join(H2O_DIRECTORY, "module")
UI_DIRECTORY=os.path.join(H2O_DIRECTORY,"UI")
versionFile = os.path.join(H2O_DIRECTORY, "version.txt")
SETTINGS_DIRECTORY=os.path.join(H2O_DIRECTORY, "settings")
# ------------------------------------------------------------------------------
def get_current_version():
    global current_version
    with open(versionFile) as version:
        current_version = version.readline().strip()
        
def main():
    global default_dl_path, default_dl_site, dl_online_sett, dl_machine_sett, url, check_path, probis_dir, probis_exe_dir
    print("Settings file for instalation directory location: ", install_dir)
    default_dl_path = os.path.join(H2O_DIRECTORY, "Probis_H2O")
    default_dl_site = "https://cdn.rcsb.org/resources/sequence/clusters"
    dl_online_sett=os.path.join(SETTINGS_DIRECTORY, "DB_Download_From.txt")
    dl_machine_sett=os.path.join(SETTINGS_DIRECTORY, "DB_Download_To.txt")
    dl=open(dl_online_sett, "r") 
    url= dl.read()
    dl.close()
    if url=="":
        dl=open(dl_online_sett, "w") 
        dl.write(default_dl_site)
        dl.close()
        dl=open(dl_online_sett, "r") 
        url= dl.read()
        dl.close()
    machine = open (dl_machine_sett, "r")
    check_path = machine.read()
    machine.close()
    if check_path=="":
        machine = open (dl_machine_sett, "w")
        machine.write(default_dl_path)
        machine.close()
        machine = open (dl_machine_sett, "r")
        check_path = machine.read()
        machine.close()
    probis_dir = os.path.join(check_path, "probis")
    probis_exe_dir = os.path.join(check_path, "probis.exe")
    get_current_version()
    settings.get_system()
    GUI().run()

# global reference to avoid garbage collection of our dialog
dialog = None

red01 = QtGui.QColor('#ffe6e6')
red02 = QtGui.QColor('#ffcccc')
red03 = QtGui.QColor('#ffb3b3')
red04 = QtGui.QColor('#ff9999')
red05 = QtGui.QColor('#ff8080')
red06 = QtGui.QColor('#ff6666')
red07 = QtGui.QColor('#ff4d4d')
red08 = QtGui.QColor('#ff3333')
red09 = QtGui.QColor('#ff1a1a')
red10 = QtGui.QColor('#ff0000')

class GUI:
    def run(self):
        '''
        Open our custom dialog
        '''
        global dialog
    
        #if main is None:
        dialog = self.make_dialog()
    
        dialog.show()
    
    def make_dialog(self):    
        # create a new Window
        global dialog
        dialog = QtWidgets.QMainWindow()
    
        # populate the Window from our *.ui file which was created with the Qt Designer
        uifile = os.path.join(UI_DIRECTORY, 'ProbisH2OMain.ui')
        self.form = loadUi(uifile, dialog)
        
        def dl_changed():
            line_input=dialog.LineDlFrom.text()
            if line_input == url:
                dialog.PushSetDL.setEnabled(False)
            else:
                dialog.PushSetDL.setEnabled(True)
        def machine_changed():
            line_input=dialog.LineDlTo.text()
            if  line_input== check_path:
                dialog.PushSetMachine.setEnabled(False)
            else:
                dialog.PushSetMachine.setEnabled(True)
        def CheckCompare_changed():
            checked = dialog.CheckCompare.isChecked()
            if checked == True:
                dialog.CheckWater.setChecked(False)
                dialog.CheckAnalyze.setChecked(False)
                dialog.CheckWater.setEnabled(False)
                dialog.CheckAnalyze.setEnabled(False)
            else:
                dialog.CheckWater.setEnabled(True)
                dialog.CheckAnalyze.setEnabled(True)
                dialog.CheckAnalyze.setChecked(True)
        def protein_change():
            global custom
            if len(dialog.LineProtein.text()) >= 5:
                custom = True
            else:
                custom = False

        # hook up button callbacks
        self.form.PushCustom.clicked.connect(custom_disk_file_get.load_file)
        self.form.LineFind.setEnabled(False)
        self.form.PushFind.clicked.connect(ClusterComplexManipulation.get_cluster_complexes)
        self.form.PushDownlad.clicked.connect(ClusterComplexManipulation.download_complexes)
        self.form.PushDownlad.setEnabled(False)
        self.form.PushIdentify.clicked.connect(BindingSites.get_binding_sites)
        self.form.PushGo.clicked.connect(h20Analysis.analyze_waters)
        self.form.PushSetup.clicked.connect(RSCB_contact.contact_rscb_pdb)
        self.form.PushDisplay.clicked.connect(pyMOLinterface.pyMOL_display_cluster)
        self.form.PushBSite.clicked.connect(pyMOLinterface.pyMOL_bsite_cluster)
        self.form.PushContacts.clicked.connect(pyMOLinterface.pyMOL_water_contacts)
        self.form.PushChain.clicked.connect(pyMOLinterface.pyMOL_chain_box)
        self.form.PushFetch.clicked.connect(pyMOLinterface.pyMOL_fetch_system)
        self.form.LineDlTo.textChanged.connect(machine_changed)
        self.form.LineDlFrom.textChanged.connect(dl_changed)
        self.form.LineDlFrom.setText(url)
        self.form.LineDlTo.setText(check_path)
        self.form.PushSetDL.clicked.connect(settings.set_download_from)
        self.form.PushSetMachine.clicked.connect(settings.set_download_to)
        self.form.PushCurrentDL.clicked.connect(settings.current_download_from)
        self.form.PushCurrentMachine.clicked.connect(settings.current_download_to)
        self.form.PushDefault.clicked.connect(settings.default)
        self.form.CheckCompare.stateChanged.connect(CheckCompare_changed)
        self.form.LineProtein.textChanged.connect(protein_change)
        
        self.form.LabelCurrent.setText(current_version)
        
        if os.path.isdir(check_path) == False:
            dialog.CheckAligned.setEnabled(False)
            dialog.CheckAnalyze.setEnabled(False)
            dialog.CheckCompare.setEnabled(False)
            dialog.CheckDebye.setEnabled(False)
            dialog.CheckWater.setEnabled(False)
            dialog.ComboBlastclust.setEnabled(False)
            dialog.LineProtein.setEnabled(False)
            dialog.ListIdentify.setEnabled(False)
            dialog.PushCustom.setEnabled(False)
            dialog.PushFind.setEnabled(False)
            dialog.PushGo.setEnabled(False)
            dialog.PushIdentify.setEnabled(False)
            dialog.CheckKeep.setEnabled(False)
            dialog.ListCalculated.setEnabled(False)
            dialog.PushBSite.setEnabled(False)
            dialog.PushChain.setEnabled(False)
            dialog.PushContacts.setEnabled(False)
            dialog.PushDisplay.setEnabled(False)
            dialog.PushFetch.setEnabled(False)
            QtWidgets.QMessageBox.about(dialog, "ProBiS H2O IMPORTANT NOTE", "On the first start of the plugin, please setup the ProBiS DB and ProBiS_H2O folder. This can be done in 'Settings' tab by clicking on the 'SETUP DATABASE' button! This needs to be done only once. We wish you an exiting adventure in the world of (conserved) waters!!! ;-)")
            print("Please setup probis DB and Probis_H2O folder first using 'Setup Database' in Settings tab!")
        else:
            os.chdir(check_path)
            RSCB_contact.file_checks()
        return dialog
    
    def open_process_window(self, maximum, text):
        global progress
        progress = QtWidgets.QDialog()
        progFile = os.path.join(UI_DIRECTORY, "ProbisH2OProgress.ui")
        self.prog = loadUi(progFile, progress)
        self.prog.label.setText(text)
        self.prog.progressBar.setMaximum(int(maximum))
        progress.show()

# ----------------------------------------------------FUNCTIONS-----------------
class settings:
    def set_download_from():
        global url
        set_from = dialog.LineDlFrom.text()
        dl=open(dl_online_sett, "w") 
        dl.write(set_from)
        dl.close()
        dl=open(dl_online_sett, "r") 
        url=dl.read()
        dl.close()        
    def set_download_to():
        global check_path, probis_dir, probis_exe_dir
        set_to = dialog.LineDlTo.text()
        machine = open (dl_machine_sett, "w")
        machine.write(set_to)
        machine.close()
        machine = open (dl_machine_sett, "r")
        check_path = machine.read()
        machine.close()
        if os.path.isdir(check_path) == False:
            dialog.CheckAligned.setEnabled(False)
            dialog.CheckAnalyze.setEnabled(False)
            dialog.CheckCompare.setEnabled(False)
            dialog.CheckDebye.setEnabled(False)
            dialog.CheckWater.setEnabled(False)
            dialog.ComboBlastclust.setEnabled(False)
            dialog.LineProtein.setEnabled(False)
            dialog.ListIdentify.setEnabled(False)
            dialog.PushCustom.setEnabled(False)
            dialog.PushFind.setEnabled(False)
            dialog.PushGo.setEnabled(False)
            dialog.PushIdentify.setEnabled(False)
            dialog.CheckKeep.setEnabled(False)
            dialog.ListCalculated.setEnabled(False)
            dialog.PushBSite.setEnabled(False)
            dialog.PushChain.setEnabled(False)
            dialog.PushContacts.setEnabled(False)
            dialog.PushDisplay.setEnabled(False)
            dialog.PushFetch.setEnabled(False)
            QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Database Warning", "You have changed the Database Machine directory!\nPlease setup probis DB and Probis_H2O folder first using 'Setup Database' in Settings tab!")
            print("You have changed the Database Machine directory!\nPlease setup probis DB and Probis_H2O folder first using 'Setup Database' in Settings tab!")
        else:
            os.chdir(check_path)
            RSCB_contact.file_checks()
        probis_dir = os.path.join(check_path, "probis")
        probis_exe_dir = os.path.join(check_path, "probis.exe")
    def current_download_from():
        dialog.LineDlFrom.setText(url)
    def current_download_to():
        dialog.LineDlTo.setText(check_path)
    def default():
        dialog.LineDlFrom.setText(default_dl_site)
        dialog.LineDlTo.setText(default_dl_path);
    def get_system():
        global platform
        platform=sys.platform
        

class custom_disk_file_get:
    @staticmethod
    def load_file():
        global custom,filename
        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(dialog, "Open..." + "PDB File", ".", "PDB File (*.pdb)")
        if filename:
            try:
                print("File read.")
                print((str(filename)))
            except:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "File error or \nFile not Found! \nPlease investigate!")
            custom=True
            dialog.LineProtein.setText(filename)


class RSCB_contact:
    """PDB database server setup"""

    lista_cluster_fajlov = ["clusters-by-entity-30.txt", "clusters-by-entity-40.txt", "clusters-by-entity-50.txt", "clusters-by-entity-70.txt",
                            "clusters-by-entity-90.txt", "clusters-by-entity-95.txt", "clusters-by-entity-100.txt"]
        
    @staticmethod
    def contact_rscb_pdb():
        text = "Downloading cluster and ProBiS files. This might take up to 5 minutes. Time to stretch."
        GUI().open_process_window(8, text)
        value = 0
        progress.progressBar.setValue(value)
        current_path = str(os.getcwd())
        if current_path == check_path:
            pass
        else:
            try:
                os.mkdir(check_path)
            except:
                pass
            os.chdir(check_path)


        """download fajlov"""
        print("Setting up the cluster database!")
        for cluster_fajl in RSCB_contact.lista_cluster_fajlov:
            url_fajl = url+"/"+cluster_fajl
            print("Downloading file " + url_fajl)
            urllib.request.urlretrieve(url_fajl, cluster_fajl)
            value += 1
            progress.progressBar.setValue(value)

        print(("Database setup finished" + "\t thank you too RCSB protein data bank"))
        if platform == "linux":
            print("Platform: LINUX")
            if os.path.isfile(probis_dir) == False:
                RSCB_contact.fetch_probis()
            value += 1
            progress.progressBar.setValue(value)
            
        elif platform == "win32":
            print("Platform: WINDOWS")
            if os.path.isfile(probis_exe_dir) == False:
                RSCB_contact.fetch_probis_exe()
            value += 1
            progress.progressBar.setValue(value)
            
        else:
            QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "System error:\nOperating on a non-compatible operating system!")
            
        dialog.CheckAligned.setEnabled(True)
        dialog.CheckAnalyze.setEnabled(True)
        dialog.CheckCompare.setEnabled(True)
        dialog.CheckDebye.setEnabled(True)
        dialog.CheckWater.setEnabled(True)
        dialog.ComboBlastclust.setEnabled(True)
        dialog.LineProtein.setEnabled(True)
        dialog.ListIdentify.setEnabled(True)
        dialog.PushCustom.setEnabled(True)
        dialog.PushFind.setEnabled(True)
        dialog.PushGo.setEnabled(True)
        dialog.PushIdentify.setEnabled(True)
        dialog.CheckKeep.setEnabled(True)
        dialog.ListCalculated.setEnabled(True)
        dialog.PushBSite.setEnabled(True)
        dialog.PushChain.setEnabled(True)
        dialog.PushContacts.setEnabled(True)
        dialog.PushDisplay.setEnabled(True)
        dialog.PushFetch.setEnabled(True)
        RSCB_contact.file_checks()
        progress.close()
        return True

    @staticmethod
    def fetch_probis():
        urllib.request.urlretrieve("http://insilab.org/files/probis-algorithm/probis", "probis")
    def fetch_probis_exe():
        urllib.request.urlretrieve("https://gitlab.com/JuricV/skupni-gui-lisica_probis/-/raw/testfiles/probis_exe/probis.exe", "probis.exe")
        urllib.request.urlretrieve("https://gitlab.com/JuricV/skupni-gui-lisica_probis/-/raw/testfiles/probis_exe/libgsl.dll", "libgsl.dll")
        urllib.request.urlretrieve("https://gitlab.com/JuricV/skupni-gui-lisica_probis/-/raw/testfiles/probis_exe/libgslcblas.dll", "libgslcblas.dll")

    @staticmethod
    def file_checks():
        """preveri ce imamo instalirano bazo"""
        print("\nProBis_H2O: checking database!")
        check = ""
        for fajl in RSCB_contact.lista_cluster_fajlov:
            if str(os.path.isfile(fajl)) == "False":
                print("ProBiS_H2O: please setup DB of rscb cluster files")
                break
            else:
                check += "a"
        if check == "aaaaaaaaaaa":
            print("ProBis_H2O: Database OK")
        if platform == "linux":
            if os.path.isfile(probis_dir) == False:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Please ensure probis is downloaded correctly using setup DB button in Settings tab on plugin GUI")
                print("ProBiS_H2O: please ensure probis is downloaded correctly using setup DB button in Settings tab on plugin GUI")
            else:
                try:
                    if os.access(probis_dir, os.X_OK) == True:
                        print("Probis executable ok")
                    else:
                        st = os.stat(probis_dir)
                        os.chmod(probis_dir, st.st_mode | stat.S_IEXEC)
                        print("Probis executable permission set")
                        print("Prois directory:      : ", probis_dir)
                except:
                    pass
        elif platform == "win32":
            if os.path.isfile(probis_exe_dir) == False:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Please ensure probis.exe is downloaded correctly using setup DB button in Settings tab on plugin GUI")
                print("ProBiS_H2O: please ensure probis.exe is downloaded correctly using setup DB button in Settings tab on plugin GUI")

# ------------------------------------------------------------------------------

class ClusterComplexManipulation:
    """download and identification of cluster complexes from RCSB"""

    @staticmethod
    def get_cluster_unique_list(target_complex, ime_selekcije, sekvenca_id):
        #target complex: kater pdb
        #ime selekcije: "clusters" ali "clusters-by-entity-"
        #sekvenca katera je izbrana 50, 70, 90
        vzorec = re.compile(target_complex, re.IGNORECASE)
        # lista z linijami ki vsebujejo iskani protein
        line_list = []
        # lista z linijami ki so del clustra
        line_list_2 = []
        # lista samo z imeni proteinov - ni unique - lahko je vec verig ....
        cluster_list = []
        examined_cluster_nums = []

        # try:
        global cluster_list_unique
        print(ime_selekcije)
        if ime_selekcije == "clusters":

            with open(ime_selekcije + sekvenca_id + ".txt", "rt") as infile:
                for linenumber, line in enumerate(infile):
                    if vzorec.search(line) != None:
                        line_list.append(line.rstrip('\n'))
                        examined_cluster_nums.append(linenumber+1)
                print("using cd-hit preclustering")
                print("""
Cd-hit: a fast program for clustering and comparing large sets of
protein or nucleotide sequences, Weizhong Li & Adam Godzik (2006)
Bioinformatics, 22:1658-9.
                    """)
                print(("Found entries in sequence file: ", line_list))
                # examined_cluster = line_list[0].split()[0]
                if len(examined_cluster_nums) >= 2:
                    print("We suggest you temporarily remove examined protein from some clusters, so it is analiyed in a single cluster")

                for line in line_list:
                    line_list_2 = line.split()
                    for element in line_list_2:
                        cluster_list.append(element[0:4])
                # make unique list set
                cluster_list_unique = set(cluster_list)
                print("\nComplexes: ")
                print(cluster_list_unique)

            dialog.LineFind.setText(str(len(cluster_list_unique)) + " compl. in cluster no.:"
                                                            + str(examined_cluster_nums))

            print(("Found num of entries in cluster: ", len(cluster_list_unique)))
            dialog.PushDownlad.setEnabled(True)
            dialog.ListIdentify.clear()
            return None

        elif ime_selekcije == "clusters-by-entity-":
            with open(ime_selekcije + sekvenca_id + ".txt", "rt") as infile:
                for linenumber, line in enumerate(infile):
                    if vzorec.search(line) != None:
                        line_list.append(line.rstrip('\n'))


            line_list_2 = line_list[0].split()
            for element in line_list_2:
                cluster_list.append(element[0:4])

            cluster_list_unique = set(cluster_list)
            print("\nComplexes: ")
            print(cluster_list_unique)

            dialog.LineFind.setText(str(len(cluster_list_unique)) + " compl. in blastclust cluster.")
            print("using blastclust pre-clustering")
            print("""
Basic local alignment search tool, S.F. Altschul, W. Gish, W. Miller,
E.W. Myers, & D.J. Lipman (1990) J. Mol. Biol. 215:403-410.
""")
            print(("Found num of entries in cluster: ", len(cluster_list_unique)))
            dialog.PushDownlad.setEnabled(True)
            dialog.ListIdentify.clear()
            return None

        # except:
        #         QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Invalid PDB ID or \nDatabase File not Found! \nPlease investigate!")

    @staticmethod
    def get_cluster_complexes():
        target_complex = dialog.LineProtein.text()
        if custom == True:
            if target_complex.endswith(".pdb") == False:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Please choose a valid .pdb file!")
            else:
                # replaced by water definition in first stage
                target_complex = os.path.split(target_complex)[1].split(".")[0]
                if dialog.ComboBlastclust.currentText() == "Custom Cluster":
                    selected_sequence = "_custom"
                    ClusterComplexManipulation.get_cluster_unique_list(target_complex, "clusters", selected_sequence)

                elif dialog.ComboBlastclust.currentText() == "Blastclust: 100":
                    selected_sequence = "100"
                    ClusterComplexManipulation.get_cluster_unique_list(target_complex, "clusters-by-entity-", selected_sequence)

                elif "Blastclust" in dialog.ComboBlastclust.currentText():
                    selected_sequence = dialog.ComboBlastclust.currentText()[12:14]
                    ClusterComplexManipulation.get_cluster_unique_list(target_complex, "clusters-by-entity-", selected_sequence)

                else:
                    selected_sequence = dialog.ComboBlastclust.currentText()[12:14]
                    ClusterComplexManipulation.get_cluster_unique_list(target_complex, "clusters-by-entity-", selected_sequence)
        else:
            if len(target_complex) < 4:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Invalid PDB ID!\n PDB IDs are 4 symbols long")

            elif len(target_complex) > 4:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Invalid PDB ID! \nFor custom protein analysis please input full path.")
            else:

                # replaced by water definition in first stage
                if dialog.ComboBlastclust.currentText() == "Custom Cluster":
                    selected_sequence = "_custom"
                    ClusterComplexManipulation.get_cluster_unique_list(target_complex, "clusters", selected_sequence)

                elif dialog.ComboBlastclust.currentText() == "Blastclust: 100":
                    selected_sequence = "100"
                    ClusterComplexManipulation.get_cluster_unique_list(target_complex, "clusters-by-entity-", selected_sequence)

                elif "Blastclust" in dialog.ComboBlastclust.currentText():
                    selected_sequence = dialog.ComboBlastclust.currentText()[12:14]
                    ClusterComplexManipulation.get_cluster_unique_list(target_complex, "clusters-by-entity-", selected_sequence)

                else:
                    selected_sequence = dialog.ComboBlastclust.currentText()[12:14]
                    ClusterComplexManipulation.get_cluster_unique_list(target_complex, "clusters-by-entity-", selected_sequence)


    @staticmethod
    def download_complexes():

        #za PDBje ki niso dostoni a imajo svoj entry
        nedostopni_datoteka = open("unavailable_pdb_list.txt", "w")

        try:
            text = "Downloading related complexes. This might take a while depending on their number. Time to stretch."
            GUI().open_process_window(len(cluster_list_unique), text)
            def get_files_2(fajl):
                # ah lepse to kasneje !!! za download individualnih ent fajlov
                lokalni_fajl = open(fajl, 'wb')
                ftp_wwpdb_server.retrbinary('RETR ' + fajl, lokalni_fajl.write)
                lokalni_fajl.close()
                # unzip

                with gzip.open(fajl, 'rb') as compressed_f:
                    lokalni_fajl_uncompressed = open(fajl_uncompressed, 'wb')
                    lokalni_fajl_uncompressed.write(compressed_f.read())
                    lokalni_fajl_uncompressed.close()
                # -----

            i = 1
            print("Downloading files... \nThis may take a while depending on the number of complexes")
            for kompleks in cluster_list_unique:
                try:
                    if os.path.isfile(str(kompleks).lower() + ".pdb"):
                        i += 1
                        ftp_wwpdb_server = FTP("ftp.wwpdb.org")
                        ftp_wwpdb_server.login()
                    else:
                        fajl = "pdb" + str(kompleks).lower() + ".ent.gz"
                        fajl_uncompressed = str(kompleks).lower() + ".pdb"
                        print(("Downloading complex " + str(i) + " out of " + str(len(cluster_list_unique))))
                        i += 1
                        ftp_wwpdb_server = FTP("ftp.wwpdb.org")
                        ftp_wwpdb_server.login()
                        ftp_wwpdb_server.cwd('/pub/pdb/data/structures/divided/pdb/' + str(kompleks[1:3]).lower() + "/")

                        get_files_2(fajl)
                except:
                    #i += 1
                    print(("removing complex: " + str(kompleks)))
                    nedostopni_datoteka.write(str(kompleks).lower() + "\n")
                    pass
                newValue = progress.progressBar.value =+ 1
                progress.progressBar.setValue(newValue)

            ftp_wwpdb_server.quit()
            QtWidgets.QMessageBox.about(dialog, "ProBiS H2O", "Complexes downloaded successfully")
            print("Download of complexes finished")
            progress.close()

            return None
        except:
            QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Check all settings, \nPlease investigate!")
        nedostopni_datoteka.close()


class BindingSites:
    """definiraj binding site"""

    bsite_unique_centers = []

    @staticmethod
    def get_binding_sites():
        try:
            dialog.ListIdentify.clear()
    
            water_sel = dialog.CheckWater.isChecked()
            chain_sel = dialog.CheckCompare.isChecked()
            if custom == True:
                target_complex_2 = dialog.LineProtein.text()
            else:
                target_complex_2 = (dialog.LineProtein.text().lower() + ".pdb")
            
            vzorec_2 = re.compile("^" + "ATOM")
            # pazi na naslednji * ali + v re
            vzorec_3 = re.compile("^" + "HETATM")
            vzorec_4 = re.compile("HOH")
            # VSE LISTE---------------------------------------------------------
            lista_za_heteroatome = []
            lista_za_atome = []
            lista_za_vode = []
            lista_binding_sites = []
            lista_water_binding_sites = []
            lista_verige = []
            lista_verige_konc = []
            warning_lista = []
            #lista_verige_unique = []
            bsite_unique = []
            # podaj rezultate v tri glavne liste--------------------------------
            try:
                with open(target_complex_2, "rt") as infile:
                    for linenumber, line in enumerate(infile):
                        if vzorec_3.search(line) != None:
                            if vzorec_4.search(line) != None:
                                lista_za_vode.append(line.rstrip('\n'))
                            else:
                                lista_za_heteroatome.append(line.rstrip('\n'))
                        elif vzorec_2.search(line) != None:
                            lista_za_atome.append(line.rstrip('\n'))
            except OSError:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "File not found \n Please Investigate!")
                print("File not found!, please investigate.")
    
            # VKLJUCITEV CHAIN VOD
            global lista_za_atome_xyzchain
            lista_za_atome_xyzchain = []
    
            for entry in lista_za_atome:
                test = []
                try:
                    # ATOM    477  CG2 ILE A  78       6.540   0.762  34.941  1.00 13.42           C
                    entry[30:38]
                    test.append(entry[30:38])
                    test.append(entry[38:46])
                    test.append(entry[46:54])
                    test.append(str(entry[21]))
                    lista_za_atome_xyzchain.append(test)
                except:
                    pass
    
    
            if water_sel == False:
                for linija in lista_za_heteroatome:
                    unique_binding_site = linija[17:20].strip(" ")+"."+linija[22:26].strip(" ")+"."+linija[21].strip(" ")
                    lista_binding_sites.append(unique_binding_site)
                    bsite_unique.append([unique_binding_site, linija[30:38].strip(" "), linija[38:46].strip(" "), linija[46:54].strip(" ")])
            else:
                for linija in lista_za_vode:
                    unique_binding_site = linija[17:20].strip(" ")+"."+linija[22:26].strip(" ")+"."+linija[21].strip(" ")
                    lista_binding_sites.append(unique_binding_site)
                    bsite_unique.append([unique_binding_site, linija[30:38].strip(" "), linija[38:46].strip(" "), linija[46:54].strip(" ")])
    
    
    
            # priprava bsite ---------------------------------------------------
            # ok grupiranje ker zelimo UNIQUE
            for key, group in groupby(bsite_unique, lambda x: x[0]):
                bsx = []
                bsy = []
                bsz = []
                for el in group:
                    bsx.append(float(el[1]))
                    bsy.append(float(el[2]))
                    bsz.append(float(el[3]))
    
                # name of bsite, axerage x, average y, average z, min x, max x, min y, max y, min z, max z
                BindingSites.bsite_unique_centers.append([key, sum(bsx)/len(bsx), sum(bsy)/len(bsy), sum(bsz)/len(bsz), min(bsx), max(bsx), min(bsy), max(bsy), min(bsz), max(bsz)])
    
    
    
            # priprava vode-----------------------------------------------------
            for linija in lista_za_vode:
                water_binding_sites = linija[17:20].strip(" ")+"."+linija[22:26].strip(" ")+"."+linija[21].strip(" ")
                lista_water_binding_sites.append(water_binding_sites)
    
            # priprava ostalo---------------------------------------------------
            for linija in lista_za_atome:
                atom_site = []
                try:
                    atom_site.append(str(linija[21]))
                    atom_site.append(int(linija[22:26]))
                    lista_verige.append(atom_site)
                except:
                    pass
    
            # priprava verige---------------------------------------------------
            for key, group in groupby(lista_verige, lambda x: x[0]):
                temp_group = []
                #residue_number = 0
    
                for el in group:
                    # TO JE ZA STETJE UNIKATNIH AK OSTANKOV
                    if el not in temp_group:
                        temp_group.append(el)
                    else:
                        pass
                    # uporbljeno za opcijo kjer se steje unikatne AK ostanke
                    ins_str = str(temp_group[-1][0]) + " chain with " + str(len(temp_group)) + " residues"
                    # ins_str = str(temp_group[-1][0]) + " chain with " + str(temp_group[-1][1]) + " residues"
    
    
                lista_verige_konc.append(ins_str)
    
            # resevanje prolematicnih pdbjev - naj preveri uporabnik
            # v bodoce mogoce avtomatsko
            #-------------------------------------------------------------------
    
            if chain_sel == False:
                for chainelement in lista_verige_konc:
                    if float(chainelement.split()[3]) < 30.0:
                        temp_str = "ONLY " + str(chainelement.split()[3]) + " residues found in chain " + str(chainelement.split()[0])
                        # problemi v warning listi
                        warning_lista.append(temp_str)
                    else:
                        pass
    
                if len(warning_lista) >= 1:
                    QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Try to compare whole chains instead of individual binding sites at the short chain location.")
                else:
                    pass
    
                if water_sel == False:
                    for entry in sorted(list(set(lista_binding_sites))):
                        dialog.ListIdentify.addItem(entry)
                else:
                    for entry in sorted(list(set(lista_binding_sites))):
                        dialog.ListIdentify.addItem(entry)
                    for entry in sorted(list(set(lista_water_binding_sites))):
                        dialog.ListIdentify.addItem(entry)
    
            else:
                for entry in lista_verige_konc:
                    dialog.ListIdentify.addItem(entry)
    
            if dialog.ListIdentify.count() == 0:
                if dialog.CheckCompare.isChecked() == False:
                    QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Message",
                                                "No binding sites found for analysis.\nPlease use Compare Whole Chain option")
                    print("No binding sites found for analysis.\nPlease use Compare Whole Chain option")
                else:
                    QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Message",
                                                "No chains found to compare.")
                    print("No chains found to compare.")
    
            return None
        # flow out except-------------------------------------------------------
        except:
            QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Invalid PDB ID or \nDatabase File not Found! \n\nPlease investigate!")
            print((sys.exc_info()))


# report lista 1----------------------------------------------------------------
report_list_1 = []
report_list_2 = []
report_list_1.append("ProBiS H2O REPORT file")
report_list_1.append("-" * 25 + "\n\n")
# ------------------------------------------------------------------------------

class h20Analysis:
    """collect, prepare, cluster, analyze, display, crystal h20 data"""

    @staticmethod
    def analyze_waters():
        global SELECTED_SITE
        global SELECTED_SITE_CHAIN
        # NUM CPU:
        try:
            processors_available_local = str(multiprocessing.cpu_count())
        except:
            processors_available_local = "1"
        # NUM_CPUS //

        if custom == False:
            nova_datoteka = open("report_" + dialog.LineProtein.text().lower() + ".txt", "w")
        else:
            target = os.path.split(dialog.LineProtein.text())[1]
            nova_datoteka = open("report_"+ "custom_" + target.split(".")[0]+ ".txt", "w")
        nova_datoteka.close()

        # za eno ali vec verig na primerjan protein
        one_or_multiple = dialog.CheckAligned.isChecked()
        # get setting on superposition starting point analysis
        bsite_space_check = dialog.CheckAnalyze.isChecked()

        chain_sel = dialog.CheckCompare.isChecked()
        vzorec_3 = re.compile("^" + "HETATM\s+\d+")
        vzorec_3_supp = re.compile("^" + "HETATM\d\d\d\d\d\s+")
        examined_list_unique = []
        examined_list = list(cluster_list_unique)
        target_complex_2 = dialog.LineProtein.text()
        if custom == True:
            protein = target_complex_2.split(".")[0]
        else:
            protein = target_complex_2.lower()
        # to je za 1j4h kjer nastopajo nedosegljivi pdb-ji ki imajo svoje
        # entrije v bazi pdb: npr: 5GKY
        # za njih bomo tvorili bazo: unavailable_pdb_list.txt datoteka
        # ki se nahaja v delovnem okolju

        with open('unavailable_pdb_list.txt', 'r') as f:
            removed_list = f.read().splitlines()
        removed_list.append(protein)



        for element in examined_list:
            if str(element).lower() not in removed_list:
                examined_list_unique.append(str(element).lower())
            else:
                pass

        try:
            bsite_selection_full = dialog.ListIdentify.currentItem()
            bsite_selection = bsite_selection_full.text()
            chain_selection = bsite_selection_full.text()[-1]
            whole_chain_compare_selection = bsite_selection_full.text()[0]
        except:
            QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Invalid selection \n\nPlease select b-site or chain!")
            return None

        if bsite_space_check == True:
            for element in BindingSites.bsite_unique_centers:
                if element[0] == bsite_selection:
                    SELECTED_SITE = element
                    SELECTED_SITE_CHAIN = str(chain_selection).upper()

        if bsite_space_check == False:
            for element in BindingSites.bsite_unique_centers:
                if element[0] == bsite_selection:
                    SELECTED_SITE = element
                    SELECTED_SITE_CHAIN = str(chain_selection).upper()
        
        if chain_sel == True:
            SELECTED_SITE = []
            SELECTED_SITE.append("no binding site used in analysis")
            SELECTED_SITE_CHAIN = str(whole_chain_compare_selection).upper()
            
        else:
            pass

        #report 2,3,4,5,6,7,8,9, 10
        report_list_1.append("\n\n\nExamined complex: " + target_complex_2)
        report_list_1.append("Whole chain setting used: " + str(chain_sel))
        if chain_sel == True:
            report_list_1.append("Whole chain selection: " + whole_chain_compare_selection)
            report_list_1.append("Binding site selection: / (not used)")
            report_list_1.append("Chain selection: " + whole_chain_compare_selection)
        else:
            report_list_1.append("Whole chain selection: / (not used)")
            report_list_1.append("Binding site selection: " + bsite_selection)
            report_list_1.append("Chain selection: " + chain_selection)


        report_list_1.append("Used PDB clusters with: " + dialog.ComboBlastclust.currentText() + " %")
        report_list_1.append("Unique structures in identified cluster: " + str(examined_list) + "\n\n\n")

        #probis_starter=('start "" "{}"').format(probis_dir)
        probis_starter=probis_exe_dir
        
        if platform == "win32":
            if chain_sel == False:
                subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                        "-extract", "-bsite", bsite_selection, "-dist 3.0", "-f1",
                        "{}.pdb".format(protein), "-c1", chain_selection,
                        " -srffile", "{}.srf".format(protein)])
            else:
                subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                        "-extract", "-f1", "{}.pdb".format(protein), "-c1",
                        whole_chain_compare_selection, "-srffile", 
                        "{}.srf".format(protein)])
        else:
            if chain_sel == False:
                subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                        "-extract", "-bsite", bsite_selection, "-dist 3.0", "-f1",
                        "{}.pdb".format(protein), "-c1", chain_selection,
                        " -srffile", "{}.srf".format(protein)])
            else:
                subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                        "-extract", "-f1", "{}.pdb".format(protein), "-c1",
                        whole_chain_compare_selection, "-srffile", 
                        "{}.srf".format(protein)])

        master_chain_list = []

        open("./srfs.txt", 'w').close()
        prot_list = []

        for element in examined_list_unique:
            unique_chain_list = []
            try:
                with open(element + ".pdb", "rt") as infile:
                    for linenumber, line in enumerate(infile):
                        if vzorec_3.search(line) != None:

                            unique_chain = str(line.rstrip('\n').split()[4])
                            if len(unique_chain) == 1:
                                unique_chain_list.append(unique_chain)
                            elif len(unique_chain) == 2:
                                #4WUC primer
                                #: HETATM 2976 NA  A NA A 403       8.964  15.893 -17.028  0.50 27.84          NA
                                unique_chain = str(line.rstrip('\n').split()[5][0])
                                unique_chain_list.append(unique_chain)
                            else:
                                # naslednja linija [4][0] je za primer PDBJA: 4BRI
                                # HETATM 5862  O2G UNP A1393      60.198   4.590  12.738  1.00 13.14           O
                                # klasicen PDB:
                                # HETATM 2769  N1  ARU A   1      35.314  25.889  32.623  1.00 60.17           N
                                unique_chain = str(line.rstrip('\n').split()[4][0])
                                unique_chain_list.append(unique_chain)

                        elif vzorec_3_supp.search(line) != None:
                                # tretji problematicen primer: PDB ID: 4BRP
                                # HETATM11092 BR    BR A1394      19.400 -62.788  -5.889  1.00 49.48          BR
                            unique_chain = str(line.rstrip('\n').split()[3][0])
                            unique_chain_list.append(unique_chain)
                        else:
                            pass


                unique_chain_list = list(set(unique_chain_list))
                master_chain_list.append(unique_chain_list)

                for chain_id in unique_chain_list:
                    # zacasna lista of unwanted
                    unwanted_chain = [1, "1", 2, "2", 3, "3", 4, "4", 5, "5", 6, "6", 7, "7", 8, "8", 9, "9"]

                    if chain_id in unwanted_chain:
                        pass

                    else:
                        # for probis 2.4.7
                        if platform == "win32":
                            subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                                      "-extract", "-f1", "{}.pdb".format(element), "-c1", 
                                      chain_id, "-srffile", "{}{}.srf".format(element, chain_id)])
                        else:
                            subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                                      "-extract", "-f1", "{}.pdb".format(element), "-c1", 
                                      chain_id, "-srffile", "{}{}.srf".format(element, chain_id)])

                        srf_fajl = open("./srfs.txt", 'a')
                        srf_fajl.write(element + chain_id + ".srf " + chain_id + "\n")
                        srf_fajl.close()
                        prot_list.append(element + " " + chain_id)
                        pass
            except OSError:
                print("Database File not Found!, please investigate.")
    ##############################
        if platform == "win32":
            os.system("DEL *.rota.pdb /S")
            os.system("DEL AAA_NOSQL.nosql /S")
        else:
            os.system("rm ./*.rota.pdb")
            os.system("rm ./AAA_NOSQL.nosql")
    ##############################
        
        if chain_sel == False:
            if platform == "win32":
                subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                          "-surfdb", "-local", "-sfile", "srfs.txt", "-f1", 
                          "{}.srf".format(protein), "-c1",
                          chain_selection, "-nosql", "AAA_NOSQL.nosql"])
                subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                          "-results", "-f1", "{}.pdb".format(protein), "-c1",
                          chain_selection, "-nosql", "AAA_NOSQL.nosql", "-json", "AAA_NOSQL.json"])
            else:
                subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                          "-surfdb", "-local", "-sfile", "srfs.txt", "-f1", 
                          "{}.srf".format(protein), "-c1",
                          chain_selection, "-nosql", "AAA_NOSQL.nosql"])
                subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                          "-results", "-f1", "{}.pdb".format(protein), "-c1",
                          chain_selection, "-nosql", "AAA_NOSQL.nosql", "-json", "AAA_NOSQL.json"])
        else:
            if platform == "win32":
                subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                          "-surfdb", "-sfile", "srfs.txt", "-f1", "{}.srf".format(protein),
                          "-c1", whole_chain_compare_selection, "-nosql", "AAA_NOSQL.nosql"])
                
                subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                          "-results", "-f1", "{}.pdb".format(protein), "-c1",
                          whole_chain_compare_selection, "-nosql", "AAA_NOSQL.nosql", "-json", "AAA_NOSQL.json"])
            else:
                subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                          "-surfdb", "-sfile", "srfs.txt", "-f1", "{}.srf".format(protein),
                          "-c1", whole_chain_compare_selection, "-nosql", "AAA_NOSQL.nosql"])

                subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                          "-results", "-f1", "{}.pdb".format(protein), "-c1",
                          whole_chain_compare_selection, "-nosql", "AAA_NOSQL.nosql", "-json", "AAA_NOSQL.json"])

        for element in prot_list:
            ele0=element.split()[0]
            ele1=element.split()[1]
            
            if chain_sel == False:
                if platform == "win32":
                    subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                              "-align", "-bkeep", "-alno", "0", "-nosql", "AAA_NOSQL.nosql", "-f1", 
                              "{}.pdb".format(protein), "-c1", chain_selection,
                              "-f2", "{}.pdb".format(ele0), "-c2", 
                              ele1])
                else:
                    subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                              "-align", "-bkeep", "-alno", "0", "-nosql", "AAA_NOSQL.nosql", "-f1", 
                              "{}.pdb".format(protein), "-c1", chain_selection,
                              "-f2", "{}.pdb".format(ele0), "-c2", 
                              ele1])
            else:
                if platform == "win32":
                    subprocess.run(args=[probis_starter, "-ncpu", processors_available_local, 
                              "-align", "-bkeep", "-alno", "0", "-nosql", "AAA_NOSQL.nosql", "-f1", 
                              "{}.pdb".format(protein), "-c1",
                              whole_chain_compare_selection, "-f2", 
                              "{}.pdb".format(ele0), "-c2", ele1]) 
                else:
                    subprocess.run(args=[probis_dir, "-ncpu", processors_available_local, 
                              "-align", "-bkeep", "-alno", "0", "-nosql", "AAA_NOSQL.nosql", "-f1", 
                              "{}.pdb".format(protein), "-c1",
                              whole_chain_compare_selection, "-f2", 
                              "{}.pdb".format(ele0), "-c2", ele1]) 
                    
        print("Rotas done ... (alignment 0 !)")


        # correction of multiple or one chain per protein allignment
        aligned_unique = []
        aligned_discard = []
        helper = []
        if one_or_multiple == True:
            with open("AAA_NOSQL.json") as json_fajl:
                z_data = json.load(json_fajl)
            for aligned in z_data:
                if str(aligned["pdb_id"]) in helper:
                    aligned_discard.append(str(aligned["pdb_id"]) + str(aligned["chain_id"]))
                else:
                    helper.append(str(aligned["pdb_id"]))
                    aligned_unique.append(str(aligned["pdb_id"]) + str(aligned["chain_id"]))
            
            if platform == "win32":
                if chain_sel == False:
                    for discarded in aligned_discard:
                        os.system("DEL " + protein + chain_selection
                                + "_" + str(discarded) + ".0.rota.pdb /S")
                else:
                    for discarded in aligned_discard:
                        os.system("DEL " + protein
                                  + whole_chain_compare_selection
                                  + "_" + str(discarded) + ".0.rota.pdb /S")
            else:
                if chain_sel == False:
                    for discarded in aligned_discard:
                        os.system("rm ./" + protein + chain_selection
                                + "_" + str(discarded) + ".0.rota.pdb")
                else:
                    for discarded in aligned_discard:
                        os.system("rm ./ " + protein
                                  + whole_chain_compare_selection
                                  + "_" + str(discarded) + ".0.rota.pdb")
        else:
            pass



        # ----------------START WATER COLLECTION------------------------------------

        # vzorci vod v PDB

        # linija1 = "HETATM 3315  O   HOH A 653       6.657   0.611  50.201  1.00 22.92           O"
        # linija2 = "HETATM 6180  O   HOH A1063      46.720   3.111  27.787  1.00 51.91           O"
        # linija3 = "HETATM 3046  O  AHOH A 562      19.114  37.882  -1.866  0.50 24.61           O"
        # linija4 = "HETATM 3047  O  BHOH A 562      20.241  36.438  -1.021  0.50 30.54           O"
        # linija5 = "HETATM11839  O   HOH A2001      45.529  16.939  64.867  1.00 20.76           O"

        PDB_master_file_list = []
        imena_fajlov = glob("*.rota.pdb")
        # ZADNJI JE KOMPLEKS
        imena_fajlov.append(protein + ".pdb")

        vzorec_water_mining1 = re.compile("^" + "HETATM\s+\d+\s+\S+\s+" + "HOH" + "\s+\D\s+\d+\s+") # ok za linijo 1
        vzorec_water_mining2 = re.compile("^" + "HETATM\s+\d+\s+\S+\s+" + "HOH" + "\s+\D\d{4}\s+") # ok za linijo 2
        vzorec_water_mining3 = re.compile("^" + "HETATM\s+\d+\s+\S+\s+" + "\wHOH" + "\s+\D\s+\d+\s+") # ok za linijo 3,4
        vzorec_water_mining4 = re.compile("^" + "HETATM\d+\s+\S+\s+" + "HOH" + "\s+\D\d{4}\s+") # za linijo 5

    # VZOREC ZA END MODELA: VSAK *.rota.pdb ima MODEL2 zacetni kompleks
        vzorec_water_only_model_1 = re.compile("^" + "ENDMDL")

        for ime_fajla in imena_fajlov:
            lista_h2o = []
            with open(ime_fajla, 'r') as brani_fajl:
                for linija in brani_fajl:
                    if vzorec_water_mining1.search(linija) != None:
                        voda = linija.split()
                        voda.append(ime_fajla)
                        lista_h2o.append(voda)

                    elif vzorec_water_mining2.search(linija) != None:
                        voda = linija.split()
                        voda.insert(5, voda[4][1:])
                        voda[4] = voda[4].strip("1234567890")
                        voda.append(ime_fajla)
                        lista_h2o.append(voda)

                    elif vzorec_water_mining3.search(linija) != None:
                        voda = linija.split()
                        voda[3] = voda[3][1:]
                        voda.append(ime_fajla)
                        lista_h2o.append(voda)

                    elif vzorec_water_mining4.search(linija) != None:
                        voda = linija.split()
                        voda.insert(4, voda[3][1:])
                        voda[3] = voda[3].strip("1234567890")
                        voda.insert(1, voda[0][6:])
                        voda[0] = voda[0].strip("1234567890")
                        voda.append(ime_fajla)
                        lista_h2o.append(voda)
                    # naslednja linija je kljucna zaradi 2 modelov v *.rota.pdb
                    elif vzorec_water_only_model_1.search(linija) != None:
                        break

                    else:
                        pass
                PDB_master_file_list.append(lista_h2o)


        MASTER_h2o_list = []
        fajl_list = []
        for PDB_water_fajl in PDB_master_file_list:
            try:
                for het, stev, atom, molekula, veriga, zapor, x, y, z, occ, R, atom2, fajl in PDB_water_fajl:

                    test = []
                    test.append(x), test.append(y), test.append(z), test.append(fajl), test.append(R), test.append(zapor)
                    MASTER_h2o_list.append(test)
                    fajl_list.append(fajl)
            except (RuntimeError, TypeError, NameError, ValueError):
                pass

        entities = int(len(set(fajl_list)))
        dialog.PlainInfo.clear()
        
        # REPORT list 11,12
        report_list_1.append(dialog.LineFind.text() + " (sequence identity pre-cluster)")
        report_list_1.append("Master water list includes %r waters" % (len(MASTER_h2o_list)))

        dialog.PlainInfo.insertPlainText("Master water list includes %r molecules /n" % (len(MASTER_h2o_list)))
        dialog.PlainInfo.insertPlainText("Superimposed chains: %r\n" % (entities))

        print ("Master lista vod narejena in vsebuje %r vod" % (len(MASTER_h2o_list)))
        print("writing H2O master list")
        nova_datoteka = open("master_water_list.txt", "w")
        for tocka in MASTER_h2o_list:
            nova_datoteka.write("%s\n" % tocka)
        nova_datoteka.close()
        print("done...")
        dialog.Tabs.setCurrentIndex(1)

        # DBSCAN formatting-----------------------------------------------------

        # binding site clustering
        # BindingSites.bsite_unique_centers
        master_bsite_lista_vod = []
        master_bsite_lista_vod_koordinata_x = []
        master_bsite_lista_vod_koordinata_y = []
        master_bsite_lista_vod_koordinata_z = []

        master_lista_vod = []
        master_lista_vod_koordinata_x = []
        master_lista_vod_koordinata_y = []
        master_lista_vod_koordinata_z = []

        # POPRAVA VOD DA NE SEGAJO IZVEN CHAINA

        correction_x = []
        correction_y = []
        correction_z = []
        for element in lista_za_atome_xyzchain:
            if SELECTED_SITE_CHAIN == element[3]:
                correction_x.append(float(element[0]))
                correction_y.append(float(element[1]))
                correction_z.append(float(element[2]))

        global atom_max_x
        global atom_min_x
        global atom_max_y
        global atom_min_y
        global atom_max_z
        global atom_min_z

        atom_max_x = max(correction_x) + 4
        atom_min_x = min(correction_x) - 4
        atom_max_y = max(correction_y) + 4
        atom_min_y = min(correction_y) - 4
        atom_max_z = max(correction_z) + 4
        atom_min_z = min(correction_z) - 4

        global boundingBox

        boundingBox = [LINEWIDTH, 2.0, BEGIN, LINES,
                COLOR, float(1), float(0), float(0),

                VERTEX, atom_min_x, atom_min_y, atom_min_z,       #1
                VERTEX, atom_min_x, atom_min_y, atom_max_z,       #2

                VERTEX, atom_min_x, atom_max_y, atom_min_z,       #3
                VERTEX, atom_min_x, atom_max_y, atom_max_z,       #4

                VERTEX, atom_max_x, atom_min_y, atom_min_z,       #5
                VERTEX, atom_max_x, atom_min_y, atom_max_z,       #6

                VERTEX, atom_max_x, atom_max_y, atom_min_z,       #7
                VERTEX, atom_max_x, atom_max_y, atom_max_z,       #8


                VERTEX, atom_min_x, atom_min_y, atom_min_z,       #1
                VERTEX, atom_max_x, atom_min_y, atom_min_z,       #5

                VERTEX, atom_min_x, atom_max_y, atom_min_z,       #3
                VERTEX, atom_max_x, atom_max_y, atom_min_z,       #7

                VERTEX, atom_min_x, atom_max_y, atom_max_z,       #4
                VERTEX, atom_max_x, atom_max_y, atom_max_z,       #8

                VERTEX, atom_min_x, atom_min_y, atom_max_z,       #2
                VERTEX, atom_max_x, atom_min_y, atom_max_z,       #6


                VERTEX, atom_min_x, atom_min_y, atom_min_z,       #1
                VERTEX, atom_min_x, atom_max_y, atom_min_z,       #3

                VERTEX, atom_max_x, atom_min_y, atom_min_z,       #5
                VERTEX, atom_max_x, atom_max_y, atom_min_z,       #7

                VERTEX, atom_min_x, atom_min_y, atom_max_z,       #2
                VERTEX, atom_min_x, atom_max_y, atom_max_z,       #4

                VERTEX, atom_max_x, atom_min_y, atom_max_z,       #6
                VERTEX, atom_max_x, atom_max_y, atom_max_z,       #8

                END
        ]


        # ----------------------------------------------------------------------

        # cluster TESTING
        mlv_datoteka = open("master_water_list.txt", "r")
        for linija in mlv_datoteka:
            vmesna_lista = []
            linija2 = linija.replace("[", "")
            linija3 = linija2.replace("]", "")
            linija4 = linija3.replace(" ", "")
            linija5 = linija4.replace("'", "")
            linija_lista = linija5.split(",")
            x = float(linija_lista[0])
            y = float(linija_lista[1])
            z = float(linija_lista[2])

            vmesna_lista.append(x)
            vmesna_lista.append(y)
            vmesna_lista.append(z)
            
            if bsite_space_check == True and chain_sel == False:
                if SELECTED_SITE[4] - 4 <= vmesna_lista[0] <= SELECTED_SITE[5] + 4:
                    if SELECTED_SITE[6] - 4 <= vmesna_lista[1] <= SELECTED_SITE[7] + 4:
                        if SELECTED_SITE[8] - 4 <= vmesna_lista[2] <= SELECTED_SITE[9] + 4:
                            master_bsite_lista_vod.append(vmesna_lista)
                            x2 = float(vmesna_lista[0])
                            master_bsite_lista_vod_koordinata_x.append(x2)
                            y2 = float(vmesna_lista[1])
                            master_bsite_lista_vod_koordinata_y.append(y2)
                            z2 = float(vmesna_lista[2])
                            master_bsite_lista_vod_koordinata_z.append(z2)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass

            if bsite_space_check == False and chain_sel == False:
                if atom_min_x <= vmesna_lista[0] <= atom_max_x:
                    if atom_min_y <= vmesna_lista[1] <= atom_max_y:
                        if atom_min_z <= vmesna_lista[2] <= atom_max_z:
                            master_lista_vod_koordinata_x.append(x)
                            master_lista_vod_koordinata_y.append(y)
                            master_lista_vod_koordinata_z.append(z)
                            master_lista_vod.append(vmesna_lista)
            if chain_sel == True:
                if atom_min_x <= vmesna_lista[0] <= atom_max_x:
                    if atom_min_y <= vmesna_lista[1] <= atom_max_y:
                        if atom_min_z <= vmesna_lista[2] <= atom_max_z:
                            master_lista_vod_koordinata_x.append(x)
                            master_lista_vod_koordinata_y.append(y)
                            master_lista_vod_koordinata_z.append(z)
                            master_lista_vod.append(vmesna_lista)
            else:
                pass

        mlv_datoteka.close()
        # /DBSCAN formatting----------------------------------------------------
        def display_cluster_info(mlist, mlist_x, mlist_y, mlist_z):

            x_dim = max(mlist_x) - min(mlist_x)
            y_dim = max(mlist_y) - min(mlist_y)
            z_dim = max(mlist_z) - min(mlist_z)

            system_volume = round(x_dim * y_dim * z_dim)

            dialog.PlainInfo.insertPlainText("System volume is: %d cubic A\n" % (system_volume))
            report_list_1.append("System volume is: %d cubic A\n" % (system_volume))
            report_list_1.append("IDENTIFIED CLUSTERS: \n")
            report_list_1.append("-" * 25)


            def calculate_clusters(lista, sample_size):
                lista_np_array = np.array(lista)
                selected_eps=dialog.SpinDB.value()
                labels3D = DBSCAN(eps=selected_eps, min_samples=sample_size).fit_predict(lista_np_array)
                # Number of clusters in labels, ignoring noise if present.
                n_clusters_3D = len(set(labels3D)) - (1 if -1 in labels3D else 0)
                return int(n_clusters_3D)


            dialog.ListCalculated.clear()
            start_population = 2
            clus_num = calculate_clusters(mlist, start_population)
            cluster_collate_list = []
            max_population = 0
            while clus_num >= 1:

                consv = round((float(start_population)/float(entities)), 2)
                # limita ena je overloaded ker je lahko teoreticno prisotnih vec molekul vode na istem mestu v istem kristalu
                # glede na to da je smisel tega orodja v eksperimentalnih podatkih bi bile taksne vode na lokaciji manjsi od 1 A
                # nesmiselne in korigirane s strani kristalografa
                # zato lahko komot v skrajno nenavadno ali eksp-nekorigiranem primeru vrednost consv presega 1
                # taksne primere tukaj reduciramo na vrednost 1 kar pomeni, da je voda na tej lokaciji nastopa v vseh eksperimentalnih entitetah
                if consv > 1:
                    consv = 1.0
                else:
                    pass

                # za report list------------------------------------------------
                text_consv = int(round(consv*10)) * "*"
                st = 10 - len(text_consv)
                text_consv += st * " "
                if str(clus_num) == "1":
                    text = (str(clus_num) + " cluster with " + str(start_population)
                            + " H2O molecules. " +  "consv. " + str(consv))
                else:
                    text = (str(clus_num) + " clusters with " + str(start_population)
                            + " H2O molecules. " +  "consv. " + str(consv))
                num_spaces = 55 - len(text)
                report_list_1.append(text +  + num_spaces * " " + "[" + text_consv + "]")
                # REPORT LIST APPEND--------------------------------------------

                cluster_collate_list.append([clus_num, start_population, text])
                start_population += 1
                clus_num = calculate_clusters(mlist, start_population)
                max_population = start_population
            
            temp_collate = []
            d=0
            for cluster_num, start_population, list_text in reversed(cluster_collate_list):
                d=d+1

                if cluster_num not in temp_collate:
                    dialog.ListCalculated.addItem(list_text)
                    temp_collate.append(cluster_num)
                else:
                    pass

            calculated_items = []
            for x in range(dialog.ListCalculated.count()):
                calculated_items.append(dialog.ListCalculated.item(x))
            for i, listbox_entry in enumerate(calculated_items):
                if 0.9 <= float(listbox_entry.text().split()[7]) :
                    dialog.ListCalculated.item(i).setBackground(red10)
                elif 0.8 <=float(listbox_entry.text().split()[7]) < 0.9:
                    dialog.ListCalculated.item(i).setBackground(red09)
                elif 0.7 <=float(listbox_entry.text().split()[7]) < 0.8:
                    dialog.ListCalculated.item(i).setBackground(red08)
                elif 0.6 <=float(listbox_entry.text().split()[7]) < 0.7:
                    dialog.ListCalculated.item(i).setBackground(red07)
                elif 0.5 <=float(listbox_entry.text().split()[7]) < 0.6:
                    dialog.ListCalculated.item(i).setBackground(red06)
                elif 0.4 <=float(listbox_entry.text().split()[7]) < 0.5:
                    dialog.ListCalculated.item(i).setBackground(red05)
                elif 0.3 <=float(listbox_entry.text().split()[7]) < 0.4:
                    dialog.ListCalculated.item(i).setBackground(red04)
                elif 0.2 <=float(listbox_entry.text().split()[7]) < 0.3:
                    dialog.ListCalculated.item(i).setBackground(red03)
                elif 0.1 <=float(listbox_entry.text().split()[7]) < 0.2:
                    dialog.ListCalculated.item(i).setBackground(red02)
                else:
                    dialog.ListCalculated.item(i).setBackground(red01)
            
            # report list  15
            report_list_1.append("-" * 25)
            max_pop_text = "Maximum occupied cluster contains %d H2O molecules \n binding site: %s" % (max_population - 1, SELECTED_SITE[0])
            dialog.PlainInfo.insertPlainText(max_pop_text)
            report_list_1.insert(10, max_pop_text)

        if chain_sel == True:
            try:
                display_cluster_info(master_lista_vod, master_lista_vod_koordinata_x,
                                master_lista_vod_koordinata_y, master_lista_vod_koordinata_z)
            except:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning",
                                            "Please ensure analized .pdb file includes water molecules")
        else:
            try:
                if bsite_space_check == True:
                    display_cluster_info(master_bsite_lista_vod, master_bsite_lista_vod_koordinata_x,
                                        master_bsite_lista_vod_koordinata_y, master_bsite_lista_vod_koordinata_z)
                else:
                    display_cluster_info(master_lista_vod, master_lista_vod_koordinata_x,
                                        master_lista_vod_koordinata_y, master_lista_vod_koordinata_z)
            except:
                QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning",
                                        "Please ensure analized .pdb file includes water molecules")

        # cleanup
        if platform == "win32":
            os.system("DEL *.ent.gz /S")
            os.system("DEL *.srf /S")
            os.system("DEL *.rota.pdb /S")
            os.system("DEL AAA_NOSQL* /S")
            os.system("DEL query.json /S")
            os.system("DEL info.json /S")
            os.system("DEL srfs.txt /S")
        else:
            os.system("rm ./*.ent.gz")
            os.system("rm ./*.srf")
            os.system("rm ./*.rota.pdb")
            os.system("rm ./AAA_NOSQL*")
            os.system("rm ./query.json")
            os.system("rm ./info.json")
            os.system("rm ./srfs.txt")
        
        dialog.Tabs.setCurrentIndex(1)
        return None

class pyMOLinterface:
    """use wonderful pyMol for visualisation of collected results"""
    """thanks! Warren L. DeLano!"""

    @staticmethod
    def pyMOL_water_contacts():
        if custom == False:
            target_complex_3 = dialog.LineProtein.text().lower()
        else:
            target_complex_3 = os.path.split(dialog.LineProtein.text())[1].split(".")[0]
        # za H-bond mejno razdajo kar 4 A
        cmd.select("protein_", "polymer and {}".format(target_complex_3))
        cmd.select("ligand_", "organic and {}".format(target_complex_3))
        cmd.select("conserved_waters", "H2O*")
        cmd.select("donors_", "(elem n,o and (neighbor hydro)) and {}".format(target_complex_3))
        cmd.select("acceptors_", "(elem o or (elem n and not (neighbor hydro))) and {}".format(target_complex_3))
        cmd.distance("prot_acceptors", "(protein_ and acceptors_)", "conserved_waters", "4.0")
        cmd.distance("prot_donors", "(protein_ and donors_)", "conserved_waters", "4.0")
        cmd.distance("ligand_acceptors", "(ligand_ and acceptors_)", "conserved_waters", "4.0")
        cmd.distance("ligand_donors", "(ligand_ and donors_)", "conserved_waters", "4.0")
        cmd.distance("inter_cons_H2O", "conserved_waters", "conserved_waters", "4.0")
        cmd.delete("donors_")
        cmd.delete("acceptors_")
        cmd.set("dash_color", "magenta")
        cmd.set("dash_gap", "0.2")
        cmd.set("dash_length", "0.2")
        cmd.set("dash_round_ends","on")
        cmd.set("dash_width","3")

    @staticmethod
    def pyMOL_fetch_system():

        cmd.delete(name = "all")

        if custom == True:
            target_complex_3 = os.path.split(dialog.LineProtein.text())[1].split(".")[0]
            cmd.load(filename, target_complex_3)
        else:
            target_complex_3 = dialog.LineProtein.text().lower()
            cmd.fetch(target_complex_3, target_complex_3)

        cmd.hide("everything", target_complex_3)
        cmd.show ("cartoon", target_complex_3)
        cmd.set("cartoon_color", "white", target_complex_3)
        cmd.hide("lines", "all")
        cmd.util.cbag(selection = target_complex_3)
        cmd.show("surface", target_complex_3)
        cmd.set("transparency", "0.9")
        cmd.set("surface_color", "white")
        cmd.show("sticks", "organic")
        cmd.color("blue", "organic")
        waters = "{}_waters".format(target_complex_3)
        cmd.select(waters, "resn hoh")
        cmd.show("nonbonded", waters)
        cmd.deselect()


    @staticmethod
    def pyMOL_chain_box():
        cmd.load_cgo(boundingBox, "box")

    @staticmethod
    def pyMOL_bsite_cluster():
        # display binding sites of clusters
        cmd.select("bsites", "H2O* around 6")
        cmd.select("byres bsites")
        cmd.show("sticks", "byres bsites")
        cmd.util.cbay("byres bsites")
        cmd.set_bond("stick_radius", "0.1", "byres bsites")
        cmd.select("sele", "name ca and byres bsites")
        cmd.label("sele", "'\{}-{}\'.format(resn, resi)")
        cmd.set("label_size", "18")
        cmd.set("label_font_id", "7")
        cmd.show("sticks", "organic")
        cmd.color("blue", "organic")
        cmd.util.cnc ("organic")
        cmd.set_bond("stick_radius", "0.25", "organic")
        
    @staticmethod
    def pyMOL_display_cluster():
        display_clusters_setting = dialog.CheckKeep.isChecked()
        bsite_space_check = dialog.CheckAnalyze.isChecked()
        chain_sel = dialog.CheckCompare.isChecked()

        # za korekcijo in pogled R faktorja
        debye_waller_check = dialog.CheckDebye.isChecked()

        # DBSCAN formatting-----------------------------------------------------

        # binding site clustering
        # BindingSites.bsite_unique_centers
        master_bsite_lista_vod = []
        master_bsite_lista_vod_koordinata_x = []
        master_bsite_lista_vod_koordinata_y = []
        master_bsite_lista_vod_koordinata_z = []
        master_lista_vod = []
        master_lista_vod_koordinata_x = []
        master_lista_vod_koordinata_y = []
        master_lista_vod_koordinata_z = []
        # za Debye Waller
        master_bsite_lista_atom_iso_displacement = []
        master_lista_atom_iso_displacement = []
        # master_lista_names = []
        master_bsite_lista_info = []
        master_lista_info = []

        mlv_datoteka = open("master_water_list.txt", "r")
        for linija in mlv_datoteka:
            vmesna_lista = []
            linija2 = linija.replace("[", "")
            linija3 = linija2.replace("]", "")
            linija4 = linija3.replace(" ", "")
            linija5 = linija4.replace("'", "")
            linija_lista = linija5.split(",")
            x = float(linija_lista[0])
            y = float(linija_lista[1])
            z = float(linija_lista[2])
            B = float(linija_lista[4])
            if B < 0:
                B = 0
            info = str(linija_lista[3]) + " location: " + str(linija_lista[5].strip("\n"))


            # anizotropni displcement bomo implementirali v V2 hopefully
            # + 1.4 je zaradi r H2O
            isotropni_displacement = math.sqrt(B/(8*((math.pi)**2))) + 1.4


            # master_lista_names.append(ime)


            vmesna_lista.append(x)
            vmesna_lista.append(y)
            vmesna_lista.append(z)



            if bsite_space_check == True and chain_sel == False:
                if SELECTED_SITE[4] - 4 <= vmesna_lista[0] <= SELECTED_SITE[5] + 4:
                    if SELECTED_SITE[6] - 4 <= vmesna_lista[1] <= SELECTED_SITE[7] + 4:
                        if SELECTED_SITE[8] - 4 <= vmesna_lista[2] <= SELECTED_SITE[9] + 4:
                            master_bsite_lista_vod.append(vmesna_lista)
                            x2 = float(vmesna_lista[0])
                            master_bsite_lista_vod_koordinata_x.append(x2)
                            y2 = float(vmesna_lista[1])
                            master_bsite_lista_vod_koordinata_y.append(y2)
                            z2 = float(vmesna_lista[2])
                            master_bsite_lista_vod_koordinata_z.append(z2)
                            master_bsite_lista_atom_iso_displacement.append(isotropni_displacement)
                            master_bsite_lista_info.append(info)

            if bsite_space_check == False and chain_sel == False:
                if atom_min_x <= vmesna_lista[0] <= atom_max_x:
                    if atom_min_y <= vmesna_lista[1] <= atom_max_y:
                        if atom_min_z <= vmesna_lista[2] <= atom_max_z:
                            master_lista_vod_koordinata_x.append(x)
                            master_lista_vod_koordinata_y.append(y)
                            master_lista_vod_koordinata_z.append(z)
                            master_lista_vod.append(vmesna_lista)
                            master_lista_atom_iso_displacement.append(isotropni_displacement)
                            master_lista_info.append(info)

            if chain_sel == True:
                if atom_min_x <= vmesna_lista[0] <= atom_max_x:
                    if atom_min_y <= vmesna_lista[1] <= atom_max_y:
                        if atom_min_z <= vmesna_lista[2] <= atom_max_z:
                            master_lista_vod_koordinata_x.append(x)
                            master_lista_vod_koordinata_y.append(y)
                            master_lista_vod_koordinata_z.append(z)
                            master_lista_vod.append(vmesna_lista)
                            master_lista_atom_iso_displacement.append(isotropni_displacement)
                            master_lista_info.append(info)


            else:
                pass

        # /DBSCAN formatting----------------------------------------------------

        # BSITE LOKALNO ALI GLOBALNO NA VERIGI
        if bsite_space_check == True and chain_sel == False:
            master_lista_vod = master_bsite_lista_vod
            master_lista_atom_iso_displacement = master_bsite_lista_atom_iso_displacement
            master_lista_info = master_bsite_lista_info
        else:
            pass

        mlv_datoteka.close()


        try:
            # example:
            # 2 clusters with 14 H2O molecules consv. 0.67
            cluster_selection = int(dialog.ListCalculated.currentItem().text().split()[3])
            consv_of_cluster = float(dialog.ListCalculated.currentItem().text().split()[7])

            # report list
            report_list_1.append("\nBinding site info (name, avg x, y, z, min x, max x, min y, max y, min z, max z; box 4 A around extremes): \n" + str(SELECTED_SITE))
            report_list_1.append("\nExamined cluster with " + str(cluster_selection) + " H2O molecules\n")
            report_list_1.append("-" * 25)

        except:
            QtWidgets.QMessageBox.about(dialog, "ProBiS H2O Warning", "Please select clusters to display")
            return
        selected_eps=dialog.SpinDB.value()
        labels3D = DBSCAN(eps=selected_eps, min_samples=cluster_selection).fit_predict(np.array(master_lista_vod))

        i = 0
        tocke = []
        for element in labels3D:
            temp = []
            if element != -1:
                temp.append(master_lista_vod[i])
                temp.append(element)
                temp.append(master_lista_atom_iso_displacement[i])
                temp.append(master_lista_info[i])
                report_list_1.append(temp)
                tocke.append(temp)

            else:
                pass
            i += 1


        if debye_waller_check == False:

            if display_clusters_setting == False:
                cmd.delete("H2O*")
            else:
                pass

            for element in list(set(labels3D)):
                cluster_temp = []
                for sub_element in tocke:
                    if sub_element[1] == element:
                        cluster_temp.append(sub_element[0])


                try:
                    cmd.set_color("clus_color", "[%f, %f, %f]" % (1.0, (1.0 - consv_of_cluster), (1.0 - consv_of_cluster)))
                    pymol.cmd.do("pseudoatom H2O_clus-%d_%.2f, vdw=1, color=clus_color, pos=[%f, %f, %f]" % (element, consv_of_cluster, cluster_temp[0][0], cluster_temp[0][1], cluster_temp[0][2]))
                    cmd.show("spheres", "H2O_clus-%d*" % (element))

                except IndexError:
                    pass

        else:

            cmd.delete("H2O*")
            cmd.delete("iso_disp")
            
            for element in list(set(labels3D)):
                cluster_temp = []
                for sub_element in tocke:
                    if sub_element[1] == element:
                        sub_element[0].append(sub_element[2])
                        cluster_temp.append(sub_element[0])

                try:
                    pymol.cmd.do("pseudoatom H2O_clus, vdw=1, color=red, pos=[%f, %f, %f]" % (cluster_temp[0][0], cluster_temp[0][1], cluster_temp[0][2]))
                    cmd.show("spheres", "H2O_clus")

                    for tocka in cluster_temp:
                        pymol.cmd.do("pseudoatom iso_disp, vdw=%f, color=red, pos=[%f, %f, %f]" % (cluster_temp[0][3], cluster_temp[0][0], cluster_temp[0][1], cluster_temp[0][2]))

                    cmd.show("dots", "iso_disp")

                except IndexError:
                    pass


        # report on cluster
        if custom == False:
            nova_datoteka = open("report_" + dialog.LineProtein.text().lower() + ".txt", "w")
        else:
            target = os.path.split(dialog.LineProtein.text())[1]
            nova_datoteka = open("report_"+ "custom_" + target.split(".")[0]+ ".txt", "w")
        for linija in report_list_1:
            nova_datoteka.write("%s\n" % linija)
        nova_datoteka.close()
        print("report created...")

# thanks Janez for Support!
