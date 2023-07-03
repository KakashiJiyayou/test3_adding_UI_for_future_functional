import sys

from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *
from PyQt5.QtCore import QDir, Qt

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMainWindow()
    # Splitter to show 2 views in same widget easily.
    # splitter = QSplitter()
    # The model.
    model = QFileSystemModel()

    model.setRootPath(r"E:\Project\Job\GQ\Python\Baidu_downlaod_upload\test3_adding_UI_for_future_functional\module\test\\")

    view = QTreeView()
    view.setModel(model)

    view.show()
    # main.show()


    # Start the main loop.
    sys.exit(app.exec_())