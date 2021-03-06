#!/usr/bin/env python
import os
import web
import json

from zk import ZooKeeperConnection

urls = ('/(.*)', 'node')
render = web.template.render('templates/')

try:
    zkc = ZooKeeperConnection(os.environ["ZOOKEEPER"])
except:
    zkc = ZooKeeperConnection("127.0.0.1:2181")


class node:
    def GET(self, url = ""):
        name = url if not url.endswith('/') else url[:-1]
        home = web.ctx.homedomain + ('/' + name if name != "" else '')
        raw_data = zkc.raw_data(name)
        # TODO: add raw tab
        data = ""
        if len(raw_data[0]) > 0:
            try:
               data = json.dumps(json.loads(raw_data[0]), indent=4)
            except ValueError:
                try:
                    data = raw_data[0].decode('UTF-8')
                except UnicodeDecodeError:
                    data = ""
        info = json.dumps(raw_data[1], indent=4)
        children = zkc.children(name)
        return render.page(home, name, data, info, children)

    def POST(self, url = ""):
        path = url if not url.endswith('/') else url[:-1]
        post_input = web.input(_method='post')
        if post_input.get("delete"):
            if url:
                try:
                    zkc.delete(path)
                    url = "/".join(url.split("/")[:-1])
                except:
                    pass
        else:
            zkc.set(path, post_input["zdata"])
        raise web.seeother("/%s" % url)


if __name__ == '__main__' :
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
