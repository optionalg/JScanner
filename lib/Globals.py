from lib.ColoredObject import Color

#url_regex = ['((http|https)\:\/\/)?([a-zA-Z0-9\.\/\?\:@\-_=#]+\.(com|net|org|co|us|ru|gov|edu|info))([a-zA-Z0-9\.\&\/\?\:@\-_=#])*']
#path_regex = ['(\/[^\/]+){0,2}\/?']

# General
url_regex = "((http|https)\:\/\/)+[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"
single_path_regex = """('|"|\(|\))(\/){1}[a-zA-Z0-9-_]+(\/)?('|"|\(|\))"""
path_regex = "([a-zA-Z0-9]+\.[a-zA-Z0-9]{3,6})?\/(([0-9a-zA-Z+.-]+)([\/&| ])){1,30}([a-zA-Z0-9]+(\.[a-zA-Z0-9]*)?)?(\?|;)?([a-zA-Z\[\]&=]*)?"
subdomain_regex = lambda subdomain: '(.*\.)?{}(\.)?'.format(subdomain)

dom_sources_regex = [
'document.url',
'document.documenturi',
'Document.URLUnencoded',
'Document.baseURI',
'Location.href',
'Location.search',
'Location.hash',
'Location.pathname',
'Document.cookie',
'Document.referrer',
'Window.name',
'History.pushState',
'History.replaceState',
'LocalStorage',
'SessionStorage',
'window.location',
'document.location'
]

dom_sinks_regex = [
'eval',
'setTimeout',
'setInterval',
'setImmediate',
'execScript',
'cyrpto.generateCRMFRequest',
'ScriptElement',
'ScriptElement.src',
'ScriptElement.text',
'ScriptElement.textContent',
'ScriptElement.innerText',
'document.write',
'document.writeln',
]

custom_insensitive = [
'API',
'key',
'secretKey',
]

# SPECIAL --->
custom_sensitive = [
'sourceMappingURL',
]
# <---

web_services_regex = [
'([0-9a-zA-Z-.]*s3[a-zA-Z-.]*\.?amazonaws\.com\/?[a-zA-Z-.]*)',
'([0-9a-zA-Z-.]*?storage\.googleapis\.com\/?[a-zA-Z-.]*)',
'([0-9a-zA-Z-.]*?digitaloceanspaces\.com\/?[a-zA-Z-.]*)',
'([0-9a-zA-Z-.]*?blob\.core\.windows\.net\/?[a-zA-Z-.]*)',
]

skip_regex = [
'.*jquery.*'
]

hexchar = "1234567890abcdefABCDEF"
base64char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
ColorObj = Color()

