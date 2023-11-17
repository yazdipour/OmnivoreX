# Textual

<https://textual.textualize.io/guide/devtools/>

## Textual Demo

```bash
python -m textual
```

## CSS Hot Reloading

```bash
pip install textual-dev
textual run --dev main_screen.py
```

## Mounting new widgets

While composing is the preferred way of adding widgets when your app starts it is sometimes necessary to add new widget(s) in response to events. You can do this by calling mount() which will add a new widget to the UI.

```python
from textual.widgets import Welcome
class WelcomeApp(App):
    def on_key(self) -> None:
        self.mount(Welcome())
        self.query_one(Button).label = "YES!"
```

### Await Mounting

If you run this example, you will find that Textual raises a NoMatches exception when you press a key. This is because the mount process has not yet completed when we attempt to change the button.

To solve this we can optionally await the result of mount(), which requires we make the function async. This guarantees that by the following line, the Button has been mounted, and we can change its label.

```python
class WelcomeApp(App):
    async def on_key(self) -> None:
        await self.mount(Welcome())
        self.query_one(Button).label = "YES!"
```
