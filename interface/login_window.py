# -*- coding: utf-8 -*-
# @Time    : 18/6/2023 下午2:12
# @Author  : LeaVES
# @FileName: LoginWindow.py
# coding: utf-8

from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from qfluentwidgets import *

from interface.resource.i18n.CN import *
from scripts.client_thread import DEFAULT_PORT


class LoginWindow:
    def __init__(self):
        # 主窗口
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.widget = QWidget(parent=self)
        size_policy = QSizePolicy()
        size_policy.Policy(QSizePolicy.Policy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(size_policy)
        self.widget.setMinimumSize(QSize(360, 0))
        self.widget.setMaximumSize(QSize(360, 16777215))
        self.widget.setStyleSheet(
            """QLabel{
            font: 13px 'Microsoft YaHei'
            }"""
        )

        self.horizontalLayout.addWidget(self.widget)

        # 背景图
        self.label = QLabel(parent=self)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.__init_vertical_qvboxlayout_2()
        self.re_set_text()
        QMetaObject.connectSlotsByName(self)

    def __init_grid_layout_server(self):
        # 设置服务器连接部分
        # 创建QGridLayout容器
        self.GridLayoutFServer = QGridLayout()
        self.GridLayoutFServer.setHorizontalSpacing(4)
        self.GridLayoutFServer.setVerticalSpacing(9)
        self.GridLayoutFServer.setObjectName("GridLayoutFServer")
        # 服务器地址E
        self.serverAdLE = EditableComboBox(parent=self.widget)
        self.serverAdLE.setClearButtonEnabled(True)
        self.serverAdLE.setObjectName("serverAdLE")
        # 端口L
        self.GridLayoutFServer.addWidget(self.serverAdLE, 1, 0, 1, 1)
        # 服务器地址L
        self.label_3 = QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.GridLayoutFServer.addWidget(self.label_3, 0, 0, 1, 1)
        # 端口E
        self.serverPortLE = LineEdit(parent=self.widget)
        self.serverPortLE.setPlaceholderText("")
        self.serverPortLE.setClearButtonEnabled(True)
        self.serverPortLE.setObjectName("serverPortLE")
        self.GridLayoutFServer.addWidget(self.serverPortLE, 1, 1, 1, 1)
        # 端口L
        self.label_4 = QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.GridLayoutFServer.addWidget(self.label_4, 0, 1, 1, 1)
        self.GridLayoutFServer.setColumnStretch(0, 2)
        self.GridLayoutFServer.setColumnStretch(1, 1)
        # 登陆到服务器按键
        self.link_server_button = PrimaryPushButton(parent=self.widget)
        self.link_server_button.setObjectName("link_server_button")
        self.GridLayoutFServer.addWidget(self.link_server_button, 3, 0, 1, 5)

    def __init_qvboxlayout_user(self):
        self.QVBoxLayout_2 = QVBoxLayout()
        self.QVBoxLayout_2.setObjectName("QVBoxLayout_2")
        # 用户名L
        self.label_5 = QLabel(parent=self.widget)
        self.label_5.setObjectName("label_5")
        self.QVBoxLayout_2.addWidget(self.label_5)
        # 用户名E
        self.userNameLE = EditableComboBox(parent=self.widget)
        self.userNameLE.setClearButtonEnabled(True)
        self.userNameLE.setObjectName("userNameLE")
        self.QVBoxLayout_2.addWidget(self.userNameLE)
        # 密码L
        self.label_6 = QLabel(parent=self.widget)
        self.label_6.setObjectName("label_6")
        self.QVBoxLayout_2.addWidget(self.label_6)
        # 密码E
        self.userPasswordLE = LineEdit(parent=self.widget)
        self.userPasswordLE.setEchoMode(QLineEdit.EchoMode.Password)
        self.userPasswordLE.setClearButtonEnabled(True)
        self.userPasswordLE.setObjectName("userPasswordLE")
        self.QVBoxLayout_2.addWidget(self.userPasswordLE)
        # spacerItem
        spacer_item3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum,
                                   QSizePolicy.Policy.Fixed)
        self.QVBoxLayout_2.addItem(spacer_item3)
        # 1111(复选框)
        self.checkBox_remember_uer = CheckBox(parent=self.widget)
        self.checkBox_remember_uer.setChecked(False)
        self.checkBox_remember_uer.setObjectName("checkBox")
        self.QVBoxLayout_2.addWidget(self.checkBox_remember_uer, 0, Qt.AlignmentFlag.AlignHCenter)
        # spacerItem
        spacer_item4 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum,
                                   QSizePolicy.Policy.Fixed)
        self.QVBoxLayout_2.addItem(spacer_item4)
        # 登入按键
        self.login_Button = PrimaryPushButton(parent=self.widget)
        self.login_Button.setObjectName("login_Button")
        self.QVBoxLayout_2.addWidget(self.login_Button)
        spacer_item5 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum,
                                   QSizePolicy.Policy.Fixed)
        self.QVBoxLayout_2.addItem(spacer_item5)
        self.back_Button = PrimaryPushButton(parent=self.widget)
        self.back_Button.setObjectName("back_Button")
        self.QVBoxLayout_2.addWidget(self.back_Button)

    def __init_vertical_qvboxlayout_2(self):
        # 创建一个容器(整个侧栏)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(9)
        #
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum,
                                  QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacer_item)

        self.label_title = QLabel(parent=self.widget)
        # 指定一个stylesheet
        self.label_title.setStyleSheet(
            """QLabel{
            font: 33px 'Microsoft YaHei'
            }"""
        )
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        # spacerItem
        spacer_item1 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacer_item1)

        # 创建一个用来放置头像的标签
        self.label_head_icon = QLabel(parent=self.widget)
        # 启用设置
        self.label_head_icon.setEnabled(True)
        size_policy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_head_icon.sizePolicy().hasHeightForWidth())
        self.label_head_icon.setSizePolicy(size_policy)
        self.label_head_icon.setMinimumSize(QSize(100, 100))
        self.label_head_icon.setMaximumSize(QSize(100, 100))

        self.label_head_icon.setScaledContents(True)
        self.label_head_icon.setObjectName("label_head_icon")
        self.verticalLayout_2.addWidget(self.label_head_icon, 0, Qt.AlignmentFlag.AlignHCenter)
        # spacerItem
        spacer_item2 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacer_item2)

        self.loadProgressBar = IndeterminateProgressBar()
        self.verticalLayout_2.addWidget(self.loadProgressBar)
        self.loadProgressBar.setVisible(False)

        self.connectedServerLabel = PushButton()
        self.verticalLayout_2.addWidget(self.connectedServerLabel)
        self.connectedServerLabel.setVisible(False)
        self.connectedServerLabel.setText("")

        spacer_item3 = QSpacerItem(20, 15, QSizePolicy.Policy.Minimum,
                                   QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacer_item3)

        self.__init_grid_layout_server()
        self.verticalLayout_2.addLayout(self.GridLayoutFServer)

        self.__init_qvboxlayout_user()
        self.verticalLayout_2.addLayout(self.QVBoxLayout_2)
        # spacerItem
        spacer_item5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacer_item5)

    def re_set_text(self):
        """登入部分
        统一设置组件的内容"""
        self.serverAdLE.setPlaceholderText("example.com")
        self.label_3.setText(f"{ENTER_ADDRESS}")
        self.serverPortLE.setText(f"{DEFAULT_PORT}")
        self.label_4.setText(f"{ENTER_PORT}")
        self.label_5.setText(f"{ENTER_USERNAME}")
        self.userNameLE.setPlaceholderText("User")
        self.label_6.setText(f"{ENTER_PASSWORD}")
        self.userPasswordLE.setPlaceholderText("••••••••••••")
        self.checkBox_remember_uer.setText(f"{REMEMBER_PASSWORD}")
        self.login_Button.setText(f"{LOGIN_TEXT}")
        self.login_Button.setToolTip(f"{LOGIN_BUTTON_TIP}")
        self.back_Button.setText("断开连接")
        self.link_server_button.setText("连接到服务器")
