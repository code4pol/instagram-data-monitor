BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
LOGOUT_URL = BASE_URL + 'accounts/logout/'
CHROME_WIN_UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
USER_URL = BASE_URL + '{0}/?__a=1'
USER_INFO = 'https://i.instagram.com/api/v1/users/{0}/info/'

STORIES_URL = 'https://i.instagram.com/api/v1/feed/user/{0}/story/'
STORIES_UA = 'Instagram 9.5.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+'
STORIES_COOKIE = 'ds_user_id={0}; sessionid={1};'

TAGS_URL = BASE_URL + 'explore/tags/{0}/?__a=1'
LOCATIONS_URL = BASE_URL + 'explore/locations/{0}/?__a=1'
VIEW_MEDIA_URL = BASE_URL + 'p/{0}/?__a=1'
SEARCH_URL = BASE_URL + 'web/search/topsearch/?context=blended&query={0}'

QUERY_COMMENTS = BASE_URL + 'graphql/query/?query_hash=33ba35852cb50da46f5b5e889df7d159&variables={0}'
QUERY_COMMENTS_VARS = '{{"shortcode":"{0}","first":50,"after":"{1}"}}'

QUERY_HASHTAG = BASE_URL + 'graphql/query/?query_hash=ded47faa9a1aaded10161a2ff32abb6b&variables={0}'
QUERY_HASHTAG_VARS = '{{"tag_name":"{0}","first":50,"after":"{1}"}}'

QUERY_LOCATION = BASE_URL + 'graphql/query/?query_hash=ac38b90f0f3981c42092016a37c59bf7&variables={0}'
QUERY_LOCATION_VARS = '{{"id":"{0}","first":50,"after":"{1}"}}'

QUERY_MEDIA = BASE_URL + 'graphql/query/?query_hash=42323d64886122307be10013ad2dcc44&variables={0}'
QUERY_MEDIA_VARS = '{{"id":"{0}","first":50,"after":"{1}"}}'

MAX_CONCURRENT_DOWNLOADS = 5
CONNECT_TIMEOUT = 90
MAX_RETRIES = 5
RETRY_DELAY = 5
MAX_RETRY_DELAY = 60

LATEST_STAMPS_USER_SECTION = 'users'
