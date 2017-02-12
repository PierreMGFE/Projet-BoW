import sys, os, platform
from PyQt5 import QtCore, QtGui, QtWidgets

format = ""
folder_path = ""
file_path = ""
input_param = {}


def start_clustering_click(window):
    #local launch variables
    start = False
    error_message_text = ""

    #fetch parameters
    format = window.format_buttonGroup.checkedButton().text().lower()

    input_param = {"freq" : window.frequency_buttonGroup.checkedButton().text(),
                   "df_min" : window.minimum_frequency.value()/100,
                   "df_max" : window.maximum_frequency.value()/100,
                   "n_feat" : window.number_features.value(),
                   "facto" : window.factorisation_buttonGroup.checkedButton().text(),
                   "n_topics" : window.number_topics.value(),
                   "n_top_feat" : window.number_most_important_features.value(),
                   "n_clust" : window.number_clusters.value()}


    # window.output_parameters = [box.isChecked() for box in window.choose_outputs.buttons()]


    # Check if path is valid
    if os.path.isdir(folder_path):
        # Check if format is valid
        if (format == "pdf" or format == "txt"):
            # Check if there are valid files in directory
            if len([file for file in os.listdir(folder_path) if file.endswith("." + format)]):
                # Check if parameters are valid
                if input_param["df_min"] < input_param["df_max"]:
                    launch = True
                else:
                    error_message_text += "Check frequency\n"
            else:
                error_message_text += "No " + format + " files in directory\n"
        else:
            error_message_text += "Invalid format\n"
    else:
        error_message_text += "Invalid directory\n"

    # Launch or error message
    if start :
        if format == "pdf":
            os.chdir(folder_path)
            if not os.path.isdir("converted"):
                os.mkdir("converted")
            pdfs = [file for file in os.listdir() if file.endswith(".pdf")]

            for file in pdfs:
                txt_name = "converted/"
                for i in range(len(file) - 4):
                    txt_name += file[i]
                txt_name += ".txt"
                try:
                    os.system("pdftotext " + file + " " + txt_name)
                except:
                    print("Conversion error")


            dir_path += "/converted"

        os.chdir(dir_path)
        input_files = [file for file in os.listdir() if file.endswith(".txt")]

        # TODO : access algorithm from here
        # output = algorithm(parameters, files)


    else :
        error_message = QtWidgets.QMessageBox()
        error_message.setWindowTitle("Error")
        error_message.setText(error_message_text)
        error_message.exec_()





def exit_program(window):
    exit_message = QtWidgets.QMessageBox()
    exit_message.setWindowTitle("Exit program")
    exit_message.setText("Any changes made will be discarded.\nDo you want to proceed ?")
    exit_message.addButton(QtWidgets.QMessageBox.Yes)
    exit_message.addButton(QtWidgets.QMessageBox.No)
    if (exit_message.exec_() == QtWidgets.QMessageBox.Yes):
        window.close()



def about_dialog(window):
    message = QtWidgets.QMessageBox()
    message.setWindowTitle("About")
    message.setText("ENPC 2016-2017\nProjet TDLOG\n"
                    "\nFrançois DUPRÉ\nPierre GIACCOBI\nPierre LECUYER\nFlorian MANTE")
    message.exec_()



def folder_path_dialog(window):
    options = QtWidgets.QFileDialog.Options()
    folder_path = QtWidgets.QFileDialog.getExistingDirectory(window, "Choose source folder", "", options=options)
    window.source_folder_line.setText(str(folder_path))



def file_path_dialog(window):
    options = QtWidgets.QFileDialog.Options()
    file_path = QtWidgets.QFileDialog.getOpenFileName(window, "Choose source file", "", options=options)
    window.source_folder_line.setText(str(file_path))



if __name__ == '__main__':
    bow_gui = QtWidgets.QApplication(sys.argv)
    mainWindow = Bow()
    mainWindow.show()
    mainWindow.raise_()
    bow_gui.exec_()
