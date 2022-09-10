my_var = 'Ciao'

try:
    my_var = float(my_var)

except ValueError:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore di tipo VALORE. "my_var" valeva "{}".'.format(my_var))

except TypeError:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore di TIPO. "my_var" era di tipo "{}".'.format(type(my_var)))

except Exception as e:
    print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un errore generico: "{}"'.format(e))