import os
from dotenv import load_dotenv
from omnivoreql import OmnivoreQL

__client = None
__username = None
__token = None


def getEnvVariable(variable_name, dotenv_path="~/.omnivorex"):
    dotenv_path = os.path.expanduser(dotenv_path)
    load_dotenv(dotenv_path)
    return os.environ.get(variable_name)


def get_token() -> str:
    """Get the Omnivore API token from ~/.omnivorex"""
    global __token
    if __token is None:
        __token = getEnvVariable("OMNIVORE_API_TOKEN")
    return __token


def save_token(token: str) -> None:
    """Save or replace the Omnivore API token into ~/.omnivorex"""
    global __token
    __token = token
    with open(os.path.expanduser("~/.omnivorex"), "w") as f:
        f.write("OMNIVORE_API_TOKEN={token}".format(token=token))


def is_logged_in() -> bool:
    return get_token() is not None


def get_client() -> OmnivoreQL:
    global __client
    if __client is None:
        __client = OmnivoreQL(get_token())
    return __client


def get_articles(limit: int, cursor: int = 0, query="in:inbox"):
    return get_client().get_articles(cursor=str(cursor), limit=limit, query=query)[
        "search"
    ]["edges"]


def get_username() -> str:
    global __username
    if __username is None:
        __username = get_client().get_profile()["me"]["profile"]["username"]
    return __username


def get_article_by_slug(slug: str) -> dict:
    article = get_client().get_article(
        username=get_username(), slug=slug, format="markdown"
    )["article"]["article"]
    content = "# {title} \n {content}".format(
        title=article["title"], content=article["content"]
    )
    return content, article


def archive_article(article_id: str, toArchive: bool = True) -> None:
    get_client().archive_article(article_id=article_id, toArchive=toArchive)
