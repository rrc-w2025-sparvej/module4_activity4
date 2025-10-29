"""The module defines the ContactList class."""

__author__ = "Sania Parvej"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import  QMainWindow, QLineEdit, QPushButton, QTableWidget, QLabel, QVBoxLayout, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot    #Added import for Slot decorator

class ContactList(QMainWindow):
    """Represents a window that provides the UI to manage contacts."""
    def __init__(self):
        """Initializes a new instance of the ContactList class."""

        super().__init__()
        self.__initialize_widgets()    

        # Connect button signals to their respective slots
        self.add_button.clicked.connect(self.__on_add_contact)
        self.remove_button.clicked.connect(self.__on_remove_contact)

    def __initialize_widgets(self):
        """Initializes the widgets on this Window.
        
        DO NOT EDIT.
        """
        self.setWindowTitle("Contact List")

        self.contact_name_input = QLineEdit(self)
        self.contact_name_input.setPlaceholderText("Contact Name")

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Phone Number")

        self.add_button = QPushButton("Add Contact", self)
        self.remove_button = QPushButton("Remove Contact", self)
        
        self.contact_table = QTableWidget(self)
        self.contact_table.setColumnCount(2)
        self.contact_table.setHorizontalHeaderLabels(["Name", "Phone"])

        self.status_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_name_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.remove_button)
        layout.addWidget(self.contact_table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Event Handlers
    @Slot()
    def __on_add_contact(self):
        """Handles the Add Contact button click event."""
        # Extract text from input fields
        contact_name = self.contact_name_input.text().strip()
        phone_number = self.phone_input.text().strip()

        # Check if both fields have data
        if len(contact_name) > 0 and len(phone_number) > 0:
            
            # Get the current number of rows
            row_position = self.contact_table.rowCount()

            # Insert a new row 
            self.contact_table.insertRow(row_position)

            # Create table items for name and phone
            name_item = QTableWidgetItem(contact_name)
            phone_item = QTableWidgetItem(phone_number)

            # Add items to the table
            self.contact_table.setItem(row_position, 0, name_item)
            self.contact_table.setItem(row_position, 1, phone_item)

            # Update
            self.status_label.setText(f"Added contact: {contact_name}")
        else:
            # Show warning with a message
            self.status_label.setText("Please enter a contact name and phone number.")
    
    @Slot()
    def __on_remove_contact(self):
        """Handles the Remove Contact button click event."""
        pass