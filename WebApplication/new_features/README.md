# Hello World

This is some text.

This is some text.

This is some text.

This is some text.

This is some text.



```python
#!/usr/bin/env python3.8

import markdown
from flask import Flask
import markdown.extensions.fenced_code

app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return md_template_string


if __name__ == "__main__":
    app.run()

```
