from app import app
from app.search import expertenservice
from flask import render_template, flash, redirect, url_for, request
from app.forms import SearchForm 
import time 

#@app.route are decoraters which modify the function that follows it. 
@app.route('/')
@app.route('/search', methods = ['GET', 'POST'])
def search():
	form  = SearchForm()
	if form.validate(): 
		#current_milli_time = lambda: int(round(time.time() * 1000))
		#start_time = current_milli_time()
		start_time = time.time()
		#print(start_time)
		#query = form.q.data
		query = request.args.get('q')
		results = expertenservice(query)
		#q = query_index_multi('websites', query)
		#time_diff = current_milli_time() - start_time
		end_time = time.time()
		time_diff = round(end_time - start_time, 2)
		print(time_diff)
		return render_template('results.html', results = results, form = form, time_diff = time_diff)
	else: 
		return render_template('search.html', form = form)

