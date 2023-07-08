import html2text

__htmlToText = html2text.HTML2Text()


def convert_html_to_markdown(
    content: str,
    prefix: str = None,
    ignore_links=False,
    ignore_images=False,
    ignore_emphasis=False,
) -> str:
    """Convert html to markdown"""
    __htmlToText.ignore_links = ignore_links
    __htmlToText.ignore_images = ignore_images
    __htmlToText.ignore_emphasis = ignore_emphasis
    markdown_text = __htmlToText.handle(content)
    if prefix is not None:
        markdown_text = f"# {prefix}\n{markdown_text}"
    return markdown_text
