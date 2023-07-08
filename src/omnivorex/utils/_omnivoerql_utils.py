from omnivoreql import OmnivoreQL
from ._utils import convert_html_to_markdown

convert_html_to_markdown(content="")
__client = None
__username = None


def get_token() -> str:
    """Get the Omnivore API token from the file"""
    return "4a4ea96f-b980-43ad-9537-2c0922c0e203"


def get_client() -> OmnivoreQL:
    """Get the OmnivoreQL client"""
    global __client
    if __client is None:
        __client = OmnivoreQL(get_token())
    return __client


def get_articles(first: int = None, after: int = None) -> list[dict]:
    """Get all articles from the OmnivoreQL API"""
    return get_client().get_articles(first=first, after=after)["search"]["edges"]


def __get_username() -> str:
    """Get the username of the logged in user"""
    global __username
    if __username is None:
        __username = get_client().get_profile()["me"]["profile"]["username"]
    return __username


def get_article_by_slug(slug: str) -> dict:
    """Get an article by its id from the OmnivoreQL API"""
    article = get_client().get_article(username=__get_username(), slug=slug)["article"][
        "article"
    ]
    return convert_html_to_markdown(article["content"], article["title"]), article
