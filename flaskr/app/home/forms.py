from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
from wtforms import ValidationError


class IndexForm(FlaskForm):
    index = IntegerField('Index', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_index(self, field):
        if field.data > 30:
            raise ValidationError("No, can't do sir!")
