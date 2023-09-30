from contabancaria import ContaBancaria

t1 = ContaBancaria('Lucas', 0, 123)

t1.depositar(5000)
print(t1.get_saldo())

t1.sacar(100)
t1.sacar(100)
print(t1.get_saldo())

t1.mudar_senha(1234, 321)
