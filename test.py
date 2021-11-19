from subprocess import stdout, PIPE

A_test = ["""2 3
""", """2 2
"""]

B_test = ["""3 3
""", """2 4
"""]

for test in A_test:
    print('input:')
    print(test)
    print('output:')
    print(run(['python', 'test.py'], input=test, stdout=PIPE, encoding="ascii").stdout)
    print('----------------------------')