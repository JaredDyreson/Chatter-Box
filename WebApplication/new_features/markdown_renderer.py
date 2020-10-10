#!/usr/bin/env python3.8

import markdown
from flask import Flask
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter

app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code", "codehilite"]
    )

    # Generate css for syntax highlighting
    formatter = HtmlFormatter(style="friendly", full=True, cssclass="codehilite")
    css_string = formatter.get_style_defs()
    md_css_string = "<style>" + css_string + "</style>"

    md_template = md_css_string + md_template_string
    print(md_template)
    return md_template

if __name__ == "__main__":
    app.run()

