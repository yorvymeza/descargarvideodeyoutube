# from progress.bar import Bar # Esto lo importamo despues
# pip install progress

from pytube import YouTube

def Descarga(link):
	youtubeObject = YouTube(link)
	youtubeObject = youtubeObject.streams.get_highest_resolution()

	try:
		youtubeObject.download()

	except:
		print('Ha habido un error al descargar tu video de youtube')
	print('¡Esta descarga se ha completado! yahoo!')


	# bar = Bar('Processing', max=20)
	# for i in range(20):
	# 	bar.next()

	# bar.finish()


link = input('Put your youtube link here!!! URL: ')
Descarga(link)
