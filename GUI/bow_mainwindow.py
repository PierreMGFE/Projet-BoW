# -*- coding: utf-8 -*-

import sys, os.path
from PyQt5 import QtCore, QtGui, QtWidgets

class bow_mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__(None)
        self.setObjectName("bow")
        self.setEnabled(True)
        self.resize(366, 533)
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setWindowTitle("Language Processing")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("BOW.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.Source_folder = QtWidgets.QLabel(self.centralwidget)
        self.Source_folder.setGeometry(QtCore.QRect(20, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Source_folder.setFont(font)
        self.Source_folder.setText("Source folder")
        self.Source_folder.setObjectName("Source_folder")
        self.Analysis_output = QtWidgets.QLabel(self.centralwidget)
        self.Analysis_output.setGeometry(QtCore.QRect(20, 280, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Analysis_output.setFont(font)
        self.Analysis_output.setText("Analysis outputs")
        self.Analysis_output.setObjectName("Analysis_output")
        self.Source_format = QtWidgets.QLabel(self.centralwidget)
        self.Source_format.setGeometry(QtCore.QRect(20, 110, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Source_format.setFont(font)
        self.Source_format.setText("Source format")
        self.Source_format.setObjectName("Source_format")
        self.Source_folder_description = QtWidgets.QLabel(self.centralwidget)
        self.Source_folder_description.setGeometry(QtCore.QRect(30, 40, 261, 21))
        self.Source_folder_description.setText("Select the folder where your source files are stored")
        self.Source_folder_description.setObjectName("Source_folder_description")
        self.Source_format_description = QtWidgets.QLabel(self.centralwidget)
        self.Source_format_description.setGeometry(QtCore.QRect(30, 140, 321, 41))
        self.Source_format_description.setText(
            "Select the file type of your source files. If PDF is selected, corresponding files will converted to TXT and saved to a subfolder before analysis.")
        self.Source_format_description.setWordWrap(True)
        self.Source_format_description.setObjectName("Source_format_description")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 320, 133, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.analysis = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.analysis.setContentsMargins(0, 0, 0, 0)
        self.analysis.setObjectName("analysis")
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setText("Stemmed words")
        self.checkBox_3.setShortcut("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.choose_outputs = QtWidgets.QButtonGroup()
        self.choose_outputs.setObjectName("choose_outputs")
        self.choose_outputs.setExclusive(False)
        self.choose_outputs.addButton(self.checkBox_3)
        self.analysis.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setText("Word Frequency")
        self.checkBox_4.setShortcut("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.choose_outputs.addButton(self.checkBox_4)
        self.analysis.addWidget(self.checkBox_4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setText("Themes")
        self.checkBox_2.setShortcut("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.choose_outputs.addButton(self.checkBox_2)
        self.analysis.addWidget(self.checkBox_2)
        self.checkBox_1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_1.setText("Text-to-text distances")
        self.checkBox_1.setShortcut("")
        self.checkBox_1.setObjectName("checkBox_1")
        self.choose_outputs.addButton(self.checkBox_1)
        self.analysis.addWidget(self.checkBox_1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 190, 284, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.format = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.format.setContentsMargins(0, 0, 0, 0)
        self.format.setObjectName("format")
        self.pdf_button = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.pdf_button.setText("PDF")
        self.pdf_button.setShortcut("")
        self.pdf_button.setObjectName("pdf_button")
        self.choose_format = QtWidgets.QButtonGroup()
        self.choose_format.setObjectName("choose_format")
        self.choose_format.addButton(self.pdf_button)
        self.format.addWidget(self.pdf_button, 0, 0, 1, 1)
        self.txt_button = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.txt_button.setText("TXT")
        self.txt_button.setShortcut("")
        self.txt_button.setObjectName("txt_button")
        self.choose_format.addButton(self.txt_button)
        self.format.addWidget(self.txt_button, 1, 0, 1, 1)
        self.pdf_description = QtWidgets.QLabel(self.gridLayoutWidget)
        self.pdf_description.setEnabled(True)
        self.pdf_description.setStyleSheet("QLabel {color: rgb(255, 186, 23)}\n" "\n" "")
        self.pdf_description.setText("- Generated .txt files will be saved to /converted")
        self.pdf_description.setTextFormat(QtCore.Qt.AutoText)
        self.pdf_description.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.pdf_description.setObjectName("pdf_description")
        self.format.addWidget(self.pdf_description, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 60, 311, 41))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.browse = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.browse.setContentsMargins(0, 0, 0, 0)
        self.browse.setObjectName("browse")
        self.source_folder_line = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_folder_line.sizePolicy().hasHeightForWidth())
        self.source_folder_line.setSizePolicy(sizePolicy)
        self.source_folder_line.setInputMask("")
        self.source_folder_line.setText("")
        self.source_folder_line.setObjectName("source_folder_line")
        self.browse.addWidget(self.source_folder_line, 0, 0, 1, 1)
        self.browse_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse_button.sizePolicy().hasHeightForWidth())
        self.browse_button.setSizePolicy(sizePolicy)
        self.browse_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse_button.setText("Browse")
        self.browse_button.setShortcut("")
        self.browse_button.setObjectName("browse_button")
        self.browse.addWidget(self.browse_button, 0, 1, 1, 1)
        self.launch_analysis_button = QtWidgets.QPushButton(self.centralwidget)
        self.launch_analysis_button.setGeometry(QtCore.QRect(220, 460, 121, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.launch_analysis_button.setFont(font)
        self.launch_analysis_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.launch_analysis_button.setText("Launch analysis")
        self.launch_analysis_button.setShortcut("Enter")
        self.launch_analysis_button.setObjectName("launch_analysis_button")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setTitle("File")
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setToolTip("")
        self.menuEdit.setStatusTip("")
        self.menuEdit.setWhatsThis("")
        self.menuEdit.setAccessibleName("")
        self.menuEdit.setAccessibleDescription("")
        self.menuEdit.setTitle("Edit")
        self.menuEdit.setObjectName("menuEdit")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setTitle("Options")
        self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTitle("Help")
        self.menuHelp.setObjectName("menuHelp")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setText("About")
        self.actionAbout.setIconText("About")
        self.actionAbout.setToolTip("About")
        self.actionAbout.setStatusTip("")
        self.actionAbout.setWhatsThis("")
        self.actionAbout.setShortcut("")
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew = QtWidgets.QAction(self)
        self.actionNew.setText("New")
        self.actionNew.setIconText("New")
        self.actionNew.setToolTip("New")
        self.actionNew.setStatusTip("")
        self.actionNew.setWhatsThis("")
        self.actionNew.setShortcut("")
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setText("Open")
        self.actionOpen.setIconText("Open")
        self.actionOpen.setToolTip("Open")
        self.actionOpen.setStatusTip("")
        self.actionOpen.setWhatsThis("")
        self.actionOpen.setShortcut("")
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(self)
        self.actionSave_as.setText("Save as...")
        self.actionSave_as.setIconText("Save as")
        self.actionSave_as.setToolTip("Save as")
        self.actionSave_as.setStatusTip("")
        self.actionSave_as.setWhatsThis("")
        self.actionSave_as.setShortcut("")
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave = QtWidgets.QAction(self)
        self.actionSave.setText("Save")
        self.actionSave.setIconText("Save")
        self.actionSave.setToolTip("Save")
        self.actionSave.setStatusTip("")
        self.actionSave.setWhatsThis("")
        self.actionSave.setShortcut("")
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(self)
        self.actionExit.setText("Exit")
        self.actionExit.setIconText("Exit")
        self.actionExit.setToolTip("Exit")
        self.actionExit.setStatusTip("")
        self.actionExit.setWhatsThis("")
        self.actionExit.setShortcut("")
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        # Menus
        self.actionExit.triggered.connect(self.exit_program)
        self.actionSave_as.triggered.connect(self.open_save_as_dialog)
        self.actionAbout.triggered.connect(self.open_about_dialog)

        # Browse
        self.dir_path = ""
        self.browse_button.clicked.connect(self.open_directory_name_dialog)
        self.input_files = []

        # Format
        self.pdf_description.setVisible(False)
        self.format = ""
        self.pdf_button.toggled['bool'].connect(self.pdf_description.setVisible)
        self.pdf_button.toggled['bool'].connect(self.set_format)

        # Analysis outputs
        self.parameters = []

        # Launch Analysis
        self.launch_analysis_button.clicked.connect(self.launch_analysis)

    def exit_program(self):
        exit_message = QtWidgets.QMessageBox()
        exit_message.setWindowTitle("Exit program")
        exit_message.setText("Any changes made will be discarded.\nDo you want to proceed ?")
        exit_message.addButton(QtWidgets.QMessageBox.Yes)
        exit_message.addButton(QtWidgets.QMessageBox.No)
        if (exit_message.exec_() == QtWidgets.QMessageBox.Yes):
            self.close()

    def launch_analysis(self):
        launch = False
        error_message_text = ""
        self.parameters = [box.isChecked() for box in self.choose_outputs.buttons()]
        print(self.parameters)
        # TODO : in save file, write what each item in self.parameters refers to

        # Check if path is valid
        if os.path.isdir(self.dir_path):
            # Check if format is valid
            if (self.format == "pdf" or self.format == "txt"):
                # Check if there are valid files in directory
                if len([file for file in os.listdir(self.dir_path) if file.endswith("." + self.format)]):
                    # Check if parameters are valid
                    if len([param for param in self.parameters if param]):
                        launch = True
                    else:
                        error_message_text += "Select at least 1 output\n"
                else:
                    error_message_text += "No " + self.format.upper() + " files in directory\n"
            else:
                error_message_text += "Invalid format\n"
        else:
            error_message_text += "Invalid directory\n"

        # Launch or error message
        if launch :
            if self.format == "pdf":
                os.mkdir(self.dir_path + "/Converted TXT files")
                # converted_files = convert() # TODO : write conversion function
                self.dir_path += "/converted"
                self.input_files = [] # TODO : load files into this table
            else:
                self.input_files = []
            # TODO : access algorithm from here
            # output = algorithm(self.parameters, self.files)


        else :
            error_message = QtWidgets.QMessageBox()
            error_message.setWindowTitle("Error")
            error_message.setText(error_message_text)
            error_message.exec_()

    def set_format(self):
        self.format = ("pdf" if self.pdf_button.isChecked() else "txt")
        # print(self.format)

    def open_about_dialog(self):
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("BOW.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        message = QtWidgets.QMessageBox()
        # message.setIcon(icon)
        message.setWindowTitle("About")
        message.setText("ENPC 2016-2017\nProjet TDLOG\n"
                        "\nFrançois DUPRÉ\nPierre GIACCOBI\nPierre LECUYER\nFlorian MANTE")
        message.exec_()

    def open_directory_name_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        self.dir_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose source folder", "", options=options)
        self.source_folder_line.setText(str(self.dir_path))

    def open_save_as_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                            "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


if __name__ == '__main__':
    bow_gui = QtWidgets.QApplication(sys.argv)
    mainWindow = bow_mainwindow()
    mainWindow.show()
    mainWindow.raise_()
    bow_gui.exec_()
