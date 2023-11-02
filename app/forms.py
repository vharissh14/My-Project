from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField,)
from wtforms.validators import InputRequired, Length , NumberRange

class IncomeForm(FlaskForm):
        name = StringField('Income name',
                                validators=[InputRequired(),
                                            Length(min=10, max=100)])
        value = IntegerField('value', validators=[InputRequired(), NumberRange(min=100, max=100000)])

class ExpenditureForm(FlaskForm):
        name = StringField('Expenditure name',
                                validators=[InputRequired(),
                                            Length(min=10, max=100)])
        value = IntegerField('value', validators=[InputRequired(), NumberRange(min=10, max=10000)])

class GoalForm(FlaskForm):
        name = StringField('Goal name',
                                validators=[InputRequired(),
                                            Length(min=10, max=100)])
        value = IntegerField('value', validators=[InputRequired(), NumberRange(min=1000, max=100000)])

class GoalSearchForm(FlaskForm):
        name = StringField('Goal name',
                                validators=[InputRequired(),
                                            Length(min=10, max=100)])
        

class IncomeDeleteForm(FlaskForm):
        id = IntegerField('id',
                                validators=[InputRequired()])