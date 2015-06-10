__author__ = 'oem'
import webapp2
import validationTest
form="""
<form method=post>
Preencha o formulario abaixo
<br>
<label>
<input type="text" name="nome" value="%(nome)s">
</label>
<br>
<label>
<input type="text" name="mail" value="%(mail)s">
</label>
<br>
<label>
<input type="text" name="password" >
</label>
<br>
<label>
<input type"text" name="credit" value="%(credit)s">
</label>
</form>
"""
class mainPage(webapp2.requestHandler):
    def write_form(self,nome="",mail="",password="",credit=""):
        self.response.out.write(form %{"nome": nome, "mail": mail, "password": password, "credit": credit })

    def get(self):
        self.write_form(self)

    def post(self):
        user_nome=self.request.get('nome')
        user_mail=self.request.get('mail')
        user_pass=self.request.get('password')
        user_credit=self.request.get('credit')
        nome= validationTest.check_letras(user_nome)
        mail= validationTest.check_mail(user_mail)
        credit= validationTest.check_num(user_credit)
        password= validationTest.check_password(user_pass)
        if not(nome and mail and credit and password):





