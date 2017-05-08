
import os

class Config(object):
		SECRET_KEY = 'my_secret_token'
		PAGE_ACCESS_TOKEN ='EAADGMZBRFMwEBAJq52oEJOYNaDFQLzApplIP9J01Rl41w29ADwxxnFSk4OKj30IG0EVJOoGwCM31Yonb7wfyaZBXvlGAwDPQsZA7ke5vXm7Qm0sidzZCaQq2Uc2LDV1SxknY2g1GIPQ5TisJGcZCAZB60ZAGhjBYukgm07wgbYZAMgZDZD'

class DevelopmentConfig(Config):
		DEBUG =  True
