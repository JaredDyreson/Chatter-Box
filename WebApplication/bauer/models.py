"""
Using Font Awesome in HTML:
https://www.w3schools.com/icons/fontawesome_icons_intro.asp

Search font awesome icons:
https://fontawesome.com/v4.7.0/icons/

"""

"""
This is an example of a class that can be used
in the webpages via this Flask application.

TODO

- Make a class representation of a calculator that can be interfaced from the front end
    - possibly use an enumeration class?
    - this can be found in lexer.py in this repository for an example of this

"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PortfolioItem():
    def __init__(self, title: str, content: str, number: int, 
                    image_path: str, demo_link: str, doc_link: str, src_link : str):
        self.title_ = title
        self.content = content
        self.number = number
        self.image_path = image_path
        self.demo_link = demo_link
        self.doc_link = doc_link
        self.src_link = src_link

class RPNExpressionIngestor(FlaskForm):

  expression_ = StringField(
    'Expression',
    validators=[DataRequired()]
  )

  submit = SubmitField('Compute')

class RPNCalculatorInterface(FlaskForm):
    def __init__(self, form: FlaskForm, buttons: list, name: str):
        self.buttons = buttons
        self.name = name
        self.signed = False
