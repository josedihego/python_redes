# standard library ou bibliotecas padrão
# xclip -selection clipboard -target image/png -out > out.png

# módulo sys
import sys
print(sys.platform)
print(sys.version)

# modulo os
import os
print(os.getcwd())
print(os.environ)
print(os.getenv('HOME'))

# módulo datetime
import datetime
print(datetime.date.today())
data_hoje  =  datetime.date.today()
print('dia {}'.format(data_hoje.day))
print('mês {}'.format(data_hoje.month))
print('ano {}'.format(data_hoje.year))
# data hoje como texto
data_como_texto = datetime.date.isoformat(datetime.date.today())
print(data_como_texto)
print(type(data_como_texto))

#módulo datetime  - parte 2
import datetime
data_passada = datetime.datetime.strptime('29/06/1985', '%d/%m/%Y')
data_hoje  =  datetime.datetime.strptime('23/09/2022', '%d/%m/%Y')
intervalo = data_hoje - data_passada
print('Quantidade de dias desde 29/06/1985 é {}'.format(intervalo.days))
print(data_passada)
print(data_hoje)


# módulo time
import time
print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))

#módulo locale
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
print(time.strftime("%A %p"))

# módulo html
import html
print(html.escape("Este HTML contém um <script>script</script>."))
print(html.unescape("Eu &hearts; Python &lt;standard library&gt;."))