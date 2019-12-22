from widgets_ui import Ui_MainWindow
from works import pro_make
# import settings
from PyQt5.Qt import *
import datetime
import json
import sys

run_argvs = sys.argv

if len(run_argvs) > 1:
    RL_PATH = run_argvs[1]
else:
    RL_PATH = ""


class MainWindow(QMainWindow):
    """
    界面显示
    """
    def __init__(self, parent=None):
        """
        初始化界面
        :param parent: 
        """
        super(MainWindow, self).__init__(parent=parent)
        self.classes_list = ["C", "C++", "Java", "Python", "JavaScript", "C#", "Swift", "go", "Ruby", "Lua", "PHP"]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.button_pro()
        self.init_classes_list()
        self.right_list_init()
        self.tc_list_init()
        self.init_show()

    def init_show(self):
        """
        界面显示
        :return: 
        """
        self.resize(800, 550)
        self.setFixedSize(800, 550)
        self.setWindowTitle("Tokin")
        self.show()

    def button_pro(self):
        """
        按键事件处理
        :return: 
        """
        self.ui.cleanButton.clicked.connect(self.clean_button)
        self.ui.addLinksButton.clicked.connect(self.add_links_button)
        self.ui.preprocButton.clicked.connect(self.preproc_button)
        self.ui.buildButton.clicked.connect(self.build_button)
        self.ui.runButton.clicked.connect(self.run_button)
        self.ui.clearButton.clicked.connect(self.info_clear)

    def init_classes_list(self):
        """
        选择Tclass
        :return: 
        """
        for item in self.classes_list:
            self.ui.comboBox.addItem(item)
        self.ui.comboBox.setCurrentIndex(-1)

    def clean_button(self):
        """
        单步调节clean
        :return: 
        """
        currn_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        format_info = f"{currn_time}-clean: process begin clean...."
        self.ui.info_output.appendPlainText(format_info)

    def add_links_button(self):
        """
        单步调节add links
        :return: 
        """
        currn_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        format_info = f"{currn_time}-add links: process begin add links...."
        self.ui.info_output.appendPlainText(format_info)

    def preproc_button(self):
        """
        单步调节preproc
        :return: 
        """
        currn_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        format_info = f"{currn_time}-preproc: process begin preproc...."
        self.ui.info_output.appendPlainText(format_info)

    def build_button(self):
        """
        但不调节build sim script
        :return: 
        """
        currn_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        format_info = f"{currn_time}-build sim script: process begin build sim script...."
        self.ui.info_output.appendPlainText(format_info)

    def run_button(self):
        """
        全跑run
        :return: 
        """
        currn_time = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        format_info = f"{currn_time}-run:"
        self.ui.info_output.appendPlainText(format_info)
        if self.ui.right_option_file.text():
            method = getattr(pro_make, self.tc_make_type)
            ret = method(self.current_select_tc)
            self.ui.info_output.appendPlainText(ret)
        else:
            msg = "please select test case example"
            self.ui.info_output.appendPlainText(msg)

    def info_clear(self):
        """
        日志输出清除
        :return: 
        """
        self.ui.info_output.setPlainText("")

    def right_list_init(self):
        """
        右边列表初始化
        :return: 
        """
        self.__rl_model = QFileSystemModel(self)
        self.__rl_model.setRootPath(QDir.rootPath())
        self.ui.left_list.setModel(self.__rl_model)
        self.__current_select_path = None
        self.ui.left_list.doubleClicked.connect(self.getCurPathEvent)
        if RL_PATH:
            self.setPath(RL_PATH)

    def getCurPathEvent(self):
        """
        双击信号 获得当前选中的节点的路径
        :return: 
        """
        index = self.ui.left_list.currentIndex()
        model = index.model()  # 请注意这里可以获得model的对象
        self.__current_select_path = model.filePath(index)
        self.getCurPath(self.__current_select_path)

    def setPath(self, path):
        """
        设置TreeView的跟文件夹
        :param path: 
        :return: 
        """
        self.ui.left_list.setRootIndex(self.__rl_model.index(path))

    def tc_list_init(self):
        self.tc_model = QFileSystemModel(self)
        self.tc_model.setRootPath(QDir.rootPath())
        self.ui.Tc_list.doubleClicked.connect(self.get_tc_event)

    def getCurPath(self, path):
        """
        获得当前选中的节点的路径
        :return: 
        """
        with open(path, "r", encoding="utf-8") as f:
            tc_json = json.loads(f.read())
        tc_path = tc_json.get("file_path")
        self.tc_make_type = tc_json.get("make_type")
        self.ui.Tc_list.setModel(self.tc_model)
        self.ui.Tc_list.setRootIndex(self.tc_model.index(tc_path))

    def get_tc_event(self):
        """
        双击tc文件获取文件路径，添加到执行文件中
        :return: 
        """
        index = self.ui.Tc_list.currentIndex()
        model = index.model()  # 请注意这里可以获得model的对象
        self.current_select_tc = model.filePath(index)
        file_name = self.current_select_tc.split("/")[-1]
        self.ui.right_option_file.setText(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

