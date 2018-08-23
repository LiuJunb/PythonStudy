from urllib.robotparser import RobotFileParser
import urllib.parse
import urllib.request
import ssl


class RobotFileParserExp(RobotFileParser):

    def __init__(self):
        super().__init__()

    def read(self, context=None):
        """Reads the robots.txt URL and feeds it to the parser."""
        if context is not None:
            c = context
        else:
            c = ssl._create_unverified_context()
        try:
            f = urllib.request.urlopen(self.url, context=c)
        except urllib.error.HTTPError as err:
            if err.code in (401, 403):
                self.disallow_all = True
            elif err.code >= 400 and err.code < 500:
                self.allow_all = True
        else:
            raw = f.read()
            self.parse(raw.decode("utf-8").splitlines())

