#!/usr/bin/env python
import os
import web
import pprint

from zk import ZooKepperConnection

urls = ('/(.*)', 'node')
render = web.template.render('templates/')

try:
    zkc = ZooKepperConnection(os.environ["ZOOKEEPER"])
except:
    zkc = ZooKepperConnection("127.0.0.1:2181")

class node:
    def GET(self, url = ""):
        name = url if not url.endswith('/') else url[:-1]
        home = web.ctx.homedomain + ('/' + name if name != "" else '')
        raw_data = zkc.raw_data(name)
        # try:
        #    TODO: add pprint tab
        #    import json
        #    data = pprint.pformat(json.loads(raw_data[0]))
        # except:
        #    data = raw_data[0]
        data = raw_data[0]
        info = pprint.pformat(raw_data[1])
        children = zkc.children(name)
        return render.page(home, name, data, info, children)

    def POST(self, url = ""):
        path = url if not url.endswith('/') else url[:-1]
        post_input = web.input(_method='post')
        zkc.set(path, post_input["zdata"])
        raise web.seeother("/%s" % url)

if __name__ == '__main__' :
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
