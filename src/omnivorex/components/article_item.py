from textual.app import ComposeResult
from textual.widgets import (
    ListItem,
    Label,
)
from utils._omnivoerql_utils import *


class ArticleItem(ListItem):
    def __init__(self, label: str, uid: str) -> None:
        super().__init__()
        self.label = label
        self.uid = uid

    def compose(self) -> ComposeResult:
        yield Label(self.label)
