from textual.app import App
from textual.widgets import (
    Footer,
    Header,
    Button,
    MarkdownViewer,
    ListView,
)
from textual.containers import Container
import os
from article_item import ArticleItem
from login_screen import LoginScreen
from utils import _omnivoerql_utils


class OmnivoreX(App):
    TITLE = "OmnivoreX"
    CSS_PATH = "main_screen.css"
    DEFAULT_LIMIT = 42
    OPENED_ARTICLE: ArticleItem = None
    WelcomePageMDContent = open(
        os.path.join(os.path.dirname(__file__), "Welcome.md"), "r"
    ).read()
    MARKDOWN_VIEWER: MarkdownViewer = MarkdownViewer(
        id="markdown", show_table_of_contents=False
    )
    BINDINGS = [
        ("k", "scroll('up')", "▲"),
        ("u", "scroll('up')", "▲"),
        ("j", "scroll('down')", "▼"),
        ("d", "scroll('down')", "▼"),
        ("h", "scroll('home')", "⇈"),
        ("g", "scroll('end')", "⇊"),
        ("a", "archive", "un/Archive"),
        ("r", "refresh", "Refresh"),
        ("s", "settings", "Settings"),
        ("t", "toggle_theme", "Toggle theme"),
        ("q", "quit", "Quit"),
    ]

    # ------------------
    # Compose
    # ------------------
    def compose(self):
        yield Header()
        yield Container(
            Container(
                ListView(id="list_view"),
                Button("Load more", id="load_more"),
                id="left_container",
            ),
            self.MARKDOWN_VIEWER,
            classes="horizontalContainer",
        )
        yield Footer()

    # ------------------
    # Events
    # ------------------
    def action_toggle_theme(self) -> None:
        self.dark = not self.dark

    def on_mount(self):
        if not _omnivoerql_utils.is_logged_in():
            self.action_settings()
        else:
            self.action_refresh()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "load_more":
            self.load_more()

    def action_settings(self) -> None:
        def set_api_token(token: str) -> None:
            _omnivoerql_utils.save_token(token)
            self.action_refresh()

        self.push_screen(LoginScreen(), set_api_token)

    def action_refresh(self) -> None:
        self.query_one("#list_view").clear()
        self.MARKDOWN_VIEWER.document.update(self.WelcomePageMDContent)
        articles = _omnivoerql_utils.get_articles(limit=self.DEFAULT_LIMIT)
        self.populate_listview(articles)

    def action_archive(self) -> None:
        if self.OPENED_ARTICLE is not None:
            article = self.OPENED_ARTICLE.details
            _omnivoerql_utils.archive_article(
                article["node"]["id"], not article["node"]["isArchived"]
            )
            article["node"]["isArchived"] = not article["node"]["isArchived"]
            if article["node"]["isArchived"]:
                self.OPENED_ARTICLE.set_status(ArticleItem.ArticleStatus.ARCHIVED)
            else:
                self.OPENED_ARTICLE.set_status(ArticleItem.ArticleStatus.DEFAULT)

    def action_scroll(self, dir: str) -> None:
        if dir == "up":
            self.MARKDOWN_VIEWER.scroll_up()
        elif dir == "down":
            self.MARKDOWN_VIEWER.scroll_down()
        elif dir == "home":
            self.MARKDOWN_VIEWER.scroll_home()
        elif dir == "end":
            self.MARKDOWN_VIEWER.scroll_end()

    # ------------------
    # Load articles
    # ------------------
    def on_list_view_selected(self, event: ListView.Selected):
        if self.OPENED_ARTICLE == event.item:
            return
        # reset status of previous article
        if (
            self.OPENED_ARTICLE is not None
            and self.OPENED_ARTICLE.status == ArticleItem.ArticleStatus.READING
        ):
            self.OPENED_ARTICLE.set_status(ArticleItem.ArticleStatus.DEFAULT)
        self.OPENED_ARTICLE = event.item
        self.OPENED_ARTICLE.set_status(ArticleItem.ArticleStatus.READING)
        self.MARKDOWN_VIEWER.document.update(
            _omnivoerql_utils.get_article_by_slug(
                self.OPENED_ARTICLE.details["node"]["slug"]
            )[0]
        )

    def populate_listview(self, list_articles):
        for article in list_articles:
            self.query_one("#list_view").append(
                ArticleItem(article["node"]["title"], article)
            )

    def load_more(self):
        lv = self.query_one("#list_view", ListView)
        cursor = 0 if len(lv.children) == 0 else lv.children[-1].details["cursor"]
        self.populate_listview(
            _omnivoerql_utils.get_articles(cursor, self.DEFAULT_LIMIT)
        )


def main():
    OmnivoreX().run()


if __name__ == "__main__":
    main()
