import zmq, sqlite3, os
from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg

from ui.main_window_ui import Ui_w_MainWindow

class MainWindow(qtw.QMainWindow, Ui_w_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.populate_tips()

        # App page constants
        self.BEGIN_PAGE = 0
        self.LIBRARY_PAGE = 1
        self.VIEW_PAGE = 2
        self.ADD_PAGE = 3

        # Home button signals
        self.btn_begin.clicked.connect(self.go_home)
        self.btn_ViewHome.clicked.connect(self.go_home)
        self.btn_AddHome.clicked.connect(self.go_home)
        self.btn_LibraryHome.clicked.connect(self.go_home)

        # Sort by signal
        self.dd_LibrarySortBy.currentIndexChanged.connect(self.populate_library_list)

        # Add Game page setup
        self.txt_AddName.textChanged.connect(self.update_name_suggestions)
        self.btn_LibraryAddGame.clicked.connect(self.navigate_to_add_game)
        self.btn_AddGameSubmit.clicked.connect(self.add_new_game)
        self.btn_AddChooseArt.clicked.connect(self.add_game_choose_art)
        self.lbl_AddGameArt.dragEnterEvent = self.art_drag_enter_event
        self.lbl_AddGameArt.dropEvent = self.art_drop_event
        self.add_game_art_changed = False
        
        # Open connections to Microservices B, C, and D
        self.ms_b_context = zmq.Context()
        self.ms_b_socket = self.ms_b_context.socket(zmq.REQ)
        self.ms_b_socket.connect("tcp://localhost:5557")

        self.ms_c_context = zmq.Context()
        self.ms_c_socket = self.ms_c_context.socket(zmq.REQ)
        self.ms_c_socket.connect("tcp://localhost:5558")

        self.ms_d_context = zmq.Context()
        self.ms_d_socket = self.ms_d_context.socket(zmq.REQ)
        self.ms_d_socket.connect("tcp://localhost:5559")

        self.show()

    def closeEvent(self, event):
        # Close connections to Microservices B, C, and D
        self.ms_b_socket.close()
        self.ms_b_context.term()
        self.ms_c_socket.close()
        self.ms_c_context.term()
        self.ms_d_socket.close()
        self.ms_d_context.term()
        return super().closeEvent(event)

    def populate_tips(self):
        ######################################
        # Get tips from Microservice A
        ######################################
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5556")
        socket.send_string("2")
        response = socket.recv_string()
        tips = response.splitlines()
        socket.close()
        context.term()

        tip_text = ""
        for tip in tips:
            tip_text += f"• {tip}\n\n"
        self.lbl_tips.setText(tip_text)

    def go_home(self):
        # Ensure they don't lost data on Add Page
        if self.pnl_pages.currentIndex() == self.ADD_PAGE:
            if self.add_game_has_changes():
                dlg_discard = qtw.QMessageBox(self)
                dlg_discard.setWindowTitle("Wait!")
                dlg_discard.setText("Wait! You still have unsaved changes! Discard this game?")
                dlg_discard.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.No)
                dlg_discard.setIcon(qtw.QMessageBox.Warning)
                discard = dlg_discard.exec()

                if discard == qtw.QMessageBox.No:
                    return

        # Prep the library list before going home
        self.populate_library_list()
        self.pnl_pages.setCurrentIndex(self.LIBRARY_PAGE)

    def navigate_to_add_game(self):
        self.add_game_art_changed = False
        self.txt_AddName.setText("")
        self.dd_AddYear.setCurrentIndex(0)
        self.dd_AddGenre.setCurrentIndex(0)
        self.txt_AddDescription.setPlainText("")
        self.lbl_AddGameArt.setPixmap(qtg.QPixmap("./ui/placeholder.png"))

        self.completer = qtw.QCompleter(self)
        self.completer.setCaseSensitivity(qtc.Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(qtc.Qt.MatchFlag.MatchContains)
        self.model = qtc.QStringListModel()
        self.completer.setModel(self.model)
        self.txt_AddName.setCompleter(self.completer)
        self.completer.activated.connect(self.on_name_chosen)
        
        self.pnl_pages.setCurrentIndex(self.ADD_PAGE)

    ######################################
    # Get game names from Microservice B
    ######################################
    def update_name_suggestions(self):
        self.ms_b_socket.send_string(self.txt_AddName.text())
        suggestions = self.ms_b_socket.recv_string().splitlines()
        self.model.setStringList(suggestions)

    def on_name_chosen(self, text):
        ######################################
        # Get description from Microservice C
        ######################################
        self.ms_c_socket.send_string(text)
        description = self.ms_c_socket.recv_string()
        if description:
            self.txt_AddDescription.setPlainText(description)

        ######################################
        # Get game art from Microservice D
        ######################################
        self.ms_d_socket.send_string(text)
        game_art = self.ms_d_socket.recv_string()
        if game_art:
            self.lbl_AddGameArt.setPixmap(qtg.QPixmap(f"./ui/images/{game_art}"))
            self.add_game_art_changed = True
            self.file_chosen = game_art

    def add_game_has_changes(self):
        return self.txt_AddName.text() != "" or self.dd_AddYear.currentIndex() != 0 or self.dd_AddGenre.currentIndex() != 0 or self.txt_AddDescription.toPlainText() != "" or self.add_game_art_changed

    def add_game_choose_art(self):
        self.file_chosen = qtw.QFileDialog.getOpenFileName(self, "Open Image", "./ui/images", "Images (*.png *.jpg)")[0]
        if self.file_chosen != "":
            self.file_chosen = os.path.basename(self.file_chosen)
            print(self.file_chosen)
            self.lbl_AddGameArt.setPixmap(qtg.QPixmap(f"./ui/images/{self.file_chosen}"))
            self.add_game_art_changed = True

    def art_drag_enter_event(self, event: qtg.QDragEnterEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if any(self.is_image_file(url.toLocalFile()) for url in urls):
                event.acceptProposedAction()
    
    def art_drop_event(self, event: qtg.QDropEvent):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            file_path = os.path.basename(file_path)
            if self.is_image_file(file_path):
                self.lbl_AddGameArt.setPixmap(qtg.QPixmap(f"./ui/images/{file_path}"))
                self.file_chosen = file_path
                self.add_game_art_changed = True
    
    def is_image_file(self, file_path):
        return os.path.splitext(file_path)[1].lower() in [".png", ".jpg"]

    def add_new_game(self):
        if self.txt_AddName.text() != "" and self.dd_AddYear.currentIndex() != 0 and self.dd_AddGenre.currentIndex() != 0 and self.txt_AddDescription.toPlainText() != "":
            values = [
                self.txt_AddName.text(),
                int(self.dd_AddYear.itemText(self.dd_AddYear.currentIndex())),
                self.dd_AddGenre.itemText(self.dd_AddGenre.currentIndex()),
                self.txt_AddDescription.toPlainText(),
                self.file_chosen if self.add_game_art_changed else ""
            ]
            query = "INSERT INTO games (name, year, genre, description, art) VALUES (?, ?, ?, ?, ?)"
            cursor.execute(query, values)
            connection.commit()
            self.populate_library_list()
            self.pnl_pages.setCurrentIndex(self.LIBRARY_PAGE)
            dlg_success = qtw.QMessageBox(self)
            dlg_success.setWindowTitle("Success!")
            dlg_success.setText(f"Success! {self.txt_AddName.text()} was added to your library!")
            dlg_success.setIcon(qtw.QMessageBox.Information)
            dlg_success.exec()
            self.ms_b_socket.send_string(f"ADD: {self.txt_AddName.text()}")
            response = self.ms_b_socket.recv_string()
        else:
            dlg_required = qtw.QMessageBox(self)
            dlg_required.setWindowTitle("Oops!")
            dlg_required.setText("Oops! You still have information to fill out!")
            dlg_required.setStandardButtons(qtw.QMessageBox.Ok)
            dlg_required.setIcon(qtw.QMessageBox.Information)
            required = dlg_required.exec()

    def navigate_to_view_game(self, id: int):
        query = "SELECT name, year, genre, description, art FROM games WHERE id = ?"
        game = cursor.execute(query, (id,)).fetchone()
        self.lbl_ViewTitle.setText(game[0])
        self.lbl_ViewDescription.setText(f"Year: {game[1]}\nGenre: {game[2]}\n\nDescription:\n{game[3]}")
        game_art = qtg.QPixmap("./ui/placeholder.png") if game[4] == "" else qtg.QPixmap(f"./ui/images/{game[4]}")
        self.lbl_ViewGameArt.setPixmap(game_art)
        self.pnl_pages.setCurrentIndex(self.VIEW_PAGE)        

    def populate_library_list(self):
        while self.grid_games.count():
            item = self.grid_games.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        sort_by = self.dd_LibrarySortBy.itemText(self.dd_LibrarySortBy.currentIndex()).lower()
        query = "SELECT id, name, year, genre, art FROM games ORDER BY name"
        match sort_by:
            case "year":
                query = "SELECT id, name, year, genre, art FROM games ORDER BY year, name"
            case "genre":
                query = "SELECT id, name, year, genre, art FROM games ORDER BY genre, name"
        games = cursor.execute(query).fetchall()
        row, col = 0, 0
        for game in games:
            game_listing = GameListing(game)
            self.grid_games.addWidget(game_listing, row, col)
            game_listing.clicked.connect(self.navigate_to_view_game)
            col += 1
            if col >= 4:
                col = 0
                row += 1

class GameListing(qtw.QWidget):
    clicked = qtc.Signal(int)
    id = -1

    def __init__(self, game):
        super().__init__()
        layout = qtw.QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        image = qtw.QLabel()
        if game[-1] == "":
            image.setPixmap(qtg.QPixmap("./ui/placeholder.png"))
        else:
            image.setPixmap(qtg.QPixmap(f"./ui/images/{game[-1]}"))
        image.setMinimumSize(120, 180)
        image.setMaximumSize(120, 180)
        image.setScaledContents(True)
        image.setSizePolicy(qtw.QSizePolicy.Policy.Minimum, qtw.QSizePolicy.Policy.Minimum)

        self.setCursor(qtg.QCursor(qtc.Qt.PointingHandCursor))
        self.id = int(game[0])

        lbl_name = qtw.QLabel(game[1])
        lbl_genre = qtw.QLabel(game[3])
        lbl_year = qtw.QLabel(str(game[2]))

        layout.addWidget(image)
        layout.addWidget(lbl_name)
        layout.addWidget(lbl_genre)
        layout.addWidget(lbl_year)

        self.setLayout(layout)
    
    def mousePressEvent(self, event: qtg.QMouseEvent):
        if event.button() == qtc.Qt.LeftButton:
            self.clicked.emit(self.id)

if __name__ == "__main__":

    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()

    app = qtw.QApplication()
    window = MainWindow()
    app.exec()

    connection.commit()
    connection.close()
    
