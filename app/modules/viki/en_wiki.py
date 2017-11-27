import wikipedia
import datetime
import json
import re



class Viki_media(object):

	def __init__(self, language='en'):
		self.language = language
		



	def Search_wiki_page(self, query=None, pages=None ):
		try:
			wikipedia.set_lang(self.language)
			data = wikipedia.search(query)
			print data.content.find('.')
			return json.dumps({'name':'THE-BOT','datetime':str(datetime.datetime.now()),'response':[i for i in data]} , indent=4)
		except wikipedia.exceptions.PageError as e:
			return json.dumps({'name':'THE-BOT','datetime':str(datetime.datetime.now()), 'response': 'No matches'}, indent=4)
		except wikipedia.exceptions.DisambiguationError as e:
			return json.dumps({'name':'THE-BOT','datetime':str(datetime.datetime.now()), 'response': "To many results"}, indent=4)
		except Exception as e:
			return {'error':str(e)}	

	
	def  Viki_page(self, page):
		data = wikipedia.page(page)
		data1 = ''.join((data.content)).encode('utf-8').strip()
		data1 = re.split(r"\n\n", data1)
		return {'name':'THE-BOT','datetime':str(datetime.datetime.now()), 'response':{'tile':data.title, 'url':data.url,
				'content':data1[0] + ' ' + 'For more infromation click :' + ''.join((data.url)).encode('utf-8').strip()  }}


	
	def viki_wikifull_page(self, query=None):
		try:
			data = wikipedia.WikipediaPage(title=query, pageid=None, redirect=True, preload=False, original_title=u'')
			print data.images
		except Exception as e:
			return json.dumps({'error':str(e)})
			

		


if __name__ == '__main__':
	d = Viki_media()
	#print d.Search_wiki_page(query='India')
	print d.Viki_page('india')
	#d.viki_wikifull_page('Baby')
