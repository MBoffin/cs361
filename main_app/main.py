import zmq, sys, random
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from ui.main_window_ui import Ui_w_MainWindow

class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.populate_tips()

        self.btn_begin.clicked.connect(self.begin)
        self.pnl_pages.currentChanged.connect(self.page_changed)

        self.show()

    # TODO: Replace with microservice
    def populate_tips(self):
        tips = [
            "This is a tip.",
            "This is another tip.",
            "This is a great tip.",
            "This is an amazing tip.",
            "Everything in this app is amazing."
        ]
        while len(tips) > 2:
            tips.pop(random.randint(0, len(tips)-1))
        tip_text = ""
        for tip in tips:
            tip_text += f"• {tip}\n\n"
        self.lbl_tips.setText(tip_text)

    def begin(self):
        self.pnl_pages.setCurrentIndex(1)

    def page_changed(self, index):
        if index == 1:
            owned_games = [1, 2, 3, 4, 5, 6, 7, 8]
            r = 0
            c = 0
            for game in owned_games:
                game_listing = GameListing()
                self.grid_games.addWidget(game_listing, r, c)
                c += 1
                if c >= 4:
                    c = 0
                    r += 1

class GameListing(qtw.QWidget):
    def __init__(self):
        super().__init__()
        layout = qtw.QVBoxLayout()
        self.image = qtw.QLabel()
        self.image.setPixmap(qtg.QPixmap("./ui/images/placeholder.png"))
        self.image.setMinimumSize(120, 180)
        self.image.setMaximumSize(120, 180)
        self.image.setScaledContents(True)
        self.image.setSizePolicy(qtw.QSizePolicy.Policy.Minimum, qtw.QSizePolicy.Policy.Minimum)

        self.lbl_name = qtw.QLabel("Game Name")
        self.lbl_genre = qtw.QLabel("Genre")
        self.lbl_year = qtw.QLabel("Year")

        layout.addWidget(self.image)
        layout.addWidget(self.lbl_name)
        layout.addWidget(self.lbl_genre)
        layout.addWidget(self.lbl_year)

        self.setLayout(layout)

if __name__ == "__main__":
    app = qtw.QApplication()
    window = MainWindow()

    sys.exit(app.exec())