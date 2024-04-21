from creditos import CredConsumo, CredHipotecario


credito1 = CredConsumo() 
credito1.definir_monto(3_000_000)
print(credito1)

credito2 = CredHipotecario()
credito2.definir_monto(120_000_000)
print(credito2.mostrar_monto()) # Mostrar monto es un método heredado