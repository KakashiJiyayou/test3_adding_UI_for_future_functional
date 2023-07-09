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
        self.showProgress()

        self.path_list = ['/软件编制 资料', '/软件编制 资料/技术文件', '/软件编制 资料/技术文件/组织安全方案.doc',
                          '/软件编制 资料/技术文件/管道养护文件40页.doc', '/软件编制 资料/技术文件/管道养护标 应急预案.doc',
                          '/软件编制 资料/技术文件/CCTV检测文件5页.doc', '/软件编制 资料/技术文件/环境方案.doc',
                          '/软件编制 资料/技术文件/管道修复文件20页.doc', '/软件编制 资料/技术文件/管道检测标应急预案.doc',
                          '/软件编制 资料/技术文件/CCTV检测技术文件10页.doc', '/软件编制 资料/业绩合同',
                          '/软件编制 资料/业绩合同/管道检测修复项目50万.doc', '/软件编制 资料/业绩合同/排水公司疏通检测项目20万.doc',
                          '/软件编制 资料/业绩合同/舟山市污水零直排项目100万.doc', '/软件编制 资料/业绩合同/管道检测项目.doc',
                          '/软件编制 资料/业绩合同/DG225销售合同【上海金佳】.doc', '/软件编制 资料/业绩合同/崇仁镇污水零直排项目3万.doc',
                          '/软件编制 资料/软件 编制(1).ppt', '/软件编制 资料/公司证件', '/软件编制 资料/公司证件/市政三级环保三级.doc',
                          '/软件编制 资料/公司证件/ISO环境证书2021-2023年.doc', '/软件编制 资料/公司证件/健康环境证书2021-2023.8月.doc',
                          '/软件编制 资料/公司证件/安全许可证.doc', '/软件编制 资料/公司证件/重信用证书.doc',
                          '/软件编制 资料/公司证件/公司营业执照.doc', '/软件编制 资料/公司证件/生产环境体系证书2021.2-2024.1.doc',
                          '/软件编制 资料/发票设备', '/软件编制 资料/发票设备/检测机器人3【0003849】.doc',
                          '/软件编制 资料/发票设备/QV设备15套.doc', '/软件编制 资料/发票设备/箱式车辆【000】.doc',
                          '/软件编制 资料/发票设备/毒气检测仪5套【089812】.doc', '/软件编制 资料/发票设备/毒气检测仪3套【09123】.doc',
                          '/软件编制 资料/发票设备/箱式车辆【0001】.doc', '/软件编制 资料/发票设备/疏通车辆【浙B0lmt】.doc',
                          '/软件编制 资料/发票设备/疏通车辆 【浙B0MET].doc', '/软件编制 资料/发票设备/检测机器人5【0012342】.doc',
                          '/软件编制 资料/发票设备/检测机器人2个【009878】.doc', '/软件编制 资料/发票设备/管道机器人5套【123401】.doc',
                          '/软件编制 资料/发票设备/正压式呼吸器4个.doc', '/软件编制 资料/人员证书',
                          '/软件编制 资料/人员证书/安全员谢嘉.doc', '/软件编制 资料/人员证书/安全员于娜.doc',
                          '/软件编制 资料/人员证书/环境工程师张明华.doc', '/软件编制 资料/人员证书/CCTV检测员王超.doc',
                          '/软件编制 资料/人员证书/二级建造师王占生.doc', '/软件编制 资料/人员证书/环境工程师谢嘉.doc',
                          '/软件编制 资料/人员证书/潜水员谢生.doc', '/软件编制 资料/人员证书/养护工谢林.doc',
                          '/软件编制 资料/人员证书/安全员张春梅.doc', '/软件编制 资料/人员证书/养护工林涛.doc',
                          '/软件编制 资料/人员证书/CCTV检测员赵红好.doc', '/软件编制 资料/人员证书/CCTV检测员周浩.doc',
                          '/软件编制 资料/人员证书/养护工张明华.doc', '/软件编制 资料/标书导图1.emmx',
                          '/软件编制 资料/rwqr.docx', '/chat', '/chat/chat.wxml', '/chat/chat.js', '/chat/chat.json',
                          '/chat/chat.wxss', '/root', '/root/server', '/root/server/public', '/root/server/public/admin']

        self.search_functionalities()


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

        # completer = QCompleter(words_list)
        completer  = QCompleter ( self.path_list )
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