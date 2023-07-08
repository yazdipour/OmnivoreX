from textual.widgets import (
    Input,
    Button,
    Static,
)
from textual.screen import ModalScreen
from textual import events


class LoginScreen(ModalScreen[str]):
    CSS_PATH = "styles/login_screen.css"

    def compose(self):
        yield Static("Enter your Omnivore API Token:")
        yield Input(placeholder="Token", password=True)
        yield Static("Please enter a valid API token!", classes="hidden", id="error")
        yield Button("Login", variant="primary", id="login")

    def get_text_from_input(self):
        api_token = self.query_one("Input").value
        if api_token:
            self.dismiss(api_token)
        else:
            self.query_one("#error").remove_class("hidden")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "login":
            self.get_text_from_input()

    def on_key(self, event: events.Key) -> None:
        # if the user presses the enter key, dismiss the screen
        if event.key == "enter":
            self.get_text_from_input()
