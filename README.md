# Casos de Prueba de Carrito de Compras

Este repositorio contiene dos casos de prueba automatizados para un carrito de compras en línea:

1. `test_add_products_to_cart`
2. `test_buy_one_item_complete`

## Descripción de los casos de prueba

### test_add_products_to_cart

Este caso de prueba realiza las siguientes acciones:

1. Genera un número aleatorio entre 1 y 9, que representa la cantidad de productos a agregar al carrito.
2. Agrega la cantidad generada de productos al carrito.
3. Navega al carrito de compras.
4. Verifica que la cantidad de productos en el carrito coincida con la cantidad agregada.

### test_buy_one_item_complete

Este caso de prueba simula el ciclo completo de una compra, realizando las siguientes acciones:

1. Agrega un producto al carrito de compras.
2. Navega al carrito de compras.
3. Procede al proceso de pago.
4. Completa el formulario de compra con la información requerida.
5. Finaliza la compra.
6. Verifica que se muestre el mensaje "Thank you for your purchase!" al completar la transacción.

## Instalación y ejecución de las pruebas

1. Asegúrate de tener Python instalado en tu sistema.

2. Clona este repositorio:

git clone https://github.com/lucin21/selenium_aplazo.git
cd nombre-del-repositorio

Copiar

3. Crea un entorno virtual (opcional pero recomendado):
python -m venv venv
source venv/bin/activate # En Windows usa: venv\Scripts\activate

Copiar

4. Instala los requisitos:
pip install -r requirements.txt

Copiar

5. Ejecuta las pruebas:
python -m unittest test_aplazo.py

Copiar

O si prefieres ejecutar una prueba específica:
python -m unittest test_aplazo.TestAplazo.test_add_products_to_cart
python -m unittest test_aplazo.TestAplazo.test_buy_one_item_complete
