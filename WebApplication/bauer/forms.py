from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class RPNExpressionIngestor(FlaskForm):

  expression_ = StringField(
    'Expression:',
    validators = [DataRequired()]
  )
  submit = SubmitField('Calculate')
