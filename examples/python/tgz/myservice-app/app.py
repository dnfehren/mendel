import cherrypy

class MendelTestApp(object):
    @cherrypy.expose
    def index(self):
        return "Hello gregor. Hello Sprout"

if __name__ == '__main__':
   cherrypy.quickstart(MendelTestApp())