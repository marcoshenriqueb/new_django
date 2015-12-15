from projectB.settings import BASE_URL
from django.http import HttpRequest
from django.core.urlresolvers import reverse
import requests
import abc

class MailerBase(object):
    """docstring for Mailer"""
    __metaclass__ = abc.ABCMeta

    def __init__(
        self,
        _to=None,
        _from=None,
        fromName=None,
        host=None,
        subject=None,
        text=None,
        username=None,
        password=None
    ):
        self._to = _to
        self._from = _from
        self.fromName = fromName
        self.host = host
        self.subject = subject
        self.text = text
        self.username = username
        self.password = password

    @abc.abstractmethod
    def send(self):
        """Sends a email"""
        return

class MailgunMailer(MailerBase):
    """docstring for MailgunMailer"""
    def __init__(self):
        self.apiKey = "key-db7ac40394e844cc777953031f26530a"
        self.domain = "sandbox36e0be12d3de4e0abb9a70914d6ee5de.mailgun.org"
        super().__init__(
            username="postmaster@sandbox36e0be12d3de4e0abb9a70914d6ee5de.mailgun.org",
            password="1f79ad6d5d12b23bf75b5c80b7ba3bfc",
            _from="postmaster@sandbox36e0be12d3de4e0abb9a70914d6ee5de.mailgun.org",
            host="smtp.mailgun.org",
            fromName="BetLoko"
        )

    def send(self, _to=["marcoshenriqueb@gmail.com",], subject="BetLoko", html="<h1>Test</h1>"):
        url = "https://api.mailgun.net/v3/%s/messages" % self.domain
        _from = "%s <%s>" % (self.fromName, self._from)
        return requests.post(
            url,
            auth=("api", self.apiKey),
            data={"from": _from,
                  "to": _to,
                  "subject": subject,
                  "html": html}
        )

    def sendRegisterConfirmation(self, _to, verified_token):
        url = BASE_URL + reverse('profile:confirmation', args=[verified_token])
        body = "<h1>BetLoko</h1></br>"
        body += "<h2>Obrigado por se cadastrar!</h2></br>"
        body += "<p>Para confimar o seu cadastro clique <a href='%s'>aqui</a>!</p></br>" % url
        self.send(_to=_to, subject="Confimação de Cadastro", html=body)
