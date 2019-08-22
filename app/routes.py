from app import app
from app.search import expertenservice
from flask import render_template, flash, redirect, url_for, request
from app.forms import SearchForm 

#@app.route are decoraters which modify the function that follows it. 
@app.route('/')
@app.route('/search', methods = ['GET', 'POST'])
def search():
	form  = SearchForm()
	if form.validate(): 
		#query = form.q.data
		query = request.args.get('q')
		results = expertenservice(query)
		#q = query_index_multi('websites', query)

		return render_template('results.html', results = results, form = form)
	else: 
		return render_template('search.html', form = form)

