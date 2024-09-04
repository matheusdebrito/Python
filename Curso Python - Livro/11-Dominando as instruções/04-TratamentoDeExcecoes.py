'''

'''

try:
    print('try (sem provocar exceções)')
except Exception as e:
    print('except', e)
else:
    print('else')
finally:
    print('finally')
    print('*' * 20)
try:
    print('try (provocando exceções)')
    print('divisão:', 2 / 0)
except Exception as e:
    print('except', e)
else:
    print('else')
finally:
    print('finally')
    print('*' * 20)
# Sequência completa sem ocorrer exceção e sem else
try:
    print('try (sem else)')
except Exception as e:
    print('except', e)
finally:
    print('finally')