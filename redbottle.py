from bottle import route, request, response, view, run
import redis

r = redis.Redis()

@route('/keyvalue/')
@view('add')
def template_keyvalue():
	return dict(title='Key-Value Store')

@route('/keyvalue/add/', method='POST')
@view('add')
def template_add():
	if 'key' in request.POST:
		key = request.POST['key']
	if 'value' in request.POST:
		value = request.POST['value']

	r.set(key,value)

	return dict(title="Key-Value Pair", key=key, value=value)

@route('/keyvalue/delete/', method='POST')
@view('delete')
def template_delete():
        if 'key_delete' in request.POST:
                key_delete = request.POST['key_delete']

        r.delete(key_delete)

        return dict(title="Key-Value Pair", key=key_delete)

@route('keyvalue/show/:key')
@view('show')

def template_show(key):
	the_key = key.strip()
	value = r.get(the_key)	
	
	return dict(title=the_key, the_key=the_key, value=value)	
run()