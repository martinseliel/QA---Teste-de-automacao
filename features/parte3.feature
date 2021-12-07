Funcionalidade: Tentar logar no site
Cenario: Logar no site com dados de login não cadastrados
Dado que navego para a página 'login' do site
E digito 'Caldeirao' no campo 'Username'
E digito '1234' no campo 'Password'
Quando clico no botão 'SIGN IN'
Entao verifico se será exibida a mensagem de erro: 'ERROR! Login failed, incorrect username or password'
