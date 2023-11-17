from textual.app import ComposeResult
from textual.widgets import (
    ListItem,
    Label,
)
from enum import Enum


class ArticleItem(ListItem):
    class ArticleStatus(Enum):
        DEFAULT = 1
        ARCHIVED = 2
        READING = 3
        DELETED = 4

    DEFAULT_CSS = """
    ArticleItem {
        height: 3;
        padding-top: 1;
        padding-left: 1;
        padding-right: 1;
    }
    ArticleItem:hover {
        background: $surface;
    }
    ArticleItem.--highlight {
        background:  $accent-lighten-1;
    }
    """
    label_content = None
    label: Label = None
    status: ArticleStatus = ArticleStatus.DEFAULT

    def __init__(self, label: str, details: str) -> None:
        super().__init__()
        self.label_content = label
        self.details = details

    def compose(self) -> ComposeResult:
        self.label = Label(self.label_content)
        yield self.label

    def set_status(self, status: ArticleStatus) -> None:
        self.status = status
        if status == self.ArticleStatus.DEFAULT:
            self.label.update(self.label_content)
        elif status == self.ArticleStatus.ARCHIVED:
            self.label.update(f"[dim]{self.label_content}[/]")
        elif status == self.ArticleStatus.READING:
            self.label.update(f"[underline]{self.label_content}[/]")
        elif status == self.ArticleStatus.DELETED:
            self.label.update(f"[dim][strike]{self.label_content}[/strike][/dim]")

    def refresh_content(self) -> None:
        self.label.update(self.label_content)
