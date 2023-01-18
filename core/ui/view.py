# Template file
"""
View Classes
"""
from PySide2 import QtWidgets, QtCore


class InterfaceAbstract(QtWidgets.QMainWindow):
    """
    InterfaceAbstract
    """

    def __init__(self):
        """

        """
        super(InterfaceAbstract).__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")
        self.set_central_widget()

    def add_btn(self, btn):
        """
        Adds a button to the grid layout , will be visible to the viewer
        :param item: (model_abstract.ScriptAbstract)
        :return:
        """
        self.container_layout.addWidget(btn)

    def set_window_title(self):
        """

        :return:
        """
        self.setWindowTitle(self.title)

    def set_central_widget(self):
        """

        :return:
        """
        self.setCentralWidget(self.central_widget)

    def show_ui(self):
        """

        :return:
        """
        self.show()

    def hide_ui(self):
        """

        :return:
        """
        self.hide()

    def get_pos(self):
        """

        :return:
        """
        return self.pos()

    def switch_view(self, target):
        """

        :param target:
        :return:
        """
        target.hide_ui()
        self.show_ui()


class DefaultInterface(InterfaceAbstract):
    """
    DefaultInterface
    """

    def __init__(self):
        """

        """
        super(DefaultInterface).__init__()
        self.title = 'Helpers Interface'
        self.set_window_title()
        self.setFixedHeight(100)
        self.setMinimumWidth(400)
        self.container_layout = QtWidgets.QHBoxLayout(self)
        self.container_layout.setAlignment(QtCore.Qt.AlignHCenter)
        self.central_widget.setLayout(self.container_layout)

        self.create_menu_bar()

    def create_menu_bar(self):
        """

        :return:
        """
        self.main_menu = self.menuBar()
        # Source
        sources_menu = self.main_menu.addMenu("&Sources")

        manage_sources_action = QtWidgets.QAction("Manage Sources..", self)
        sources_menu.addAction(manage_sources_action)
        manage_sources_action.triggered.connect(self.open_sources_manager)

        # Help
        self.help_menu = self.menuBar()
        help_menu = self.help_menu.addMenu("&Help")

        shorcuts_action = QtWidgets.QAction("Shortcuts", self)
        help_menu.addAction(shorcuts_action)
        shorcuts_action.triggered.connect(self.open_shortcuts)

    def open_sources_manager(self):
        """

        :return:
        """
        self.sources_manager = SourcesManagerInterface()
        self.sources_manager.show_ui()

    def open_shortcuts(self):
        """

        :return:
        """
        print('Shortcuts Opened')


class AdvancedInterface(InterfaceAbstract):
    """
    AdvancedInterface
    """

    def __init__(self, data, btn):
        """

        :param data:
        :param btn:
        """
        super(AdvancedInterface).__init__()
        self.data = data
        self.btn = btn

        self.resize(600, 400)

        self.container_layout = QtWidgets.QVBoxLayout(self)
        self.container_layout.setAlignment(QtCore.Qt.AlignHCenter)

        self.tab = misc_widgets_cls.Tab()
        self.container_layout.addWidget(self.tab)

        self.central_widget.setLayout(self.container_layout)

    def set_documentation(self):
        """

        :return:
        """
        method_exists = getattr(self.data, "get_doc", None)
        if method_exists:
            documentation = self.data.get_doc()
            self.tab.text_edit_doc.set_text(documentation)

    def set_source_code(self):
        """

        :return:
        """
        src_code = open(self.data.get_module_path(), 'r')
        self.tab.text_edit_source.set_text(src_code.read())


class SourcesManagerInterface(QtWidgets.QMainWindow):
    """
    SourcesManagerInterface
    """

    def __init__(self):
        """

        """
        super(SourcesManagerInterface).__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.setStyleSheet("background-color: #221E1D;"
                           "border :2px solid ;")
        self.set_central_widget()

        self.container_layout = QtWidgets.QVBoxLayout(self)
        self.container_layout.setAlignment(QtCore.Qt.AlignHCenter)

    def set_window_title(self):
        """

        :return:
        """
        self.setWindowTitle('Sources Manager')

    def set_central_widget(self):
        """

        :return:
        """
        self.setCentralWidget(self.central_widget)

    def show_ui(self):
        """

        :return:
        """
        self.show()

    def hide_ui(self):
        """

        :return:
        """
        self.hide()

    def get_pos(self):
        """

        :return:
        """
        return self.pos()

    def switch_view(self, target):
        """

        :param target:
        :return:
        """
        target.hide_ui()
        self.show_ui()
