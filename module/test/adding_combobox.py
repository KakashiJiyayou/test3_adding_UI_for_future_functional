import  sys
from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *
import  json
 
# setting path
sys.path.append('E:\\Project\\Job\\GQ\\Python\\Baidu_downlaod_upload\\test3_adding_UI_for_future_functional\\')

print(sys.path)
from resource_ui2  import Ui_MainWindow



class MainWindow( QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.page_stackedWidget.setCurrentIndex(1)
        self.ui.home_btn_2.setChecked(1)

        # add combobox
        # self.addingComboboxAndLabel()
        self.addingComboboxAndLabel2()
        self.addingComboboxAndLabel3()
        self.search_functionalities()
        self.showProgress()

    def addingComboboxAndLabel(self):
        ## create vertical layout
        main_vertical_window = QVBoxLayout()

        ## load layout for the page
        uplaod_page = self.ui.upload_page
        uplaod_page.setLayout(main_vertical_window)

        ## add scrolbar to the main layout
        scroll_content = QScrollArea()
        main_vertical_window.addWidget(scroll_content)

        ## run a loop to add multiple vbox
        vbox = QVBoxLayout()
        for i in range(1, 20):
            widget = self.get_h_layout(i,["test1","test2"])
            vbox.addWidget(widget)

        widget = QWidget()
        widget.setLayout(vbox)

        # scroll_content.setWidgetResizable(True)
        scroll_content.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_content.setWidget(widget)
        scroll_content.setGeometry(0,0,400,400)
        scroll_content.setMaximumHeight(400)


    def addingComboboxAndLabel2(self):
        ## create vertical layout
        # main_vertical_window = QGridLayout()

        ## load layout for the page
        # uplaod_page = self.ui.upload_page
        # uplaod_page.setLayout(main_vertical_window)

        ## add scrolbar to the main layout
        scroll_content = self.ui.scrollArea
        # main_vertical_window.addWidget(scroll_content)

        ## run a loop to add multiple vbox
        vbox = QVBoxLayout()
        for i in range(1, 20):
            widget = self.get_h_layout(i,["test1","test2"])
            vbox.addWidget(widget)

        widget = self.get_h_layout2(21,["test1","test2"])
        vbox.addWidget(widget)

        widget = QWidget()
        widget.setLayout(vbox)

        # scroll_content.setWidgetResizable(True)
        scroll_content.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_content.setWidget(widget)
        # scroll_content.setGeometry(0,0,0,0)
        # scroll_content.setMaximumHeight(400)
        # scroll_content.setMinimumHeight(400)

    def addingComboboxAndLabel3(self):
        ## create vertical layout
        # main_vertical_window = QGridLayout()

        ## load layout for the page
        # uplaod_page = self.ui.upload_page
        # uplaod_page.setLayout(main_vertical_window)

        ## add scrolbar to the main layout
        scroll_content = self.ui.scrollArea_2_edit_page
        # main_vertical_window.addWidget(scroll_content)

        ## run a loop to add multiple vbox
        vbox = QVBoxLayout()
        for i in range(1, 20):
            widget = self.get_h_layout(i,["test1","test2"])
            vbox.addWidget(widget)

        widget = self.get_h_layout2(21,["test1","test2"])
        vbox.addWidget(widget)

        widget = QWidget()
        widget.setLayout(vbox)

        # scroll_content.setWidgetResizable(True)
        scroll_content.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_content.setWidget(widget)
        # scroll_content.setGeometry(0,0,0,0)
        # scroll_content.setMaximumHeight(400)
        # scroll_content.setMinimumHeight(400)

    def search_functionalities(self):
        with open("data.json", "r") as f:
            self.data = json.load(f)

        words_list = self.data.keys()

        completer = QCompleter(words_list)
        self.ui.search_input.setCompleter(completer)

    def showProgress(self):
        bar1 = QProgressBar()
        bar2 = QProgressDialog()

        bar1.setGeometry(0,0,800,800)

        bar1.setValue(10)
        bar2.setValue(10)

        bar2.setLabelText("doing uploading")

        bar2.show()
        bar1.show()

    def on_search_input_textChanged(self, text):

        print(" From search " + text)

        # defination = self.data.get(text)
        #
        # self.ui.listWidget.clear()
        #
        # if defination:
        #     for i, item in enumerate(defination):
        #         self.ui.listWidget.addItem(f"{i + 1}. {item}")


    def get_h_layout(self, label_text, items):
        label = QLabel(self)
        label.setText("File Type 文件类型" + str(label_text))

        combo = QComboBox(self)
        combo.addItem("test1")
        combo.addItems(["test2", "test3"])
        combo.setCurrentIndex(0)

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(combo)

        widget = QWidget()
        widget.setFixedHeight(40)
        widget.setLayout(layout)

        return widget

    def get_h_layout2(self, label_text, items):
        label = QLabel(self)
        label.setText("File Type 文件类型" + str(label_text))

        combo = QComboBox(self)
        combo.addItem("test1")
        combo.addItems(["test2", "test3"])
        combo.setCurrentIndex(0)

        combo2 = QComboBox(self)
        combo2.addItem("test1")
        combo2.addItems(["test2", "test3"])
        combo2.setCurrentIndex(0)

        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(combo)
        layout.addWidget(combo2)

        widget = QWidget()
        widget.setFixedHeight(40)
        widget.setLayout(layout)

        return widget





### start the app
if __name__  == "__main__":
    app = QApplication(sys.argv)

    ## laod css
    with open("style.qss","r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    ## make applicaiton object
    window = MainWindow()
    window.show()

    sys.exit(app.exec())