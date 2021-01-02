from pymongo import MongoClient
from PyQt5 import QtWidgets
from Students_class import all_data
import sys
import random
from StudentForm import Ui_MainWindow
idNumber=100500
serchBool=""
class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.combobox_changes()
        self.ui.comboBox.activated.connect(self.combobox_changes)
        self.conn = MongoClient()
        self.base = self.conn["StudBase"]
        self.coll = self.base["BaseColl"]
        self.ui.butt_record.clicked.connect(self.make_record)
        self.ui.butt_all_record.clicked.connect(self.yvelas_chawera)
        self.ui.butt_find.clicked.connect(self.dzebna)
        self.ui.butt_delete.clicked.connect(self.washla)
        self.ui.butt_update.clicked.connect(self.ganaxleba)
    def combobox_changes(self):
        text = self.ui.comboBox.currentText()
        if  text == "ჩანაწერის გაკეთება":
            self.ui.record_grp_names.setEnabled(False)
            self.ui.record_subjects.setEnabled(False)
            self.ui.record_te_num.setEnabled(False)

            self.ui.butt_update.setEnabled(False)
            self.ui.butt_delete.setEnabled(False)
            self.ui.butt_all_record.setEnabled(True)
            self.ui.butt_record.setEnabled(False)

            self.ui.fing_grp.setEnabled(False)

        elif text == "ჩანაწერის განახლება":
            self.ui.record_grp_names.setEnabled(False)
            self.ui.record_subjects.setEnabled(False)
            self.ui.record_te_num.setEnabled(False)

            self.ui.butt_update.setEnabled(False)
            self.ui.butt_delete.setEnabled(False)
            self.ui.butt_all_record.setEnabled(False)
            self.ui.butt_record.setEnabled(False)
            self.ui.fing_grp.setEnabled(True)

        elif text == "ჩანაწერის ძებნა":
            self.ui.record_grp_names.setEnabled(False)
            self.ui.record_subjects.setEnabled(False)

            self.ui.butt_all_record.setEnabled(False)
            self.ui.butt_record.setEnabled(False)
            self.ui.butt_update.setEnabled(False)
            self.ui.butt_delete.setEnabled(False)

            self.ui.fing_grp.setEnabled(True)

    def make_record(self):
        global idNumber
        idNumber+=1
        self.coll.insert_one({
            "_id": idNumber,

            "lname": self.ui.record_te_lname_2.toPlainText(),
            "fname": self.ui.record_te_fname_2.toPlainText(),

            "subject1": self.ui.te_subj_name1.toPlainText(),
            "score1": self.ui.te_subj_score1.toPlainText(),

            "subject2": self.ui.te_subj_name2.toPlainText(),
            "score2": self.ui.te_subj_score2.toPlainText(),

            "subject3": self.ui.te_subj_name3.toPlainText(),
            "score3": self.ui.te_subj_score3.toPlainText(),

            "subject4": self.ui.te_subj_name4.toPlainText(),
            "score4": self.ui.te_subj_score4.toPlainText(),

            "subject5": self.ui.te_subj_name5.toPlainText(),
            "score5": self.ui.te_subj_score5.toPlainText(),

            "subject6": self.ui.te_subj_name6.toPlainText(),
            "score6": self.ui.te_subj_score6.toPlainText(),

            "subject7": self.ui.te_subj_name7.toPlainText(),
            "score7": self.ui.te_subj_score7.toPlainText(),

            "subject8": self.ui.te_subj_name8.toPlainText(),
            "score8": self.ui.te_subj_score8.toPlainText(),

            "subject9": self.ui.te_subj_name9.toPlainText(),
            "score9": self.ui.te_subj_score9.toPlainText(),

            "subject10": self.ui.te_subj_name10.toPlainText(),
            "score10": self.ui.te_subj_score10.toPlainText()

        })


        self.ui.record_te_lname_2.setText("")
        self.ui.record_te_fname_2.setText("")

        self.ui.te_subj_name1.setText("")
        self.ui.te_subj_score1.setText("")

        self.ui.te_subj_name2.setText("")
        self.ui.te_subj_score2.setText("")

        self.ui.te_subj_name3.setText("")
        self.ui.te_subj_score3.setText("")

        self.ui.te_subj_name4.setText("")
        self.ui.te_subj_score4.setText("")

        self.ui.te_subj_name5.setText("")
        self.ui.te_subj_score5.setText("")

        self.ui.te_subj_name6.setText("")
        self.ui.te_subj_score6.setText("")

        self.ui.te_subj_name7.setText("")
        self.ui.te_subj_score7.setText("")

        self.ui.te_subj_name8.setText("")
        self.ui.te_subj_score8.setText("")

        self.ui.te_subj_name9.setText("")
        self.ui.te_subj_score9.setText("")

        self.ui.te_subj_name10.setText("")
        self.ui.te_subj_score10.setText("")

    def yvelas_chawera(self):

        Stud_list=all_data()
        mongo_list = [stud.obj_to_dict() for stud in Stud_list]

        # მოვახდინოთ ბაზაში მონაცემების ჩაწერა
        try:
            self.coll.insert_many(mongo_list)
        except:
            pass
        #გავთიშოთ "ყველას ჩაწერა" ღილაკი
        self.ui.butt_all_record.setEnabled(False)
        self.ui.butt_record.setEnabled(True)
        self.ui.record_grp_names.setEnabled(True)
        self.ui.record_subjects.setEnabled(True)


    def dzebna(self):
        text = self.ui.comboBox.currentText()
        find_id=self.ui.delete_te_num.toPlainText()
        find_fn=self.ui.delete_te_fname.toPlainText()
        find_ln=self.ui.delete_te_lname.toPlainText()
        global serchBool

        if len(find_id)>0:
            temp=self.coll.find_one({"_id": int(find_id)},{})
            if(temp==None):
                self.ui.label_find.setText("Can't find")

            else:
                self.ui.label_find.setText("Find")
                serchBool ={"_id": int(find_id)}
                if (text == "ჩანაწერის ძებნა"):
                    self.ui.butt_delete.setEnabled(True)
                if (text == "ჩანაწერის განახლება"):
                    self.ui.butt_update.setEnabled(True)
                    self.ui.record_subjects.setEnabled(True)

        else:
            if((len(find_fn)>0 and len(find_ln)>0)):
                temp=self.coll.find_one({"lname": find_ln,"fname": find_fn},{})
                if (temp == None):
                    self.ui.label_find.setText("Can't find")
                else:
                    self.ui.label_find.setText("Find")
                    serchBool = {"lname": find_ln,"fname": find_fn}
                    if (text == "ჩანაწერის ძებნა"):
                        self.ui.butt_delete.setEnabled(True)
                    if (text == "ჩანაწერის განახლება"):
                        self.ui.butt_update.setEnabled(True)
                        self.ui.record_subjects.setEnabled(True)


    def washla(self):
        global  serchBool
        self.coll.delete_one(serchBool)
        serchBool=""
        self.ui.butt_delete.setEnabled(False)
        self.ui.label_find.setText("")
        self.ui.delete_te_num.setText("")
        self.ui.delete_te_fname.setText("")
        self.ui.delete_te_lname.setText("")
    def ganaxleba(self):
        #vanaxlebt yvela sagnebis da qulis shesaxeb yvela monacems
        doc_update={
            "subject1": self.ui.te_subj_name1.toPlainText(),
            "score1": self.ui.te_subj_score1.toPlainText(),

            "subject2": self.ui.te_subj_name2.toPlainText(),
            "score2": self.ui.te_subj_score2.toPlainText(),

            "subject3": self.ui.te_subj_name3.toPlainText(),
            "score3": self.ui.te_subj_score3.toPlainText(),

            "subject4": self.ui.te_subj_name4.toPlainText(),
            "score4": self.ui.te_subj_score4.toPlainText(),

            "subject5": self.ui.te_subj_name5.toPlainText(),
            "score5": self.ui.te_subj_score5.toPlainText(),

            "subject6": self.ui.te_subj_name6.toPlainText(),
            "score6": self.ui.te_subj_score6.toPlainText(),

            "subject7": self.ui.te_subj_name7.toPlainText(),
            "score7": self.ui.te_subj_score7.toPlainText(),

            "subject8": self.ui.te_subj_name8.toPlainText(),
            "score8": self.ui.te_subj_score8.toPlainText(),

            "subject9": self.ui.te_subj_name9.toPlainText(),
            "score9": self.ui.te_subj_score9.toPlainText(),

            "subject10": self.ui.te_subj_name10.toPlainText(),
            "score10": self.ui.te_subj_score10.toPlainText()

        }
        global serchBool
        self.coll.update_one(serchBool,{"$set":doc_update})
        serchBool = ""
        self.ui.butt_update.setEnabled(False)
        self.ui.label_find.setText("")
        self.ui.delete_te_num.setText("")
        self.ui.delete_te_fname.setText("")
        self.ui.delete_te_lname.setText("")
        #gavasuftaod sagnebis shetanis velebi
        self.ui.te_subj_name1.setText("")
        self.ui.te_subj_score1.setText("")

        self.ui.te_subj_name2.setText("")
        self.ui.te_subj_score2.setText("")

        self.ui.te_subj_name3.setText("")
        self.ui.te_subj_score3.setText("")

        self.ui.te_subj_name4.setText("")
        self.ui.te_subj_score4.setText("")

        self.ui.te_subj_name5.setText("")
        self.ui.te_subj_score5.setText("")

        self.ui.te_subj_name6.setText("")
        self.ui.te_subj_score6.setText("")

        self.ui.te_subj_name7.setText("")
        self.ui.te_subj_score7.setText("")

        self.ui.te_subj_name8.setText("")
        self.ui.te_subj_score8.setText("")

        self.ui.te_subj_name9.setText("")
        self.ui.te_subj_score9.setText("")

        self.ui.te_subj_name10.setText("")
        self.ui.te_subj_score10.setText("")
        self.ui.record_subjects.setEnabled(False)

app = QtWidgets.QApplication([])
application = myApp()
application.show()
sys.exit(app.exec())


