from textual.widgets import (
    Input,
    Button,
    Static,
)
from textual.screen import ModalScreen
from textual import events


class LoginScreen(ModalScreen[str]):
    DEFAULT_CSS = """
    LoginScreen {
        layout: vertical;
        align: center middle;
        border: thick $background 80%;
        background: $surface;
    }
    LoginScreen * {
        text-align: center;
        max-width: 40;
        align: center middle;
        width: 100%;
    }
    .hidden {
        display: none;   
    }
    #error {
        color: red;
    }
    #login {
        width: 100%;
    }
    """

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
