
{'date': 'Tue Oct 15 2019 09:54:07.944 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''criou camara
criou explorador
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 33
    templo.inicia()
  module <module> line 29
    self.camara.entra(self.jogador)
AttributeError: 'Templo' object has no attribute 'jogador'
'''},
{'date': 'Tue Oct 15 2019 11:01:57.674 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 18
  if "entra na camara de novo?" == "s"
                                       ^
SyntaxError: invalid syntax
'''},