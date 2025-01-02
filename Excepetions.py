# utilizamos as exception caso o problema mostre um erro potencial e o programa pare
# No problema abaixo, apresentamos um erro comum, caso o usuario digite uma chave inexistente no dicionário

algo = {"felipe":10,"luana":14}

try:
    algo["felipeee"]
except (Exception,TypeError,NameError,ZeroDivisionError):
    print("O programa nao encontrou o usuario no banco de dados")
finally:
    print("Isso ai camarada")

# Podemos usar um finally - Ele é chamada independente se ocorrer ou nao um exception
    
# Podemos passar mais de um valor para o except
#except (RuntimeError, TypeError, NameError):
#   pass

def divisao(a,b):
    try:
        resultado = a /b 
    except ZeroDivisionError:
        print("Você não pode dividir um número por 0")
    
    else:
        print(f"Resultado {resultado}")
    finally:
        print("Operação concluida")


divisao(15,0)


# Criando a própria exceção

