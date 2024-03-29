import http.cookiejar
import json
import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import urllib.parse
from lxml import html
from urllib.parse import quote_plus as _quote_plus

ua_gary = 'Gary for Slack - https://github.com/Mu5tank05/Gary'


def get(*args, **kwargs):
    if kwargs.get("decode", True):
        return open(*args, **kwargs).read().decode()
    else:
        return open(*args, **kwargs).read()


def get_json(*args, **kwargs):
    return json.loads(get(*args, **kwargs))


def open(url, query_params=None, user_agent=None, post_data=None,
         referer=None, get_method=None, cookies=False, timeout=None, headers=None, **kwargs):
    if query_params is None:
        query_params = {}

    if user_agent is None:
        user_agent = ua_gary

    query_params.update(kwargs)

    url = prepare_url(url, query_params)

    request = urllib.request.Request(url, post_data)

    if get_method is not None:
        request.get_method = lambda: get_method

    if headers is not None:
        for header_key, header_value in headers.items():
            request.add_header(header_key, header_value)

    request.add_header('User-Agent', user_agent)

    if referer is not None:
        request.add_header('Referer', referer)

    if cookies:
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))
    else:
        opener = urllib.request.build_opener()

    if timeout:
        return opener.open(request, timeout=timeout)
    else:
        return opener.open(request)


def prepare_url(url, queries):
    if queries:
        scheme, netloc, path, query, fragment = urllib.parse.urlsplit(url)

        query = dict(urllib.parse.parse_qsl(query))
        query.update(queries)
        query = urllib.parse.urlencode(dict((to_utf8(key), to_utf8(value))
                                            for key, value in query.items()))

        url = urllib.parse.urlunsplit((scheme, netloc, path, query, fragment))

    return url


def to_utf8(s):
    if isinstance(s, str):
        return s.encode('utf8', 'ignore')
    else:
        return str(s)


def quote_plus(s):
    return _quote_plus(to_utf8(s))


def unescape(s):
    if not s.strip():
        return s
    return html.fromstring(s).text_content()
