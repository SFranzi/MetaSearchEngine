from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import request

class SearchForm(FlaskForm):
	q = StringField('Wonach möchtest Du suchen?', validators=[DataRequired()])
	
	#The formdata argument determines from where flask_wtf receives form submissions 
	#Forms that are submitted via GET request as search forms are, have the field values in the query string 
	#So request.args is used where Flask writes the query string arguments.

	#Forms have CSRF protection added by default, with the inclusion of a CSRF token that is added to the form 
	#via the form.hidden_tag(). For clickable search links to work, CSRF needs to be disabled. 
	def __init__(self, *args, **kwargs):
		if 'formdata' not in kwargs:
			kwargs['formdata'] = request.args
		if 'csrf_enabled' not in kwargs:
			kwargs['csrf_enabled'] = False
		super(SearchForm, self).__init__(*args, **kwargs)
	

